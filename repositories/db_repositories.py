import sqlite3
from constants import (DATABASE,
                       CREATE_TABLE_PROJECTS, 
                        CREATE_TABLE_TASKS)

class DbReposiroty:
    def __init__(self):
        self.create_tables_statements = []
        self.init_database()
        
def init_database():

    create_tables_statements = [
        CREATE_TABLE_PROJECTS,
        CREATE_TABLE_TASKS
    ]

    try:
        # 1.KORAK Kreiranje konekcijež
        with sqlite3.connect(DATABASE) as conn:
        
        # 2.KORAK Kreiranje Cursor objekta za rad s bazom(predstavlja nasu bazu)
            cursor = conn.cursor()

        # 3.KORAK Izvrsavanje SQL Query naredbi
        for statement in create_tables_statements:
            cursor.execute(create_tables_statements)
            
            # Pokreni postupak snimanja promjena u bazi!!!
            conn.commit()

        # 4.KORAK Zatvaranje konekcije na bazu - with automatski zatvara konekciju
        # conn.close()
        
    except sqlite3.OperationalError as e:
        print(f'Failed to open database: {e}')
        
    except Exception as ex:
        print(f'Dogodila se greska {ex}.')