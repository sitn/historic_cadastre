# -*- coding: utf-8 -*-


def check_rights(request, type_):

    if request.user is None:
        return False

    user = request.user

    role_links = user.children_relation

    authorized = False

    for role_link in role_links:
        if type_ == role_link.role.role_name:
            authorized = True
            break

    return authorized
