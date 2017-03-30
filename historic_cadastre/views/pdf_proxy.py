# -*- coding: utf-8 -*-
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound

from pyramid.response import FileResponse

from historic_cadastre.models import DBSession

from historic_cadastre.models import VPlanMut

import logging
import os

log = logging.getLogger(__name__)

@view_config(route_name='pdf_proxy', renderer='json')
def pdf_proxy(request):

    mapper = {
        'mutation': VPlanMut
    }

    type = request.matchdict['type']

    id_folio = int(request.matchdict['id'])
    
    db_filepath = DBSession.query(mapper[type]).get(id_folio)

    db_filepath = db_filepath.chemin_desi

    log.info("Get pdf mutation with id = %s." % id_folio)

    file = os.path.join(request.registry.settings['image_server_mutation'], db_filepath)
    fileName, fileExtension = os.path.splitext(file)

    return FileResponse(
        file,
        request = request,
        content_type = 'application/pdf'
    )
