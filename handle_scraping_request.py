import re
from unidecode import unidecode
from extract_coach import extract_coach
from extract_coach_link import extract_coach_link
from extract_championships import extract_championships
from extract_last_matches_score import extract_last_matches_score
from extract_next_match_date_time import extract_next_match_date_time
from extract_next_match_format_and_stage import extract_next_match_format_and_stage
from extract_next_match_opponent import extract_next_match_opponent
from extract_players_links import extract_players_links
from extract_players import extract_players
from extract_team import extract_team


def handle_scraping_request(user_text):
    team_url = "https://www.hltv.org/team/8297/furia"

    # Padroniza a entrada do usuário para melhor verificação
    user_text = unidecode(user_text.lower())

    responses = {"raw_data": {}}
    messages = []
    found_valid_data = False

    # Função auxiliar para verificar palavras-chave
    def has_keyword(user_text, keywords):
        # Garante que o texto está sem acentos e minúsculo
        user_text = unidecode(user_text.lower())

        for keyword in keywords:
            # Expressão regular que permite palavras intermediárias
            pattern = r'.*' + r'.*'.join([re.escape(word) for word in keyword.split()]) + r'.*'

            # Verifica se a expressão regular encontra correspondência no texto
            if re.search(pattern, user_text):
                return True
        return False

    # Palavras-chave para cada tipo de pergunta
    keywords_players = [r"jogadores", r"jogador", r"players", r"player", r"quais jogadores"]
    keywords_coach = [r"treinador", r"coach", r"tecnico"]
    keywords_team = [r"time", r"elenco", r"squad", r"equipe"]
    keywords_championship = [r"campeonato", r"campeonatos", r"torneio", r"torneios"]
    keywords_next_match = [r"proximo jogo", r"proximas partidas", r"proximos resultados",
       r"proximos jogos", r"proximos jogos da furia", r"quando vai ser a proxima partida",
       r"qual vai ser o proximo jogo", r"proximos resultados da furia", r"proximo game",
       r"resultados futuros", r"jogos futuros", r"proximos games", r"proxima partida",
       r"partidas futuras", "contra", "quem vai jogar"]
    keywords_format = [r"formato", r"tipo de partida", r"formato do jogo", r"bo1", r"bo2", r"bo3"]
    keywords_stage = [r"etapa", r"fase", r"stages", r"fase do jogo"]
    keywords_opponent = [r"adversario", r"oponente", r"contra"]
    keywords_last_matches = [
        r"ultimo jogo", r"ultimas partidas", r"ultima partida", r"ultimos resultados",
        r"ultimos jogos", r"ultimos jogos da furia", r"quando foi", r"quais foram",
        r"qual foi o ultimo jogo", r"ultimos resultados da furia", r"ultimo game", r"ultimos resultados",
        r"resultados recentes", r"jogos passados", r"ultimos games", r"partida passada",
        r"partidas passadas", r"resultados"
    ]

    # Caso o usuário pergunte sobre o formato da próxima partida
    if has_keyword(user_text, keywords_format):
        match_data = extract_next_match_format_and_stage(team_url)
        if match_data:
            format = match_data.get("format")
            messages.append(f"O formato da próxima partida será {format}.")
            responses["raw_data"]["format"] = format
            found_valid_data = True

    # Caso o usuário pergunte sobre a etapa da próxima partida
    elif has_keyword(user_text, keywords_stage):
        match_data = extract_next_match_format_and_stage(team_url)
        if match_data:
            stage = match_data.get("stage")
            messages.append(f"A partida será disputada na fase: {stage}.")
            responses["raw_data"]["stage"] = stage
            found_valid_data = True

    # Caso o usuário pergunte sobre o adversário da próxima partida
    elif has_keyword(user_text, keywords_opponent):
        opponent = extract_next_match_opponent(team_url)
        if opponent:
            messages.append(f"O adversário da próxima partida será: {opponent}.")
            responses["raw_data"]["opponent"] = opponent
            found_valid_data = True

    # Caso o usuário pergunte sobre o próximo jogo
    elif has_keyword(user_text, keywords_next_match):
        match_data = extract_next_match_date_time(team_url)
        match_opponent = extract_next_match_opponent(team_url)
        if match_data:
            date, time, opponent = match_data.get("date"), match_data.get("time"), match_data.get("team2")
            if date and time:
                messages.append(f"O próximo jogo da FURIA está marcado para o dia {date} às {time} contra {match_opponent}.")
            elif date:
                messages.append(f"O próximo jogo da FURIA será no dia {date}.")
            elif time:
                messages.append(f"O próximo jogo da FURIA será às {time}.")
            elif match_opponent:
                messages.append(f"O próximo jogo da FURIA será contra {match_opponent}.")
            responses["raw_data"]["next_game"] = match_data
            found_valid_data = True

    # Caso o usuário pergunte sobre os jogadores
    elif has_keyword(user_text, keywords_players):
        players = extract_players(team_url)
        players_links = extract_players_links(team_url)
        # Garante que ambos (jogadores e links) tenham o mesmo número de itens
        if len(players) == len(players_links):
            # Monta as mensagens com o nome do jogador e o link
            player_info = [f"{player} [{link}]" for player, link in zip(players, players_links)]

            # Junta as informações dos jogadores em uma string separada por vírgulas
            names = '\n'.join(player_info)

            # Adiciona a resposta
            messages.append(f"Atualmente, os jogadores da FURIA são:\n{names}.")

            # Salva os dados
            responses["raw_data"]["players"] = players
            responses["raw_data"]["players_links"] = players_links
            found_valid_data = True

    # Caso o usuário pergunte sobre o treinador
    elif has_keyword(user_text, keywords_coach):
        coach = extract_coach(team_url)
        coach_link = extract_coach_link(team_url)

        if coach and coach_link:
            # Monta a mensagem com o nome do treinador e o link
            messages.append(f"Atualmente, o treinador da FURIA é {coach} [{coach_link}].")

            # Salva os dados
            responses["raw_data"]["coach"] = coach
            responses["raw_data"]["coach_link"] = coach_link
            found_valid_data = True

    # Caso o usuário pergunte sobre o time
    elif has_keyword(user_text, keywords_team):
        team = extract_team(team_url)
        players = extract_players(team_url)
        players_links = extract_players_links(team_url)
        coach = extract_coach(team_url)
        coach_link = extract_coach_link(team_url)

        if team:
            # Resposta sobre o time
            messages.append(f"A equipe da FURIA compete atualmente com o elenco principal no cenário de CS2.\n")

            # Variáveis para armazenar as informações dos jogadores e do coach
            player_info = ""
            coach_info = ""

            # Se os jogadores foram encontrados
            if players and players_links:
                # Garante que ambos (jogadores e links) tenham o mesmo número de itens
                if len(players) == len(players_links):
                    # Monta as mensagens com o nome do jogador e o link
                    player_info = [f"{player} [{link}]" for player, link in zip(players, players_links)]
                    names = '\n'.join(player_info)
                else:
                    names = "Erro: Dados dos jogadores incompletos."
            else:
                names = "Informações dos jogadores não encontradas."

            # Se o coach foi encontrado
            if coach and coach_link:
                coach_info = f"{coach} [{coach_link}]"
            else:
                coach_info = "Informações do coach não encontradas."

            # Adiciona a resposta
            messages.append(f"Os jogadores atuais da FURIA são:\n{names}")
            messages.append(f"\nO coach atual da FURIA é: {coach_info}")

            # Adicionando os dados brutos
            responses["raw_data"]["team"] = team
            responses["raw_data"]["team_link"] = team_url
            responses["raw_data"]["players"] = players
            responses["raw_data"]["players_links"] = players_links
            responses["raw_data"]["coach"] = coach
            responses["raw_data"]["coach_link"] = coach_link

            found_valid_data = True

    # Caso o usuário pergunte sobre o torneio atual do time
    elif has_keyword(user_text, keywords_championship):
        championships = extract_championships(team_url)
        if championships:
            messages.append("A FURIA está participando dos seguintes campeonatos (principais):")
            messages.extend([f"- {c}" for c in championships])
            responses["raw_data"]["championships"] = championships
            found_valid_data = True

    # Caso o usuário pergunte sobre os últimos resultados
    elif has_keyword(user_text, keywords_last_matches):
        last_matches = extract_last_matches_score(team_url)

        if last_matches:
            messages.append("Últimos resultados da FURIA:\n")

            # Formata no padrão: "Data - Adversário: [placar]"
            for match in last_matches:
                formatted_match = f"- {match['date']} - {match['team1']} contra {match['team2']}: {match['score']}"
                messages.append(formatted_match)

            responses["raw_data"]["last_matches"] = last_matches
            found_valid_data = True

    # Verifica se alguma resposta foi gerada
    if found_valid_data:
        return {
            "status": "success",
            "messages": messages,
            "raw_data": responses["raw_data"]
        }

    # Caso não haja respostas, retornam uma mensagem de fallback
    return {
        "status": "fallback",
        "messages": [],
        "raw_data": {}
    }