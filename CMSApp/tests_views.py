from django.test import TestCase
from django.urls import reverse
from django.test import Client
from django.urls import resolve
from CMSApp.views import *

class ViewURLsTest(TestCase):
    def test_home_pass(self):
        expected = home
        found = resolve('/')
        self.assertEqual(found.func, expected)

    def test_input_pass(self):
        expected = input
        found = resolve('/input/')
        self.assertEqual(found.func, expected)

    def test_archive_pass(self):
        expected = archive
        found = resolve('/archive/')
        self.assertEqual(found.func, expected)