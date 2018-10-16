# -*- coding: utf-8 -*-

from pyramid.view import view_config

from historic_cadastre.models import DBSession, HistoricParcelTree
from historic_cadastre.lib.misc import list_append
import copy


@view_config(route_name='historic_parcel_get', renderer='json')
def historic_parcel_get(request):

    id_ = request.matchdict['id']

    results = DBSession.query(HistoricParcelTree).filter(HistoricParcelTree.imm_dest == id_)

    results = results.all()

    base_route = request.route_url('historic_parcel')
    base_route_doc = request.route_url('historic_parcel_doc')

    if results:
        root = id_
        origine = ''
        doc = base_route_doc + '?id='+root
        value = ''

    else:
        results2 = DBSession.query(HistoricParcelTree).filter(HistoricParcelTree.imm_source == id_)

        results2 = results2.first()

        root = id_
        doc = base_route_doc + '?id='+id_
        value = None
        if results2.origine == 'origine':
            origine = 'origine'
        elif results2.origine == 'continue':
            origine = 'rompu'
        elif results2.origine == 'rp':
            origine = 'rp'

    children = []
    children0 = []
    children1 = []
    children2 = []
    children3 = []
    children4 = []
    children5 = []
    children6 = []
    children7 = []

# LEVEL INITIAL

    children0 = list_append(children, {
        "name": root,
        "lien": doc,
        "value": value,
        "origine": origine,
        "children": []
        })

    # LEVEL 0

    for row in results:
        id_s = row.imm_source
        orig = row.origine
        level1_data = []
        url = base_route + "?id="+id_s
        doc = base_route_doc + '?id='+id_s

        if 'DP' in id_s or 'RP' in id_s:
            origdp = 'origine'
            children1 = list_append(children0, {
                "name": id_s,
                "origine": origdp,
            })

        elif len(row.children) > 0:
            level1_data = row.children

            children1 = list_append(children0, {
                "name": id_s,
                "lien": doc,
                "value": url,
                "origine": orig,
                "children": []
            })

        elif len(row.children) == 0 and orig == 'continue':
            orig = 'rompu'

            children1 = list_append(children0, {
                "name": id_s,
                "lien": doc,
                "origine": orig,
            })

        else:
            children1 = list_append(children0, {
                "name": id_s,
                "lien": doc,
                "origine": orig,
            })

        # LEVEL1

        for row1 in level1_data:
            id_s1 = row1.imm_source
            orig1 = row1.origine
            level2_data = []
            url = base_route + "?id="+id_s1
            doc = base_route_doc + '?id='+id_s1

            if 'DP' in id_s1 or 'RP' in id_s1:
                origdp1 = 'origine'
                children1 = list_append(children0, {
                    "name": id_s1,
                    "origine": origdp1,
                })

            elif len(row1.children) > 0:
                level2_data = row1.children

                children2 = list_append(children1, {
                    "name": id_s1,
                    "lien": doc,
                    "value": url,
                    "origine": orig1,
                    "children": []
                })

            elif len(row.children) == 0 and orig1 == '':
                orig1 = 'rompu'

                children2 = list_append(children1, {
                    "name": id_s1,
                    "lien": doc,
                    "origine": orig1,
                })

            else:
                children2 = list_append(children1, {
                    "name": id_s1,
                    "lien": doc,
                    "origine": orig1,
                })

            # LEVEL2

            for row2 in level2_data:
                id_s2 = row2.imm_source
                orig2 = row2.origine
                level3_data = []
                url = base_route + "?id="+id_s2
                doc = base_route_doc + '?id='+id_s2

                if 'DP' in id_s2 or 'RP' in id_s2:
                    origdp2 = 'origine'
                    children1 = list_append(children0, {
                        "name": id_s2,
                        "origine": origdp2,
                    })

                elif len(row2.children) > 0:
                    level3_data = row2.children

                    children3 = list_append(children2, {
                        "name": id_s2,
                        "lien": doc,
                        "value": url,
                        "origine": orig2,
                        "children": []
                    })

                elif len(row.children) == 0 and orig2 == '':
                    orig2 = 'rompu'

                    children3 = list_append(children2, {
                        "name": id_s2,
                        "lien": doc,
                        "origine": orig2,
                    })

                else:
                    children3 = list_append(children2, {
                        "name": id_s2,
                        "lien": doc,
                        "origine": orig2,
                    })

                # LEVEL3

                for row3 in level3_data:
                    id_s3 = row3.imm_source
                    orig3 = row3.origine
                    level4_data = []
                    url = base_route + "?id="+id_s3
                    doc = base_route_doc + '?id='+id_s3

                    if 'DP' in id_s3 or 'RP' in id_s3:
                        children1 = list_append(children0, {
                            "name": id_s3,
                            "origine": orig,
                        })

                    elif len(row3.children) > 0:
                        level4_data = row3.children

                        children4 = list_append(children3, {
                            "name": id_s3,
                            "lien": doc,
                            "value": url,
                            "origine": orig3,
                            "children": []
                        })

                    elif len(row.children) == 0 and orig3 == '':
                        orig3 = 'rompu'

                        children4 = list_append(children3, {
                            "name": id_s3,
                            "lien": doc,
                            "origine": orig3,
                        })

                    else:
                        children4 = list_append(children3, {
                            "name": id_s3,
                            "lien": doc,
                            "origine": orig3,
                        })

                    # LEVEL4

                    for row4 in level4_data:
                        id_s4 = row4.imm_source
                        orig4 = row4.origine
                        level5_data = []
                        url = base_route + "?id="+id_s4
                        doc = base_route_doc + '?id='+id_s4

                        if 'DP' in id_s4 or 'RP' in id_s4:
                            children1 = list_append(children0, {
                                "name": id_s4,
                                "origine": orig,
                            })

                        elif len(row4.children) > 0:
                            level5_data = row4.children

                            children5 = list_append(children4, {
                                "name": id_s4,
                                "lien": doc,
                                "value": url,
                                "origine": orig4,
                                "children": []
                            })

                        elif len(row.children) == 0 and orig4 == '':
                            orig4 = 'rompu'

                            children5 = list_append(children4, {
                                "name": id_s4,
                                "lien": doc,
                                "origine": orig4,
                            })

                        else:
                            children5 = list_append(children4, {
                                "name": id_s4,
                                "lien": doc,
                                "origine": orig4,
                            })

                        # LEVEL5

                        for row5 in level5_data:
                            id_s5 = row5.imm_source
                            orig5 = row.origine
                            level6_data = []
                            url = base_route + "?id="+id_s5
                            doc = base_route_doc + '?id='+id_s5

                            if 'DP' in id_s5 or 'RP' in id_s5:
                                children1 = list_append(children0, {
                                    "name": id_s5,
                                    "origine": orig,
                                })

                            elif len(row5.children) > 0:
                                level6_data = row5.children

                                children6 = list_append(children5, {
                                    "name": id_s5,
                                    "lien": doc,
                                    "value": url,
                                    "origine": orig5,
                                    "children": []
                                })

                            elif len(row.children) == 0 and orig5 == '':
                                orig5 = 'rompu'

                                children6 = list_append(children5, {
                                    "name": id_s5,
                                    "lien": doc,
                                    "origine": orig5,
                                })

                            else:
                                children6 = list_append(children5, {
                                    "name": id_s5,
                                    "lien": doc,
                                    "origine": orig5,
                                })

                            # LEVEL6

                            for row6 in level6_data:
                                id_s6 = row6.imm_source
                                orig6 = row6.origine
                                level7_data = []
                                url = base_route + "?id="+id_s6
                                doc = base_route_doc + '?id='+id_s6

                                if 'DP' in id_s6 or 'RP' in id_s6:
                                    children1 = list_append(children0, {
                                        "name": id_s6,
                                        "origine": orig,
                                    })

                                elif len(row6.children) > 0:
                                    level7_data = row6.children

                                    children7 = list_append(children6, {
                                        "name": id_s6,
                                        "lien": doc,
                                        "value": url,
                                        "origine": orig6,
                                        "children": []
                                    })

                                elif len(row.children) == 0 and orig6 == '':
                                    orig6 = 'rompu'

                                    children7 = list_append(children6, {
                                        "name": id_s6,
                                        "lien": doc,
                                        "origine": orig6,
                                    })

                                else:
                                    children7 = list_append(children6, {
                                        "name": id_s6,
                                        "lien": doc,
                                        "origine": orig6,
                                    })

                                # LEVEL7

                                for row7 in level7_data:
                                    id_s7 = row7.imm_source
                                    orig7 = row.origine
                                    url = base_route + "?id="+id_s7
                                    doc = base_route_doc + '?id='+id_s7

                                    if 'DP' in id_s7 or 'RP' in id_s7:
                                        children1 = list_append(children0, {
                                            "name": id_s7,
                                            "origine": orig,
                                        })

                                    elif len(row7.children) > 0:

                                        children8 = list_append(children7, {
                                            "name": id_s7,
                                            "lien": doc,
                                            "value": url,
                                            "origine": orig7,
                                            "children": []
                                        })

                                    elif len(row7.children) == 0 and orig7 == '':
                                        orig7 = 'chaîne brisée'

                                        children8 = list_append(children7, {
                                            "name": id_s7,
                                            "lien": doc,
                                            "origine": orig7,
                                        })

                                    else:
                                        children8 = list_append(children7, { # NOQA
                                            "name": id_s7,
                                            "lien": doc,
                                            "origine": orig7,
                                        })

    data = copy.copy(children)

    # Added to make it work in IE11, but do not ask why...
    request.response.headers['Access-Control-Allow-Origin'] = '*'

    return data[0]


@view_config(route_name='historic_parcel', renderer='historic_parcel.html')
def historic_parcel(request):

    id_ = request.params['id']

    d = {
        'id': id_
    }

    return d
