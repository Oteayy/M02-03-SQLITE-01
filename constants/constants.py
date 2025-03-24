
DATABASE = 'databases/projects.db'



CREATE_TABLE_PROJECTS = '''
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            begin_date DATE,
            end_date DATE
        );'''

CREATE_PROJECT = '''
        INSERT INTO projects(name, begin_date, end_date)
        VALUES(?, ?, ?)
    '''

GET_PROJECTS = '''
        SELECT * FROM projects
    '''

GET_PROJECT = '''
        SELECT * FROM projects
        WHERE id = (?)
    '''



CREATE_TABLE_TASKS = '''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            priority INTEGER,
            project_id INTEGER NOT NULL,
            status_id INTEGER NOT NULL,
            begin_date DATE NOT NULL,
            end_date DATE NOT NULL,

            FOREIGN KEY (project_id) REFERENCES projects (id) ON DELETE CASCADE ON UPDATE CASCADE
        );'''

CREATE_TASK = '''
        INSERT INTO tasks(name, priority, status_id,
                            begin_date, end_date, project_id)
        VALUES(?, ?, ?, ?, ?, ?)
    '''
