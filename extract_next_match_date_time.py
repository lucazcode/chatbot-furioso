from scraper import get_page
from bs4 import BeautifulSoup
from datetime import datetime, timedelta, UTC

# Extrai a data e horário da próxima partida
def extract_next_match_date_time(my_url):
    # Obtém o conteúdo da página
    page_content = get_page(my_url)
    soup = BeautifulSoup(page_content, "html.parser")

    # Verifica se não há partidas futuras
    empty_state = soup.select_one("div.empty-state span")
    if empty_state and "No upcoming matches" in empty_state.get_text():
        return None

    # Extrai o timestamp Unix
    time_span = soup.select_one("table.match-table span[data-unix]")
    if not time_span or not time_span.has_attr("data-unix"):
        return None

    # Trata o valor que vem em milissegundos
    unix_timestamp = int(time_span["data-unix"]) / 1000
    match_datetime_utc = datetime.fromtimestamp(unix_timestamp, tz=UTC)

    # Converte para UTC-3 (Brasil)
    match_datetime_utc3 = match_datetime_utc - timedelta(hours=3)

    # Formata data e hora
    date_str = match_datetime_utc3.strftime("%d/%m/%Y")
    time_str = match_datetime_utc3.strftime("%H:%M")

    return {
        "date": date_str,
        "time": time_str
    }