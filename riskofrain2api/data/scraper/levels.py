import requests

from bs4 import BeautifulSoup
from riskofrain2api.data.scrapper.helper import remove_linebreak
from riskofrain2api.data.models import (
    Level,
)


def clear_levels():
    Level.objects.all().delete()


def get_levels():
    page = 'https://riskofrain.fandom.com/wiki/Environments_(Risk_of_Rain_2)'

    html = requests.get(page)
    soup = BeautifulSoup(html.content, 'html.parser')

    content = soup.find("div", {"id": "mw-content-text"})

    children = content.findChildren()

    new_level = None

    for child in children:
        if child.name == "h3":
            if new_level is None:
                new_level = Level()
            else:
                new_level.save()
                new_level = Level()
            new_level.name = child.find('b').text

        elif new_level is not None and child.name == "p":
            text = remove_linebreak(child.text)
            if text.startswith('\"') and text.endswith('\"'):
                new_level.title = text[1:-1]
            else:
                descriptions = [new_level.description, text]
                new_level.description += ' '.join(filter(None, descriptions))

    new_level.save()
