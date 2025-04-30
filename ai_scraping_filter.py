from model_initializer import model

# Função de classificação de entrada
def ai_scraping_filter(user_text):
    # Definir as labels (categorias)
    candidate_labels = ["factual_request", "opinion_request", "commentary_request"]
    result = model(user_text, candidate_labels)
    return result["labels"][0]