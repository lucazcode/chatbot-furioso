from ai_scraping_filter import ai_scraping_filter
from flux_control import handle_input
from ai_classification import classify_input

# Testes
test_questions = [

    # Perguntas genéricas/fallback
    "Quantos anos tem a organização?",
    "Onde fica a sede da FURIA?",
    "Quem é o CEO da FURIA?",

    # Combinações contextuais de jogos
    "Quando é o próximo jogo da FURIA?",
    "Que horas começa o jogo de hoje?",
    "Onde posso assistir ao jogo da FURIA?",
    "Contra quem a FURIA vai jogar?",
    "Qual a data do próximo match?",

    # Combinações contextuais de torneios
    "Qual o próximo torneio da FURIA?",
    "Quando vai ser o próximo Major de CS2?",
    "A FURIA está classificada para quais eventos?",
    "Para quais campeonatos a FURIA vai?",

    # Combinações contextuais de jogadores
    "Como está o Fallen jogando?",
    "Quais são os jogadores do time principal?",

    # Combinações contextuais de história
    "Quantos títulos a FURIA já ganhou?",
    "Qual foi a maior conquista da FURIA?",
    "Desde quando a FURIA existe?",

    # Combinações contextuais de notícias
    "Tem novidades no time?",
    "Mudou algo no elenco?",
    "Vai ter mudança no time?",

    # Perguntas com palavras-chave individuais
    "Me fale sobre os jogos da FURIA",
    "Como está o time principal?",
    "Quais os próximos torneios?",
    "Me conta sobre o cenário atual",
    "Quais foram os últimos resultados?",
    "Me fale um pouco do histórico",
    "Alguma curiosidade sobre a FURIA?",
    "Como está o yuurih jogando?",

    # Perguntas mistas/complexas
    "Quando a FURIA joga no próximo campeonato?",
    "O Fallen vai jogar no próximo torneio?",
    "Quais são as estatísticas do time no atual campeonato?"
]

# Testando cada pergunta
for question in test_questions:
    response = handle_input(question)
    input_type = classify_input(question)
    question_type = ai_scraping_filter(question)

    print(f"Usuário: {question}\nClassificação: {input_type}\nTipo de pergunta: {question_type}\nFURIOSO: {response}\n")