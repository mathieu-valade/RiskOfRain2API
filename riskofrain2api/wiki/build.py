from riskofrain2api.wiki.parser import parse_description
from riskofrain2api.data.models import (
    Item,
    Achievement,
)
from django.core.exceptions import ObjectDoesNotExist


def get_stats(item_name, item_count):
    try:
        item = Item.objects.get(name=item_name)
        description = parse_description(item.description)

        stat_list = []

        for param, multi in zip(description['param'], description['multi']):
            stat_list.append(str(
                max(0, int(param) + (item_count - 1) * int(multi))))

        return description['text'].format(* stat_list)

    except ObjectDoesNotExist:
        return None


def get_achievements(item_name):
    try:
        achievement = Achievement.objects.get(item__name=item_name)
        return achievement.name
    except ObjectDoesNotExist:
        return None