from model_initializer import model

# Classifica a entrada
def ai_scraping_filter(user_text):
    # Verifica se a entrada do usuário é uma pergunta direta
    question_keywords = ["quem", "qual", "quantos", "quando", "onde", "?"]
    if any(keyword in user_text for keyword in question_keywords):
        return "factual_request"

    # Caso não seja indentificada como tal, passa para a IA definir as labels
    candidate_labels = ["factual_request", "opinion_request", "commentary_request"]
    result = model(user_text, candidate_labels)
    classification = result["labels"][0]
    return classification