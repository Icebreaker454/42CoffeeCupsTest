# -*- coding: utf-8 -*-
"""
    This is the views module for the ticket1 project
"""

from django.views.generic import TemplateView

from ticket1.models import Person


class IndexView(TemplateView):
    """ The index view for ticket1 """
    template_name = 'ticket1/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        # Selecting the first object, for the data is only for myself
        person = Person.objects.first()
        context['person'] = person
        return context
