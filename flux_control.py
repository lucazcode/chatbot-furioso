from unidecode import unidecode
from ai_classification import classify_input
from handle_scraping_request import handle_scraping_request
from fallback_deny import fallback_deny
from ai_scraping_filter import ai_scraping_filter
from fallback_response import fallback_response
import re

# Palavras-chave
keywords = {
    "jogos": [
        "jogo", "partida", "jogam", "proximo jogo", "quando jogam", "agenda", "horario do jogo", "quem enfrentam",
        "adversario", "proximo adversario", "match", "calendar", "fixtures", "round"
    ],
    "times": [
        "time", "equipe", "lineup", "elenco", "jogadores", "squad", "composicao", "mudanca de time",
        "transferencia", "team", "roster", "substituicao", "novato", "coach", "tecnico", "treinador"
    ],
    "torneios": [
        "campeonato", "torneio", "liga", "major", "qualifier", "eliminatoria", "competicao", "evento",
        "final", "semi-final", "playoffs", "fase de grupos", "bracket", "classificacao", "ranking"
    ],
    "cenario": [
        "cenario", "csgo", "cs2", "atualizacao", "meta", "mudanca de meta", "mudanca no csgo", "cenario atual",
        "ranking mundial", "hltv ranking", "ranking csgo", "patch notes", "update", "balanco", "mudancas", "furia",
        "organizacao"
    ],
    "resultados": [
        "resultado", "resultados", "score", "placar", "quantos rounds", "ganhou", "perdeu", "quem venceu",
        "desempenho", "estatisticas", "kda", "rating", "mvp", "melhor jogador", "top fragger", "frag lider",
        "ultima partida", "ultimas partidas"
    ],
    "historico": [
        "historico", "ultimos jogos", "retrospecto", "ultimas partidas", "ultimos resultados",
        "estatisticas passadas", "ultimos confrontos", "head-to-head", "historico contra"
    ],
    "curiosidades": [
        "curiosidade", "fato curioso", "historia do time", "historia da furia", "recordes", "recorde de kills",
        "recorde de vitorias", "momento marcante", "melhor jogo", "melhor campanha", "maior vitoria"
    ],
    "jogadores especificos": [
        "yuurih", "kscerato", "fallen", "chelo", "art", "drop", "coldzera", "fer", "fnx", "boltz",
        "cogu", "coach guerri", "guerri", "zews", "fnx", "lucas1", "hen1"
    ],
    "saudacoes": [
    "ola", "bom dia", "boa tarde", "boa noite", "saudacoes", "cumprimentos",
    "como vai", "como esta", "tudo bem", "tudo certo", "prazer",
    "com licenca", "oi", "eai", "fala", "fala ai", "opa", "salve",
    "beleza?", "ta tranquilo?", "suave?", "tranquilo?", "tudo beleza?",
    "bao?", "de boa?", "yo", "ae", "ae man", "eae", "oie", "oi oi", "mano",
    "fala mano", "fala campeao", "fala guerreiro", "fala brother", "fala truta",
    "fala chefe", "fala fera", "fala meu consagrado", "sussa?", "boa", "furioso"
    ]
}

keywords_scraping = [
    "jogadores", "quais jogadores", "treinador", "coach", "técnico",
    "time", "elenco", "campeonato", "campeonatos", "torneio", "torneios", "proximo jogo",
    "quando jogam", "data","data do proximo jogo", "proxima partida", "formato",
    "tipo de partida", "formato do jogo", "etapa", "fase", "stages",
    "fase do jogo", "adversario", "oponente", "ultimo resultado",
    "ultima partida", "resultado recente", "ultimos resultados",
    "ultimas partidas", "resultados recentes" "ultimos jogos", "ultimo jogo", "contra"
]


# Normaliza a entrada do usuário
def normalize_text(text):
    return unidecode(text.lower())

# Retorna os dados da mensagem de fallback individualmente
def get_fallback_message(user_text):
    message = fallback_response(user_text)

    # Sempre retorna um dicionário
    if isinstance(message, dict):
        response = message.get('response', "Informação indisponível")
        emoji = message.get('emoji', "")
        additional_phrase = message.get('additional_phrase', "")

        return {
            "response": response,
            "emoji": emoji,
            "additional_phrase": additional_phrase
        }
    else:
        # Se a mensagem não for um dicionário, retorna uma mensagem de erro
        return {
            "response": "Erro ao obter a mensagem de fallback.",
            "emoji": "",
            "additional_phrase": ""
        }

