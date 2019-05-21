from bs4 import BeautifulSoup
import requests
from riskofrain2api.data.scraper.helper import remove_linebreak
from riskofrain2api.data.models import (
    Ability,
    Character,
)


def clear_abilities():
    Ability.objects.all().delete()


def get_abilities():
    base_page = 'https://riskofrain.fandom.com'
    page = base_page + '/wiki/Characters_(RoR2)'

    html = requests.get(page)

    soup = BeautifulSoup(html.content, 'html.parser')
    table = soup.find("table", {'class': 'article-table'})
    characters = table.find_all("tr")[1:]

    for character in characters:

        fields = character.find_all("td")
        character_page = fields[1].find('a')['href']

        character_html = requests.get(base_page + character_page)
        character_soup = BeautifulSoup(character_html.content, 'html.parser')

        character_table = character_soup.find(
            "table", {'class': 'article-table'}
        )

        abilities = character_table.find_all("tr")
        character_name = fields[1].find('a').text
        existing_character = Character.objects.get(name=character_name)

        for ability in abilities:
            new_ability = Ability()
            ability_fields = ability.find_all("td")

            new_ability.character = existing_character
            new_ability.name = remove_linebreak(
                ability_fields[0].find("b").text
            )

            icon = ability_fields[0].find("img")
            if icon is not None:
                if icon.has_attr('data-src'):
                    new_ability.icon = icon['data-src']
                else:
                    new_ability.icon = icon['src']

            # new_ability.description = remove_linebreak(
            #         ability_fields[1].text
            # )
            if len(ability_fields) > 1:
                new_ability.description = remove_linebreak(
                    ability_fields[1].text
                )

            new_ability.save()
