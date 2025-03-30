import sqlite3
from typing import Tuple

from constants import (DATABASE,
                       CREATE_TABLE_PROJECTS,
                       CREATE_PROJECT,
                       GET_PROJECTS,
                       GET_PROJECT,
                       CREATE_TABLE_TASKS,
                       CREATE_TASK)


def init_database():
    create_tables_statements = [
        CREATE_TABLE_PROJECTS,
        CREATE_TABLE_TASKS
    ]

    try:
        # 1. KORAK Kreiranje konekcije
        with sqlite3.connect(DATABASE) as conn:
            # 2. KORAK Kreiranje Cursor objekta za rad s bazom (predstavlja nasu bazu)
            cursor = conn.cursor()

            # 3. KORAK Izvrsavanje SQL Query naredbi
            for statement in create_tables_statements:
                cursor.execute(statement)

            # Pokreni postupak snimanja promjena u bazi!!!
            conn.commit()

            # 4. KORAK Zatvarnje konekcije na bazu
            # - with automatski zatvara konekciju
            # conn.close()
    except sqlite3.OperationalError as e:
        print(f'Failed to open database: {e}')

    except Exception as ex:
        print(f'Dogodila se greska {ex}.')



def create_project(project: Tuple):
    projects_from_db = get_projects()
    project_from_db = list(filter(lambda p: p[1] == project[0], projects_from_db))
    if len(project_from_db) > 0:
        # Update project
        return
    _commit_to_db(CREATE_PROJECT, project)

def get_project(project_id: int):
    return _get_from_db(GET_PROJECT, (project_id,))

def get_projects():
    return _get_from_db(GET_PROJECTS)

def update_project(project_id: int, project: Tuple):
    # TODO - dovrsiti funkciju tako da koristi neku od dolje kreiranih private funkcija
    pass

def delete_project(project_id: int):
    # TODO - dovrsiti funkciju tako da koristi neku od dolje kreiranih private funkcija
    pass


def create_task(task):
    # TODO Provjeriti postoji li ovaj projekt u bazi?
    # Ako postoji azuriraj ga, a ako ne postoji kreiraj ga

    _commit_to_db(CREATE_TASK, task)

# TODO - ostale CRUD funkcija za Taskove
# OPREZ - svaki task mora biti povezan uz project!!!



def _commit_to_db(statement, data):
    try:
        # 1. KORAK Kreiranje konekcije
        with sqlite3.connect(DATABASE) as conn:
            # 2. KORAK Kreiranje Cursor objekta za rad s bazom (predstavlja nasu bazu)
            cursor = conn.cursor()

            # 3. KORAK Izvrsavanje SQL Query naredbi
            cursor.execute(statement, data)

            # Pokreni postupak snimanja promjena u bazi!!!
            conn.commit()

    except sqlite3.OperationalError as e:
        print(f'Failed to open database: {e}')

    except Exception as ex:
        print(f'Dogodila se greska {ex}.')

def _get_from_db(statement, condition: Tuple = ()):
    try:
        # 1. KORAK Kreiranje konekcije
        with sqlite3.connect(DATABASE) as conn:
            # 2. KORAK Kreiranje Cursor objekta za rad s bazom (predstavlja nasu bazu)
            cursor = conn.cursor()

            # 3. KORAK Izvrsavanje SQL Query naredbi
            if len(condition) > 0:
                cursor.execute(statement, condition)
            else:
                cursor.execute(statement)

            data_from_db = cursor.fetchall()

            # Vrati podatke koji su dohvaceni iz baze
            if len(data_from_db) > 0:
                return data_from_db
            else:
                return None

    except sqlite3.OperationalError as e:
        print(f'Failed to open database: {e}')

    except Exception as ex:
        print(f'Dogodila se greska {ex}.')