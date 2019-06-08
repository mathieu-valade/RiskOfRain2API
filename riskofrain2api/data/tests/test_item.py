from rest_framework.test import (
    APITestCase,
)
from riskofrain2api.data.models import (
    Item
)
from riskofrain2api.data.scraper.achievements import (
    clear_achievements,
    get_achievements
)
from riskofrain2api.data.scraper.items import (
    clear_items,
    get_items
)


class ItemTestCase(APITestCase):

    item = {'icon': 'icon',
            'name': 'name',
            'description': 'description'}

    def setUp(self):
        item = Item.objects.create(icon=self.item['icon'],
                                   name=self.item['name'],
                                   description=self.item['description'],
                                   achievement=None)
        self.item_id = item.id

    def test_get_all_items(self):
        response = self.client.get('/items', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0], self.item)

    def test_get_item(self):
        response = self.client.get(
            f'/items/{self.item_id}', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, self.item)

    def test_clear_items(self):
        clear_items()

        response = self.client.get('/items', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertCountEqual(response.data, [])

    def test_scraper_items(self):
        clear_achievements()
        get_achievements()

        clear_items()
        get_items()

        response = self.client.get('/items', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(any(response.data))
