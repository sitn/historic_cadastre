# -*- coding: utf-8 -*-

import sqlahelper


from sqlalchemy import (
    Column,
    Integer
    )

from papyrus.geo_interface import GeoInterface
from geoalchemy import GeometryColumn, Geometry
    
Base = sqlahelper.get_base()
DBSession = sqlahelper.get_session()