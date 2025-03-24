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
def create_task():
    pass