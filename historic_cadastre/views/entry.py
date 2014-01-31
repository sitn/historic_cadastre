# -*- coding: utf-8 -*-
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound

from historic_cadastre.models import DBSession
from historic_cadastre.models import VPlanGraphique

class Entry(object):

    def __init__(self, request):
        self.request = request
        self.settings = request.registry.settings
        self.debug = "debug" in request.params

    @view_config(route_name='home', renderer='index.html')
    def home(self):

        if 'id' not in self.request.params:
            return HTTPNotFound()

        return {
            'debug': self.debug,
            'id': self.request.params['id']
        }
        
    @view_config(route_name='viewer', renderer='viewer.js')
    def viewer(self):

        id_plan = int(self.request.params['id_plan'])
#        type = self.request.params['type']
        type = 'graphique'

        params = DBSession.query(VPlanGraphique).get(id_plan)

        plan_url = self.request.route_url('image_proxy', type=type, id=id_plan)

        self.request.response.content_type = 'application/javascript'
        return {
            'debug': self.debug,
            'id_plan': id_plan,
            'plan_largeur': params.larg,
            'plan_hauteur': params.haut,
            'plan_resolution': params.resol,
            'plan_url': plan_url
        }
