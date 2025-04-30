from scraper import get_page
from bs4 import BeautifulSoup

def extract_next_match_opponent(my_url):
    # Obtém o conteúdo da página
    page_content = get_page(my_url)
    soup = BeautifulSoup(page_content, "html.parser")

    # Verifica se não há partidas futuras
    empty_state = soup.select_one("div.empty-state span")
    if empty_state and "No upcoming matches" in empty_state.get_text():
        return None

    # Seleciona o nome do segundo time (o adversário)
    opponent_tag = soup.select_one(".team-name.team-2")
    if opponent_tag:
        opponent_name = opponent_tag.get_text(strip=True)
        return opponent_name
    return None