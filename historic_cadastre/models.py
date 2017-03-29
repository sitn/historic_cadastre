# -*- coding: utf-8 -*-

import sqlahelper

from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref

Base = sqlahelper.get_base()
DBSession = sqlahelper.get_session()


class VPlanGraphique(Base):
    __label__ = "v_plan_graphique"
    __tablename__ = "v_plan_graphique"
    __table_args__ = {"schema": "plan_histo", "autoload": True}
    id_plan = Column("id_plan", Integer, primary_key=True)


class Servitude(Base):
    __label__ = "servitudes"
    __tablename__ = "servitudes"
    __table_args__ = {"schema": "plan_histo", "autoload": True}
    id_plan = Column("id_plan", Integer, primary_key=True)


class CadastreGraphique(Base):
    __label__ = "cadastre_graphique"
    __tablename__ = "cadastres_graphiques"
    __table_args__ = {"schema": "plan_histo", "autoload": True}
    id_plan = Column("id_plan", Integer, primary_key=True)


class VPlanDistr(Base):
    __label__ = "v_plan_distr"
    __tablename__ = "v_plan_distr"
    __table_args__ = {"schema": "plan_histo", "autoload": True}
    id_plan = Column("id_plan", Integer, primary_key=True)


class VPlanMut(Base):
    __label__ = "v_plan_mut"
    __tablename__ = "v_plan_mut"
    __table_args__ = {"schema": "plan_histo", "autoload": True}
    id_folio = Column("id_folio", Integer, primary_key=True)


class Ppe(Base):
    __label__ = "pp03_pieces_techniques"
    __tablename__ = "pp03_pieces_techniques"
    __table_args__ = {"schema": "registre_foncier", "autoload": True}
    id_piece = Column("id_piece", Integer, primary_key=True)
    chemin_cad = Column("lien_piece_tech", String)


# AUTHENTICATION
class AuthenticationRole(Base):
    __label__ = "authentication_role"
    __tablename__ = "authentication_role"
    __table_args__ = {"schema": "plan_histo", "autoload": True}
    id_role = Column(Integer, primary_key=True)


class AuthenticationUser(Base):
    __label__ = "authentication_user"
    __tablename__ = "authentication_user"
    __table_args__ = {"schema": "plan_histo", "autoload": True}
    id_user = Column(Integer, primary_key=True)


class AuthenticationUserRole(Base):
    __label__ = "authentication_user_role"
    __tablename__ = "authentication_user_role"
    __table_args__ = {"schema": "plan_histo", "autoload": True}
    id = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey("plan_histo.authentication_user.id_user"))
    user = relationship(
        "AuthenticationUser",
        backref=backref(
            "children_relation",
            cascade="save-update,merge,delete,delete-orphan",
        ),
        primaryjoin="AuthenticationUserRole.id_user==AuthenticationUser.id_user",
    )
    id_role = Column(Integer, ForeignKey("plan_histo.authentication_role.id_role"))
    role = relationship(
        "AuthenticationRole",
        backref=backref(
            "parent_relation",
            cascade="save-update,merge,delete,delete-orphan",
        ),
        primaryjoin="AuthenticationUserRole.id_role==AuthenticationRole.id_role",
    )


mapped_classes_registry = {}
for value in globals().values():
    if hasattr(value, '__tablename__') and value.__tablename__.startswith('authentication_') is False:
        if hasattr(value, '__table_args__'):
            mapped_class = value
            mapped_classes_registry[mapped_class.__tablename__] = mapped_class
