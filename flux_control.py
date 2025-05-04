from unidecode import unidecode
from ai_classification import classify_input
from handle_scraping_request import handle_scraping_request
from fallback_deny import fallback_deny
from ai_scraping_filter import ai_scraping_filter
from fallback_response import fallback_response
import logging
import re

# Palavras-chave
keywords = {
    'jogos': [
        "jogo",
        "jogar",
        "partida",
        "jogam",
        "proximo jogo",
        "quando jogam",
        "agenda",
        "horario do jogo",
        "quem enfrentam",
        "adversario",
        "proximo adversario",
        "match",
        "calendar",
        "fixtures",
        "round",
        "data",
        "dia",
        "fase",
        "oponente"
    ],
    'times': [
        "time",
        "equipe",
        "lineup",
        "elenco",
        "jogadores",
        "player",
        "players",
        "squad",
        "composicao",
        "mudanca de time",
        "transferencia",
        "team",
        "roster",
        "substituicao",
        "novato",
        "coach",
        "tecnico",
        "treinador"
    ],
    'torneios': [
        "campeonato",
        "campeonatos",
        "torneio",
        "torneios",
        "liga",
        "major",
        "qualifier",
        "eliminatoria",
        "competicao",
        "evento",
        "final",
        "semi-final",
        "playoffs",
        "fase de grupos",
        "bracket",
        "classificacao",
        "ranking",
        "formato",
        "bo1",
        "bo2",
        "bo3",
        "etapa",
        "fase",
        "stages"
    ],
    'cenario': [
        "furia",
        "cenario",
        "organizacao",
        "csgo",
        "cs2",
        "atualizacao",
        "meta",
        "mudanca de meta",
        "mudanca no csgo",
        "cenario atual",
        "ranking mundial",
        "hltv ranking",
        "ranking csgo",
        "patch notes",
        "update",
        "balanco",
        "mudancas",
        "rival",
        "rivais"
    ],
    'resultados': [
        "resultado",
        "score",
        "placar",
        "quantos rounds",
        "ganhou",
        "perdeu",
        "quem venceu",
        "desempenho",
        "estatisticas",
        "kda",
        "rating",
        "mvp",
        "melhor jogador",
        "top fragger",
        "frag lider"
    ],
    'historico': [
        "historico",
        "retrospecto",
        "ultimas partidas",
        "ultimos resultados",
        "estatisticas passadas",
        "ultimos confrontos",
        "head-to-head",
        "resultados recentes",
        "passado",
        "passada",
        "passados",
        "passadas"
    ],
    'curiosidades': [
        "brasil",
        "recorde",
        "superacao",
        "conquista",
        "estrelas",
        "momentos marcantes",
        "eua",
        "ceo",
        "sede",
        "curiosidade",
        "curiosidades"
    ],
    'jogadores especificos': [
        "yekindar",
        "yuurih",
        "kscerato",
        "fallen",
        "chelo",
        "molodoy",
        "sidde"
    ],
    'saudacoes': [
        "furioso",
        "nome",
        "voce",
        "seu",
        "ola",
        "saudacoes",
        "cumprimentos",
        "prazer",
        "oi",
        "opa",
        "salve",
        "beleza",
        "yo",
        "ae",
        "oie",
        "boa",
        "eai",
        "fala",
        "obrigado",
        "valeu"
    ]
}

keywords_scraping = [
    "jogadores", "quais jogadores","player", "players", "treinador", "coach", "tecnico", "equipe",
    "time", "elenco", "campeonato", "campeonatos", "torneio", "torneios", "evento", "eventos", "proximo jogo",
    "quando jogam", "data", "data do proximo jogo", "dia", "proxima partida", "formato",
    "tipo de partida", "formato do jogo", "etapa", "fase", "stages", "fase do jogo", "adversario", "oponente", "ultimo jogo",
    "ultimas partidas", "ultimos resultados", "ultimos jogos", "ultimos jogos da furia", "quando foi a ultima partida",
    "qual foi o último jogo", "ultimos resultados da furia", "ultimo game", "contra",
    "resultados recentes", "jogos passados", "ultimos games", "partida passada",
    "partidas passadas", "bo1", "bo2", "bo3"
]

# Lista para armazenar os logs de debug
log_buffer = []

# Função para adicionar logs à lista
def log_to_buffer(message, level="DEBUG"):
    if logging.getLogger().isEnabledFor(logging.DEBUG):
        log_buffer.append(f"DEBUG: {message}")

# Normaliza a entrada do usuário
def normalize_text(text):
    log_to_buffer(f"Normalizando o seguinte texto de entrada: {text}")
    return unidecode(text.lower())

# Retorna os dados da mensagem de fallback individualmente
def get_fallback_message(user_text):
    log_to_buffer(f"Obtendo mensagem de fallback para: {user_text}")
    message = fallback_response(user_text)

    if isinstance(message, dict):
        response = message.get('response', "Informação indisponível")
        emoji = message.get('emoji', "")
        additional_phrase = message.get('additional_phrase', "")
        log_to_buffer(f"Fallback dict retornado: {message}")
        return {
            "response": response,
            "emoji": emoji,
            "additional_phrase": additional_phrase
        }
    else:
        log_to_buffer("Mensagem de fallback não é um dicionário!")
        return {
            "response": "Erro ao obter a mensagem de fallback.",
            "emoji": "",
            "additional_phrase": ""
        }


# Formata a mensagem de fallback completa
def fallback_message_format(fallback_message):
    log_to_buffer(f"Formatando mensagem de fallback: {fallback_message}")
    if isinstance(fallback_message, dict):
        return f"{fallback_message.get('response')} {fallback_message.get('emoji')}{fallback_message.get('additional_phrase')}"
    else:
        return fallback_message

