# -*- coding: utf-8 -*-
"""
    Functional tests for my application
"""

from django.test import TestCase
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User

from ticket1.models import Person


class Ticket1Test(TestCase):
    """ The ticket1 test case """
    fixtures = ['test.json']
    
    def test_database(self):
        queryset = Person.objects.all()
        if len(queryset) > 1:
            self.fail("There shouldn't be another database entry")

    def test_auth(self):
        user = User.objects.first()
        self.client.login()

    def test_page_info(self):
        """ Test whether the page displays data """
        response = self.client.get(reverse_lazy('home'))

        self.assertIn('42 Coffee Cups Test Assignment', response.content)
        self.assertIn('John', response.content)
        self.assertIn('Smith', response.content)
        self.assertIn('July 12, 1990', response.content)
        self.assertIn('FBI agent', response.content)
        self.assertIn('jsmith@gmail.com', response.content)
        self.assertIn('jsmith@jabber.me', response.content)
        self.assertIn('jsmith_007', response.content)
        self.assertIn('Phone: +39912034', response.content)


