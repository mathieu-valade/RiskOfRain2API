from riskofrain2api.data.scraper.achievements import (
    clear_achievements,
    get_achievements,
)

from riskofrain2api.data.scraper.items import (
    clear_items,
    get_items,
)

from riskofrain2api.data.scraper.characters import (
    clear_characters,
    get_characters,
)

from riskofrain2api.data.scraper.abilities import (
    clear_abilities,
    get_abilities,
)

from riskofrain2api.data.scraper.enemies import (
    clear_enemies,
    get_enemies,
)

from riskofrain2api.data.scraper.levels import (
    clear_levels,
    get_levels,
)

from riskofrain2api.data.data_access.data_version import export_data


def clear_data():
    clear_achievements()
    clear_items()
    clear_characters()
    clear_abilities()
    clear_enemies()
    clear_levels()


def get_data():
    get_achievements()
    get_items()
    get_characters()
    get_abilities()
    get_enemies()
    get_levels()


def clean_get_data():
    clear_data()
    get_data()
