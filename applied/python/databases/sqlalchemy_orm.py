# Engine
from sqlalchemy import create_engine

'''
engine is the main object which sqlalchemy uses to interct with the database
it does not make connection until we call an operation which requires interaction with db
in url : sqlite-> type of db we are connecting can be MySQL, postgresql etc.
       : pysqlite-> the python DBAPI interface for interacting with the db
       : memory -> location of db -- in memory, on disk, network etc.
echo true means log all sql events to stdout.
'''
engine = create_engine(url="sqlite+pysqlite:///:memory:", echo=True)
