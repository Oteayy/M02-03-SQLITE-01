from datetime import datetime as dt
from repositories import (init_database,
                          create_project,
                          create_task,
                          get_projects,
                          get_project)

from repositories.sa_db_repo import (Base, engine, Project, Task, session)


def get_projects():
    return session.query(Project).all()


def get_project(id: int):
    return session.query(Project).filter(Project.id == id).one_or_none()


def create_project(project: Project):
    # Provjera imam li ovaj projekt u bazi
    project_from_db = session.query(Project).filter(Project.name == project.name).one_or_none()

    if project_from_db == None:
        session.add(project)
        session.commit()
        return project

    return project_from_db


def update_project(project: Project):
    project_from_db = session.query(Project).filter(Project.id == project.id).one_or_none()

    if project_from_db != None:
        project_from_db = project
        session.commit()

    return project_from_db


def delete_project(id: int):
    project_from_db = session.query(Project).filter(Project.id == id).one_or_none()
    session.delete(project_from_db)
    session.commit()


def create_task(task: Task):
    task_from_db = session.query(Task).filter(Task.name == task.name).one_or_none()

    if task_from_db == None:
        session.add(task)
        session.commit()
        return task

    return task_from_db




def main():
    #region SQLITE3 module
    # init_database()
    # project = ('Demo project 12', '2024-12-06', '2025-03-10')
    # create_project(project)

    # project_id = 6 # TODO Dohvatiti iz baze!!!
    # task = ('Task 12', 1, 1,
    #         '2024-12-06', '2025-03-10', project_id)
    # create_task(task)

    # project = get_project(5)
    # print(project)

    # projects = get_projects()
    # print(projects)
    #endregion

    Base.metadata.create_all(engine)

    project = Project(name='Refactor Repository',
                      begin_date=dt.strptime('2025-01-31', '%Y-%m-%d'),
                      end_date=dt.strptime('2025-02-28', '%Y-%m-%d'))
    project = create_project(project=project)


    task = Task(name = 'Install SQL Alchemy',
                priority = 'High',
                status = 'New',
                begin_date = dt(2025, 1, 31, 15, 35),  #.strptime('2025-01-31', '%Y-%m-%d'),
                end_date = dt.strptime('2025-01-31', '%Y-%m-%d'))
    task.project = project
    task = create_task(task)


    projects = get_projects()

    for project in projects:
        print(project, project.begin_date.strftime('%A %d.%m.%Y %H:%M:%S'), project.tasks)

    id = 1
    project_2 = get_project(id)
    if project_2 != None:
        print(project_2)
    else:
        print(f'Ne postoji trazeni projekt u bazi {id}')



if __name__ == '__main__':
    main()