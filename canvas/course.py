# -*- coding: utf-8 -*-

__author__ = 'Garrett Pennington'
__date__ = '09/16/13'

import requests
import json
#import urllib
#import datetime

from .core import CanvasObject

class Course(CanvasObject):
    """
    Course object
    Takes a dict of course attrs
    """
    _resource_url = 'courses/'

    @property
    def name(self):
        return self.dict['name']

    @property
    def course_code(self):
        return self.dict['course_code']

    @property
    def default_view(self):
        return self.dict['default_view']

    @property
    def start_at(self):
        return self.dict['start_at']

    @property
    def account_id(self):
        return self.dict['account_id']

    def get_account(self):
        return self.canvas.get_account(self.account_id)


    """

        {
            u'default_view': u'syllabus',
            u'start_at': None,
            u'account_id': 2,
            u'workflow_state': u'unpublished',
            u'storage_quota_mb': 5000,
            u'public_syllabus': False,
            u'hide_final_grades': False,
            u'end_at': None,
            u'sis_course_id': None,
            u'apply_assignment_group_weights': False,
            u'calendar': {
                u'ics': u'https://k-state.instructure.com/feeds/calendars/course_15r1Gj0DWG4qUdS8VWuhp28d6gmdjoMxVqPh2StV.ics'
            },
            u'enrollments': [],
            u'course_code': u'GRSC',
            u'id': 10,
            u'name': u'GRSC Test'
        }
    """