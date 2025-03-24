from repositories import (init_database,
                          create_project,
                          create_task,
                          get_project,
                          get_projects)

def main():
    init_database()
    project = ('Demo project', '2024-12-06', '2025-03-10')
    create_project(project)
    
    project_id = 1 # TODO Dohvatiti iz baze !!!
    create_task(project_id)
    
    project = get_project(1)
    print(project)
    
    projects = get_projects()
    print(projects)

if __name__ == '__main__':
    main()