from database import Database

def setup():
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'Pass@123',  # replace with your MySQL password
        'database': 'school_management'
    }

    Database.create_database(db_config['host'], db_config['user'], db_config['password'], db_config['database'])
    Database.create_tables(db_config['host'], db_config['user'], db_config['password'], db_config['database'])

if __name__ == "__main__":
    setup()
