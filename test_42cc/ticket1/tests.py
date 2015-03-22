# -*- coding: utf-8 -*-
"""
    Functional tests for my application
"""

from django.test import LiveServerTestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from models import Person


class Ticket1Test(LiveServerTestCase):
    """ The ticket1 test case """
    fixtures = ['test.json']

    def setUp(self):
        self.wd = webdriver.Firefox()

    def tearDown(self):
        self.wd.quit()

    def test_database(self):
        queryset = Person.objects.all()
        if len(queryset) > 1:
            self.fail("There shouldn't be another database entry")

    def test_auth(self):
        self.wd.get('%s%s' % (self.live_server_url, '/admin/'))
        self.wd.find_element_by_css_selector('#id_username').send_keys(User.objects.first().username)
        self.wd.find_element_by_css_selector('#id_password').send_keys(User.objects.first().password)
        self.wd.find_element_by_xpath('//input[@value="Log in"]').click()
        self.wd.find_element_by_css_selector('#content-main')

    def test_page_info(self):
        """ Test whether the page displays data """
        self.wd.get(
            '%s%s' %
            (self.live_server_url, reverse('home'))
        )

        body = self.wd.find_element_by_css_selector('#container')
        if not body:
            raise NoSuchElementException('container')

        self.assertIn('42 Coffee Cups Test Assignment', body.text)
        self.assertIn('John', body.text)
        self.assertIn('Smith', body.text)
        self.assertIn('July 12, 1990', body.text)
        self.assertIn('FBI agent', body.text)
        self.assertIn('jsmith@gmail.com', body.text)
        self.assertIn('jsmith@jabber.me', body.text)
        self.assertIn('jsmith_007', body.text)
        self.assertIn('Phone: +39912034', body.text)


