import mysql.connector
from sql_request import *
class DataBase:
    def __init__(self):
        self.mydb = mysql.connector.connect(
                port=3306,
                host='localhost',
                user='root',
                password='egormirkin',
                database='flight_passengers',

        )
    def add_to_database_clients_info(self, first_name_value, last_name_value, surname_value, Password_value, Email_value):
        val = (first_name_value, last_name_value, surname_value, Password_value, Email_value)
        self.mydb.cursor().execute(sql_add_information_of_clients, val)
        self.mydb.commit()

    def add_to_database_booking_info(self, first_name_value, last_name_value, flight_info_value, seat_number_value, flight_date_value, arrival_date_value, flight_duration_value, aircompany_value, firstairport_value, secondairport_value):
        val = (first_name_value, last_name_value, flight_info_value, seat_number_value, flight_date_value, arrival_date_value, flight_duration_value, aircompany_value, firstairport_value, secondairport_value)
        self.mydb.cursor().execute(sql_add_information_of_booking, val)
        self.mydb.commit()

    def select_booking_info(self):
        with self.mydb.cursor(buffered=True) as cursor:
            cursor.execute('SELECT * FROM `Booking`')
            row = cursor.fetchone()

            while row is not None:
                yield row
                row = cursor.fetchone()

    def delete_flights_info(self, Deleteflights_value):
        flight_id_to_delete = Deleteflights_value
        self.mydb.cursor().execute(sql_delete_flight, (flight_id_to_delete,))
        self.mydb.commit()

    def select_authentication_clients_info(self, first_name_value, last_name_value, surname_value, Password_value, Email_value):
        with self.mydb.cursor(buffered=True) as cursor:
            val= (first_name_value, last_name_value, surname_value, Password_value, Email_value)
            cursor.execute(sql_authentication_clients, val)
            result = cursor.fetchone()
            return result