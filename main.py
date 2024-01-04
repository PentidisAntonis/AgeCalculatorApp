from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, QLineEdit, QPushButton

# We used QGridLayout because it is more powerful than QVBoxLayout
# (it only allows to position the widgets vertically stacked on top of one another)
# QHBoxLayout (it only allows to position the widgets horizontally stacked on top of one another)


import sys

import sys
from datetime import datetime

class AgeCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Age Calculator")
        grid = QGridLayout()

        # create widgets
        name_label = QLabel("Name:")
        self.name_line_edit = QLineEdit()

        date_birth_label = QLabel("Date of Birth MM/DD/YYYY:")
        self.date_birth_line_edit = QLineEdit()
        #from local variable to intance variable so that I can accesses it below in the year_of_birth

        # buttons
        calculate_button = QPushButton("Calculate Age")
        calculate_button.clicked.connect(self.calculate_age)
        self.output_label = QLabel("")

        # Add widgets to grid
        grid.addWidget(name_label, 0, 0)                    # row, column 0.0
        grid.addWidget(self.name_line_edit, 0, 1)           # row, column 0.1

        grid.addWidget(date_birth_label, 1, 0)              # row, column 1.0
        grid.addWidget(self.date_birth_line_edit, 1, 1)     # row, column 1.1

        grid.addWidget(calculate_button, 2, 0, 1, 2)  # row, column 2.0 span 1 row and 2 columns
        grid.addWidget(self.output_label, 3, 0, 1, 2)  # row, column 3.0 span 1 row and 2 columns


        self.setLayout(grid)  ##this method is inherited by the QWidget

    def calculate_age(self):
        current_year = datetime.now().year
        date_of_birth = self.date_birth_line_edit.text()  # to extract it
        year_of_birth = datetime.strptime(date_of_birth,
                                          "%m/%d/%Y").date().year  # we converted it in a datetime object and then we get the year
        age = current_year - year_of_birth
        self.output_label.setText(f"{self.name_line_edit.text()} is {age} years old.")  # setText is a method of a QLabel


app = QApplication(sys.argv)
age_calculator = AgeCalculator()
age_calculator.show()
sys.exit(app.exec())