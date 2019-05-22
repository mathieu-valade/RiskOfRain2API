import os
from riskofrain2api.data.models import DataVersion
from riskofrain2api.data.admin import (
    AbilityResource,
    AchievementResource,
    CharacterResource,
    EnemyResource,
    ItemResource,
    LevelResource,
)

SAVE_ROOT = 'save'

RESOURCE_DICT = {
    'achievement.json': AchievementResource(),
    'character.json': CharacterResource(),
    'ability.json': AbilityResource(),
    'enemy.json': EnemyResource(),
    'item.json': ItemResource(),
    'level.json': LevelResource(),
}


def export_data():
    data_version = DataVersion()
    data_version.save()

    version_name = data_version.date.strftime("%Y%m%d%H%M%S")
    folder_name = os.path.join(SAVE_ROOT, version_name)
    os.makedirs(folder_name, exist_ok=True)
    for name, resource in RESOURCE_DICT.items():
        dataset = resource.export()
        file_name = os.path.join(SAVE_ROOT, version_name, name)
        with open(file_name, 'x') as save_file:
            save_file.write(dataset.json)
