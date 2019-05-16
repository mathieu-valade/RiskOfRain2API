import requests
from bs4 import BeautifulSoup
from riskofrain2api.data.scrapper.helper import remove_linebreak
from riskofrain2api.data.models import Ability


def clear_abilities():
    Ability.objects.all().delete()


# def get_abilities():
