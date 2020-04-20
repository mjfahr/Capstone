# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\miser\Desktop\test2.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from csv_gen import *
from generic_graphs import *
import os.path

class Ui_MainWindow(object):
    def __init__(self):
        self.file_name = "transformers"
        self.file_directory = ""
        self.output_directory = ""

    def set_outputtext(self,text):
        self.OutPutText.clear
        self.OutPutText.setText(text)

    def get_dataDir(self, MainWindow):
        self.file_directory = QtWidgets.QFileDialog.getExistingDirectory(None, "Select directory.")
        self.file_directory = self.file_directory + '/'
        self.DataPath.setText(self.file_directory)

    def get_outDir(self, MainWindow):
        self.output_directory = QtWidgets.QFileDialog.getExistingDirectory(None, "Select output directory.")
        self.output_directory = self.output_directory + '/'
        self.CSVPath.setText(self.output_directory)

    def csvButton1_onclick(self,MainWindow):
        create_section_csv(self.file_name, self.file_directory, self.output_directory)
        self.set_outputtext("section_files.csv created.")

    def csvButton2_onclick(self, MainWindow):
        create_section_stat_csv(self.file_name, self.file_directory, self.output_directory)
        self.set_outputtext("section_word_statistics.csv created.")

    def graphButton1_onclick(self, MainWindow):
        fileName = QtWidgets.QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()", "", "CSV Files (*.csv)")
        important_word = QtWidgets.QInputDialog.getText(None, "Get Word", "Important Word:", QtWidgets.QLineEdit.Normal, "")
        user_input_graph_name = QtWidgets.QInputDialog.getText(None, "Get Graph Name", "Graph Name:", QtWidgets.QLineEdit.Normal, "")
        graph = Graphs(fileName[0], user_input_graph_name[0])
        frequency_per_section(graph, important_word)

    def graphButton2_onclick(self, MainWindow):
        fileName = QtWidgets.QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()", "", "CSV Files (*.csv)")
        user_input = QtWidgets.QInputDialog.getText(None, "Get Important Words", "Important Words:", QtWidgets.QLineEdit.Normal, "")
        important_words = list(user_input[0].split(" "))
        user_input_graph_name = QtWidgets.QInputDialog.getText(None, "Get Graph Name", "Graph Name:", QtWidgets.QLineEdit.Normal, "")
        graph = Graphs(fileName[0], user_input_graph_name[0])
        frequency_comparison(graph, important_words)    

    def graphButton3_onclick(self, Mainwindow):
        fileName = QtWidgets.QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()", "", "CSV Files (*.csv)")
        user_input = QtWidgets.QInputDialog.getText(None, "Get Important Words", "Important Words:", QtWidgets.QLineEdit.Normal, "")
        important_words = list(user_input[0].split(" "))
        user_input_graph_name = QtWidgets.QInputDialog.getText(None, "Get Graph Name", "Graph Name:", QtWidgets.QLineEdit.Normal, "")
        graph = Graphs(fileName, user_input_graph_name[0])
        multi_word_frequency(graph, important_words)
    
    def graphButton4_onclick(self, MainWindow):
        fileName = QtWidgets.QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()", "", "CSV Files (*.csv)")
        user_input = QtWidgets.QInputDialog.getText(None, "Get Important Words", "Important Words:", QtWidgets.QLineEdit.Normal, "")
        important_words = list(user_input[0].split(" "))
        user_input_graph_name = QtWidgets.QInputDialog.getText(None, "Get Graph Name", "Graph Name:", QtWidgets.QLineEdit.Normal, "")
        graph = Graphs(fileName[0], user_input_graph_name[0])
        multi_word_frequency_alternative(graph, important_words)  

    def graphButton5_onclick(self, MainWindow):
        fileName = QtWidgets.QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()", "", "CSV Files (*.csv)")
        user_input_graph_name = QtWidgets.QInputDialog.getText(None, "Get Graph Name", "Graph Name:", QtWidgets.QLineEdit.Normal, "")
        graph = Graphs(fileName[0], user_input_graph_name[0])
        word_count_section(graph)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(851, 390)
        MainWindow.setFixedSize(851,390)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.CSV = QtWidgets.QGroupBox(self.centralwidget)
        self.CSV.setGeometry(QtCore.QRect(10, 10, 311, 351))
        self.CSV.setObjectName("CSV")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.CSV)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 20, 291, 144))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.gridLayout = QtWidgets.QGridLayout(self.verticalLayoutWidget_3)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        self.csvButton = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.csvButton.setObjectName("csvButton")
        self.csvButton.clicked.connect(self.get_outDir)
        self.gridLayout.addWidget(self.csvButton, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.CSVPath = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.CSVPath.setReadOnly(True)
        self.CSVPath.setObjectName("CSVPath")
        self.gridLayout.addWidget(self.CSVPath, 1, 0, 1, 2)
        self.dataButton = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.dataButton.setObjectName("dataButton")
        self.dataButton.clicked.connect(self.get_dataDir)
        self.gridLayout.addWidget(self.dataButton, 5, 0, 1, 1)
        self.DataPath = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.DataPath.setReadOnly(True)
        self.DataPath.setObjectName("DataPath")
        self.gridLayout.addWidget(self.DataPath, 4, 0, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 5, 1, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.CSV)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 190, 291, 151))
        self.groupBox_4.setObjectName("groupBox_4")
        self.formLayoutWidget = QtWidgets.QWidget(self.groupBox_4)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 20, 271, 121))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.csvButton1 = QtWidgets.QPushButton(self.formLayoutWidget)
        self.csvButton1.setObjectName("csvButton1")
        self.csvButton1.clicked.connect(self.csvButton1_onclick)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.csvButton1)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.csvButton2 = QtWidgets.QPushButton(self.formLayoutWidget)
        self.csvButton2.setObjectName("csvButton2")
        self.csvButton2.clicked.connect(self.csvButton2_onclick)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.csvButton2)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.csvButton3 = QtWidgets.QPushButton(self.formLayoutWidget)
        self.csvButton3.setObjectName("csvButton3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.csvButton3)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.csvButton4 = QtWidgets.QPushButton(self.formLayoutWidget)
        self.csvButton4.setObjectName("csvButton4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.csvButton4)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(330, 10, 281, 351))
        self.groupBox.setObjectName("groupBox")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 180, 261, 161))
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_2)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 241, 151))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.graphButton1 = QtWidgets.QPushButton(self.formLayoutWidget_2)
        self.graphButton1.setObjectName("graphButton1")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.graphButton1)
        self.graphButton1.clicked.connect(self.graphButton1_onclick)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.graphButton2 = QtWidgets.QPushButton(self.formLayoutWidget_2)
        self.graphButton2.setObjectName("graphButton2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.graphButton2)
        self.graphButton2.clicked.connect(self.graphButton2_onclick)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.graphButton3 = QtWidgets.QPushButton(self.formLayoutWidget_2)
        self.graphButton3.setObjectName("graphButton3")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.graphButton3)
        self.graphButton3.clicked.connect(self.graphButton3_onclick)
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_10.setObjectName("label_10")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.graphButton4 = QtWidgets.QPushButton(self.formLayoutWidget_2)
        self.graphButton4.setObjectName("graphButton4")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.graphButton4)
        self.graphButton4.clicked.connect(self.graphButton4_onclick)
        self.label_11 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_11.setObjectName("label_11")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.graphButton5 = QtWidgets.QPushButton(self.formLayoutWidget_2)
        self.graphButton5.setObjectName("graphButton5")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.graphButton5)
        self.graphButton5.clicked.connect(self.graphButton5_onclick)
        self.scrollArea = QtWidgets.QScrollArea(self.groupBox)
        self.scrollArea.setGeometry(QtCore.QRect(9, 20, 261, 151))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 259, 149))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(-1, 0, 261, 151))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.textEdit = QtWidgets.QTextEdit(self.gridLayoutWidget_2)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_3.addWidget(self.textEdit, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(620, 10, 221, 351))
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox_3)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 201, 321))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.OutPutText = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.OutPutText.setReadOnly(True)
        self.OutPutText.setObjectName("OutPutText")
        self.gridLayout_2.addWidget(self.OutPutText, 0, 0, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 851, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.actiontest = QtWidgets.QAction(MainWindow)
        self.actiontest.setObjectName("actiontest")

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.OutPutText.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Data Visualization"))
        self.CSV.setTitle(_translate("MainWindow", "CSV Generation"))
        self.csvButton.setText(_translate("MainWindow", "Select"))
        self.label_2.setText(_translate("MainWindow", "Data Path:"))
        self.label.setText(_translate("MainWindow", "CSV Path:"))
        self.dataButton.setText(_translate("MainWindow", "Select"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Generate CSVs"))
        self.label_3.setText(_translate("MainWindow", "Seciton files"))
        self.csvButton1.setText(_translate("MainWindow", "Generate"))
        self.label_4.setText(_translate("MainWindow", "Section word stats."))
        self.csvButton2.setText(_translate("MainWindow", "Generate"))
        self.label_5.setText(_translate("MainWindow", "Document word stats."))
        self.csvButton3.setText(_translate("MainWindow", "Generate"))
        self.label_6.setText(_translate("MainWindow", "Section word count"))
        self.csvButton4.setText(_translate("MainWindow", "Generate"))
        self.groupBox.setTitle(_translate("MainWindow", "Visualization"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Select graph"))
        self.label_9.setText(_translate("MainWindow", "Freq. per Section"))
        self.graphButton1.setText(_translate("MainWindow", "Generate"))
        self.label_7.setText(_translate("MainWindow", "Freq. Comparison"))
        self.graphButton2.setText(_translate("MainWindow", "Generate"))
        self.label_8.setText(_translate("MainWindow", "Multi word freq."))
        self.graphButton3.setText(_translate("MainWindow", "Generate"))
        self.label_10.setText(_translate("MainWindow", "Multi word freq. alt"))
        self.graphButton4.setText(_translate("MainWindow", "Generate"))
        self.label_11.setText(_translate("MainWindow", "Section word freq."))
        self.graphButton5.setText(_translate("MainWindow", "Generate"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Welcome to our data visualization tool!</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">To begin use the buttons to the left. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">These will allow you to select the folders where you want to save CSV files (&quot;CSV Path&quot;) and where your data source files are located (&quot;Data Path&quot;).</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Once you have selected your desired folders you can use the buttons bellow that to generate basic CSV files. </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">The possible files include.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1. <span style=\" font-style:italic;\">Section files</span> - A small CSV indicating which sections have associated graphs or figures.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2. <span style=\" font-style:italic;\">Section word statistics</span> - A large CSV that will contains all words and their frequency per section.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3. <span style=\" font-style:italic;\">Document word statistics</span> - Similar to the former but shows total word frequency for the entire document. </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4.<span style=\" font-style:italic;\"> Section word count</span> - This CSV contains the number of total words occuring in each section. </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">To visualize data use the buttons to bellow.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1. <span style=\" font-style:italic;\">Frequency Per Section</span> - Creates a bar graph showing the frequency of a given word per section in which that word appears.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2. <span style=\" font-style:italic;\">Frequency Comparison</span> - Creates a line graph comparing the frequency of several words for the entire document.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3. <span style=\" font-style:italic;\">Multiple Word Frequency</span> - Creates a line graph with one line per indicated word comparing frequencies for each section in which any of the words appear.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4. <span style=\" font-style:italic;\">Multiple Word Frequency alt.</span> - Alternative to the last graph. Creates the same visual comparison but using a bar graph instead of a line graph.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">5. <span style=\" font-style:italic;\">Section Word Frequency</span> - Creates a line graph comparing the total word occurance of each section. </p></body></html>"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Output"))
        self.pushButton.setText(_translate("MainWindow", "Clear"))
        self.actiontest.setText(_translate("MainWindow", "test"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
