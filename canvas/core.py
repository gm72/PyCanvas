# -*- coding: utf-8 -*-

__author__ = 'Garrett Pennington'
__date__ = '09/16/13'
        
#import requests

class CanvasObject(object):
    """
    Base class for all Canvas classes
    """

    def __init__(self, canvas, _dict):
        """
        init
        canvas - instance of Canvas class caller
        _dict - dict of object
        
        """
        self.canvas = canvas
        self.dict = _dict

        
    def __unicode__(self):
        return self.dict['name']
    
    def to_dict(self):
        return self.dict
        
    #def _call(self, url, token):
        #return requests.get('%s?access_token=%s' % (url, token))

    @classmethod
    def resource_url(cls):
        return cls._resource_url
