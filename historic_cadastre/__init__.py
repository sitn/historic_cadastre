# -*- coding: utf-8 -*-

from pyramid.config import Configurator
from pyramid.mako_templating import renderer_factory as mako_renderer_factory

from sqlalchemy import engine_from_config

import sqlahelper

from historic_cadastre.lib import dbreflection

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """

    engine = engine_from_config(
        settings,
        'sqlalchemy.')
    sqlahelper.add_engine(engine)

    dbreflection.init(engine)

    settings.setdefault('mako.directories','historic_cadastre:templates')
    settings.setdefault('reload_templates',True)

    config = Configurator(settings=settings)
    
    config.add_renderer('.html', mako_renderer_factory)
    config.add_renderer('.js', mako_renderer_factory)
    
    config.add_static_view('static', 'static', cache_max_age=3600)

    config.add_route('home', '/')
    config.add_route('viewer', '/viewer.js')

    config.scan()
    return config.make_wsgi_app()