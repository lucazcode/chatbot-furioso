from bs4 import BeautifulSoup

# Extrai o nome + nick dos jogadores da página
def extract_players(page_content):
    soup = BeautifulSoup(page_content, "html.parser")
    players = soup.select("a.col-custom img.bodyshot-team-img")

    if players:
        player_names = [player.get("title").strip() for player in players]
        return player_names
    else:
        return None