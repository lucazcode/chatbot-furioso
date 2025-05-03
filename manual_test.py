import logging
from flux_control import handle_input, log_buffer
from logger import enable_debug

# Executa testes manuais com exemplos de perguntas para testar o comportamento do bot.
# Esse arquivo não faz parte do funcionamento do chatbot.

# Testes
test_questions = [
    # Exemplo de mensagens com respostas disponíveis via scraping
    "Quem são os jogadores da FURIA?",
    "Quem é o treinador da FURIA?",
    "Qual é o elenco atual da FURIA?",
    "Em qual campeonato a FURIA está jogando agora?",
    "Quando é o próximo jogo da FURIA?",
    "A próxima partida vai ser BO1 ou BO3?",
    "Qual é a fase atual da FURIA no campeonato?",
    "Quem vai ser o adversário da FURIA?",
    "Quais foram os últimos resultados da FURIA?"

    # # Mensagens genéricas/fallback
    # "Quantos anos tem a organização?",
    # "Onde fica a sede da FURIA?",
    # "Quem é o CEO da FURIA?",

    # # Mensagens contextuais de jogos
    # "Quando é o próximo jogo da FURIA?",
    # "Onde posso assistir ao jogo da FURIA?",
    # "Contra quem a FURIA vai jogar?",
    # "Qual a data do próximo match?",

    # # Mensagens com combinações contextuais de torneios
    # "Quando vai ser o próximo Major de CS2?",
    # "Para quais campeonatos a FURIA vai?",

    # # Mensagens com combinações contextuais de jogadores
    # "Como está o Fallen jogando?",
    # "Quais são os jogadores do time principal?",

    # # Mensagens com combinações contextuais de história
    # "Quantos títulos a FURIA já ganhou?",
    # "Qual foi a maior conquista da FURIA?",
    # "Desde quando a FURIA existe?",

    # # Mensagens com palavras-chave individuais
    # "Me conta sobre o cenário atual",
    # "Quais foram os últimos resultados?",
    # "Me fale um pouco do histórico",
    # "Alguma curiosidade sobre a FURIA?",
    # "Como o yuurih está jogando?"
]

# Habilita ou desabilita os logs no terminal (opcional)
enable_debug()

# Testando cada pergunta
print("[ENTRADAS E SAÍDAS]\n")
for message in test_questions:
    response = handle_input(message)
    print("-" * 40)
    print(f"Usuário: {message}")
    print(f"FURIOSO: {response}")
    print("-" * 40 + "\n")

if logging.getLogger().isEnabledFor(logging.DEBUG):
    print("[LOG DE EXECUÇÃO]\n")
    for log in log_buffer:
        print(log)