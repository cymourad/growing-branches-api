# this file constitutes a base class that connects to the db

import os
from dotenv import load_dotenv

from sqlalchemy import create_engine, Table, MetaData, Column, Integer, String
# from sqlalchemy.ext.declarative import declarative_base

# this is the base class of a sqlalchyemy model
# Base = declarative_base()


class GBTable(object):
    def __init__(self):
        # get the config from env variables
        load_dotenv()
        self._db_username = os.getenv("DB_USERNAME")
        self._db_password = os.getenv("DB_PASSWORD")
        self._db_name = os.getenv("DB_NAME")
        self._db_hostname = os.getenv("DB_HOSTNAME")
        print(self._db_username, self._db_password,
              self._db_name, self._db_hostname)
    # create a connection to the DB

    def get_sql_engine(self):
        return create_engine("mysql+mysqldb://{username}:{password}@{hostname}/{db_name}".format(
            username=self._db_username, password=self._db_password, hostname=self._db_hostname, db_name=self._db_name
        ))

    def create_test_table(self):
        meta_data = MetaData()

        test_table = Table("test_table", meta_data,
                           Column("id", Integer, primary_key=True),
                           Column("dummy_column", String(32))
                           )

        engine = self.get_sql_engine()

        meta_data.create_all(engine)

    # echo prints all the SQL that gets generated to the console using Python logging
