from scraper import get_page
from extract_players import extract_players
from extract_coach import extract_coach


def extract_team(my_url):

    # Obtém o conteúdo da página
    page_content = get_page(my_url)

    # Extrai os jogadores
    players = extract_players(page_content)
    if not players:
        players = "Informação Indisponível."

    # Extrai o coach
    coach = extract_coach(page_content)
    if not coach:
        coach = "Informação indisponível."

    return {"players": players, "coach": coach}

# Teste
furia_data = extract_team("https://www.hltv.org/team/8297/furia")
print(f"Jogadores da FURIA: {furia_data["players"]}\nCoach da FURIA: {furia_data["coach"]}")