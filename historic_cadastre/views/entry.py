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

        code = None

        if 'code' in self.request.params:
            code = self.request.params['code']

        return {
            'debug': self.debug,
            'id': self.request.params['id'],
            'code': code
        }

    @view_config(route_name='viewer', renderer='viewer.js')
    def viewer(self):

        id_plan = int(self.request.params['id_plan'])

        code = None

        if 'code' in self.request.params:
            code = self.request.params['code']

        type = 'graphique'

        params = DBSession.query(VPlanGraphique).get(id_plan)

        plan_url = self.request.route_url('image_proxy', type=type, id=id_plan)

        if code:
            plan_url += '?code=' + code

        self.request.response.content_type = 'application/javascript'

        return {
            'debug': self.debug,
            'id_plan': id_plan,
            'plan_largeur': params.larg,
            'plan_hauteur': params.haut,
            'plan_resolution': params.resol,
            'plan_url': plan_url,
            'nomcad': params.cadastre,
            'no_plan': params.plan
        }
