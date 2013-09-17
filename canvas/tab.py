# -*- coding: utf-8 -*-

__author__ = 'Garrett Pennington'
__date__ = '09/16/13'

from .core import CanvasObject

class Tab(CanvasObject):
    """
    Tab object
    Takes a dict of course attrs
    """
    _resource_url = 'tabs/'

    def __unicode__(self):
        return self.dict['label']

    @property
    def html_url(self):
        return self.dict['html_url']

    @property
    def id(self):
        return self.dict['id']

    @property
    def label(self):
        return self.dict['label']

    @property
    def type(self):
        return self.dict['type']

"""
{
  "html_url": "/courses/1/external_tools/4",
  "id": "context_external_tool_4",
  "label": "WordPress",
  "type": "external"
}
"""