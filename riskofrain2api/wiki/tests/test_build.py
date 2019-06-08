from rest_framework.test import (
    APITestCase,
)
from riskofrain2api.data.models import (
    Item,
    Achievement,
)


class BuildTestCase(APITestCase):

    def test_item_no_achievement(self):
        item_dict = {'icon': 'icon',
                     'name': "Soldier's Syringe",
                     'description':
                     'Increases attack speed by 15%. (+15% per stack).'}

        expected_data = {
            'stats': ['Increases attack speed by 15%.'],
            'achievements': []
        }

        Item.objects.create(icon=item_dict['icon'],
                            name=item_dict['name'],
                            description=item_dict['description'])

        response = self.client.post(
            '/build/', {"Soldier's Syringe": 1}, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.data, expected_data)
