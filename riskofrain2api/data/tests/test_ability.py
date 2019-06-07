from rest_framework.test import (
    APITestCase,
)
from riskofrain2api.data.models import (
    Character,
    Ability,
)
from riskofrain2api.data.scraper.characters import (
    clear_characters,
    get_characters
)
from riskofrain2api.data.scraper.abilities import (
    clear_abilities,
    get_abilities
)


class AbilityTestCase(APITestCase):
    ability = {'icon': 'path',
               'name': 'ability1',
               'description': 'description',
               'cooldown': 'cooldown',
               'character_name': 'character'}

    def setUp(self):
        character = Character.objects.create(icon='icon',
                                             name='character',
                                             health='health',
                                             achievement=None)
        ability = Ability.objects.create(icon=self.ability['icon'],
                                         name=self.ability['name'],
                                         description=self.ability
                                         ['description'],
                                         cooldown=self.ability['cooldown'],
                                         character=character)
        self.ability_id = ability.id

    def test_get_all_abilities(self):
        response = self.client.get('/abilities', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0], self.ability)

    def test_get_ability(self):
        response = self.client.get(
            f'/abilities/{self.ability_id}', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, self.ability)

    def test_clear_abilities(self):
        clear_abilities()

        response = self.client.get('/abilities', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertCountEqual(response.data, [])

    def test_scraper_abilities(self):
        clear_characters()
        get_characters()

        clear_abilities()
        get_abilities()

        response = self.client.get('/abilities', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(any(response.data))
