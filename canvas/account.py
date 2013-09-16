# -*- coding: utf-8 -*-

__author__ = 'Garrett Pennington'
__date__ = '09/16/13'


import urllib
import datetime
import requests
import json

DEFAULT_BASE_URL = "https://k-state.instructure.com/api/v1/"
TOKEN = '1726~bQFj1jZNDBfpCw3OSEgO6L716GuKkZwce00EJQBbMiuuoZp2X00a3EIHaShom0Ad'

class Account(object):
    """
    Account object
    """

    def __init__(self, id):
        """
        :param id: int
        """
        self.resource_url = 'accounts/'
        
        r = requests.get('%saccounts/%s/?access_token=%s' % (DEFAULT_BASE_URL, id, TOKEN))
        self.response = r.text
        self.dict = json.loads(self.response)


    def to_dict(self):
        return self.dict

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
