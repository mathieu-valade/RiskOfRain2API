from bs4 import BeautifulSoup
import requests
from riskofrain2api.data.models import Achievement,\
                                        Item


def remove_linebreak(text):
    text = text.replace('\n', '')
    return text


def get_achievements():

    page = 'https://riskofrain.fandom.com/wiki/Challenges'

    html = requests.get(page)

    soup = BeautifulSoup(html.content, 'html.parser')

    table = soup.find("table", {'class': 'article-table'})

    achievements = table.find_all("tr")[1:]

    for achievement in achievements:
        new_achievement = Achievement()

        fields = achievement.find_all("td")
        icon = fields[0].find("img")
        if icon.has_attr('data-src'):
            new_achievement.icon = icon['data-src']
        else:
            new_achievement.icon = icon['src']


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


def get_data():
    Achievement.objects.all().delete()
    get_achievements()
    get_items()
