# -*- coding: utf-8 -*-

__author__ = 'Garrett Pennington'
__date__ = '09/16/13'

import urllib
import requests
import json

from .course import Course
from .account import Account

DEFAULT_API_VERSION = 'v1'

class Canvas(object):
    """
    main Canvas class
    """

    def __init__(self, account, token):
        #self.base_url = base_url
        self.account = account
        self.token = token
        
    def _endpoint(self):
        return "https://%s.instructure.com/api/%s/" % (self.account, DEFAULT_API_VERSION)

    def _call(self, resource_url):
        """
        Calls Canvas API
        Returns Requests reponse
        """
        url = "%s%s%s" % (self._endpoint(), resource_url, self._auth())
        #print "url"
        #print url
        return requests.get(url)


    def _auth(self):
        return "?access_token=%s" % self.token
        




    def get_course(self, id):
        """
        get_course
        """
        #courses/:id/
        url = "%s%s/" % (Course.resource_url(), id)
        return Course( self, json.loads(self._call(url).text) )

    def get_courses(self, path=None):
        """
        get_courses
        """
        if path:
            url = path
        else:
            url = "%s" % Course.resource_url()

        courses_response = self._call(url)
        courses = []
        for course in json.loads(courses_response.text ):
            courses.append(Course(self, course))
        return courses
        
    def get_account(self, id):
        """
        get_account
        """
        url = "%s%s/" % (Account.resource_url(), id)
        
        return Account( self, json.loads(self._call(url).text) )
