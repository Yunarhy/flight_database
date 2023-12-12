sql_add_information_of_clients = """
INSERT INTO clients (first_name, last_name, surname, Password, Email)
VALUES (%s, %s, %s, %s, %s);
"""
sql_add_information_of_booking = """
INSERT INTO booking (first_name, last_name, flight_info, seat_number, flight_date, arrival_date, flight_duration, aircompany, firstairport, secondairport)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
"""
sql_delete_flight = """
DELETE FROM `Booking` WHERE flight_info = %s
"""
sql_authentication_clients = """SELECT "Correct" AS Result FROM `clients` WHERE first_name = %s 
AND last_name = %s AND surname = %s AND password = %s AND email = %s; """
