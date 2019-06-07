from rest_framework.test import (
    APITestCase,
)
from riskofrain2api.data.models import (
    Character,
)
from riskofrain2api.data.scraper.characters import (
    clear_characters,
    get_characters
)
from riskofrain2api.data.scraper.achievements import (
    clear_achievements,
    get_achievements
)


class AbilityTestCase(APITestCase):

    character = {'icon': 'icon',
                 'name': 'name',
                 'health': 'health'}

    def setUp(self):
        character = Character.objects.create(icon=self.character['icon'],
                                             name=self.character['name'],
                                             health=self.character['health'],
                                             achievement=None)
        self.character_id = character.id

    def test_get_all_characters(self):
        response = self.client.get('/characters', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0], self.character)

    def test_get_character(self):
        response = self.client.get(
            f'/characters/{self.character_id}', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, self.character)

    def test_clear_characters(self):
        clear_characters()

        response = self.client.get('/characters', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertCountEqual(response.data, [])

    def test_scraper_characters(self):
        clear_achievements()
        get_achievements()

        clear_characters()
        get_characters()

        response = self.client.get('/characters', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(any(response.data))