# Formata a mensagem de fallback completa
def fallback_message_format(fallback_message):
    if isinstance(fallback_message, dict):
        return f"{fallback_message.get('response')} {fallback_message.get('emoji')}{fallback_message.get('additional_phrase')}"
    else:
        return fallback_message

# Verifica a existência de palavras-chave na entrada do usuário referenciando uma dicionário de listas
def has_keyword(user_text, keywords_dict):
    for topic, keyword_list in keywords_dict.items():
        if any(keyword in user_text for keyword in keyword_list):
            return True
    return False

# Verifica a existência de palavras-chave na entrada do usuário referenciando uma lista
def has_keyword_list(user_text, keyword_list):
    return any(keyword in user_text for keyword in keyword_list)

def format_scraping_messages(messages):
    if isinstance(messages, list):
        # Verifica se tem ao menos 1 item não vazio
        filtered = [m for m in messages if m.strip()]
        if filtered:
            return "\n".join(filtered)
    elif isinstance(messages, str) and messages.strip():
        return messages

    # Se não tiver mensagens úteis, retorna None
    return "Erro na formatação da resposta"

# Controla o fluxo de resposta baseado no tipo de entrada (pergunta ou comentário) e nas palavras-chave detectadas
def control_flow(user_text, user_text_type):
    scraping_classification = ai_scraping_filter(user_text)

    # Verifica se não tem nenhuma palavra-chave
    if not has_keyword(user_text, keywords) and not has_keyword_list(user_text, keywords_scraping):
        return fallback_deny(user_text)

    # Se o texto contém palavras-chave de scraping sobre o time e "furia", aciona a busca por scraping
    if any(keyword in user_text for keyword in keywords_scraping) and "furia" in user_text:
        print("[Busca por scraping iniciada]")

        scraping_answer = handle_scraping_request(user_text)

        # Se o status de retorno for um sucesso, retorna o scraping
        if scraping_answer and scraping_answer.get("status") == "success":
            messages = scraping_answer.get("messages")
            formatted = format_scraping_messages(messages)
            if formatted:
                return formatted

        # Se o scraping falhou
        scraping_answer["messages"] = "Não tenho essa informação no momento..." + get_fallback_message(user_text).get('additional_phrase')

        messages = scraping_answer.get("messages")
        return format_scraping_messages(messages)

    # Verificação principal para scraping
    if (user_text_type == "question" and
            has_keyword(user_text, keywords) and
            scraping_classification == "factual_request" and
            has_keyword_list(user_text, keywords_scraping)):

        print("[Busca por scraping iniciada]")

        scraping_answer = handle_scraping_request(user_text)

        # Se o status de retorno for um sucesso, retorna o scraping
        if scraping_answer and scraping_answer.get("status") == "success":
            messages = scraping_answer.get("messages")
            formatted = format_scraping_messages(messages)
            if formatted:
                return formatted

        # Se o scraping falhou
        scraping_answer["messages"] = "Não tenho essa informação no momento...\n" + get_fallback_message(user_text).get('additional_phrase')

        messages = scraping_answer.get("messages")
        return format_scraping_messages(messages)

    # Fallback para perguntas não factuais ou sem keywords de scraping
    return fallback_message_format(get_fallback_message(user_text))

# Processa a entrada do usuário, classificando e direcionando para o controle adequado
def handle_input(user_text):
    # Verifica se o texto do usuário é válido
    if not user_text or user_text.strip() == "":
        return "Desculpe, não entendi bem. Poderia reformular sua pergunta? ☺️"

    # Normaliza entrada do usuário
    user_text = normalize_text(user_text)

    # Classifica como "question" ou "commentary"
    input_type = classify_input(user_text)

    # Verifica se o tipo de entrada é valido
    if input_type not in ["question", "commentary"]:
        return "Desculpe, não consegui entender o contexto da sua mensagem. Poderia reformular sua pergunta? ☺️"

    # Passa o tipo diretamente para o fluxo de controle
    return control_flow(user_text, input_type)