# -*- coding: utf-8 -*-

import sqlahelper

from sqlalchemy import (
    Column,
    Integer
    )
    
Base = sqlahelper.get_base()
DBSession = sqlahelper.get_session()


class VPlanGraphique(Base):
    __label__ = 'v_plan_graphique'
    __tablename__ ='v_plan_graphique'
    __table_args__ = {'schema': 'plan_histo', 'autoload': True}
    id_plan = Column('id_plan', Integer, primary_key=True)

class Servitude(Base):
    __label__ = 'servitudes'
    __tablename__ ='servitudes'
    __table_args__ = {'schema': 'plan_histo', 'autoload': True}
    id_plan = Column('id_plan', Integer, primary_key=True)

class CadastreGraphique(Base):
    __label__ = 'cadastre_graphique'
    __tablename__ ='cadastres_graphiques'
    __table_args__ = {'schema': 'plan_histo', 'autoload': True}
    id_plan = Column('id_plan', Integer, primary_key=True)

class VPlanDistr(Base):
    __label__ = 'v_plan_distr'
    __tablename__ ='v_plan_distr'
    __table_args__ = {'schema': 'plan_histo', 'autoload': True}
    id_plan = Column('id_plan', Integer, primary_key=True)

class VPlanMut(Base):
    __label__ = 'v_plan_mut'
    __tablename__ ='v_plan_mut'
    __table_args__ = {'schema': 'plan_histo', 'autoload': True}
    id_folio = Column('id_folio', Integer, primary_key=True)
