from scraper import get_page
from bs4 import BeautifulSoup

# Função que extrai o link da próxima partida
def extract_next_match_url(my_url):
    # Obtém o conteúdo da página do time
    page_content = get_page(my_url)
    soup = BeautifulSoup(page_content, "html.parser")

    # Verifica se não há partidas futuras
    empty_state = soup.select_one("div.empty-state span")
    if empty_state and "No upcoming matches" in empty_state.get_text():
        return None

    # Encontra o link para a próxima partida
    match_link_tag = soup.select_one("td.matchpage-button-cell a.matchpage-button")
    if match_link_tag:
        match_url = "https://www.hltv.org" + match_link_tag["href"]
        return match_url
    return None

# Função que extrai o formato da partida da página
def extract_next_match_format_and_stage(match_url):
    if not match_url:
        return None

    # Extrai os dados da página
    match_page_content = get_page(match_url)
    match_soup = BeautifulSoup(match_page_content, "html.parser")

    # Extrai o formato da partida
    format_tag = match_soup.select_one("div.standard-box.veto-box div.padding.preformatted-text")
    if format_tag:
        format_stage_info = format_tag.get_text(strip=True)
        # Divide as informações conjuntas
        match_format, match_stage = format_stage_info.split("*")
        return {
            "format": match_format.strip(),
            "stage": match_stage.strip()
        }
    return None