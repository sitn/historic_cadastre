from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

@view_config(route_name='home', renderer='index.html')
def my_view(request):
    #~ try:
        #~ one = DBSession.query(MyModel).filter(MyModel.name == 'one').first()
    #~ except DBAPIError:
        #~ return Response(conn_err_msg, content_type='text/plain', status_int=500)
    one = 'toto'    
    return {'one': one, 'project': 'historic_cadastre'}
