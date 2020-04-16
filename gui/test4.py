from PyQt5 import QtCore, QtGui, QtWidgets
from csv_gen import *
import os.path

class Ui_MainWindow(object):
    def __init__(self):
        self.file_name = "transformers"
        self.file_directory = ""
        self.output_directory = ""

    def set_outputtext(self,text):
        self.OutPutText.clear
        self.OutPutText.setText(text)

    def check_paths(self):
        if os.path.exists(self.file_directory) and os.path.exists(self.output_directory):
            return True
        elif not os.path.exists(self.file_directory):
            self.set_outputtext("Invalid data directory.\n" + self.file_directory)
            return False
        elif not os.path.exists(self.output_directory):
            self.set_outputtext("Invalid output directory.\n" + self.output_directory)
            return False

    def csvButton1_onclick(self,MainWindow):
        self.OutPutText.clear
        if self.check_paths():
            create_section_csv(self.file_name, self.file_directory, self.output_directory)
            self.set_outputtext("CSV created.")
    
    def csvButton2_onclick(self, MainWindow):
        self.OutPutText.clear
        if self.check_paths():
            create_section_stat_csv(self.file_name, self.file_directory, self.output_directory)

    def data_onclick(self):
        self.file_directory = self.DataPath.text()
        self.set_outputtext(self.file_directory)
        self.DataPath.clear()

    def csv_onclick(self):
        self.output_directory = self.CSVPath.text()
        self.set_outputtext(self.output_directory)
        self.CSVPath.clear()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(305, 484)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.CSV = QtWidgets.QGroupBox(self.centralwidget)
        self.CSV.setGeometry(QtCore.QRect(10, 10, 281, 421))
        self.CSV.setObjectName("CSV")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.CSV)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 120, 81, 201))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.csvButton1 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.csvButton1.setObjectName("csvButton1")
        self.csvButton1.clicked.connect(self.csvButton1_onclick)
        self.verticalLayout.addWidget(self.csvButton1)
        self.csvButton2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.csvButton2.setObjectName("csvButton2")
        self.csvButton2.clicked.connect(self.csvButton2_onclick)
        self.verticalLayout.addWidget(self.csvButton2)
        self.csvButton3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.csvButton3.setObjectName("csvButton3")
        self.verticalLayout.addWidget(self.csvButton3)
        self.csvButton4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.csvButton4.setObjectName("csvButton4")
        self.verticalLayout.addWidget(self.csvButton4)
        self.csvButton5 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.csvButton5.setObjectName("csvButton5")
        self.verticalLayout.addWidget(self.csvButton5)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.CSV)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(110, 120, 161, 161))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.OutPutText = QtWidgets.QTextEdit(self.verticalLayoutWidget_2)
        self.OutPutText.setObjectName("OutPutText")
        self.verticalLayout_2.addWidget(self.OutPutText)
        self.pushButton = QtWidgets.QPushButton(self.CSV)
        self.pushButton.setGeometry(QtCore.QRect(220, 290, 51, 23))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.CSV)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 20, 261, 92))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.gridLayout = QtWidgets.QGridLayout(self.verticalLayoutWidget_3)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.CSVPath = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.CSVPath.setObjectName("CSVPath")
        self.gridLayout.addWidget(self.CSVPath, 1, 0, 1, 1)
        self.DataPath = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.DataPath.setObjectName("DataPath")
        self.gridLayout.addWidget(self.DataPath, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.csvButton = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.csvButton.setObjectName("csvButton")
        self.csvButton.clicked.connect(self.csv_onclick)
        self.gridLayout.addWidget(self.csvButton, 1, 1, 1, 1)
        self.dataButton = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.dataButton.setObjectName("dataButton")
        self.dataButton.clicked.connect(self.data_onclick)
        self.gridLayout.addWidget(self.dataButton, 3, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 305, 21))
        self.menubar.setObjectName("menubar")
        self.menuTest = QtWidgets.QMenu(self.menubar)
        self.menuTest.setObjectName("menuTest")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuTest.menuAction())

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.OutPutText.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.CSV.setTitle(_translate("MainWindow", "CSV Generation"))
        self.csvButton1.setText(_translate("MainWindow", "CSV 1"))
        self.csvButton2.setText(_translate("MainWindow", "CSV 2"))
        self.csvButton3.setText(_translate("MainWindow", "CSV 3"))
        self.csvButton4.setText(_translate("MainWindow", "CSV 4"))
        self.csvButton5.setText(_translate("MainWindow", "CSV 5"))
        self.pushButton.setText(_translate("MainWindow", "Clear"))
        self.label_2.setText(_translate("MainWindow", "Data Path:"))
        self.label.setText(_translate("MainWindow", "CSV Path:"))
        self.csvButton.setText(_translate("MainWindow", "Enter"))
        self.dataButton.setText(_translate("MainWindow", "Enter"))
        self.menuTest.setTitle(_translate("MainWindow", "Data Visualization"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
