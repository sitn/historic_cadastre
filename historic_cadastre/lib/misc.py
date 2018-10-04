# -*- coding: utf-8 -*-

def list_append(lst, item):
    lst.append(item)
    if 'children' in item:
        children = item['children']
        return children
    else:
        return None

def dateToString(date):

    strDate = date.isoformat()[8:10] + '.' + date.isoformat()[5:7] + '.' + date.isoformat()[:4]
    return strDate
