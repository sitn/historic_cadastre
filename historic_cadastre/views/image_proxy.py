# -*- coding: utf-8 -*-
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound

from pyramid.response import FileResponse

from historic_cadastre.models import DBSession
from historic_cadastre.models import VPlanGraphique, Servitude
from historic_cadastre.models import CadastreGraphique, VPlanDistr
from historic_cadastre.models import VPlanMut

import logging
import os

log = logging.getLogger(__name__)


@view_config(route_name='image_proxy')
def image_proxy(request):

    mapper = {
        'graphique': VPlanGraphique,
        'servitude': Servitude,
        'cadastre_graphique': CadastreGraphique,
        'distribution': VPlanDistr,
        'mutation': VPlanMut
    }

    type = request.matchdict['type']

    if type == 'graphique':
        id_img = int(request.matchdict['id'])
    else:
        id_img = request.matchdict['id']

    code = None

    if 'code' in request.params:
        code = request.params['code']

    is_intranet = False

    if code and code == request.registry.settings['intranet_code']:
        is_intranet = True

    db_filepath = DBSession.query(mapper[type]).get(id_img)

    if db_filepath.is_internet is False and is_intranet is False:
        return HTTPNotFound()

    db_filepath = db_filepath.chemin_cad

    if type == 'graphique' or type == 'distribution':
        registry_string = 'image_server_graphique'
    elif type == 'mutation':
        registry_string = 'image_server_mutation'
    elif type == 'servitude':
        registry_string = 'image_server_servitudes'
    elif type == 'cadastre_graphique':
        registry_string = 'image_server_cadastre_graphique'

    log.info("Get image with id = %s." % id_img)

    file = os.path.join(
        request.registry.settings[registry_string],
        db_filepath
    )

    fileName, fileExtension = os.path.splitext(file)

    extension = {
        '.jpg': 'image/jpg',
        '.jpeg': 'image/jpg',
        '.png': 'image/png',
        '.tif': 'image/tif',
        '.tiff': 'image/tif',
    }

    return FileResponse(
        file,
        request=request,
        content_type=extension[fileExtension.lower()]
    )
