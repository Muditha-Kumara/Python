# Copyright (c) 2025 Muditha Kumara.
# License: MIT

from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
from typing import Iterable, List
import calendar


@dataclass(frozen=True)
class Measurement:
    """Stores one hourly measurement row."""

    timestamp: datetime
    day: date
    consumption_kwh: float
    production_kwh: float
    temperature_c: float


def read_data(filename: str) -> List[Measurement]:
    """Reads a CSV file and returns parsed measurement rows."""

    measurements: List[Measurement] = []
    with open(filename, "r", encoding="utf-8") as file:
        header = file.readline()
        if not header:
            return measurements
        for line in file:
            line = line.strip()
            if not line:
                continue
            parts = [part.strip() for part in line.split(";")]
            if len(parts) < 4:
                continue
            timestamp = datetime.fromisoformat(parts[0])
            consumption = _parse_number(parts[1])
            production = _parse_number(parts[2])
            temperature = _parse_number(parts[3])
            measurements.append(
                Measurement(
                    timestamp=timestamp,
                    day=timestamp.date(),
                    consumption_kwh=consumption,
                    production_kwh=production,
                    temperature_c=temperature,
                )
            )
    return measurements


def show_main_menu() -> str:
    """Prints the main menu and returns the user selection."""

    print("Choose a report type:")
    print("1) Daily summary for a date range")
    print("2) Monthly summary for one month")
    print("3) Full year 2025 summary")
    print("4) Exit the program")
    return input("Select: ").strip()


def show_post_menu() -> str:
    """Prints the post-report menu and returns the user selection."""

    print("What would you like to do next?")
    print("1) Write the report to the file report.txt")
    print("2) Create a new report")
    print("3) Exit")
    return input("Select: ").strip()


def create_daily_report(data: List[Measurement]) -> List[str]:
    """Builds a daily report for a selected date range."""

    start_day = _prompt_date("Enter start date (dd.mm.yyyy): ")
    end_day = _prompt_date("Enter end date (dd.mm.yyyy): ")
    while end_day < start_day:
        print("End date must be on or after start date.")
        end_day = _prompt_date("Enter end date (dd.mm.yyyy): ")

    selected = [row for row in data if start_day <= row.day <= end_day]
    return _build_range_report_lines(selected, start_day, end_day)


def create_monthly_report(data: List[Measurement]) -> List[str]:
    """Builds a monthly summary report for a selected month."""

    month = _prompt_month("Enter month number (1-12): ")
    selected = [row for row in data if row.day.month == month]
    month_name = calendar.month_name[month]

    lines = [
        "-----------------------------------------------------",
        f"Report for the month: {month_name}",
    ]
    lines.extend(_build_summary_lines(selected))
    return lines


def create_yearly_report(data: List[Measurement]) -> List[str]:
    """Builds a full-year summary report."""

    lines = [
        "Report for the year: 2025",
    ]
    lines.extend(_build_summary_lines(data))
    return lines


def print_report_to_console(lines: List[str]) -> None:
    """Prints report lines to the console."""

    for line in lines:
        print(line)


def write_report_to_file(lines: List[str]) -> None:
    """Writes report lines to the file report.txt."""

    with open("report.txt", "w", encoding="utf-8") as file:
        for line in lines:
            file.write(f"{line}\n")


def main() -> None:
    """Main function: reads data, shows menus, and controls report generation."""

    data_file = _data_file_path("2025.csv")
    data = read_data(data_file)

    while True:
        choice = show_main_menu()
        if choice == "1":
            report_lines = create_daily_report(data)
        elif choice == "2":
            report_lines = create_monthly_report(data)
        elif choice == "3":
            report_lines = create_yearly_report(data)
        elif choice == "4":
            break
        else:
            print("Invalid selection. Try again.")
            continue

        print_report_to_console(report_lines)
        if not _handle_post_report_menu(report_lines):
            break


def _data_file_path(filename: str) -> str:
    """Returns an absolute path to a data file next to this script."""

    return str(Path(__file__).with_name(filename))


def _parse_number(value: str) -> float:
    """Parses a number with a comma decimal separator into float."""

    return float(value.replace(" ", "").replace(",", "."))


def _format_date(day: date) -> str:
    """Formats a date as dd.mm.yyyy."""

    return f"{day.day}.{day.month}.{day.year}"


def _format_number(value: float) -> str:
    """Formats a number with two decimals and a comma separator."""

    return f"{value:.2f}".replace(".", ",")


def _prompt_date(prompt: str) -> date:
    """Asks for a date in dd.mm.yyyy format and returns it as a date."""

    while True:
        raw = input(prompt).strip()
        try:
            return datetime.strptime(raw, "%d.%m.%Y").date()
        except ValueError:
            print("Invalid date format. Use dd.mm.yyyy.")


def _prompt_month(prompt: str) -> int:
    """Asks for a month number (1-12) and returns it."""

    while True:
        raw = input(prompt).strip()
        try:
            month = int(raw)
        except ValueError:
            print("Invalid month. Enter a number from 1 to 12.")
            continue
        if 1 <= month <= 12:
            return month
        print("Invalid month. Enter a number from 1 to 12.")


def _build_range_report_lines(
    rows: Iterable[Measurement],
    start_day: date,
    end_day: date,
) -> List[str]:
    """Builds report lines for a selected date range."""

    lines = [
        "-----------------------------------------------------",
        f"Report for the period {_format_date(start_day)}-{_format_date(end_day)}",
    ]
    lines.extend(_build_summary_lines(rows))
    return lines


def _build_summary_lines(rows: Iterable[Measurement]) -> List[str]:
    """Builds summary lines for totals and average temperature."""

    rows_list = list(rows)
    if not rows_list:
        return ["No data for the selected period."]

    total_consumption = sum(row.consumption_kwh for row in rows_list)
    total_production = sum(row.production_kwh for row in rows_list)
    avg_temperature = sum(row.temperature_c for row in rows_list) / len(rows_list)

    return [
        f"- Total consumption: {_format_number(total_consumption)} kWh",
        f"- Total production: {_format_number(total_production)} kWh",
        f"- Average temperature: {_format_number(avg_temperature)} °C",
    ]


def _handle_post_report_menu(lines: List[str]) -> bool:
    """Handles the post-report menu and returns False if the program should exit."""

    while True:
        choice = show_post_menu()
        if choice == "1":
            write_report_to_file(lines)
        elif choice == "2":
            return True
        elif choice == "3":
            return False
        else:
            print("Invalid selection. Try again.")


if __name__ == "__main__":
    main()
