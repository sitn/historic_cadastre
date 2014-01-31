# -*- coding: utf-8 -*-
from pyramid.view import view_config

from pyramid.response import FileResponse

from historic_cadastre.models import DBSession
from historic_cadastre.models import VPlanGraphique

@view_config(route_name='image_proxy')
def image_proxy(request):
    
    mapper = {
        'graphique': VPlanGraphique
    }
    
    
    id_plan = int(request.matchdict['id'])
    type = request.matchdict['type']
    
    db_filepath = DBSession.query(mapper[type].chemin_cad).get(id_plan)
    
    
    asd
    
    
    
    file = "K:/Consultation_plans/Plans_cadastraux/Boudry/Auvernier/Rf_14_0_o_10000_1876.jpg"
    file = "C:/travail/tmp/Rf_20_2_o_500_2.jpg"

    return FileResponse(
        file,
        request = request,
        content_type = 'image/jpg'
    )
