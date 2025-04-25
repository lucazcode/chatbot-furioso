from scraper import get_page
from bs4 import BeautifulSoup

# Extrai o nome + nick dos jogadores da página
def extract_players_links(my_url):
    # Obtém o conteúdo da página
    page_content = get_page(my_url)

    soup = BeautifulSoup(page_content, "html.parser")
    # Define um escopo maior para a extração
    players = soup.select("a.col-custom")

    if players:
        # Define um escopo definido para a extração
        player_links = ["https://www.hltv.org/" + player_tag.get("href") for player_tag in players]
        return player_links
    else:
        return None

team_player_links = extract_players_links("https://www.hltv.org/team/8297/furia")
print(team_player_links)