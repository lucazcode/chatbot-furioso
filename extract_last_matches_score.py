from scraper import get_page
from bs4 import BeautifulSoup

def extract_last_matches_score(my_url):
    # Obtém o conteúdo da página
    page_content = get_page(my_url)
    soup = BeautifulSoup(page_content, "html.parser")

    # Encontra a seção "Recent results" de forma flexível (verifique se o título está correto)
    recent_results_header = soup.find("h2", string=lambda text: text and "recent" in text.lower())

    # Se a seção "Recent results" não for encontrada, retorna None
    if not recent_results_header:
        return None

    # Encontra a tabela de resultados recentes após o título "Recent results"
    recent_results_table = recent_results_header.find_next("table", class_="table-container match-table")

    # Se a tabela de resultados não for encontrada, retorna None
    if not recent_results_table:
        return None

    # Seleciona as linhas de partidas dentro da tabela
    matches_rows = recent_results_table.select("tbody tr.team-row")

    # Se não encontrar nenhuma linha de partida
    if not matches_rows:
        return None

    last_matches = []

    # Itera sobre as partidas encontradas
    for row in matches_rows:
        match_data = {}

        # Extrai a data da partida
        date_tag = row.select_one("td.date-cell span")
        if date_tag:
            match_data['date'] = date_tag.get_text(strip=True)

        # Extrai os times e o placar
        team1_tag = row.select_one("td .team-name.team-1")
        team2_tag = row.select_one("td .team-name.team-2")
        score_tag = row.select_one("td .score-cell")

        # Se todos os dados necessários estiverem presentes, salva a partida
        if team1_tag and team2_tag and score_tag:
            match_data['team1'] = team1_tag.get_text(strip=True)
            match_data['team2'] = team2_tag.get_text(strip=True)
            match_data['score'] = score_tag.get_text(strip=True).replace("\n", " ").strip()

        # Extrai o link para a partida
        match_link_tag = row.select_one("td .stats-button a")
        if match_link_tag:
            match_data['match_link'] = "https://www.hltv.org" + match_link_tag["href"]

        # Adiciona a partida à lista de últimas partidas
        last_matches.append(match_data)

    return last_matches