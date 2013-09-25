# -*- coding: utf-8 -*-

__author__ = 'Garrett Pennington'
__date__ = '09/16/13'

import json

from .core import CanvasObject
from .tab import Tab
from .assignment import Assignment

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
    
    @property
    def account(self):
        return self.canvas.get_account(self.account_id)


    @property
    def tabs(self):
        tabs_response = self.canvas._call("%s%s/%s" % (self._resource_url, self.dict['id'], Tab.resource_url()))
        tabs = []
        for tab in json.loads(tabs_response.text ):
            tabs.append(Tab(self, tab))
        return tabs

    @property
    def assignments(self):
        assignments_response = self.canvas._call("%s%s/%s" % (self._resource_url, self.dict['id'], Assignment.resource_url()))
        assignments = []
        for assignment in json.loads(assignments_response.text ):
            assignments.append(Assignment(self, assignment))
        return assignments

"""
{
    // the unique identifier for the course
    id: 370663,
 
    // the SIS identifier for the course, if defined
    sis_course_id: null,
 
    // the full name of the course
    name: "InstructureCon 2012",
 
    // the course code
    course_code: "INSTCON12",
 
    // the current state of the course
    // one of "unpublished", "available", "completed", or "deleted"
    workflow_state: "available",
 
    // the account associated with the course
    account_id: 81259,
 
    // the start date for the course, if applicable
    start_at: "2012-06-01T00:00:00-06:00",
 
    // the end date for the course, if applicable
    end_at: null,
 
    // A list of enrollments linking the current user to the course.
    // for student enrollments, grading information may be included
    // if include[]=total_scores
    enrollments: [
      {
        type: student,
        role: StudentEnrollment,
        computed_final_score: 41.5,
        computed_current_score: 90,
        computed_final_grade: 'F'
        computed_current_grade: 'A-',
      }
    ],
 
    // course calendar
    calendar: {
      ics: "https:\/\/canvas.instructure.com\/feeds\/calendars\/course_abcdef.ics"
    }
 
    // the type of page that users will see when they first visit the course
    // - 'feed': Recent Activity Dashboard
    // - 'wiki': Wiki Front Page
    // - 'modules': Course Modules/Sections Page
    // - 'assignments': Course Assignments List
    // - 'syllabus': Course Syllabus Page
    // other types may be added in the future
    default_view: 'feed'
 
    // optional: user-generated HTML for the course syllabus
    syllabus_body: "<p>syllabus html goes here<\/p>",
 
    // optional: the number of submissions needing grading
    // returned only if the current user has grading rights
    // and include[]=needs_grading_count
    needs_grading_count: '17'
 
    // optional: the name of the enrollment term for the course
    // returned only if include[]=term
    term: {
      id: 1,
      name: 'Default Term',
      start_at: "2012-06-01T00:00:00-06:00",
      end_at: null
    },
 
    // weight final grade based on assignment group percentages
    apply_assignment_group_weights: true
 
}
"""