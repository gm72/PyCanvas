# -*- coding: utf-8 -*-

__author__ = 'Garrett Pennington'
__date__ = '09/16/13'
        

class CanvasObject(object):
    """
    Base class for all Canvas classes
    """
    
    def to_dict(self):
        return self.dict

    def endpoint(self):
        return Canvas._endpoint()
