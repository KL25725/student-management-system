from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QWidget,
    QGridLayout,
    QLineEdit,
    QPushButton,
)

import sys
from datetime import datetime

# hello hello test
class AgeCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Age Calculator")
        grid = QGridLayout()

        # Create widgets
        name_label = QLabel("Name:")
        self.name_line_edit = QLineEdit()

        birth_label = QLabel("Date of birth (MM/DD/YY):")
        self.birth_line_edit = QLineEdit()

        calculate_button = QPushButton("Calculate Age")
        calculate_button.clicked.connect(self.calculate_age)
        self.output_label = QLabel("")

        # Add widgets to grid
        grid.addWidget(name_label, 0, 0)
        grid.addWidget(self.name_line_edit, 0, 1)
        grid.addWidget(birth_label, 1, 0)
        grid.addWidget(self.birth_line_edit, 1, 1)
        grid.addWidget(calculate_button, 2, 0, 1, 2)
        grid.addWidget(self.output_label, 3, 0, 1, 2)

        self.setLayout(grid)

    def calculate_age(self):
        current_year, current_month, current_day = (
            datetime.now().year,
            datetime.now().month,
            datetime.now().day,
        )
        name = self.name_line_edit.text()
        birth_date = self.birth_line_edit.text()
        birth_year, birth_month, birth_day = (
            int(birth_date[-4:]),
            int(birth_date[:2].strip("0")),
            int(birth_date[3:5].strip("0")),
        )
        if birth_month - current_month > 0:
            age = current_year - birth_year - 1
        elif birth_month - current_month == 0:
            if birth_day - current_day > 0:
                age = current_year - birth_year - 1
            else:
                age = current_year - birth_year
        else:
            age = current_year - birth_year
        # birth_year = datetime.strptime(birth_date, "%m/%d/%Y").date().year
        # age = current_year - birth_year

        self.output_label.setText(f"{name} is {age} years old.")


app = QApplication(sys.argv)
age_calculator = AgeCalculator()
age_calculator.show()
sys.exit(app.exec())
