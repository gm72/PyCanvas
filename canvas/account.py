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
        url = "%s%s/courses/" % (self._resource_url, self.dict['id'], )
        return self.canvas.get_courses(url)

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

    @property
    def parent_account(self):
        return self.canvas.get_account(self.parent_account_id)

    @property
    def root_account_id(self):
        return self.dict['root_account_id']

    def root_account(self):
        return Account(self.root_account_id)
