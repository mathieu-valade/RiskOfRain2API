import requests
from bs4 import BeautifulSoup
from riskofrain2api.data.scraper.helper import remove_linebreak
from riskofrain2api.data.models import Achievement


def clear_achievements():
    Achievement.objects.all().delete()


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

        if fields[1].has_attr('a'):
            new_achievement.name = remove_linebreak(fields[1].find("a").string)
        else:
            new_achievement.name = remove_linebreak(fields[1].text)

        new_achievement.description = remove_linebreak(
            remove_linebreak(fields[2].text))

        new_achievement.save()
