# -*- coding: utf-8 -*-
from __future__ import division
import sys
from PyQt4 import QtGui, QtCore

class Calculator(QtGui.QWidget):
    """
    A simple calculator using PyQt4.
    Supports +, -, *, / operations with GUI.

    Task 1: Formal Code Review Target
    This code has been forked from an open-source PyQt calculator project and reviewed
    for software testing assignment purposes.
    """

    def __init__(self):
        super(Calculator, self).__init__()
        self.initUI()

    def initUI(self):
        # Initializes GUI components and state
        self.num1 = '0'               # First number input as string
        self.num2 = ''                # Second number input
        self.result = ''              # Calculation result
        self.operator = ''            # +, -, *, /
        self.operator_set = False     # Flag to check if operator has been set
        self.result_displayed = False # Flag for result visibility

        # Window configuration
        self.setWindowTitle("PyQt4 Calculator")
        self.setGeometry(300, 300, 280, 370)
        grid = QtGui.QGridLayout()
        self.setLayout(grid)

        # Display output area
        self.display = QtGui.QTextBrowser()
        self.display.setText("0")
        self.display.setFixedHeight(80)
        self.display.setFont(QtGui.QFont("Arial", 18))
        grid.addWidget(self.display, 0, 0, 1, 4)

        # Define button text and corresponding handlers
        buttons = [
            ('7', self.press_digit), ('8', self.press_digit), ('9', self.press_digit), ('/', self.set_operator),
            ('4', self.press_digit), ('5', self.press_digit), ('6', self.press_digit), ('*', self.set_operator),
            ('1', self.press_digit), ('2', self.press_digit), ('3', self.press_digit), ('-', self.set_operator),
            ('0', self.press_digit), ('.', self.press_dot), ('C', self.clear), ('+', self.set_operator),
            ('=', self.calculate_result)
        ]

        # Arrange buttons in a grid layout
        positions = [(i + 1, j) for i in range(5) for j in range(4)]
        for pos, (text, handler) in zip(positions, buttons):
            btn = QtGui.QPushButton(text)
            btn.setFixedSize(60, 40)
            btn.setFont(QtGui.QFont("Arial", 14))
            # Use lambda to bind each button's label to its handler
            btn.clicked.connect(lambda _, t=text: handler(t))
            grid.addWidget(btn, *pos)

        self.show()

    def press_digit(self, digit):
        """Handles number input (0–9)."""
        if self.result_displayed:
            self.clear('C')

        if not self.operator_set:
            if self.num1 == '0':
                self.num1 = digit
            else:
                self.num1 += digit
            self.display.setText(self.num1)
        else:
            self.num2 += digit
            self.display.setText(f"{self.num1} {self.operator} {self.num2}")

    def press_dot(self, _):
        """Handles decimal point input."""
        if not self.operator_set:
            if '.' not in self.num1:
                self.num1 += '.'
                self.display.setText(self.num1)
        else:
            if '.' not in self.num2:
                self.num2 += '.'
                self.display.setText(f"{self.num1} {self.operator} {self.num2}")

    def set_operator(self, op):
        """Sets the operator (+, -, *, /)."""
        if not self.operator_set:
            self.operator = op
            self.operator_set = True
            self.display.setText(f"{self.num1} {self.operator}")

    def calculate_result(self, _):
        """
        Calculates the result when '=' is pressed.
        Task 1: This function was a key target of formal review:
        - Checked input validation
        - Handled divide by zero
        - Used proper try-except blocks
        """
        try:
            n1 = float(self.num1)
            n2 = float(self.num2)
            if self.operator == '+':
                self.result = str(n1 + n2)
            elif self.operator == '-':
                self.result = str(n1 - n2)
            elif self.operator == '*':
                self.result = str(n1 * n2)
            elif self.operator == '/':
                if n2 == 0:
                    self.result = "Error: Division by zero"
                else:
                    self.result = str(n1 / n2)
            else:
                self.result = "Invalid operation"
        except:
            self.result = "Error"

        self.display.setText(f"{self.num1} {self.operator} {self.num2} = {self.result}")
        self.result_displayed = True

    def clear(self, _):
        """Clears all values and resets the calculator."""
        self.num1 = '0'
        self.num2 = ''
        self.operator = ''
        self.operator_set = False
        self.result_displayed = False
        self.display.setText("0")

# Application Entry Point
def main():
    app = QtGui.QApplication(sys.argv)
    ex = Calculator()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
