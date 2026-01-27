> [!NOTE]
> The material was created with the help of ChatGPT and Copilot.

# 🐍  Task B - Using Functions

## 🎯 goal

The goal of this task is to practice:

*   using functions in Python
*   performing data type conversions inside functions
*   building a program that reads and prints a reservation line in a structured way

---

## 📄 Description

*   You are given a text file **`reservations.txt`**, where each line contains the details of a single reservation.
*   You are also given a Python script **`read_reservations.py`**, which reads the reservations from the **`reservations.txt`** file.
*   The data is separated by a vertical bar `|`. → In the program, line 51 contains `reservation = reservation.split('|')` → a list-type variable `reservation` is used.

> [!NOTE]
> **You are not allowed to alter the reservations.txt file in this task!**

**Example line in the `reservations.txt` file:**


```
123|Anna Virtanen|2025-10-31|10:00|2|19.95|True|Meeting Room A|0401234567|anna.virtanen@example.com
```

---

The line contains the following fields:

| Column | Description        | Data Type       |
| ------ | ------------------ | --------------- |
| 1      | Reservation number | `int`           |
| 2      | Booker’s name      | `str`           |
| 3      | Reservation date   | `datetime.date` |
| 4      | Start time         | `datetime.time` |
| 5      | Number of hours    | `int`           |
| 6      | Hourly price (€)   | `float`         |
| 7      | Paid               | `bool`          |
| 8      | Resource           | `str`           |
| 9      | Phone number       | `str`           |
| 10     | Email              | `str`           |

---

## 🧠 Task instructions

1.  Copy the file **`reservations.txt`** into your own **Git repo** under the folder **`TaskB`**.
2.  Copy the Python script **`read_reservations.py`** into your **Git repo** under the folder **`TaskB`**.
3.  Rename the Python script file to **`task_b.py`**
4.  Modify the script so that, when executed, it prints the following output:

      ```
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
      ```
5. The program has its own function for each data type and output → Implement the following functions, taking type hints and docstrings into account.

      ```python
      def print_reservation_number(reservation): ...
      def print_booker(reservation): ...
      def print_date(reservation): ...
      def print_start_time(reservation): ...
      def print_hours(reservation): ...
      def print_hourly_rate(reservation): ...
      def print_total_price(reservation): ...
      def print_paid(reservation): ...
      def print_venue(reservation): ...
      def print_phone(reservation): ...
      def print_email(reservation): ...
      ```

---

## 📤 Submission Instructions to Itslearning

Submit a **link to your GitHub repo** ([Example link](https://github.com/vheikkiniemi/FundamentalsOfPythonProgramming2026S/tree/main/Tasks/TaskB)) and a **screenshot of the console** showing the program execution and output.

The folder structure of the Github repo must be as follows:

```
📁 Github Repo/
├─ 📁 TaskA/
|  ├─ 🐍 task_a.py
|  └─ 📄 reservations.txt
├─ 📁 TaskB/
   ├─ 🐍 task_b.py
   └─ 📄 reservations.txt

```


Also include a short note:

> What was the most memorable thing about this task?

---

## 💬 Grading Criteria (points):
* **`0:`** The program does not work and/or its structure has been significantly altered. The file names are incorrect.
* **`1:`** The program works, but the output does not meet the requirements, and the correct data types and/or functions have not been used.
* **`2:`** The program produces the required output and uses the correct data types and functions. The program structure follows the given task.

---

## 💡 Most Common Errors and Solutions

| Error            | Cause                             | Solution                               |
| ---------------- | --------------------------------- | -------------------------------------- |
| “File not found” | Script is run in the wrong folder | Move to the folder where the script is |
| “File not found” | Files haven’t been copied         | Copy the files into your folder        |
| “File not found” | Files are misnamed                | Verify the file names are correct      |

---