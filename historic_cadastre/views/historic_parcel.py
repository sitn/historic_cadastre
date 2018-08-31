# -*- coding: utf-8 -*-

from pyramid.httpexceptions import HTTPBadRequest, HTTPNotFound, HTTPForbidden
from pyramid.view import view_config

from historic_cadastre.models import DBSession, HistoricParcelTree


@view_config(route_name='historic_parcel_get', renderer='json')
def historic_parcel_get(request):
    
    id_ = request.matchdict['id']
    
    results = DBSession.query(HistoricParcelTree).filter(HistoricParcelTree.imm_source == id_)
    
    results = results.all()
    
    data = [{
        'id': id_,
        'value':'',
        'text': "https://epfl.ch",
    },]

    root = id_
    
    # LEVEL 0
    for row in results:
      level1 = root + "." + row.imm_dest
      level1_data = []
      
      if len(row.children) > 0:
          level1_data = row.children
      
      data.append({
          'id': level1,
          'text': "https://epfl.ch",
          'value':''
      })
      
      # LEVEL 1
      for row1 in level1_data:
          level2 = level1 + "." + row1.imm_dest
          level2_data = []
          if len(row1.children) > 0:
              level2_data = row1.children
      
          data.append({
              'id': level2,
              'text': "https://epfl.ch",
              'value':''
          })

          # LEVEL 2
          for row2 in level2_data:
              level3 = level2 + "." + row2.imm_dest
              level3_data = []
              if len(row2.children) > 0:
                  level3_data = row2.children
          
              data.append({
                  'id': level3,
                  'text': "https://epfl.ch",
                  'value':''
              })

              # LEVEL 3
              for row3 in level3_data:
                  level4 = level3 + "." + row3.imm_dest
                  level4_data = []
                  if len(row3.children) > 0:
                      level4_data = row3.children
              
                  data.append({
                      'id': level4,
                      'text': "https://epfl.ch",
                      'value':''
                  })








    return data
    
    #~ return [
        #~ {'id': 'flare','value':''},
        #~ {'id': 'flare.analytics','value':''},
        #~ {'id': 'flare.analytics.cluster','value':''},
        #~ {'id': 'flare.analytics.cluster.AgglomerativeCluster','value':''},
        #~ {'id': 'flare.analytics.cluster.CommunityStructure','value':''},
        #~ {'id': 'flare.analytics.cluster.HierarchicalCluster','value':''},
        #~ {'id': 'flare.analytics.cluster.MergeEdge','value':''},
        #~ {'id': 'flare.analytics.graph','value':''},
        #~ {'id': 'flare.analytics.graph.BetweennessCentrality','value':''},
        #~ {'id': 'flare.analytics.graph.LinkDistance','value':''},
    #~ ]

 
@view_config(route_name='historic_parcel', renderer='historic_parcel.html')
def historic_parcel(request):
  
  d = {}
  
  return d
 