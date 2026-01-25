# Copyright (c) 2025 Ville Heikkiniemi
#
# This code is licensed under the MIT License.
# You are free to use, modify, and distribute this code,
# provided that the original copyright notice is retained.
#
# See LICENSE file in the project root for full license information.

# Modified by nnn according to given task

"""
Program that reads reservation details from a file
and prints them to the console:

Reservation number: 123
Booker: Anna Virtanen
Date: 31.10.2025
Start time: 10.00
Number of hours: 2
Hourly price: 19,95 €
Total price: 39,90 €
Paid: Yes
Location: Meeting Room A
Phone: 0401234567
Email: anna.virtanen@example.com
"""

from datetime import datetime

def main():
    # Define the file name directly in the code
    reservations = "reservations.txt"

    # Open the file and read its contents
    with open(reservations, "r", encoding="utf-8") as f:
        reservation = f.read().strip()
        parts = reservation.split('|')

    # Print the reservation to the console
    # print(reservation)
    # print(parts)

    reservation_number = int(parts[0])
    print(f"Reservation number: {reservation_number}")

    print(f"Booker: {parts[1]}")

    day = datetime.strptime(parts[2], "%Y-%m-%d").date()
    # print(type(day))
    finnish_day = day.strftime("%d.%m.%Y")
    # print(type(finnish_day))
    print(f"Date: {finnish_day}")

    time = datetime.strptime(parts[3], "%H:%M").time()
    # print(type(time))
    finnish_time = time.strftime("%H.%M")
    print(f"Start time: {finnish_time}")

    hours = int(parts[4])
    print(f"Number of hours: {hours}")

    hourly_price = float(parts[5])
    formatted_hourly = f"{hourly_price:.2f}".replace(".", ",")
    print(f"Hourly price: {formatted_hourly} €")

    total_price = hours * hourly_price
    formatted_total = f"{total_price:.2f}".replace(".", ",")
    print(f"Total price: {formatted_total} €")

    paid = bool(parts[6])
    # paid = parts[6] == 'True'
    print(f"Paid: {'Yes' if paid else 'No'}")

    print(f"Location: {parts[7]}")
    print(f"Phone: {parts[8]}")
    print(f"Email: {parts[9]}")    

if __name__ == "__main__":
    main()
