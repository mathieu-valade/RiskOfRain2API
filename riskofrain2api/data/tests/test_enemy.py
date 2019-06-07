from rest_framework.test import (
    APITestCase,
)
from riskofrain2api.data.models import (
    Enemy
)
from riskofrain2api.data.scraper.enemies import (
    clear_enemies,
    get_enemies
)


class AchievementTestCase(APITestCase):
    enemy = {'icon': 'icon',
             'name': 'name',
             'health': 'health',
             'damage': 'damage'}

    def setUp(self):
        enemy = Enemy.objects.create(icon=self.enemy['icon'],
                                     name=self.enemy['name'],
                                     health=self.enemy
                                     ['health'],
                                     damage='damage')
        self.enemy_id = enemy.id

    def test_get_all_enemies(self):
        response = self.client.get('/enemies', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.data[0], self.enemy)

    def test_get_enemey(self):
        response = self.client.get(
            f'/enemies/{self.enemy_id}', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.data, self.enemy)

    def test_clear_enemies(self):
        clear_enemies()

        response = self.client.get('/enemies', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertCountEqual(response.data, [])

    def test_scrap_enemies(self):
        clear_enemies()
        get_enemies()

        response = self.client.get('/enemies', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(any(response.data))
