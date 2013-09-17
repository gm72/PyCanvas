# -*- coding: utf-8 -*-

__author__ = 'Garrett Pennington'
__date__ = '09/16/13'

from .core import CanvasObject

class Assignment(CanvasObject):
    """
    Assignment object
    Takes a dict of course attrs
    https://canvas.instructure.com/doc/api/assignments.html
    
    """
    _resource_url = 'assignments/'

    @property
    def id(self):
        return self.dict['id']

    @property
    def name(self):
        return self.dict['name']

    @property
    def description(self):
        return self.dict['description']

    @property
    def html_url(self):
        return self.dict['html_url']

    @property
    def due_at(self):
        return self.dict['due_at']

    """
        The rest unimplemented for now...
    """