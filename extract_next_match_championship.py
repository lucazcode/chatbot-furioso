from scraper import get_page
from bs4 import BeautifulSoup

# Extrai o nome do campeonato da próxima partida
def extract_next_match_championship(my_url):
    # Obtém o conteúdo da página
    page_content = get_page(my_url)
    soup = BeautifulSoup(page_content, "html.parser")

    # Verifica se não há partidas futuras
    empty_state = soup.select_one("div.empty-state")
    if empty_state:
        return None

    # Define um escopo maior para a extração
    match_info = soup.select_one("table.match-table")
    if not match_info:
        return None

    match_championship_tag = match_info.select_one(".event-header-cell a.a-reset")
    match_championship_name = match_championship_tag.getText() if match_championship_tag else "Informação Indisponível"

    return match_championship_name

# Teste
next_match_info = extract_next_match_championship("https://www.hltv.org/team/5973/liquid#tab-matchesBox")
print(next_match_info)