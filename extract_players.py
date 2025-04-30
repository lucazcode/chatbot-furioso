from bs4 import BeautifulSoup
from scraper import get_page


# Extrai o nome + nick dos jogadores da página
def extract_players(my_url):
    # Obtém o conteúdo da página
    page_content = get_page(my_url)
    soup = BeautifulSoup(page_content, "html.parser")

    # Define um escopo maior para a extração
    players = soup.select("a.col-custom img.bodyshot-team-img")

    if players:
        # Define um escopo definido para a extração
        player_names = [player.get("title").strip() for player in players]
        return player_names
    else:
        return None