# Verifica a existência de palavras-chave na entrada do usuário referenciando uma dicionário de listas
def has_keyword(user_text, keywords_dict):
    log_to_buffer(f"Buscando palavras-chave em: {user_text}")
    for topic, keyword_list in keywords_dict.items():
        for keyword in keyword_list:
            if keyword in user_text:
                log_to_buffer(f"Palavra-chave encontrada: {keyword} no tópico: {topic}")
                return True
    log_to_buffer("Nenhuma palavra-chave encontrada no dicionário.")
    return False

# Verifica a existência de palavras-chave na entrada do usuário referenciando uma lista
def has_keyword_list(user_text, keyword_list):
    log_to_buffer(f"Buscando palavras-chave específicas em: {user_text}")
    if any(keyword in user_text for keyword in keyword_list):
        log_to_buffer("Palavra-chave da lista encontrada.")
        return True
    log_to_buffer("Nenhuma palavra-chave da lista encontrada.")
    return False

# Formata mensagens com scraping extraído
def format_scraping_messages(messages):
    log_to_buffer(f"Formatando mensagens de scraping: {messages}")
    if isinstance(messages, list):
        filtered = [m for m in messages if m.strip()]
        if filtered:
            return "\n".join(filtered)
    elif isinstance(messages, str) and messages.strip():
        return messages
    log_to_buffer("Nenhuma mensagem útil para formatar.")
    return "Erro na formatação da resposta"

# Controla o fluxo de resposta baseado no tipo de entrada (pergunta ou comentário) e nas palavras-chave detectadas
def control_flow(user_text, user_text_type):
    log_to_buffer(f"Iniciando controle de fluxo para entrada: '{user_text}' do tipo: '{user_text_type}'")
    scraping_classification = ai_scraping_filter(user_text)
    log_to_buffer(f"Classificação AI para scraping: {scraping_classification}")

    if not has_keyword(user_text, keywords) and not has_keyword_list(user_text, keywords_scraping):
        log_to_buffer("Nenhuma palavra-chave detectada. Ativando fallback deny.")
        return fallback_deny(user_text)

    if any(keyword in user_text for keyword in keywords_scraping) and "furia" in user_text:
        log_to_buffer("Critérios de scraping diretos atendidos.")
        scraping_answer = handle_scraping_request(user_text)

        if scraping_answer and scraping_answer.get("status") == "success":
            log_to_buffer("Resposta de scraping bem-sucedida.")
            messages = scraping_answer.get("messages")
            return format_scraping_messages(messages)

        log_to_buffer("Scraping falhou. Recorre ao fallback.")
        scraping_answer["messages"] = "Não tenho essa informação no momento..." + get_fallback_message(user_text).get(
            'additional_phrase')
        return format_scraping_messages(scraping_answer.get("messages"))

    if (user_text_type == "question" and
            has_keyword(user_text, keywords) and
            scraping_classification == "factual_request" and
            has_keyword_list(user_text, keywords_scraping)):

        log_to_buffer("Critérios de scraping com pergunta atendidos.")
        scraping_answer = handle_scraping_request(user_text)

        if scraping_answer and scraping_answer.get("status") == "success":
            log_to_buffer("Resposta de scraping bem-sucedida.")
            return format_scraping_messages(scraping_answer.get("messages"))

        log_to_buffer("Scraping falhou. Recorre ao fallback.")
        scraping_answer["messages"] = "Não tenho essa informação no momento..." + get_fallback_message(user_text).get(
            'additional_phrase')
        return format_scraping_messages(scraping_answer.get("messages"))

    log_to_buffer("Fluxo final: Fallback genérico aplicado.")
    return fallback_message_format(get_fallback_message(user_text))


# Faz a requisição de resposta do chatbot
def handle_input(user_text):
    log_to_buffer("...")
    log_to_buffer("-" * 33)
    log_to_buffer(f"Recebida entrada do usuário: {user_text}")
    if not user_text or user_text.strip() == "":
        log_to_buffer("Entrada vazia recebida.")
        return "Hmm, parece que a mensagem veio vazia. Que tal tentar novamente? 😊"

    user_text = normalize_text(user_text)
    log_to_buffer(f"Texto de entrada normalizado: {user_text}")

    # Resposta rápida para saudações
    if has_keyword(user_text, {'saudacoes': keywords['saudacoes']}):
        log_to_buffer("Saudação detectada. Retornando resposta imediata.")
        return fallback_message_format(get_fallback_message(user_text))

    if '?' in user_text:
        input_type = "question"
    else:
        input_type = classify_input(user_text)

    log_to_buffer(f"Tipo de entrada classificado como: {input_type}")

    if input_type not in ["question", "commentary"]:
        log_to_buffer(f"Tipo de entrada inválido detectado: {input_type}")
        return "Desculpe, não consegui entender o contexto da sua mensagem. Poderia reformular sua pergunta? ☺️"

    log_to_buffer(f"Nova interação iniciada com input: {user_text}")

    # Resposta rápida se não for uma pergunta ou não tiver palavras-chave de scraping
    if input_type != "question" or not has_keyword_list(user_text, keywords_scraping):
        log_to_buffer("Input não relacionado a scraping. Resposta direta via fallback.")
        return fallback_message_format(get_fallback_message(user_text))

    response = control_flow(user_text, input_type)

    log_to_buffer(f"Interação finalizada para: {user_text}")
    log_to_buffer("-" * 33)

    return response