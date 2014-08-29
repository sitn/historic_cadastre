# -*- coding: utf-8 -*-
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound

from historic_cadastre.models import DBSession
from historic_cadastre.models import VPlanMut
import datetime

@view_config(route_name='mutation_list', renderer='mutations_list.html')
def mutation_list(request):

    code = None

    if 'code' in request.params:
        code = request.params['code']
    else:
        return HTTPNotFound()

    if 'id' in request.params:
        id = request.params['id']
    else:
        return HTTPNotFound()

    debug = False

    if 'debug' in request.params:
        debug = True

    list = []

    qq = DBSession.query(VPlanMut).filter(VPlanMut.id_cad_geom==int(id)).order_by(VPlanMut.plan)

    results = qq.all()

    for result in results:

        date_plan = result.date_plan
        if date_plan:
            date_plan = dateToString(date_plan)
        else:
            date_plan = ''

        date_acte = result.date_acte
        if date_acte:
            date_acte = dateToString(date_acte)
        else:
            date_acte = ''

        date_depot = result.date_depot
        if date_depot:
            date_depot = dateToString(date_depot)
        else:
            date_depot = ''

        req_bidon = result.req_bidon
        if req_bidon:
            req_bidon = 'oui'
        else:
            req_bidon = 'non'

        cut_plan = result.nom_plan
        list_cut = cut_plan.split('_')
        nom_plan = list_cut[1]

        list.append({
            'id': result.id_folio,
            'cadastre': result.cadastre,
            'nom_plan': nom_plan,
            'plan': result.plan,
            'indice': result.indice,
            'req_tot': result.req_tot,
            'req_bidon': req_bidon,
            'date_plan': date_plan,
            'date_acte': date_acte,
            'date_depot': date_depot,
            'chemin_desi': result.chemin_desi
        })

    return {'list': list, 'code':code, 'debug':debug}
    
def dateToString(date):
    
    strDate = date.isoformat()[8:10] + '.' + date.isoformat()[5:7] + '.' + date.isoformat()[:4]
    return strDate
