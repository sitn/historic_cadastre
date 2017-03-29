# -*- coding: utf-8 -*-

from zope.interface import implementer

from pyramid.authentication import RemoteUserAuthenticationPolicy as PyramidRemoteUserAuthenticationPolicy
from pyramid.interfaces import IAuthenticationPolicy

import os


@implementer(IAuthenticationPolicy)
class RemoteUserAuthenticationPolicy(PyramidRemoteUserAuthenticationPolicy):
    """ A :app:`Pyramid` :term:`authentication policy` which
is inherited from the default Pyramid remote user authentication policy.

All calls through Apache (mod_wsgi) will have a REMOTE_USER variable,
if not it means that the current user is running on the pserve mode,
thus we connect him using his server/computer login.

"""

    def unauthenticated_userid(self, request):
        """ The ``REMOTE_USER`` value found within the ``environ``."""

        username = None
        # To be sure that the pserve mode is used on that one is actually logged on...

        if request.environ.get(self.environ_key) is None \
                and int(request.host_port) >= 5000 \
                and os.environ.get('USERNAME') != 'SYSTEM':

            username = os.environ.get('USERNAME')
        else:
            username = request.environ.get(self.environ_key)
            # username may be None because of Satisfy any in the Apache SSPI conf
            # see Intranet buildout files, variable sspi_apache_conf
            if username:
                username = username.split('\\')[-1]

        return username
