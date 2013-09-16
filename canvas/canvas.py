# -*- coding: utf-8 -*-

__author__ = 'Garrett Pennington'
__date__ = '09/16/13'

import urllib
import requests

from .course import Course
from .account import Account

DEFAULT_API_VERSION = 'v1'
#DEFAULT_BASE_URL = "https://%s.instructure.com/api/v1/"

class Canvas(object):
    """
    main Canvas class
    """

    def __init__(self, account, token):
        #self.base_url = base_url
        self.account = account
        self.token = token
        
    @staticmethod
    def _endpoint():
        return "https://%s.instructure.com/api/%s/" % (self.account, DEFAULT_API_VERSION)


    def get_course(self, id):
        """
        get_course
        """
        return Course(id)

    def get_courses(self):
        """
        get_courses
        """
        #r = requests.get('%saccounts/1/courses/?access_token=%s' % (self.base_url,  TOKEN))
        #return r.text
        return None