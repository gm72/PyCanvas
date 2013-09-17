# -*- coding: utf-8 -*-

__author__ = 'Garrett Pennington'
__date__ = '09/16/13'

import requests
import json

from .core import CanvasObject

class Account(CanvasObject):
    """
    Account object
    """
    _resource_url = 'accounts/'


    @property
    def courses(self):
        new_url = "%scourses/" % self.url
        #return self._call(new_url, self.token)
        
        """
        courses = self._call(new_url, self.token)
        courses_dict = self.to_dict(courses)
        new_courses = []
        for course in courses_dict:
            new_courses.append(course)
        Course(self._en dpoint(), self.token, id)
        return courses
        """


    @property
    def default_time_zone(self):
        return self.dict['default_time_zone']

    @property
    def name(self):
        return self.dict['name']

    @property
    def id(self):
        return self.dict['id']

    @property
    def parent_account_id(self):
        return self.dict['parent_account_id']

    def parent_account(self):
        return Account(self.parent_account_id)

    @property
    def root_account_id(self):
        return self.dict['root_account_id']

    def root_account(self):
        return Account(self.root_account_id)
