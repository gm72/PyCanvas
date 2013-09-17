# -*- coding: utf-8 -*-

__author__ = 'Garrett Pennington'
__date__ = '09/16/13'
        
import requests

class CanvasObject(object):
    """
    Base class for all Canvas classes
    """

    def __init__(self, _dict):
        """
        init
        """
        self.dict = _dict
    
    def to_dict(self):
        return self.dict
        
    #def _call(self, url, token):
        #return requests.get('%s?access_token=%s' % (url, token))

    @classmethod
    def resource_url(cls):
        return cls._resource_url
