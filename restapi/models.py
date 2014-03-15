from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    String,
    ForeignKey,
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    relationship,
    backref
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class Favorites(Base):
    __tablename__ = 'favorites'
    uid = Column(Integer, primary_key=True)
    rank = Column(Integer)
    service_id = Column(Integer, ForeignKey('csh_services.id'))
    services_mapper = relationship('CSH_Services',
            backref=backref('favorites', order_by= uid),
            order_by="desc(CSH_Services.id)")


    def to_dict(self):
        return{
                'id': self.uid,
                'rank': self.rank,
                'serivce_id': self.serivce_id,
                'services_mapper': [s.to_dict() for s in self.services_mapper]
                }

class CSH_Services(Base):
    __tablename__ = 'csh_services'
    id = Column(Integer, primary_key=True)
    icon = Column(String)
    name = Column(String)
    url = Column(String)

