import flet as ft
from database import DataBase

def main(page: ft.Page):
    page.add(ft.Text(f"Initial route: {page.route}"))
    # Начало
    page.title = "База даних про перевезення авіапасажирів"
    first_name = ft.TextField(label="Ім'я", autofocus=True, icon=ft.icons.MAN)
    last_name = ft.TextField(label="Фамілія", icon=ft.icons.MAN)
    surname = ft.TextField(label="По-батькові", icon=ft.icons.MAN)
    Password = ft.TextField(label="Пароль", icon=ft.icons.PASSWORD)
    Email = ft.TextField(label="Електронна адреса", icon=ft.icons.EMAIL)

    greetings = ft.Column()
# Booking
    seat_number = ft.TextField(label="Номер місця", icon=ft.icons.CHAIR)
    flight_info = ft.TextField(label="Рейс", icon=ft.icons.AIRPLANE_TICKET)
    flight_date = ft.TextField(label="Дата вильоту", icon=ft.icons.DATE_RANGE)
    arrival_date = ft.TextField(label="Дата прибуття", icon=ft.icons.DATE_RANGE)
    flight_duration = ft.TextField(label="Тривалість польоту", icon=ft.icons.LOCK_CLOCK)
    aircompany = ft.TextField(label="Авіакомпанія", icon=ft.icons.AIRPLANEMODE_ACTIVE)
    firstairport = ft.TextField(label="Аеропорт відправки", icon=ft.icons.OUTPUT)
    secondairport = ft.TextField(label="Аеропорт прибуття", icon=ft.icons.INPUT)

    testtime = ft.Text(value=" ", color="red")


    def btn_click(e):
        if all(value is not None and value != "" for value in
               [first_name.value, last_name.value, surname.value, Password.value, Email.value]):
            first_name_value = first_name.value
            last_name_value = last_name.value
            surname_value = surname.value
            Password_value = Password.value
            Email_value = Email.value
            result = DataBase().select_authentication_clients_info(first_name_value, last_name_value, surname_value, Password_value, Email_value)
            if result:
                page.update(page.go("/suc_auth"))
        else:
            testtime.value = "Хоча б одне значення порожнє."
            page.update()

    def Registration(e):
        if all(value is not None and value != "" for value in
               [first_name.value, last_name.value, surname.value, Password.value, Email.value]):
            first_name_value = first_name.value
            last_name_value = last_name.value
            surname_value = surname.value
            Password_value = Password.value
            Email_value = Email.value
            DataBase().add_to_database_clients_info(first_name_value, last_name_value, surname_value, Password_value, Email_value)
            first_name.value = ""
            last_name.value = ""
            surname.value = ""
            Password.value = ""
            Email.value = ""
            page.update()
        else:
            testtime.value = "Хоча б одне значення порожнє."
            page.update()

    def Booking(e):
        if all(value is not None and value != "" for value in
               [first_name.value, last_name.value, flight_info.value, seat_number.value, flight_date.value, arrival_date.value, flight_duration.value, aircompany.value, firstairport.value, secondairport.value]):
            first_name_value = first_name.value
            last_name_value = last_name.value
            flight_info_value = flight_info.value
            seat_number_value = seat_number.value
            flight_date_value = flight_date.value
            arrival_date_value = arrival_date.value
            flight_duration_value = flight_duration.value
            aircompany_value = aircompany.value
            firstairport_value = firstairport.value
            secondairport_value = secondairport.value
            DataBase().add_to_database_booking_info(first_name_value, last_name_value, flight_info_value, seat_number_value, flight_date_value, arrival_date_value, flight_duration_value, aircompany_value, firstairport_value, secondairport_value)
            last_name.value = ""
            flight_info.value = ""
            seat_number.value = ""
            flight_date.value = ""
            arrival_date.value = ""
            flight_duration.value = ""
            aircompany.value = ""
            firstairport.value = ""
            secondairport.value = ""
            page.update(page.go("/suc_auth"))
        else:
            testtime.value = "Хоча б одне значення порожнє."
            page.update()



    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                        ft.AppBar(title=ft.Text("Вхід"), bgcolor=ft.colors.SURFACE_VARIANT),

                        first_name,
                        last_name,
                        surname,
                        Password,
                        Email,
                        ft.ElevatedButton("Авторизуватися", on_click=btn_click, icon=ft.icons.LOCK_OPEN),
                        ft.ElevatedButton("Реєстарція", on_click=lambda _: page.go("/reg"), icon=ft.icons.LOCK),
                        testtime,
                        ft.ElevatedButton("Про програму", on_click=lambda _: page.go("/about")),

                        ],
                )
            )
        if page.route == "/about":
            page.views.append(
                ft.View(
                    "/about",
                    [
                        ft.AppBar(title=ft.Text("Про програму"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Text("Ця програма була разроблена для курсового проекту студентом Міркіним Єгором"),
                        ft.ElevatedButton("Назад", on_click=lambda _: page.go("/")),
                    ],
                )
            )
        if page.route == "/reg":
            page.views.append(
                ft.View(
                    "/reg",
                    [
                        ft.AppBar(title=ft.Text("Зареєструватися"), bgcolor=ft.colors.SURFACE_VARIANT),

                        first_name,
                        last_name,
                        surname,
                        Password,
                        Email,
                        ft.ElevatedButton("Назад", on_click=lambda _: page.go("/"), icon=ft.icons.ARROW_BACK),
                        ft.ElevatedButton("Зареєструватися", on_click=Registration, icon=ft.icons.LOCK),
                        testtime,
                    ],
                )
            )
        if page.route == "/suc_auth":
            page.views.append(
                ft.View(
                    "/suc_auth",
            [
                        ft.AppBar(title=ft.Text("Меню"), bgcolor=ft.colors.SURFACE_VARIANT),

                        ft.ElevatedButton("Переглянути авіарейс", on_click=lambda _: page.go("/flights"), icon=ft.icons.VIEW_LIST),
                        ft.ElevatedButton("Зареєструвати авіарейс", on_click=lambda _: page.go("/Booking"), icon=ft.icons.EDIT_DOCUMENT),
                    ],
                )
            )
        if page.route == "/Booking":
            page.views.append(

                ft.View(
                    "/Booking",
                    [

                        ft.AppBar(title=ft.Text("Реєстрація авіарейсу"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.ElevatedButton("Назад", on_click=lambda _: page.go("/suc_auth")),

                        testtime,
                        first_name,
                        last_name,
                        flight_info,
                        aircompany,
                        firstairport,
                        secondairport,
                        seat_number,
                        flight_date,
                        arrival_date,
                        flight_duration,
                        ft.ElevatedButton("Зареєструвати авіарейс", on_click= Booking, icon=ft.icons.LOCK)
                    ],
                    scroll=True
                )
            )
        if page.route == "/flights":
            page.views.append(

                ft.View(
                    "/flights",
                    [

                        ft.AppBar(title=ft.Text("Авіарейси"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.ElevatedButton("Оновити", on_click=rebut, icon=ft.icons.REFRESH),
                        lv,
                        ft.ElevatedButton("Видалити рейс", on_click=lambda _: page.go("/flight_delete"), icon=ft.icons.DELETE),
                        ft.ElevatedButton("Назад", on_click=lambda _: page.go("/suc_auth"), icon=ft.icons.ARROW_BACK),

                    ],
                )
            )
        if page.route == "/flight_delete":
            page.views.append(

                ft.View(
                    "/flight_delete",
                    [
                        ft.AppBar(title=ft.Text("Видалення авіарейсів"), bgcolor=ft.colors.SURFACE_VARIANT),
                        lv,
                        flight_info,
                        ft.ElevatedButton("Видалити", on_click=Deleteflights_button, icon=ft.icons.DELETE_OUTLINE),
                        ft.ElevatedButton("Назад", on_click=lambda _: page.go("/flights"), icon=ft.icons.ARROW_BACK),
                        ],
                    )
                )

    #лист рейсов
    lv = ft.ListView(expand=1, spacing=10, item_extent=50)
    page.add(lv)
    for row in DataBase().select_booking_info():
        lv.controls.append(ft.Text("Id клієнта {}, Ім'я {}, Фамілія {}, Інформація про рейс {}, Номер місця {}, Дата вильоту {}, Дата прильоту {},"
                                   " Тривалість {} годин, Авіакомпанія {}, Аеропорт відправки {}, Аеропорт прибуття {}".format(
            *row)))
    #обновлення сторінки авіарейсів
    def rebut(e):

        lv.controls.append(ft.Text(""))
        page.update(lv)
        lv.controls.clear()
        for row in DataBase().select_booking_info():
            lv.controls.append(ft.Text(
                "Id клієнта {}, Ім'я {}, Фамілія {}, Інформація про рейс {}, Номер місця {}, Дата вильоту {}, Дата прильоту {},"
                "Тривалість {} годин, Авіакомпанія {}, Аеропорт відправки {}, Аеропорт прибуття {}".format(
                *row)))
        # Видалення рейсів
        Deleteflights = ft.TextField(label="Номер рейсу")

    def Deleteflights_button(e):
        Deleteflights_value = flight_info.value
        DataBase().delete_flights_info(Deleteflights_value)
        page.update()
        first_name.focus()


    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main,)