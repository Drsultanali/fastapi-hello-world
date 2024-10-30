from sqlmodel import create_engine, SQLModel
import os
 
connection_string = os.getenv("DB_URI")
print(connection_string)

engine = create_engine(connection_string)
def create_table():
    SQLModel.metadata.create_all(engine)

