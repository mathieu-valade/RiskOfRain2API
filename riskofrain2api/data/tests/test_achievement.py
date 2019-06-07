from rest_framework.test import (
    APITestCase,
)
from riskofrain2api.data.models import (
    Achievement
)
from riskofrain2api.data.scraper.achievements import (
    clear_achievements,
    get_achievements
)


class AchievementTestCase(APITestCase):
    achievement = {'icon': 'icon',
                   'name': 'name',
                   'description': 'description'}

    def setUp(self):
        achievement = Achievement.objects.create(icon=self.achievement['icon'],
                                                 name=self.achievement['name'],
                                                 description=self.achievement
                                                 ['description'])
        self.achievement_id = achievement.id

    def test_get_all_achievements(self):
        response = self.client.get('/achievements', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.data[0], self.achievement)

    def test_get_achievement(self):
        response = self.client.get(
            f'/achievements/{self.achievement_id}', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.data, self.achievement)

    def test_clear_achievements(self):
        clear_achievements()

        response = self.client.get('/achievements', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertCountEqual(response.data, [])

    def test_scrap_achievements(self):
        clear_achievements()
        get_achievements()

        response = self.client.get('/achievements', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(any(response.data))
