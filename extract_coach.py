from bs4 import BeautifulSoup

from scraper import get_page


# Extrai o nome + nick do coach da página
def extract_coach(my_url):
    # Obtém o conteúdo da página
    page_content = get_page(my_url)
    soup = BeautifulSoup(page_content, "html.parser")
    coach_tag = soup.select_one("a.right")

    if coach_tag:
        spans = coach_tag.find_all("span", class_="bold a-default")

        if spans:
            nickname = spans[0].text.strip("'")

            full_text = coach_tag.get_text(strip=True)

            full_name = full_text.replace(f"'{nickname}'", " ").strip()

            # Divide o nome completo em primeiro e último nome
            name_parts = full_name.split()

            if len(name_parts) >= 2:
                first_name = name_parts[0]
                last_name = name_parts[-1]

                # Caso o nome tenha de duas ou mais partes, insere o nick ao meio
                coach = f"{first_name} '{nickname}' {last_name}"
            else:
                # Caso seja o nome seja único, insere o nick ao final
                coach = f"{full_name} {nickname}"

            return coach
        else:
            return None
    else:
        return None