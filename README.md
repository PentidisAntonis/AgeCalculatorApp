Age Calculator

**Description**

This simple PyQt6 application allows users to calculate their age based on the provided name and date of birth (MM/DD/YYYY). The application uses a graphical user interface (GUI) to input the necessary information and display the calculated age.

Dependencies

Install Python

If you don't have Python installed, you can download and install it from the official Python website: [Python Downloads](https://www.python.org/downloads/)

Install PyQt6

Make sure you have PyQt6 installed. You can install it using the following command:

>pip install PyQt6

**Usage**

Run the script.
Enter your name in the "Name" field.

Enter your date of birth in the "Date of Birth MM/DD/YYYY" field.

Click the "Calculate Age" button.

The calculated age will be displayed below the button.

**Code Overview**

The code uses PyQt6 to create a simple GUI with the following components:

**QLabel**: Display labels for "Name" and "Date of Birth MM/DD/YYYY".

**QLineEdit**: Input fields for name and date of birth.

**QPushButton**: Button to trigger the age calculation.

**QGridLayout**: Organizes the layout of the widgets in a grid.

**QWidget**: Base class for all UI objects.

The calculate_age method uses the current year and the provided date of birth to calculate the age and updates the output label accordingly.

**How to Run**

Run the script using a Python interpreter. The application window will appear, and you can interact with it using the provided interface.

>python your_script_name.py

**Note**

Ensure that PyQt6 is installed before running the script.

Make sure to enter the date of birth in the specified format (MM/DD/YYYY) for accurate age calculation.