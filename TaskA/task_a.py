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

def main():
    # Define the file name directly in the code
    reservations = "reservations.txt"

    # Open the file and read its contents
    with open(reservations, "r", encoding="utf-8") as f:
        reservation = f.read().strip()
        parts = reservation.split('|')

    # Print the reservation to the console
    print(reservation)
    print(parts)
    print(f"Reservation number: {parts[0]}")
    print(f"Booker: {parts[1]}")
    print(f"Date: {parts[2]}")
    print(f"Start time: {parts[3]}")
    print(f"Number of hours: {parts[4]}")
    print(f"Hourly price: {parts[5]} €")
    print(f"Total price: {float(parts[4]) * float(parts[5])} €")
    print(f"Paid: {parts[6]}")
    print(f"Location: {parts[7]}")
    print(f"Phone: {parts[8]}")
    print(f"Email: {parts[9]}")    

if __name__ == "__main__":
    main()