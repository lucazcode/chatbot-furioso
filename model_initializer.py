from transformers import pipeline

model = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")