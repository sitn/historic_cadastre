# -*- coding: utf-8 -*-
from pyramid.view import view_config

from pyramid.response import FileResponse

from historic_cadastre.models import DBSession
from historic_cadastre.models import VPlanGraphique

import os

@view_config(route_name='image_proxy')
def image_proxy(request):
    
    mapper = {
        'graphique': VPlanGraphique
    }

    id_plan = int(request.matchdict['id'])
    type = request.matchdict['type']
    
    db_filepath = DBSession.query(mapper[type]).get(id_plan)
    db_filepath = db_filepath.chemin_cad
    
    if type == 'graphique':
        registry_string = 'image_server_graphique'
    elif type == 'mutation':
        registry_string = 'image_server_mutation'

    file = os.path.join(request.registry.settings[registry_string], db_filepath)

    return FileResponse(
        file,
        request = request,
        content_type = 'image/jpg'
    )
