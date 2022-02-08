import requests
import json
from bs4 import BeautifulSoup


def main():
    PROFESSION_LIST_URL = "https://psz.praca.gov.pl/rynek-pracy/bazy-danych/klasyfikacja-zawodow-i-specjalnosci/wyszukiwarka-opisow-zawodow//-/klasyfikacja_zawodow/litera/{letter}"  # noqa: E501
    PROF_START_LETTERS = [
        "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "Ł",
        "M", "N", "O", "P", "R", "S", "Ś", "T", "U", "W", "Z", "Ż"
    ]

    professions = {letter: [] for letter in PROF_START_LETTERS}
    for letter in PROF_START_LETTERS:
        response = requests.get(url=PROFESSION_LIST_URL.format(letter=letter))
        if not response.ok:
            continue

        soup = BeautifulSoup(response.text, 'html.parser')
        professions_table = soup.find(
            "table", attrs={
                "class": "job-classification_search-results results-grid"
            }
        )

        prof_cells = professions_table.find_all("td", attrs={"class": "last"})
        for cell in prof_cells:
            for txt in cell.a.stripped_strings:
                profession = txt
                professions[letter].append(profession)
                break

    with open("professions.json", "w") as f:
        json.dump(professions, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
