# -*- coding: utf-8 -*-

from pyramid.config import Configurator
from sqlalchemy import engine_from_config
import sqlahelper

import pyramid_tm
import yaml

from historic_cadastre.lib import dbreflection


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """

    config = Configurator(settings=settings)
    settings = config.get_settings()
    settings.update(yaml.load(file(settings.get("app.cfg"))))

    add_mako_renderer(config, ".html")
    add_mako_renderer(config, ".js")

    engine = engine_from_config(settings, 'sqlalchemy.')
    sqlahelper.add_engine(engine)
    dbreflection.init(engine)

    config.include('pyramid_mako')
    config.include(pyramid_tm.includeme)

    config.add_static_view('static', 'static', cache_max_age=3600)

    config.add_route('home', '/')
    config.add_route('viewer', '/viewer.js')
    config.add_route('image_proxy',  '/img/{type}/{id}')
    config.add_route('pdf_proxy', '/pdf/{type}/{id}')

    # print proxy routes
    config.add_route('printproxy', '/printproxy')
    config.add_route('printproxy_info', '/printproxy/info.json')
    config.add_route('printproxy_create', '/printproxy/create.json')
    config.add_route('printproxy_get', '/printproxy/{file}.printout')

    # mutation
    config.add_route('mutation_list', '/mutation/list')

    config.scan()
    return config.make_wsgi_app()
