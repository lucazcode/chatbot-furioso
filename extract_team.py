from scraper import get_page
from extract_players import extract_players
from extract_coach import extract_coach


def extract_team(my_url):

    # Extrai os jogadores
    players = extract_players(my_url)
    if not players:
        return None

    # Extrai o coach
    coach = extract_coach(my_url)
    if not coach:
        return None

    return {"players": players, "coach": coach}