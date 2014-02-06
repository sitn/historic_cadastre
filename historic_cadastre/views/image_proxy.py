# -*- coding: utf-8 -*-
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound

from pyramid.response import FileResponse

from historic_cadastre.models import DBSession
from historic_cadastre.models import VPlanGraphique

import logging
import os

log = logging.getLogger(__name__)

@view_config(route_name='image_proxy')
def image_proxy(request):

    mapper = {
        'graphique': VPlanGraphique
    }

    id_plan = int(request.matchdict['id'])
    type = request.matchdict['type']

    code = None

    if 'code' in request.params:
        code = request.params['code']

    is_intranet = False

    if code and code == request.registry.settings['intranet_code']:
        is_intranet = True

    db_filepath = DBSession.query(mapper[type]).get(id_plan)

    if db_filepath.is_internet is False and is_intranet is False:
        return HTTPNotFound()

    db_filepath = db_filepath.chemin_cad

    if type == 'graphique':
        registry_string = 'image_server_graphique'
    elif type == 'mutation':
        registry_string = 'image_server_mutation'

    log.info("Get image with id = %s." % id_plan)

    file = os.path.join(request.registry.settings[registry_string], db_filepath)

    return FileResponse(
        file,
        request = request,
        content_type = 'image/jpg'
    )
