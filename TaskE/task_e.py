# Copyright (c) 2026 Muditha Kumara
# License: MIT
"""
Task E - Three Weeks of Electricity Consumption and Production (kWh) to a File

This program reads hourly electricity consumption and production data from three CSV files,
calculates daily totals for weeks 41, 42, and 43, converts from Wh to kWh, and writes the results
in a user-friendly report to summary.txt with Finnish formatting.
"""

from datetime import datetime, date
import csv
from typing import List, Dict, Any

WEEK_FILES = ["week41.csv", "week42.csv", "week43.csv"]
WEEK_NUMBERS = [41, 42, 43]
WEEKDAY_NAMES = [
    "Maanantai", "Tiistai", "Keskiviikko", "Torstai",
    "Perjantai", "Lauantai", "Sunnuntai"
]


def read_data(filename: str) -> List[Dict[str, Any]]:
    """Reads a CSV file and returns a list of hourly measurements as dictionaries."""
    data = []
    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=";")
        next(reader, None)  # Skip header
        for parts in reader:
            if len(parts) >= 7:
                row = {
                    "timestamp": datetime.fromisoformat(parts[0]),
                    "consumption_v1": int(parts[1]),
                    "consumption_v2": int(parts[2]),
                    "consumption_v3": int(parts[3]),
                    "production_v1": int(parts[4]),
                    "production_v2": int(parts[5]),
                    "production_v3": int(parts[6]),
                }
                data.append(row)
    return data


def summarize_week(data: List[Dict[str, Any]]) -> Dict[date, Dict[str, Any]]:
    """Calculates daily summaries for one week from hourly data."""
    daily = {}
    for row in data:
        day = row["timestamp"].date()
        if day not in daily:
            daily[day] = {
                "consumption_v1": 0,
                "consumption_v2": 0,
                "consumption_v3": 0,
                "production_v1": 0,
                "production_v2": 0,
                "production_v3": 0,
            }
        daily[day]["consumption_v1"] += row["consumption_v1"]
        daily[day]["consumption_v2"] += row["consumption_v2"]
        daily[day]["consumption_v3"] += row["consumption_v3"]
        daily[day]["production_v1"] += row["production_v1"]
        daily[day]["production_v2"] += row["production_v2"]
        daily[day]["production_v3"] += row["production_v3"]
    return daily


def format_number(value: float) -> str:
    """Formats a float to two decimals with comma as decimal separator."""
    return f"{value:.2f}".replace(".", ",")


def format_row(day: date, summary: Dict[str, Any]) -> str:
    """Formats a report row for one day with Finnish conventions."""
    weekday = WEEKDAY_NAMES[day.weekday()]
    date_str = f"{day.day:02d}.{day.month:02d}.{day.year}"
    cons = [format_number(summary[f"consumption_v{i}"]/1000) for i in range(1,4)]
    prod = [format_number(summary[f"production_v{i}"]/1000) for i in range(1,4)]
    return f"{weekday:<9} {date_str:<12} {cons[0]:>6} {cons[1]:>6} {cons[2]:>6}   {prod[0]:>6} {prod[1]:>6} {prod[2]:>6}"


def write_report(week_summaries: List[Dict[date, Dict[str, Any]]], week_numbers: List[int], filename: str) -> None:
    """Writes the weekly summaries to a text file in a clear, structured format."""
    with open(filename, "w", encoding="utf-8") as file:
        total_cons = [0,0,0]
        total_prod = [0,0,0]
        for week_idx, summary in enumerate(week_summaries):
            week_num = week_numbers[week_idx]
            file.write(f"Week {week_num} electricity consumption and production (kWh, by phase)\n")
            file.write("Day      Date           Consumption [kWh]            Production [kWh]\n")
            file.write("           v1      v2      v3           v1     v2      v3\n")
            file.write("---------------------------------------------------------------------------\n")
            for day in sorted(summary.keys()):
                row = format_row(day, summary[day])
                file.write(row + "\n")
                for i in range(3):
                    total_cons[i] += summary[day][f"consumption_v{i+1}"]
                    total_prod[i] += summary[day][f"production_v{i+1}"]
            file.write("\n")
        # Optional combined summary
        file.write("Total for all weeks (kWh):\n")
        cons_str = " ".join([format_number(c/1000) for c in total_cons])
        prod_str = " ".join([format_number(p/1000) for p in total_prod])
        file.write(f"Consumption: {cons_str}\n")
        file.write(f"Production:  {prod_str}\n")


def main() -> None:
    """Main function: reads data, computes weekly summaries, and writes the report to a file."""
    week_summaries = []
    for fname in WEEK_FILES:
        data = read_data(fname)
        summary = summarize_week(data)
        week_summaries.append(summary)
    write_report(week_summaries, WEEK_NUMBERS, "summary.txt")


if __name__ == "__main__":
    main()
