import logging

# Silencia logging externo de bibliotecas
for noisy_module in ["urllib3", "requests", "transformers", "torch", "httpx"]:
    logging.getLogger(noisy_module).setLevel(logging.CRITICAL)

def setup_logging(level=logging.CRITICAL):
    # Remove handlers antigos
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    # Configura o sistema de logging global
    logging.basicConfig(
        # Define o nível de logging global
        level=level,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

def enable_debug():
    # Ativa o logging globalmente
    setup_logging(logging.DEBUG)