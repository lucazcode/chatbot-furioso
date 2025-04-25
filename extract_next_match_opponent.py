from scraper import get_page
from bs4 import BeautifulSoup

def extract_opponent(my_url):
    # Obtém o conteúdo da página
    page_content = get_page(my_url)
    soup = BeautifulSoup(page_content, "html.parser")

    # Seleciona o nome do segundo time (o adversário)
    opponent_tag = soup.select_one(".team-name.team-2")
    if opponent_tag:
        opponent_name = opponent_tag.get_text(strip=True)
        return opponent_name
    else:
        return None

# Teste
opponent = extract_opponent("https://www.hltv.org/team/5973/liquid#tab-matchesBox")
print(opponent)