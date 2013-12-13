# -*- coding: utf-8 -*-
from pyramid.view import view_config

class Entry(object):

    def __init__(self, request):
        self.request = request
        self.settings = request.registry.settings
        self.debug = "debug" in request.params
    
    @view_config(route_name='home', renderer='index.html')
    def home(self):

        return {
            'debug': self.debug
        }
        
    @view_config(route_name='viewer', renderer='viewer.js')
    def viewer(self):

        self.request.response.content_type = 'application/javascript'
        return {
            'debug': self.debug
        }
        