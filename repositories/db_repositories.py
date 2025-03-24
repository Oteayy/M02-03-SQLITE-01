import sqlite3

from constants.constants import DATABASE


def init_database():


    DATABASE = 'database/projects.db'

    create_tables = ['''
        CREATE TABLE IF NOT EXISTS projects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        begin_date DATE,
        end_date DATE

    );''',

    '''
        CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        priority INTEGER,
        project_id INTEGER NOT NULL,
        status_id INTEGER NOT NULL,
        begin_date DATE NOT NULL,
        end_date DATE NOT NULL,
        
        FOREIGN KEY (project_id) REFERENCES projects (id) ON DELETE CASCADE ON UPDATE CASCADE 
    );
    '''
    ]

    try:
        # 1.KORAK Kreiranje konekcijež
        with sqlite3.connect(DATABASE) as conn:
        
        # 2.KORAK Kreiranje Cursor objekta za rad s bazom(predstavlja nasu bazu)
            cursor = conn.cursor()

        # 3.KORAK Izvrsavanje SQL Query naredbi
        for statement in create_tables:
            cursor.execute(create_tables)
            
            # Pokreni postupak snimanja promjena u bazi!!!
            conn.commit()

        # 4.KORAK Zatvaranje konekcije na bazu - with automatski zatvara konekciju
        # conn.close()
        
    except sqlite3.OperationalError as e:
        print(f'Failed to open database: {e}')
        
    except Exception as ex:
        print(f'Dogodila se greska {ex}.')
        

def create_project():
    insert_project_statement = '''
        INSERT INTO projects_name(name, begin_date, end_date)
        VALUES(?, ?, ?)
        '''
        
    try:
        # 1.KORAK Kreiranje konekcijež
        with sqlite3.connect(DATABASE) as conn:
        
        # 2.KORAK Kreiranje Cursor objekta za rad s bazom(predstavlja nasu bazu)
            cursor = conn.cursor()

        # 3.KORAK Izvrsavanje SQL Query naredbi
        cursor.execute(insert_project_statement, ('Project name', '2025-01-25', '2025-02-08'))
            
            # Pokreni postupak snimanja promjena u bazi!!!
        conn.commit()

        # 4.KORAK Zatvaranje konekcije na bazu - with automatski zatvara konekciju
        # conn.close()
        
    except sqlite3.OperationalError as e:
        print(f'Failed to open database: {e}')
        
    except Exception as ex:
        print(f'Dogodila se greska {ex}.')


def get_project(project_id: int):
    get_project_statement = '''
        SELECT * FROM projects
        WHERE id = (?)
        '''
        
        
    try:
        # 1.KORAK Kreiranje konekcije
        with sqlite3.connect(DATABASE) as conn:
        
        # 2.KORAK Kreiranje Cursor objekta za rad s bazom(predstavlja nasu bazu)
            cursor = conn.cursor()

        # 3.KORAK Izvrsavanje SQL Query naredbi
        cursor.execute(get_project_statement, (project_id))
        projects = cursor.fetchall()
            
            # Vrati podatke koji su dohvaceni iz baze
        if len(projects) > 0:
            return projects[0]
        else:
            return None

        # 4.KORAK Zatvaranje konekcije na bazu - with automatski zatvara konekciju
        # conn.close()
        
    except sqlite3.OperationalError as e:
        print(f'Failed to open database: {e}')
        
    except Exception as ex:
        print(f'Dogodila se greska {ex}.')

def create_projects(project: tuple):
    get_project_statement = '''
        SELECT * FROM projects
        WHERE id = (?)
        '''
    projects_from_db = get_project
    projects_from_db = list(filter(lambda p: p[1] == project[0], projects_from_db))
    if len(projects_from_db) > 0:
        return
        
    try:
        # 1.KORAK Kreiranje konekcije
        with sqlite3.connect(DATABASE) as conn:
        
        # 2.KORAK Kreiranje Cursor objekta za rad s bazom(predstavlja nasu bazu)
            cursor = conn.cursor()

        # 3.KORAK Izvrsavanje SQL Query naredbi
        cursor.execute(get_project_statement)
            
            # Vrati podatke koji su dohvaceni iz baze
        if len(project) > 0:
            return project[0]
        else:
            return None

        # 4.KORAK Zatvaranje konekcije na bazu - with automatski zatvara konekciju
        # conn.close()
        
    except sqlite3.OperationalError as e:
        print(f'Failed to open database: {e}')
        
    except Exception as ex:
        print(f'Dogodila se greska {ex}.')


def create_task(project_id: int):
    insert_task_statement = '''
        INSERT INTO tasks(name, priority, status_id, 
                        begin_date, end_date,project_id,)
        VALUES(?, ?, ?, ?, ?, ?)
        '''
        
        # TODO Provjeriti postoji li ovaj projekt u bazi?
        # Ako postoji azuriraj ga, a ako ne postoji kreiraj ga
        
    try:
        # 1.KORAK Kreiranje konekcije
        with sqlite3.connect(DATABASE) as conn:
        
        # 2.KORAK Kreiranje Cursor objekta za rad s bazom(predstavlja nasu bazu)
            cursor = conn.cursor()

        # 3.KORAK Izvrsavanje SQL Query naredbi
        cursor.execute(insert_task_statement, 
                       ('Task 1', 1, 1, '2025-01-31', '2025-02-10', project_id))
            
            # Pokreni postupak snimanja promjena u bazi!!!
        conn.commit()

        # 4.KORAK Zatvaranje konekcije na bazu - with automatski zatvara konekciju
        # conn.close()
        
    except sqlite3.OperationalError as e:
        print(f'Failed to open database: {e}')
        
    except Exception as ex:
        print(f'Dogodila se greska {ex}.')