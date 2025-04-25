from scraper import get_page
from bs4 import BeautifulSoup

# Extrai o link do coach da página
def extract_coach_link(my_url):
    # Obtém o conteúdo da página
    page_content = get_page(my_url)
    soup = BeautifulSoup(page_content, "html.parser")

    # Encontra o link do coach
    coach_tag = soup.select_one("a.right")
    if not coach_tag:
        return None

    coach_link = "https://www.hltv.org" + coach_tag["href"]

    return coach_link

# Teste
team_coach_link = extract_coach_link("https://www.hltv.org/team/8297/furia")
print(team_coach_link)