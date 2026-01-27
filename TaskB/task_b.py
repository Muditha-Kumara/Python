# Copyright (c) 2025 Ville Heikkiniemi
#
# This code is licensed under the MIT License.
# You are free to use, modify, and distribute this code,
# provided that the original copyright notice is retained.
#
# See LICENSE file in the project root for full license information.

# Modified by nnn according to given task

"""
A program that reads reservation data from a file
and prints them to the console using functions:

Reservation number: 123
Booker: Anna Virtanen
Date: 31.10.2025
Start time: 10.00
Number of hours: 2
Hourly rate: 19,95 €
Total price: 39,90 €
Paid: Yes
Venue: Meeting Room A
Phone: 0401234567
Email: anna.virtanen@example.com

"""
from datetime import datetime

def print_booker(reservation: list) -> None:
    """
    Prints the reservation number

    Parameters:
     reservation (lst): reservation -> columns separated by |
    """
    booker = reservation[1]
    print(f"Booker: {booker}")


def print_reservation_number(reservation: list) -> None:
    """
    Prints the reservation number

    Parameters:
     reservation (lst): reservation -> columns separated by |
    """
    reservation_number = int(reservation[0])
    print(f"Reservation number: {reservation_number}")


def print_date(reservation: list) -> None:
    """
    Prints the reservation date in dd.mm.yyyy format.

    Parameters:
     reservation (list): A list of reservation details.
    """
    date_str = reservation[2]
    date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()
    print(f"Date: {date_obj.strftime('%d.%m.%Y')}")


def print_start_time(reservation: list) -> None:
    """
    Prints the start time in HH.MM format.

    Parameters:
     reservation (list): A list of reservation details.
    """
    time_str = reservation[3]
    time_obj = datetime.strptime(time_str, "%H:%M").time()
    print(f"Start time: {time_obj.strftime('%H.%M')}")


def print_hours(reservation: list) -> None:
    """
    Prints the number of hours.

    Parameters:
     reservation (list): A list of reservation details.
    """
    hours = int(reservation[4])
    print(f"Number of hours: {hours}")


def print_hourly_rate(reservation: list) -> None:
    """
    Prints the hourly rate with a comma as a decimal separator and a € symbol.

    Parameters:
     reservation (list): A list of reservation details.
    """
    hourly_rate = float(reservation[5])
    print(f"Hourly price: {hourly_rate:.2f}".replace(".", ",") + " €")


def print_total_price(reservation: list) -> None:
    """
    Calculates and prints the total price.

    Parameters:
     reservation (list): A list of reservation details.
    """
    hours = int(reservation[4])
    hourly_rate = float(reservation[5])
    total_price = hours * hourly_rate
    print(f"Total price: {total_price:.2f}".replace(".", ",") + " €")


def print_paid(reservation: list) -> None:
    """
    Prints whether the reservation is paid or not.

    Parameters:
     reservation (list): A list of reservation details.
    """
    is_paid = reservation[6] == "True"
    print(f"Paid: {'Yes' if is_paid else 'No'}")
    # print(f"Paid: {is_paid and 'Yes' or 'No'}")
    # print(f"Paid: {is_paid and '' or 'No'}")
    # print(f"Paid: {'Yes' if reservation[6] == 'True' else 'No'}")
    # print(f"Paid: {reservation[6] == 'True' and 'Yes' or 'No'}")


def print_venue(reservation: list) -> None:
    """
    Prints the venue of the reservation.

    Parameters:
     reservation (list): A list of reservation details.
    """
    venue = reservation[7]
    print(f"Venue: {venue}")


def print_phone(reservation: list) -> None:
    """
    Prints the phone number of the booker.

    Parameters:
     reservation (list): A list of reservation details.
    """
    phone = reservation[8]
    print(f"Phone: {phone}")


def print_email(reservation: list) -> None:
    """
    Prints the email of the booker.

    Parameters:
     reservation (list): A list of reservation details.
    """
    email = reservation[9]
    print(f"Email: {email}")


def main():
    """
    Reads reservation data from a file and
    prints them to the console using functions
    """
    # Define the file name directly in the code
    reservations = "reservations.txt"

    # Open the file, read it, and split the contents
    with open(reservations, "r", encoding="utf-8") as f:
        reservation = f.read().strip()
        reservation = reservation.split('|')

    # Implement the remaining parts following
    # the function print_booker(reservation)

    # The functions to be created should perform type conversions
    # and print according to the sample output

    print_reservation_number(reservation)
    print_booker(reservation)
    print_date(reservation)
    print_start_time(reservation)
    print_hours(reservation)
    print_hourly_rate(reservation)
    print_total_price(reservation)
    print_paid(reservation)
    print_venue(reservation)
    print_phone(reservation)
    print_email(reservation)

if __name__ == "__main__":
    main()
