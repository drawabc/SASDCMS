from django.test import TestCase
from django.urls import reverse
from django.test import Client
from django.urls import resolve
import CMSApp.views as cv

class ViewURLsTest(TestCase):
    def test_home_pass(self):
        expected = cv.home
        found = resolve('/')
        self.assertEqual(found.func, expected)

    def test_input_pass(self):
        expected = cv.input
        found = resolve('/input/')
        self.assertEqual(found.func, expected)

    def test_detail_pass(self):
        expected = cv.detail
        found = resolve('/detail/')
        self.assertEqual(found.func, expected)

    def test_archive_pass(self):
        expected = cv.archive
        found = resolve('/archive/')
        self.assertEqual(found.func, expected)
