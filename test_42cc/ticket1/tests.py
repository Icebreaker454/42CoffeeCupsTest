# -*- coding: utf-8 -*-
"""
    Functional tests for my application
"""

from django.test import LiveServerTestCase
from django.core.urlresolvers import reverse

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from models import Person


class Ticket1Test(LiveServerTestCase):
    """ The ticket1 test case """
    def setUp(self):
        self.wd = webdriver.Firefox()
        Person.objects.create(
            first_name=u'John',
            last_name=u'Smith',
            birth_date='1990-07-12',
            bio='FBI agent',
            contacts_email='jsmith@gmail.com',
            contacts_jabber_id='jsmith@jabber.me',
            contacts_skype_id=r'jsmith_007',
            contacts_other=r'Phone: +39912034'
        )

    def tearDown(self):
        self.wd.quit()

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
        self.assertIn('1990-07-12', body.text)
        self.assertIn('FBI agent', body.text)
        self.assertIn('jsmith@gmail.com', body.text)
        self.assertIn('jsmith@jabber.me', body.text)
        self.assertIn('jsmith_007', body.text)
        self.assertIn('Phone: +39912034', body.text)


