import oracledb
import getpass
def initialize_db2_connection():
    # userpwd = getpass.getpass("Enter password :")
    userpwd = 'admin'
    # Add your logic to initialize the DB2 connection here
    print("Initializing DB2 connection...")
    pool = oracledb.create_pool(user="system", password=userpwd, dsn="localhost:1521/XEPDB1",
                            min=1, max=5, increment=1)

    with pool.acquire() as connection:
        with connection.cursor() as cursor:
            for result in cursor.execute("SELECT * from all_users"):
                print(result)
    # Simulate initializing the DB2 connection (random values)
    db2_status = "DB2_CONNECTION_SUCCESSFUL"

    # Simulate preparing statements (random values)
    db2_prepared_status = "STATEMENTS_PREPARED"

    # Check if the DB2 connection and statement preparation were successful
    if db2_status == "DB2_CONNECTION_SUCCESSFUL" and db2_prepared_status == "STATEMENTS_PREPARED":
        print("DB2 connection initialized successfully.")
    else:
        print("Error: DB2 connection initialization failed.")

# Call the function to initialize the DB2 connection
initialize_db2_connection()
