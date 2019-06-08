import os
from tablib import Dataset
from import_export import resources
from django.conf import settings
from riskofrain2api.data.models import DataVersion
from riskofrain2api.data.admin import (
    AbilityResource,
    AchievementResource,
    CharacterResource,
    EnemyResource,
    ItemResource,
    LevelResource,
)
from riskofrain2api.data.models import (
    Ability,
    Achievement,
    Character,
    Enemy,
    Item,
    Level,
)

from riskofrain2api.data.scraper.core import (
    clear_data
)

SAVE_ROOT = settings.SAVE_ROOT

RESOURCE_CLASS = {
    'achievement.json': AchievementResource(),
    'character.json': CharacterResource(),
    'ability.json': AbilityResource(),
    'enemy.json': EnemyResource(),
    'item.json': ItemResource(),
    'level.json': LevelResource(),
}


MODEL_CLASS = {
    'achievement.json': Achievement,
    'character.json': Character,
    'ability.json': Ability,
    'enemy.json': Enemy,
    'item.json': Item,
    'level.json': Level,
}


def export_data():
    data_version = DataVersion()
    data_version.save()

    version_name = data_version.date.strftime("%Y%m%d%H%M%S")
    folder_name = os.path.join(SAVE_ROOT, version_name)
    os.makedirs(folder_name, exist_ok=True)

    for name, resource in RESOURCE_CLASS.items():
        dataset = resource.export()
        file_name = os.path.join(SAVE_ROOT, version_name, name)
        print(file_name)
        with open(file_name, 'x') as save_file:
            save_file.write(dataset.json)


def import_data(version):
    filename = f'save/{version}'
    if not os.path.isdir(filename):
        return

    clear_data()

    for name, model_class in MODEL_CLASS.items():
        try:
            resource = resources.modelresource_factory(model=model_class)()
            dataset = Dataset()
            import_file = open(f'{filename}/{name}')
            dataset.load(import_file.read())
            dataset.append_col(col=range(1, dataset.height + 1), header='id')

            result = resource.import_data(dataset, dry_run=True,
                                          raise_errors=True)
            if not result.has_errors():
                resource.import_data(dataset, dry_run=False, raise_errors=True)
        except FileNotFoundError:
            pass
