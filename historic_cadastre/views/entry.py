# -*- coding: utf-8 -*-
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound, HTTPForbidden

from historic_cadastre.models import DBSession, mapped_classes_registry
from historic_cadastre.lib.authorization import check_rights


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

        return {
            'debug': self.debug,
            'id': self.request.params['id'],
            'type': self.request.params['type']
        }

    @view_config(route_name='viewer', renderer='viewer.js')
    def viewer(self):

        mapping_conf = self.request.registry.settings['type_configuration']

        type_plan = {
            'o': u'original',
            'm': u'muté',
            'rp': u'remanié',
            'c': u'copié',
            't': u'minute',
            'p': u'plaque alu',
            'n': u'minute remaniée',
            'b': u'minute copiée'
        }

        id_plan = self.request.params['id_plan']

        type_ = self.request.params['type']

        mapper = mapping_conf[type_]

        pass_through = True

        if mapper['public'] is False:
            pass_through = check_rights(self.request, type_)

        if pass_through is False:
            return HTTPForbidden()

        mapped_class = mapped_classes_registry[mapper['table']]

        params = DBSession.query(mapped_class).get(id_plan)

        plan_url = self.request.route_url('image_proxy', type=type_, id=id_plan)

        self.request.response.content_type = 'application/javascript'

        type_plan_ = None

        if 'type_plan' in params.__table__.c.keys():
            if params.type_plan[0:1] in type_plan.keys():
                type_plan_ = type_plan[params.type_plan[0:1]]
            else:
                type_plan_ = params.type_plan

        if params.echelle:
            echelle = params.echelle
        else:
            echelle = None

        list_folio = None
        nom_folio = None
        cadastre = None
        plan = None
        num_dossier = None
        nom_liste_tech = None
        district = None

        if type_ == 'servitude' or type_ == 'cadastre_graphique':
            list_folio = params.id_plan.split('_')
            nom_folio = list_folio[2]
        else:
            if hasattr(params, 'nom_plan') is True and hasattr(params, 'folio') is True:
                list_folio = params.nom_plan.split('_')
                nom_folio = list_folio[1]
                if nom_folio == '0':
                    nom_folio = params.folio

        if hasattr(params, 'cadastre') is True:
            cadastre = params.cadastre
        if hasattr(params, 'plan') is True:
            plan = params.plan

        if hasattr(params, 'num_dossier') is True:
            num_dossier = params.num_dossier
        if hasattr(params, 'nom_liste_tech') is True:
            nom_liste_tech = params.nom_liste_tech
        if hasattr(params, 'district') is True:
            district = params.district

        return {
            'debug': self.debug,
            'id_plan': id_plan,
            'nom_folio': nom_folio,
            'plan_largeur': params.larg,
            'plan_hauteur': params.haut,
            'plan_resolution': params.resol,
            'plan_url': plan_url,
            'nomcad': cadastre,
            'no_plan': plan,
            'type_plan': type_plan_,
            'echelle': echelle,
            'type_': type_,
            'district': district,
            'nom_liste_tech': nom_liste_tech,
            'num_dossier': num_dossier,
        }
