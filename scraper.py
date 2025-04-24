import cloudscraper

# Cria o scraper para extrair dados da url
def create_scraper():
    scraper = cloudscraper.create_scraper()
    return scraper

# Extrai os dados da url
def get_page(url):
    scraper = create_scraper()
    response = scraper.get(url)
    return response.text