
# ✅ TaskA Answer

### Print Screen

![alt text](image.png)

### What was the most memorable thing about this task?

> convert '.' to ','

---

> [!NOTE]
> The material was created with the help of ChatGPT and Copilot.

# 🐍 Task A - Processing a Reservation Line from a File

## 🎯 Goal

The goal of this task is to practice:

*   handling and splitting strings (`str`)
*   using various data types (`int`, `float`, `bool`, `datetime`)
*   converting between data types
*   printing information in a structured way

---

## 📄 Description

* You are given a text file **`reservations.txt`** that contains one line per reservation.
* You are also given a Python script **`read_reservations.py`** that reads the reservations from **`reservations.txt`**.
* Fields are separated by the pipe character `|`.

> [!NOTE]
> **You are not allowed to alter the reservations.txt file in this task!**

**Example line in the `reservations.txt` file:**

```
123|Anna Virtanen|2025-10-31|10:00|2|19.95|True|Meeting Room A|0401234567|anna.virtanen@example.com
```

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

## 🧠 Task Instructions

1.  Copy the file **`reservations.txt`** into your own **Git repo** under the folder **`TaskA`**.
2.  Copy the Python script **`read_reservations.py`** into your **Git repo** under the folder **`TaskA`**.
3.  Rename the Python script file to **`task_a.py`**
4.  Modify the script so that, when executed, it prints the following output:


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

> [!NOTE]  
> All console output is emitted via print() calls scoped to main()

---

### 🧩 Tips

*   Split the line using the `split('|')` method as in the example below → produces a list-type variable (the following examples then work):

    ```python
    reservation = reservation.split('|')
    ```

> [!NOTE]  
> If you don’t do the above, in the examples below `reservation[0]` is equivalent to `reservation.split('|')[0]`.

*   Convert data types. A few examples:

    ```python
    reservation_number = int(reservation[0])
    hourly_price = float(reservation[5])
    paid = bool(reservation[6])
    ```

*   You can convert the date and start time to `datetime`:

    ```python
    from datetime import datetime

    day = datetime.strptime(reservation[2], "%Y-%m-%d").date()
    finnish_day = day.strftime("%d.%m.%Y")

    time = datetime.strptime(reservation[3], "%H:%M").time()
    finnish_time = time.strftime("%H.%M")
    ```

> [!TIP]  
> Why is this important, even though we could use plain text?  
> BECAUSE `datetime` doesn’t accept a date like 2025-10-32 and will raise an error during conversion!  
> This helps keep the data consistent and correct!

*   Compute the total price by multiplying the number of hours by the hourly price.

*   If you want to print “Yes” or “No” based on the paid flag, use a conditional expression like this:

    ```python
    print(f"Paid: {'Yes' if paid else 'No'}")
    ```

---

## 📤 Submission Instructions to Itslearning

Submit a **link to your GitHub repo** ([Example link](https://github.com/vheikkiniemi/FundamentalsOfPythonProgramming2026S/tree/main/Tasks/TaskA)) and a **screenshot of the console** showing the program execution and output.

The folder structure of the Github repo must be as follows:

```
📁 Github Repo/
├─ 📁 TaskA/
   ├─ 🐍 task_a.py
   └─ 📄 reservations.txt

```


Also include a short note:

> What was the most memorable thing about this task?

---

## 💬 Grading Criteria (points):
* **`0:`** The program does not work and/or its structure has been significantly altered. The file names are incorrect.
* **`1:`** The program works, but the output does not meet the requirements, and the correct data types have not been used.
* **`2:`** The program produces the required output and uses the correct data types. The program structure follows the given task.

---

## 💡 Most Common Errors and Solutions

| Error            | Cause                             | Solution                               |
| ---------------- | --------------------------------- | -------------------------------------- |
| “File not found” | Script is run in the wrong folder | Move to the folder where the script is |
| “File not found” | Files haven’t been copied         | Copy the files into your folder        |
| “File not found” | Files are misnamed                | Verify the file names are correct      |

---