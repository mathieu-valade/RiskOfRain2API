import requests
from bs4 import BeautifulSoup
from riskofrain2api.data.scrapper.helper import remove_linebreak
from riskofrain2api.data.models import (
    Item,
    Achievement
)


def clear_items():
    Item.objects.all().delete()


def get_items():

    page = 'https://riskofrain.fandom.com/wiki/Item_(Risk_of_Rain_2)'

    html = requests.get(page)

    soup = BeautifulSoup(html.content, 'html.parser')

    tables = soup.find_all("table", {'class': 'article-table'})

    for table in tables:
        items = table.find_all("tr")[1:]
        for item in items:

            new_item = Item()

            fields = item.find_all("td")
            icon = fields[0].find("img")
            if icon.has_attr('data-src'):
                new_item.icon = icon['data-src']
            else:
                new_item.icon = icon['src']

            new_item.name = fields[1].find("a").string
            new_item.description = remove_linebreak(fields[2].text)
            achievement_name = ""

            if fields[2].has_attr('a'):
                achievement_name = remove_linebreak(fields[3].find("a").string)
            else:
                achievement_name = remove_linebreak(fields[3].text)

            if achievement_name != 'Default':
                new_item.achievement = Achievement.objects.get(
                    name=achievement_name)

            new_item.save()
