from riskofrain2api.data.scrapper.achievements import clear_achievements,\
                            get_achievements
from riskofrain2api.data.scrapper.items import clear_items,\
                    get_items


def get_data():
    clear_achievements()
    clear_items()

    get_achievements()
    get_items()
