from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

from constants import (NAME_LENGTH)


# 1. Kreirati engine = veza prema bazi podataka
engine = create_engine('sqlite:///databases/sa_projects.db')

# 1.1. Kreirati Python klase koji ce predstavljati tablice u bazi podataka
Base = declarative_base()

class Project(Base):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=NAME_LENGTH), nullable=False, default='No name')
    begin_date = Column(DateTime, nullable=True)
    end_date = Column(DateTime, nullable=True)

    # Relacije prema drugim tablicama
    # tasks = relationship('Task')

    def __repr__(self):
        return f'Project: {self.name}'


class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=NAME_LENGTH), nullable=False)
    priority = Column(String(length=30), nullable=False, default='Normal')
    status = Column(String(length=30), nullable=False, default='New')
    begin_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)

    # Relacije prema drugim tablicama
    project_id = Column(Integer, ForeignKey('projects.id'))
    project = relationship(Project, backref='tasks')

    def __repr__(self):
        return f'Task: {self.name} ({self.status})'


# 2. Kreirati Session = slicno kao cursor
Session = sessionmaker(bind=engine)
session = Session()
