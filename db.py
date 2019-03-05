import psycopg2
from pprint import pprint


class DatabaseConnection:
    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                host="localhost",
                database="ulak",
                user="postgres",
                password="1",
                port="5432")
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
        except:
            pprint("Does not Db:")

    def get_user_password(self, username):
        get_users_query = """select password from users where username = '{0}'""".format(username)
        self.cursor.execute(get_users_query)
        response = self.cursor.fetchone()

        return response[0] if response is not None else False

    def user_signup(self, username, password, user_type_id):
        signup_query = """insert into users (username, password, user_types_id) values('{0}', '{1}', '{2}')""" \
            .format(username, password, user_type_id)
        try:
            self.cursor.execute(signup_query)
            return True
        except:
            return False

    """   
    :return
    """

    def hour_report(self, saha_id, swm_id, reset_cause, swm_date, hour_date, sum_reset_id, hour_reset_id, bbca0, bbca1,
                    bbca2):
        print(type(sum_reset_id), sum_reset_id)
        hour_query = """ insert into hours (saha_id, bbca0, bbca1, bbca2, sum_reset_id, hour_reset_id, swm_id, reset_cause,
         swm_date_value, hour_date_value) values ('{0}', '{1}', '{2}', '{3}', '{4}', {5}, '{6}', '{7}', '{8}', '{9}')""".format(
            saha_id, bbca0, bbca1, bbca2, sum_reset_id, hour_reset_id, swm_id, reset_cause, swm_date, hour_date)
        try:
            self.cursor.execute(hour_query)
            return True
        except Exception as e:
            print(e)
            return False

    def get_hour_report(self):
        select_query = """select * from hours"""
        try:
            self.cursor.execute(select_query)
            response = self.cursor.fetchall()
            return response
        except:
            return False

    def day_report(self, day_date, saha_id, sum_reset_id, swm_did, sum_ue):
        day_query = """insert into day_ra(day_date, saha_id, sum_reset_id, swm_did, sum_ue) values 
        ({{0}, {1}, {2}, {3}, {4}})""".format(day_date, saha_id, sum_reset_id, swm_did, sum_ue)
        try:
            self.cursor.execute(day_query)
            return True
        except:
            return False

    def create_table(self):
        create_table_command = "Create table alarms (id PRIMARY key serial, name varchar(100), tanım varchar(100))"
        self.cursor.execute(create_table_command)

    def insert_new_record(self, tanim, name):
        insert_command = """INSERT INTO alarms(name, tanım) Values(tanim , new_record[1])"""
        pprint(insert_command)
        self.cursor.execute(insert_command)

    def update_record(self):
        update_command = "update alarms set name =aaa where id =3"
        self.cursor.execute(update_command)

    def query_all(self):
        self.cursor.execute('Select * from alarms')
        cats = self.cursor.fetchall()
        for cat in cats:
            pprint("alarms : {0}".format(cat))

    def drop_table(self):
        drop_table_command = "Drop table alarms"
        self.cursor.execute(drop_table_command)


''' if __name__ == '__main__':
    database_connection = DatabaseConnection()
    # database_connection.create_table()
    # database_connection.insert_new_record()
    # database_connection.query_all()
    # database_connection.update_record()
    # database_connection.drop_Table() '''
