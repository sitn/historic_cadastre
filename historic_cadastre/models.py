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

print DBSession

class VPlanGraphique(Base):
    __label__ = 'v_plan_graphique'
    __tablename__ ='v_plan_graphique'
    __table_args__ = {'schema': 'plan_histo', 'autoload': True}
    id_plan = Column('id_plan', Integer, primary_key=True)