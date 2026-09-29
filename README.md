# Campus Lost & Found Management System

## 1. Overview of the Project

The **Campus Lost & Found Management System** is a simple terminal-based Python application designed to help students report and find lost items within a campus.

The system allows users to report lost items, report items they have found, search through reported items, and identify possible matches between lost and found items.

The project focuses on applying basic problem-solving and programming concepts such as **input/output, conditional statements, loops, functions, lists, dictionaries, searching, sorting, and input validation**.

A simple matching algorithm is also included. It compares details such as the item name, category, colour, location, and description to calculate a match score between a lost item and a found item.

---

## 2. Features

### 2.1 Report Lost Item

Users can enter information about a lost item, including:

* Item name
* Category
* Colour
* Location where it was lost
* Date
* Description

The information is stored in the program for further searching and matching.

### 2.2 Report Found Item

Users can report an item that they have found by entering:

* Item name
* Category
* Colour
* Location where it was found
* Date
* Description

### 2.3 Search Items

Users can search reported items using:

* Item name
* Category
* Colour
* Location

The system displays items that match the entered search keyword.

### 2.4 Find Possible Match

The system compares a selected lost item with reported found items.

The matching algorithm considers:

* Item name
* Category
* Colour
* Location
* Description

A score is calculated for each possible match, and the results are displayed from the highest score to the lowest score.

### 2.5 View All Items

Users can view all currently reported lost and found items.

### 2.6 Update Item Status

Users can update the status of an item.

Available statuses include:

* Lost
* Found
* Matched
* Claimed

### 2.7 Input Validation

The system checks user input to prevent common invalid entries, such as:

* Empty input
* Invalid menu choices
* Invalid item IDs
* Incorrect date format

---

## 3. Technologies and Tools Used

### Programming Language

* **Python**

### Concepts Used

* Variables
* Input and output
* Conditional statements
* `for` and `while` loops
* Functions
* Lists
* Dictionaries
* Tuples
* Searching
* Sorting
* String operations
* Input validation
* Basic algorithm design

### Development Tools

* Python interpreter
* Any Python-compatible code editor or IDE
* Terminal / Command Prompt
* Git and GitHub for version control

---

## 4. Installation and Setup

### Step 1: Install Python

Download and install Python from the official Python website if it is not already installed.

Python 3.x is recommended.

### Step 2: Download or Clone the Project

Clone the GitHub repository using:

```bash
git clone <repository-url>
```

Or download the project as a ZIP file and extract it.

### Step 3: Open the Project Folder

Open the project folder in a terminal or command prompt.

For example:

```bash
cd Campus-Lost-and-Found
```

### Step 4: Run the Program

Run the main Python file using:

```bash
python main.py
```

If your system uses `python3`, use:

```bash
python3 main.py
```

### Step 5: Use the Main Menu

After starting the program, the following menu will be displayed:

```text
==================================================
       CAMPUS LOST & FOUND SYSTEM
==================================================

1. Report Lost Item
2. Report Found Item
3. Search Items
4. Find Possible Match
5. View All Items
6. Update Item Status
7. Exit
```

Enter the number corresponding to the operation you want to perform.

---

## 5. Instructions for Testing

Testing can be performed directly through the terminal by checking each major function of the system.

### Test 1: Report a Lost Item

1. Run the program.
2. Select `1. Report Lost Item`.
3. Enter valid item information.
4. Check that the system displays:

   * "Lost item reported successfully."
   * A Lost Item ID.

**Expected Result:**
The lost item should be added successfully.

---

### Test 2: Report a Found Item

1. Select `2. Report Found Item`.
2. Enter valid item information.
3. Check that the system displays a Found Item ID.

**Expected Result:**
The found item should be added successfully.

---

### Test 3: Search for an Item

1. Add one or more lost/found items.
2. Select `3. Search Items`.
3. Enter an item name, category, colour, or location.

**Expected Result:**
The system should display items containing the entered search information.

---

### Test 4: Find a Possible Match

1. Report a lost item.
2. Report a found item with some or all similar details.
3. Select `4. Find Possible Match`.
4. Enter the Lost Item ID.

**Expected Result:**
The system should compare the lost item with found items and display possible matches with their match scores.

---

### Test 5: Update Item Status

1. Select `6. Update Item Status`.
2. Select whether the item is lost or found.
3. Enter the Item ID.
4. Select a new status.

**Expected Result:**
The item's status should be updated successfully.

---

### Test 6: Invalid Input

Test the program using invalid inputs such as:

```text
abc
empty input
invalid menu number
invalid item ID
incorrect date format
```

**Expected Result:**
The program should display an appropriate error message instead of terminating unexpectedly.

---

### Test 7: Exit

1. Select `7. Exit`.

**Expected Result:**

```text
Thank you for using the Campus Lost & Found System.
```

The program should terminate normally.

---

## 6. Testing Summary

The following areas should be tested before submission:

| Feature    | Test Case                    | Expected Result          |
| ---------- | ---------------------------- | ------------------------ |
| Lost Item  | Enter valid lost item        | Item is added            |
| Found Item | Enter valid found item       | Item is added            |
| Search     | Search using keyword         | Matching items displayed |
| Matching   | Compare lost and found items | Match score displayed    |
| Status     | Update item status           | Status changes           |
| Validation | Enter invalid input          | Error message displayed  |
| Exit       | Select exit option           | Program terminates       |

The testing focuses on verifying that the major functions work correctly and that incorrect user input is handled properly.
