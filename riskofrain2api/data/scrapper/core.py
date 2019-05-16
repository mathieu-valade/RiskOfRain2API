from riskofrain2api.data.scrapper.achievements import (
    clear_achievements,
    get_achievements
)

from riskofrain2api.data.scrapper.items import (
    clear_items,
    get_items
)

from riskofrain2api.data.scrapper.characters import (
    clear_characters,
    get_characters
)


def get_data():
    clear_achievements()
    clear_items()
    clear_characters()

    get_achievements()
    get_items()
    get_characters()
