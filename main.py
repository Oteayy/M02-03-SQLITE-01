from repositories import (init_database,
                          create_project,
                          create_task)

def main():
    init_database()
    create_project()
    
    project_id = 1 # TODO Dohvatiti iz baze !!!
    create_task(project_id)
# NASTAVAK izvrsavanje programa

if __name__ == '__main__':
    main()