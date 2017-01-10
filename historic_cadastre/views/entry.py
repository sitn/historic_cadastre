# -*- coding: utf-8 -*-
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound

from historic_cadastre.models import DBSession
from historic_cadastre.models import VPlanGraphique, Servitude, CadastreGraphique, VPlanDistr
from historic_cadastre.models import VPlanMut

class Entry(object):

    def __init__(self, request):
        self.request = request
        self.settings = request.registry.settings
        self.debug = "debug" in request.params

    @view_config(route_name='home', renderer='index.html')
    def home(self):

        if 'id' not in self.request.params:
            return HTTPNotFound()

        if 'type' not in self.request.params:
            return HTTPNotFound()

        code = None

        if 'code' in self.request.params:
            code = self.request.params['code']

        return {
            'debug': self.debug,
            'id': self.request.params['id'],
            'code': code,
            'type': self.request.params['type']
        }

    @view_config(route_name='viewer', renderer='viewer.js')
    def viewer(self):

        mapper = {
            'graphique': VPlanGraphique,
            'servitude': Servitude,
            'cadastre_graphique': CadastreGraphique,
            'distribution': VPlanDistr,
            'mutation': VPlanMut
        }


        type_plan = {
            'o': u'original',
            'm': u'muté',
            'r': u'remanié',
            'c': u'copié',
            'to': u'minute',
            'ta': u'plaque alu',
            'trp': u'minute remaniée',
            'tc': u'minute copiée'
        }

        id_plan = self.request.params['id_plan']

        code = None

        if 'code' in self.request.params:
            code = self.request.params['code']

        type_ = self.request.params['type']

        mapped_class = mapper[type_]

        params = DBSession.query(mapped_class).get(id_plan)

        plan_url = self.request.route_url('image_proxy', type=type_, id=id_plan)

        if code:
            plan_url += '?code=' + code

        self.request.response.content_type = 'application/javascript'

        type_plan_ = None

        if 'type_plan' in params.__table__.c.keys():
            if params.type_plan[0:1] in type_plan.keys():
                type_plan_ = type_plan[params.type_plan[0:1]]
            elif params.type_plan in type_plan.keys():
                type_plan_ = type_plan[params.type_plan]
            else:
                type_plan_ = params.type_plan

        if params.echelle:
            echelle = params.echelle
        else:
            echelle = None

        if type_ == 'servitude' or type_ == 'cadastre_graphique':
            list_folio = params.id_plan.split('_')
            nom_folio = list_folio[2]
        else:
            if params.nom_plan:
                list_folio = params.nom_plan.split('_')
                nom_folio = list_folio[1]

        return {
            'debug': self.debug,
            'id_plan': id_plan,
            'nom_folio':nom_folio,
            'plan_largeur': params.larg,
            'plan_hauteur': params.haut,
            'plan_resolution': params.resol,
            'plan_url': plan_url,
            'nomcad': params.cadastre,
            'no_plan': params.plan,
            'type_plan': type_plan_,
            'echelle': echelle,
            'type_': type_
        }
