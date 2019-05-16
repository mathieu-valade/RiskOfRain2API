import requests
from bs4 import BeautifulSoup
from riskofrain2api.data.scrapper.helper import remove_linebreak
from riskofrain2api.data.models import (
    Character,
    Achievement
)


def clear_characters():
    Character.objects.all().delete()


def get_characters():
    base_page = 'https://riskofrain.fandom.com'
    page = base_page + '/wiki/Characters_(RoR2)'
    html = requests.get(page)
    soup = BeautifulSoup(html.content, 'html.parser')
    table = soup.find("table", {'class': 'article-table'})
    characters = table.find_all("tr")[1:]

    for character in characters:
        new_character = Character()

        fields = character.find_all("td")
        icon = fields[0].find("img")
        if icon is not None:
            if icon.has_attr('data-src'):
                new_character.icon = icon['data-src']
            else:
                new_character.icon = icon['src']

        character_page = fields[1].find('a')['href']
        new_character.name = fields[1].find('a').text

        if fields[2].has_attr('a'):
            achievement_name = remove_linebreak(fields[2].find("a").string)
        else:
            achievement_name = remove_linebreak(fields[2].text)

        if achievement_name != 'Unlocked by default':
            new_character.achievement = Achievement.objects.get(
                name=achievement_name)

        character_html = requests.get(base_page + character_page)
        character_soup = BeautifulSoup(character_html.content, 'html.parser')
        description_div = character_soup.find("div", {'id': 'mw-content-text'})
        description = ""

        for child in description_div.children:
            child_tag = child.name
            print(child_tag)
            if child_tag == 'dl':
                continue
            if child_tag == 'h2':
                break

            if isinstance(child.string, str):
                description += child.string

        new_character.description = description
        base_hp_div = character_soup.find("div", {'data-source': 'BaseHP'})
        base_hp = base_hp_div.find('div').text
        new_character.health = base_hp

        new_character.save()
