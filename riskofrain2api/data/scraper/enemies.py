import requests
from bs4 import BeautifulSoup
from riskofrain2api.data.scraper.helper import remove_linebreak
from riskofrain2api.data.models import (
    Enemy,
    reset_sequence
)


def clear_enemies():
    Enemy.objects.all().delete()
    reset_sequence(Enemy)


def get_enemies():
    page = 'https://riskofrain.fandom.com/wiki/'\
        'Enemies_%26_Bosses_(Risk_of_Rain_2)'

    html = requests.get(page)
    soup = BeautifulSoup(html.content, 'html.parser')

    table = soup.find("table", {'class': 'article-table'})

    enemies = table.find_all("tr")[1:]

    for enemy in enemies:
        new_enemy = Enemy()

        fields = enemy.find_all("td")

        icon = fields[0].find("img")
        if icon.has_attr('data-src'):
            new_enemy.icon = icon['data-src']
        else:
            new_enemy.icon = icon['src']

        if fields[1].has_attr('a'):
            new_enemy.name = remove_linebreak(fields[1].find("a").string)
        else:
            new_enemy.name = remove_linebreak(fields[1].text)

        new_enemy.health = remove_linebreak(fields[2].text)
        new_enemy.damage = remove_linebreak(fields[3].text)

        new_enemy.save()
