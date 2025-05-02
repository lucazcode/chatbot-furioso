from scraper import get_page
from bs4 import BeautifulSoup

# Função que extrai o link da próxima partida
def extract_next_match_url(my_url):
    page_content = get_page(my_url)
    soup = BeautifulSoup(page_content, "html.parser")

    empty_state = soup.select_one("div.empty-state span")
    if empty_state and "No upcoming matches" in empty_state.get_text():
        return None

    match_rows = soup.select("tr.team-row")
    for row in match_rows:
        link_tag = row.select_one("td.matchpage-button-cell a.matchpage-button")
        if link_tag and "href" in link_tag.attrs:
            match_url = "https://www.hltv.org" + link_tag["href"]
            return match_url
    return None

# Função que extrai o formato da partida da página
def extract_next_match_format_and_stage(team_url):

    # Descobre a URL da partida
    match_url = extract_next_match_url(team_url)

    if not match_url:
        return None

    match_page_content = get_page(match_url)
    match_soup = BeautifulSoup(match_page_content, "html.parser")

    # Procura a caixa de veto com o formato
    format_tag = match_soup.select_one("div.standard-box.veto-box div.padding.preformatted-text")
    if format_tag:
        format_stage_info = format_tag.get_text(strip=True)

        # Divide as informações se houver "*"
        if "*" in format_stage_info:
            match_format, match_stage = format_stage_info.split("*", 1)
            return {
                "format": match_format.strip(),
                "stage": match_stage.strip()
            }
    return None
