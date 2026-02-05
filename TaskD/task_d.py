"""
Task D - Weekly Electricity Consumption and Production (kWh) in the Console

This program reads hourly electricity consumption and production data from a CSV file,
calculates daily totals for week 42, converts from Wh to kWh, and displays the results
in a user-friendly table format with Finnish formatting.

Author: Muditha Kumara
Date: February 2026
"""

from datetime import datetime, date
from typing import List, Dict


def read_data(filename: str) -> list:
    """
    Reads the CSV file and returns the rows in a suitable structure.
    
    Args:
        filename: Path to the CSV file containing electricity data
        
    Returns:
        List of dictionaries, each containing parsed data for one hour
    """
    data = []
    
    # Open and read the file
    file = open(filename, 'r', encoding='utf-8')
    
    # Skip the first line (header)
    first_line = file.readline()
    
    # Read each line of data
    for line in file:
        # Remove extra spaces and split by semicolon
        parts = line.strip().split(';')
        
        # Make sure we have enough columns
        if len(parts) >= 7:
            # Create a dictionary for this hour's data
            row = {}
            row['timestamp'] = datetime.fromisoformat(parts[0])
            row['consumption_v1'] = int(parts[1])
            row['consumption_v2'] = int(parts[2])
            row['consumption_v3'] = int(parts[3])
            row['production_v1'] = int(parts[4])
            row['production_v2'] = int(parts[5])
            row['production_v3'] = int(parts[6])
            
            # Add this row to our list
            data.append(row)
    
    file.close()
    return data


def calculate_daily_totals(data: list) -> dict:
    """
    Calculates daily totals for consumption and production phases.
    
    Args:
        data: List of hourly measurement dictionaries
        
    Returns:
        Dictionary with date as key and daily totals as values
    """
    daily_totals = {}
    
    # Go through each hour's data
    for row in data:
        # Get the date from the timestamp
        day = row['timestamp'].date()
        
        # If this is a new day, create empty totals
        if day not in daily_totals:
            daily_totals[day] = {}
            daily_totals[day]['consumption_v1'] = 0
            daily_totals[day]['consumption_v2'] = 0
            daily_totals[day]['consumption_v3'] = 0
            daily_totals[day]['production_v1'] = 0
            daily_totals[day]['production_v2'] = 0
            daily_totals[day]['production_v3'] = 0
        
        # Add this hour's values to the daily totals
        daily_totals[day]['consumption_v1'] = daily_totals[day]['consumption_v1'] + row['consumption_v1']
        daily_totals[day]['consumption_v2'] = daily_totals[day]['consumption_v2'] + row['consumption_v2']
        daily_totals[day]['consumption_v3'] = daily_totals[day]['consumption_v3'] + row['consumption_v3']
        daily_totals[day]['production_v1'] = daily_totals[day]['production_v1'] + row['production_v1']
        daily_totals[day]['production_v2'] = daily_totals[day]['production_v2'] + row['production_v2']
        daily_totals[day]['production_v3'] = daily_totals[day]['production_v3'] + row['production_v3']
    
    return daily_totals


def get_finnish_weekday(date_obj: date) -> str:
    """
    Returns the Finnish weekday name for a given date.
    
    Args:
        date_obj: Date object
        
    Returns:
        Finnish weekday name
    """
    # Get the weekday number (0=Monday, 6=Sunday)
    weekday_number = date_obj.weekday()
    
    # Convert number to Finnish name
    if weekday_number == 0:
        return 'Maanantai'
    elif weekday_number == 1:
        return 'Tiistai'
    elif weekday_number == 2:
        return 'Keskiviikko'
    elif weekday_number == 3:
        return 'Torstai'
    elif weekday_number == 4:
        return 'Perjantai'
    elif weekday_number == 5:
        return 'Lauantai'
    else:
        return 'Sunnuntai'


def main() -> None:
    """
    Main function: reads data, computes daily totals, and prints the report.
    """
    filename = 'week42.csv'
    
    # Read data from CSV file
    data = read_data(filename)
    
    # Calculate daily totals
    daily_totals = calculate_daily_totals(data)
    
    # Print the header
    print("Week 42 electricity consumption and production (kWh, by phase)")
    print()
    print("Day          Date        Consumption [kWh]               Production [kWh]")
    print("            (dd.mm.yyyy)  v1      v2      v3             v1     v2     v3")
    print("---------------------------------------------------------------------------")
    
    # Get all dates and sort them
    all_dates = list(daily_totals.keys())
    all_dates.sort()
    
    # Print each day
    for day in all_dates:
        # Get the totals for this day
        totals = daily_totals[day]
        
        # Convert Wh to kWh (divide by 1000)
        cons_v1_kwh = totals['consumption_v1'] / 1000
        cons_v2_kwh = totals['consumption_v2'] / 1000
        cons_v3_kwh = totals['consumption_v3'] / 1000
        prod_v1_kwh = totals['production_v1'] / 1000
        prod_v2_kwh = totals['production_v2'] / 1000
        prod_v3_kwh = totals['production_v3'] / 1000
        
        # Format with 2 decimals and comma separator
        cons_v1_str = f"{cons_v1_kwh:.2f}".replace(".", ",")
        cons_v2_str = f"{cons_v2_kwh:.2f}".replace(".", ",")
        cons_v3_str = f"{cons_v3_kwh:.2f}".replace(".", ",")
        prod_v1_str = f"{prod_v1_kwh:.2f}".replace(".", ",")
        prod_v2_str = f"{prod_v2_kwh:.2f}".replace(".", ",")
        prod_v3_str = f"{prod_v3_kwh:.2f}".replace(".", ",")
        
        # Get weekday name and format date
        weekday = get_finnish_weekday(day)
        date_str = day.strftime("%d.%m.%Y")
        
        # Print the row
        print(f"{weekday:<12} {date_str:<11} "
              f"{cons_v1_str:>6}  {cons_v2_str:>6}  {cons_v3_str:>6}         "
              f"{prod_v1_str:>6} {prod_v2_str:>6} {prod_v3_str:>6}")


if __name__ == "__main__":
    main()
