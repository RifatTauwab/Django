# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIRequestFactory
from rest_framework import status
from rest_framework.test import APITestCase

# Create your tests here.
from Media.models import Media_Statistics

# http://www.django-rest-framework.org/api-guide/testing/#coreapiclient
# class Media_StatisticsTestCase(TestCase):
#     def setUp(self):
#         Media_Statistics.objects.create(name="test 1", played=5)
#         Media_Statistics.objects.create(name="test 2", played=6)
#
#     def test_animals_can_speak(self):
#         """Animals that can speak are correctly identified"""
#         lion = Animal.objects.get(name="lion")
#         cat = Animal.objects.get(name="cat")
#         self.assertEqual(lion.speak(), 'The lion says "roar"')
#         self.assertEqual(cat.speak(), 'The cat says "meow"')

class Media_StatisticsTests(APITestCase):
    def test_create_media_statistics(self):
        """
        Ensure we can create a new account object.
        """
        url = '/api/media/statistics/mediastat/'
        data = {'name': 'test 1', 'played': 5}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Media_Statistics.objects.count(), 1)
        self.assertEqual(Media_Statistics.objects.get().name, 'test 1')
        response = self.client.get('/api/media/statistics/mediastat/1/')
        self.assertEqual(response.data, {'id': 1, 'name': 'test 1', 'played': 5})