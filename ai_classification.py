from model_initializer import model

def classify_input(user_text):
    # Classificar se é pergunta ou comentário
    candidate_labels = ["question", "commentary"]
    result = model(user_text, candidate_labels)
    classification = result["labels"][0]
    return classification
