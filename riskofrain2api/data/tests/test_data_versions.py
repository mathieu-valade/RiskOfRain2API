from rest_framework.test import (
    APITestCase,
)
from riskofrain2api.data.models import (
    DataVersion
)


class DataVersionTestCase(APITestCase):

    def setUp(self):
        data_version = DataVersion.objects.create()
        self.data_version_id = data_version.id
        self.data_version_dict = {
            'date': data_version.date.strftime("%Y%m%d%H%M%S")}

    def test_get_all_dataversions(self):
        response = self.client.get('/dataversions', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.data[0], self.data_version_dict)

    def test_get_data_version(self):
        response = self.client.get(
            f'/dataversions/{self.data_version_id}', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.data, self.data_version_dict)
