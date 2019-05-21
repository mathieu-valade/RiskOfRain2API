from riskofrain2api.data.scrapper.achievements import (
    clear_achievements,
    get_achievements,
)

from riskofrain2api.data.scrapper.items import (
    clear_items,
    get_items,
)

from riskofrain2api.data.scrapper.characters import (
    clear_characters,
    get_characters,
)

from riskofrain2api.data.scrapper.abilities import (
    clear_abilities,
    get_abilities,
)

from riskofrain2api.data.scrapper.enemies import (
    clear_enemies,
    get_enemies,
)

from riskofrain2api.data.scrapper.levels import (
    clear_levels,
    get_levels,
)


def get_data():
    clear_achievements()
    clear_items()
    clear_characters()
    clear_abilities()
    clear_enemies()
    clear_levels()

    get_achievements()
    get_items()
    get_characters()
    get_abilities()
    get_enemies()
    get_levels()
