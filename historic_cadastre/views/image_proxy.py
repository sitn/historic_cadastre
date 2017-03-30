# -*- coding: utf-8 -*-
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPForbidden

from pyramid.response import FileResponse

from historic_cadastre.models import DBSession, mapped_classes_registry
from historic_cadastre.lib.authorization import check_rights

import logging
import os

log = logging.getLogger(__name__)


@view_config(route_name='image_proxy')
def image_proxy(request):

    mapping_conf = request.registry.settings['type_configuration']

    type = request.matchdict['type']

    mapper = mapping_conf[type]

    pass_through = True

    if mapper['public'] is False:
        pass_through = check_rights(request, type)

    if pass_through is False:
        return HTTPForbidden()

    mapped_class = mapped_classes_registry[mapper['table']]

    img_base_path = mapper['image_server']

    if type == 'graphique':
        id_img = int(request.matchdict['id'])
    else:
        id_img = request.matchdict['id']

    db_filepath = DBSession.query(mapped_class).get(id_img)

    db_filepath = db_filepath.chemin_cad

    log.info("Get image with id = %s." % id_img)

    file = os.path.join(img_base_path, db_filepath)
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
