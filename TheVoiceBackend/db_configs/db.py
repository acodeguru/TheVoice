# Common functions across different databases
# Main database class that provides some commonly used functionality across different database

from django.db import DatabaseError


class VoiceTVInstanceDB:

    def __init__(self):
        print("Nothing to see here")

    ###################################################################################################
    # returns all rows from a cursor as a dictionary
    ###################################################################################################

    def dict_fetch_all(self, cursor):
        desc = cursor.description
        data = cursor.fetchall()
        if data is None:
            return {}
        else:
            return [
                dict(zip([col[0] for col in desc], row))
                for row in data
            ]

    ###################################################################################################
    # returns one row from a cursor as a dictionary
    ###################################################################################################
    def dict_fetch_one(self, cursor):
        desc = cursor.description
        data = cursor.fetchone()
        if data is None:
            return {}
        else:
            return dict(zip([col[0] for col in desc], data))

    ###################################################################################################
    # returns generic data based on a provided sql
    ###################################################################################################
    def get_report_data(self, cursor, sql):
        try:
            cursor.execute(sql)
            data = list(cursor.fetchall())
            headings = list([d[0] for d in cursor.description])
            data.insert(0, headings)
            return data
        except DatabaseError as e:
            error, = e.args
            return error

    ###################################################################################################
    # returns list based on a the first column of data returned from the provided sql
    ###################################################################################################
    def get_sql_as_list(self, cursor, sql):
        ret = []
        if sql is None:
            error = 'The connection is not initiated or the sql or key have not been passed'
            self.log.critical(error)
            raise Exception(error)

        cursor.execute(sql)

        for row in cursor:
            ret.append(row[0])

        return ret