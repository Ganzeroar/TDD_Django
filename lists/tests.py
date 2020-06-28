from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_page

class HomePageTest(TestCase):
    '''test home page'''

    def test_home_page_returns_correct_html(self):
        '''test home page returns correct html'''
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')