# -*- coding: utf-8 -*-

from pyramid.config import Configurator
from pyramid_mako import add_mako_renderer
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.security import remember
from pyramid_multiauth import MultiAuthenticationPolicy

from sqlalchemy import engine_from_config

import sqlahelper
import pyramid_tm
import yaml

from historic_cadastre.lib import dbreflection
from historic_cadastre.lib.authentication import RemoteUserAuthenticationPolicy


def _create_get_user_from_request(settings):
    def get_user_from_request(request):
        """ Return the User object for the request.
        Return ``None`` if:
        * user is anonymous
        * it does not exist in the database
        * the referer is invalid
        """
        from historic_cadastre.models import DBSession, AuthenticationUser

        if not hasattr(request, "_user"):
            request._user = None
            username = request.authenticated_userid

            if username is not None:
                username = username.lower()
                # We know we will need the role object of the
                # user so we use joined loading
                user = DBSession.query(AuthenticationUser) \
                    .filter_by(username=username) \
                    .first()

                if user is not None:
                    headers = remember(request, user.username)
                    request.response.headerlist.extend(headers)
                    request._user = user

        return request._user
    return get_user_from_request


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """

    config = Configurator(settings=settings)
    settings = config.get_settings()
    yaml_config = yaml.load(open(settings.get("app.cfg")))['vars']
    settings.update(yaml_config)

    add_mako_renderer(config, ".html")
    add_mako_renderer(config, ".js")

    engine = engine_from_config(settings, 'sqlalchemy.')
    sqlahelper.add_engine(engine)
    dbreflection.init(engine)

    config.set_authorization_policy(ACLAuthorizationPolicy())

    config.add_request_method(
        _create_get_user_from_request(settings),
        name="user",
        property=True
    )

    authtkt_authentication_policy = AuthTktAuthenticationPolicy(
        settings.get('authtkt_cookie_name'),
        cookie_name=settings.get('authtkt_cookie_name'),
        hashalg='sha512'
    )

    remote_user_authentication_policy = RemoteUserAuthenticationPolicy()
    policies = [remote_user_authentication_policy, authtkt_authentication_policy]
    authentication_policy = MultiAuthenticationPolicy(policies)
    config.set_authentication_policy(authentication_policy)

    config.include('pyramid_mako')
    config.include(pyramid_tm.includeme)

    config.add_static_view('static', 'static', cache_max_age=3600)

    config.add_route('home', '/')
    config.add_route('viewer', '/viewer.js')
    config.add_route('image_proxy', '/img/{type}/{id}')
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
