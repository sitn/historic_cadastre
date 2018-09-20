# -*- coding: utf-8 -*-
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound

from historic_cadastre.models import DBSession
from historic_cadastre.models import HistoricParcelDoc
from historic_cadastre.lib.misc import dateToString


@view_config(route_name='historic_parcel_doc', renderer='historic_parcel_doc.html')
def historic_parcel_doc(request):

    if 'id' in request.params:
        id_ = request.params['id']
    else:
        return HTTPNotFound()

    debug = False

    if 'debug' in request.params:
        debug = True

    list = []

    qq = DBSession.query(HistoricParcelDoc).filter(HistoricParcelDoc.imm_ref == id_).order_by(HistoricParcelDoc.plan)

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

        list.append({
            'parcel': result.parcel,
            'imm_ref': result.imm_ref,
            'plan': result.plan,
            'indice': result.indice,
            'date_plan': date_plan,
            'date_acte': date_acte,
            'date_depot': date_depot,
            'affaire': result.affaire,
            'type_affaire': result.type_affaire,
            'texte_affaire': result.texte_affaire,
            'chemin_plan': result.chemin_plan,
            'chemin_desi': result.chemin_des,
            'id_mut_plan': result.id_mut_plan,
            'cadastre': result.cadastre
        })

    return {'list': list, 'debug': debug}
