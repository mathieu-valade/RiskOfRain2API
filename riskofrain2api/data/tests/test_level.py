from rest_framework.test import (
    APITestCase,
)
from riskofrain2api.data.models import (
    Level
)
from riskofrain2api.data.scraper.levels import (
    clear_levels,
    get_levels
)
from riskofrain2api.data.scraper.achievements import (
    clear_achievements,
    get_achievements
)


class LevelTestCase(APITestCase):
    level = {'name': 'name',
             'title': 'title',
             'description': 'description'}

    def setUp(self):
        level = Level.objects.create(name=self.level['name'],
                                     title=self.level['title'],
                                     description=self.level
                                     ['description'])
        self.level_id = level.id

    def test_get_all_levels(self):
        response = self.client.get('/levels', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.data[0], self.level)

    def test_get_level(self):
        response = self.client.get(
            f'/levels/{self.level_id}', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.data, self.level)

    def test_clear_levels(self):
        clear_levels()

        response = self.client.get('/levels', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertCountEqual(response.data, [])

    def test_scrap_levels(self):
        clear_levels()
        get_levels()

        response = self.client.get('/levels', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(any(response.data))
