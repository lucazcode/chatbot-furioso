from scraper import get_page
from bs4 import BeautifulSoup

# Extrai o nome do campeonato da próxima partida
def extract_championships(my_url):
    # Obtém o conteúdo da página
    page_content = get_page(my_url)
    soup = BeautifulSoup(page_content, "html.parser")

    # Encontrar o container dos eventos principais
    upcoming_holder = soup.find('div', class_='upcoming-events-holder')
    if not upcoming_holder:
        return None

    # Define um escopo maior para a extração
    championships_info = soup.find_all('a', class_='a-reset ongoing-event')
    if not championships_info:
        return None

    championships_list = []

    # Extrair os nomes dos eventos e adicionar à lista
    for event in championships_info:
        championship_name = event.find('div', class_='eventbox-eventname').text.strip()
        championships_list.append(championship_name)

        if len(championships_list) >= 3:
            break

    return championships_list