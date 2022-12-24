from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import cars

class carsBlogTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username='asad', password='asadh001')
        test_user.save()

        test_post = cars.objects.create(
            purchaser=test_user,
            type='Toyata',
            car_model='prius2016',
            car_fuel = 'gasoline',
            car_size = 'mini suv',
            car_economy=" low consumption"

        )
        test_post.save()

    def test_blog_content(self):
        post = cars.objects.get(id=1)
        actual_purchaser = str(post.purchaser)
        actual_type = str(post.type)
        actual_model = str(post.car_model)
        actual_fuel=str(post.car_fuel)
        actual_size=str(post.car_size)
        actual_economy=str(post.car_economy)
        self.assertEqual(actual_purchaser, 'asad')
        self.assertEqual(actual_type, 'Toyata')
        self.assertEqual(actual_model, 'prius2016')
        self.assertEqual(actual_fuel, 'gasoline')
        self.assertEqual(actual_size, 'suv')
        self.assertEqual(actual_economy, 'high consumption')
