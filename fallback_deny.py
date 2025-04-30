import random

# Função que lida com entradas fora do escopo das keywords com respostas de fallback
def fallback_deny(user_text):

    # Definir categorias de resposta
    polite_responses = [
        "Desculpe, não consigo te ajudar com isso. Pergunte-me sobre a FURIA ou CS!",
        "Não posso ajudar com isso. Vamos falar sobre o time da FURIA ou sobre CS?",
        "Eu adoraria ajudar, mas preciso que a pergunta seja sobre a FURIA ou CS.",
        "Ops, isso não está no meu escopo. Pergunte-me sobre o time da FURIA ou CS!",
        "Isso não é algo que posso responder, mas posso te ajudar com informações sobre a FURIA ou CS!"
    ]

    fun_responses = [
        "Ah, essa é uma boa pergunta, mas não é algo que eu saiba. Que tal perguntar sobre o time da FURIA?",
        "Hmm, essa está fora do meu alcance, mas vou te contar: a FURIA é top no CS! Quer saber mais?",
        "Essa não é minha praia! Mas posso te contar tudo sobre a FURIA e o CS. Vamos lá!",
        "Poxa, isso não é bem a minha área de especialização... Vamos voltar para o CS ou o time da FURIA?",
        "Você me pegou, não posso ajudar aqui! Mas, e o time da FURIA? Algo sobre CS?"
    ]

    respectful_responses = [
        "Sinto muito, não posso responder a isso. Minha especialidade é falar sobre a FURIA e CS.",
        "Lamento, mas isso não está dentro do que eu posso responder. Que tal perguntar sobre a FURIA ou CS?",
        "Infelizmente, não posso ajudar com isso. Fico à disposição para falar sobre o time da FURIA e CS.",
        "Não tenho informações sobre isso. Por favor, pergunte-me sobre a FURIA ou o CS.",
        "Desculpe, isso não é algo que eu possa ajudar. Vamos falar sobre o time da FURIA ou CS?"
    ]

    humorous_responses = [
        "Oops! Eu não sei nada sobre isso... Mas se você quiser, posso te contar tudo sobre a FURIA! 😉",
        "Eu adoraria ajudar, mas parece que essa é uma pergunta que não está no meu radar... Quer saber mais sobre CS?",
        "Ah, você quer saber sobre outra coisa? Vou ficar com a FURIA e o CS, se você não se importar! 😄",
        "Uau, que pergunta interessante... mas isso não é o meu forte. Vou te dar uma dica: FURIA é incrível no CS! 😎",
        "Haha, essa foi boa! Mas vamos focar na FURIA e no CS, que é onde eu sou expert! 😜"
    ]

    # Escolhe o tipo de resposta dependendo do tom da pergunta
    if "por favor" in user_text.lower() or "desculpe" in user_text.lower():
        # Se o usuário for educado, responder de forma mais formal e respeitosa
        response = random.choice(respectful_responses)
    elif any(word in user_text.lower() for word in ["qual", "porque", "como", "quem", "o que"]):
        # Respostas mais "divertidas" para perguntas com maior curiosidade
        response = random.choice(fun_responses)
    elif "?" in user_text or "?" in user_text[-1]:
        # Respostas humorísticas para perguntas diretas
        response = random.choice(humorous_responses)
    else:
        # Se a pergunta estivem altamente fora do escopo, retorna uma resposta educada e neutra
        response = random.choice(polite_responses) + "\nSe quiser informações detalhadas sobre nosso time, se liga nesse link:\n[https://www.hltv.org/team/8297/furia]"

    return response
