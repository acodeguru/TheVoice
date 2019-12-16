from django.db import connections, DatabaseError
from db_configs import db


class VoiceTVInstance(db.VoiceTVInstanceDB):
    cursor = ''

    def __init__(self):
        self.cursor = connections['default'].cursor()
        super().__init__()

    def __del__(self):
        self.cursor.close()

    ###################################################################################################
    # execute and fetch related data 
    ###################################################################################################

    def execute_related_query(self, execute_query, params):
        try:
            self.cursor.execute(execute_query, params)
            return self.dict_fetch_all(self.cursor)
        except DatabaseError as e:
            error, = e.args
            return error

    def execute_insert_query(self, execute_query):
        try:
            self.cursor.execute(execute_query )
            return self.cursor.rowcount
        except DatabaseError as e:
            error, = e.args
            return error