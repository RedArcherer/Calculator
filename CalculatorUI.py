from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication 
from PyQt5.uic import loadUi
import sys



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(334, 391)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 140, 331, 191))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.decimal = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.decimal.setObjectName("decimal")
        self.gridLayout.addWidget(self.decimal, 4, 1, 1, 1)
        self.zero = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.zero.setObjectName("zero")
        self.gridLayout.addWidget(self.zero, 4, 0, 1, 1)
        self.minus = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.minus.setObjectName("minus")
        self.gridLayout.addWidget(self.minus, 2, 3, 1, 1)
        self.one = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.one.setObjectName("one")
        self.gridLayout.addWidget(self.one, 3, 0, 1, 1)
        self.six = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.six.setObjectName("six")
        self.gridLayout.addWidget(self.six, 2, 2, 1, 1)
        self.eight = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.eight.setObjectName("eight")
        self.gridLayout.addWidget(self.eight, 1, 1, 1, 1)
        self.plus = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.plus.setObjectName("plus")
        self.gridLayout.addWidget(self.plus, 1, 3, 1, 1)
        self.multiply = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.multiply.setObjectName("multiply")
        self.gridLayout.addWidget(self.multiply, 3, 3, 1, 1)
        self.five = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.five.setObjectName("five")
        self.gridLayout.addWidget(self.five, 2, 1, 1, 1)
        self.three = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.three.setObjectName("three")
        self.gridLayout.addWidget(self.three, 3, 2, 1, 1)
        self.two = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.two.setObjectName("two")
        self.gridLayout.addWidget(self.two, 3, 1, 1, 1)
        self.four = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.four.setObjectName("four")
        self.gridLayout.addWidget(self.four, 2, 0, 1, 1)
        self.nine = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.nine.setObjectName("nine")
        self.gridLayout.addWidget(self.nine, 1, 2, 1, 1)
        self.equal = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.equal.setObjectName("equal")
        self.gridLayout.addWidget(self.equal, 4, 2, 1, 1)
        self.divide = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.divide.setObjectName("divide")
        self.gridLayout.addWidget(self.divide, 4, 3, 1, 1)
        self.seven = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.seven.setObjectName("seven")
        self.gridLayout.addWidget(self.seven, 1, 0, 1, 1)
        self.square = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.square.setObjectName("square")
        self.gridLayout.addWidget(self.square, 0, 0, 1, 1)
        self.root = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.root.setObjectName("root")
        self.gridLayout.addWidget(self.root, 0, 1, 1, 1)
        self.clear = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.clear.setObjectName("clear")
        self.gridLayout.addWidget(self.clear, 0, 2, 1, 2)
        self.CurrentDisplay = QtWidgets.QLabel(self.centralwidget)
        self.CurrentDisplay.setGeometry(QtCore.QRect(0, 50, 321, 81))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.CurrentDisplay.setFont(font)
        self.CurrentDisplay.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.CurrentDisplay.setObjectName("CurrentDisplay")
        self.TotalDisplay = QtWidgets.QLabel(self.centralwidget)
        self.TotalDisplay.setGeometry(QtCore.QRect(0, 0, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.TotalDisplay.setFont(font)
        self.TotalDisplay.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.TotalDisplay.setObjectName("TotalDisplay")
        self.AC = QtWidgets.QPushButton(self.centralwidget)
        self.AC.setGeometry(QtCore.QRect(0, 330, 331, 23))
        self.AC.setObjectName("AC")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 334, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.seven.clicked.connect(lambda: self.UpdateCurrentLabel('7'))
        self.eight.clicked.connect(lambda: self.UpdateCurrentLabel('8'))
        self.nine.clicked.connect(lambda: self.UpdateCurrentLabel('9'))
        self.four.clicked.connect(lambda: self.UpdateCurrentLabel('4'))
        self.five.clicked.connect(lambda: self.UpdateCurrentLabel('5'))
        self.six.clicked.connect(lambda: self.UpdateCurrentLabel('6'))
        self.one.clicked.connect(lambda: self.UpdateCurrentLabel('1'))
        self.two.clicked.connect(lambda: self.UpdateCurrentLabel('2'))
        self.three.clicked.connect(lambda: self.UpdateCurrentLabel('3'))
        self.zero.clicked.connect(lambda: self.UpdateCurrentLabel('0'))
        self.decimal.clicked.connect(lambda: self.UpdateCurrentLabel('.'))
        self.equal.clicked.connect(self.evaluate)
        self.multiply.clicked.connect(lambda: self.OperationClicked('*'))
        self.divide.clicked.connect(lambda: self.OperationClicked('/'))
        self.plus.clicked.connect(lambda: self.OperationClicked('+'))
        self.minus.clicked.connect(lambda: self.OperationClicked('-'))
        self.clear.clicked.connect(self.Clear)
        self.AC.clicked.connect(self.ClearAll)
        self.square.clicked.connect(self.Square)
        self.root.clicked.connect(self.SquareRoot)
        
        self.CurrentExpression = ""
        self.DisplayedTotalExpression = ""
        self.TotalExpression = ""

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.decimal.setText(_translate("MainWindow", "."))
        self.decimal.setShortcut(_translate("MainWindow", "."))
        self.zero.setText(_translate("MainWindow", "0"))
        self.zero.setShortcut(_translate("MainWindow", "0"))
        self.minus.setText(_translate("MainWindow", "-"))
        self.minus.setShortcut(_translate("MainWindow", "-"))
        self.one.setText(_translate("MainWindow", "1"))
        self.six.setText(_translate("MainWindow", "6"))
        self.six.setShortcut(_translate("MainWindow", "6"))
        self.eight.setText(_translate("MainWindow", "8"))
        self.eight.setShortcut(_translate("MainWindow", "8"))
        self.plus.setText(_translate("MainWindow", "+"))
        self.plus.setShortcut(_translate("MainWindow", "+"))
        self.multiply.setText(_translate("MainWindow", "x"))
        self.multiply.setShortcut(_translate("MainWindow", "*"))
        self.five.setText(_translate("MainWindow", "5"))
        self.five.setShortcut(_translate("MainWindow", "5"))
        self.three.setText(_translate("MainWindow", "3"))
        self.three.setShortcut(_translate("MainWindow", "3"))
        self.two.setText(_translate("MainWindow", "2"))
        self.two.setShortcut(_translate("MainWindow", "2"))
        self.four.setText(_translate("MainWindow", "4"))
        self.four.setShortcut(_translate("MainWindow", "4"))
        self.nine.setText(_translate("MainWindow", "9"))
        self.nine.setShortcut(_translate("MainWindow", "9"))
        self.equal.setText(_translate("MainWindow", "="))
        self.equal.setShortcut(_translate("MainWindow", "="))
        self.divide.setText(_translate("MainWindow", "÷"))
        self.divide.setShortcut(_translate("MainWindow", "/"))
        self.seven.setText(_translate("MainWindow", "7"))
        self.seven.setShortcut(_translate("MainWindow", "7"))
        self.square.setText(_translate("MainWindow", "x²"))
        self.root.setText(_translate("MainWindow", "√x"))
        self.clear.setText(_translate("MainWindow", "CLEAR"))
        self.CurrentDisplay.setText(_translate("MainWindow", "0"))
        self.TotalDisplay.setText(_translate("MainWindow", "0"))
        self.AC.setText(_translate("MainWindow", "CLEAR ALL"))

    def UpdateCurrentLabel(self, value):
        self.CurrentExpression += value
        self.CurrentDisplay.setText(self.CurrentExpression)

    def UpdateTotalLabel(self): 
        self.TotalExpression += self.CurrentExpression
        self.TotalDisplay.setText(self.DisplayedTotalExpression)

    def OperationClicked(self, operator):
        self.DisplayedTotalExpression += self.CurrentExpression
        self.CurrentExpression += operator
        self.TotalExpression += self.CurrentExpression
        
        appended = ""
        if operator == "*":
            appended = "\u00D7"
        elif operator == "/":
            appended = "\u00F7"
        else:
            appended = operator

        self.DisplayedTotalExpression+=appended

        self.TotalDisplay.setText(self.DisplayedTotalExpression)
        self.CurrentDisplay.setText("")
        self.CurrentExpression = ""

    def Square(self):
        CEint = int(self.CurrentExpression)
        CEint = CEint ** 2
        self.CurrentExpression = str(CEint)
        self.CurrentDisplay.setText(self.CurrentExpression)

    def SquareRoot(self):
        CEint = int(self.CurrentExpression)
        CEint = CEint ** 0.5
        self.CurrentExpression = str(CEint)
        self.CurrentDisplay.setText(self.CurrentExpression)


    def evaluate(self):
        self.TotalExpression += self.CurrentExpression
        self.DisplayedTotalExpression += self.CurrentExpression
        self.TotalDisplay.setText(self.DisplayedTotalExpression)
        self.CurrentDisplay.setText("") 
        self.FinalAnswer = str(eval(self.TotalExpression))
        self.CurrentDisplay.setText(self.FinalAnswer)
        self.CurrentExpression = self.FinalAnswer

    def Clear(self):
        self.CurrentExpression = ""
        self.UpdateCurrentLabel("0")

    def ClearAll(self):
        self.CurrentExpression = ""
        self.TotalExpression = ""
        self.DisplayedTotalExpression = ""
        self.CurrentDisplay.setText("0")
        self.TotalDisplay.setText("0")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())