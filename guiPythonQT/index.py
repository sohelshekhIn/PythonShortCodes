from PyQt5 import QtCore, QtGui, QtWidgets
import os
import time
import sys

class Ui_MainWindow(object):
    FileLocation = "F:\\"
    LocationPicked = False

    def errorText(self,text):
        self.label_5.setText(text)
        time.sleep(5)
        self.label_5.setText("")

    def ShowError(self,errId): 
        if errId == "emptyFeilds":
          self.errorText("Enter all fields!")
        elif errId == "dirAlExist":
          self.errorText("Location already exist, Choose another")
    
    
    def createProject(self):
        self.errorText("Hello, M gorgoues frined")
        ProjectName = self.plainTextEdit.toPlainText()
        FileLocation = self.plainTextEdit_2.toPlainText()

        if self.radioButton.isChecked():
                ProjectLang = "py"
        elif self.radioButton_2.isChecked():
                ProjectLang = "js"

        if self.radioButton_3.isChecked():
                ProjectType = "project"
        elif self.radioButton_4.isChecked():
                ProjectType = "site"

        if ProjectName != "" and FileLocation != "" and ProjectLang != "" and ProjectType != "":
            # Declaration of variables
            npmInit = "npm init -y"
            installVirtualEnv = "pip install virtualenv"
            virtualEnv = "py -m virtualenv -p py venv"
            activateVenv = "venv\\Scripts\\activate"
            installFlask = "pip install flask"


            if ProjectLang == "py":

                if ProjectType == "project":
                    try:
                        filePath = FileLocation
                        os.mkdir(filePath)
                        os.chdir(filePath)
                        with open("index.py", "w") as fp:
                            print("Creating Project...")
                            try:
                                os.popen("pip install virtualenv").read()
                                os.popen(virtualEnv).read()
                                os.popen(activateVenv).read()
                                os.popen("code .").read()
                            except Exception as e:
                                print(e)
                    except OSError as e:
                        print(e)
                else:
                    try:
                        print("Creating project...")
                        filePath = FileLocation
                        os.mkdir(filePath)
                        os.chdir(filePath)
                        os.popen(installVirtualEnv).read()
                        os.popen(virtualEnv).read()
                        os.popen(activateVenv).read()
                        os.popen(installFlask).read()
                        staticFolder = os.path.join(filePath, "static")
                        templatesFolder = os.path.join(filePath, "templates")
                        os.mkdir(staticFolder)
                        os.chdir(staticFolder)
                        try:
                            cssFlask = os.path.join(staticFolder, "css")
                            os.mkdir(cssFlask)
                            os.chdir(cssFlask)
                            with open("index.css", "w") as fp:
                                try:
                                    jsFlaskPath = os.path.join(staticFolder, "js")
                                    os.mkdir(jsFlaskPath)
                                    os.chdir(jsFlaskPath)
                                    with open("index.js", "w") as fp:
                                        try:
                                            os.mkdir(templatesFolder)
                                            os.chdir(templatesFolder)
                                            with open("index.html", "w") as fp:
                                                try:
                                                    os.chdir(filePath)
                                                    with open("index.py", "w") as fp:
                                                        print("Flask App Created")
                                                        os.chdir(filePath)
                                                        os.popen("code .").read()
                                                except OSError as e:
                                                    print(e)
                                        except OSError as e:
                                            print(e)
                                except OSError as e:
                                    print(e)
                        except OSError as e:
                            print(e)
                    except OSError as e:
                        print(e)

            elif ProjectLang == "js":
                filePath = FileLocation
                os.mkdir(filePath)
                os.chdir(filePath)

                if ProjectType == "site": #means static
                    try:
                        publicFolder = os.path.join(filePath, "public")
                        os.mkdir(publicFolder)
                        os.chdir(publicFolder)
                        with open("index.html", "w") as fp:
                            print("Creating projects...")
                            try:
                                cssFolder = os.path.join(publicFolder, "css")
                                os.mkdir(cssFolder)
                                os.chdir(cssFolder)
                                with open("index.css", "w") as fp:
                                    try:
                                        jsFolder = os.path.join(publicFolder, "js")
                                        os.mkdir(jsFolder)
                                        os.chdir(jsFolder)
                                        with open("index.js", "w") as fp:
                                            print("Project Created!")
                                            os.chdir(publicFolder)
                                            os.popen("code .").read()
                                    except OSError as e:
                                        print(e)
                            except OSError as e:
                                print(e)
                    except OSError as e:
                        print(e)
                elif ProjectType == "project": #means dynamic
                    try:
                        with open("server.js", "w") as fp:
                            print("Creating Project...")
                            publicDir = os.path.join(filePath, "public")
                            os.popen("code .").read()

                    except OSError as e:
                        print(e)
        else:
            # self.errorText("Please enter all fields!")
            print("Bye")


    def checkNChange(self):
        if self.radioButton_2.isChecked():
            self.radioButton_4.setText("Static")
            self.radioButton_3.setText("Dynamic")
        elif self.radioButton.isChecked():
            self.radioButton_4.setText("Site")
            self.radioButton_3.setText("Project")


    def pickLocation(self):
        '''
        Pop Explorer to pick location
        '''

        dirr = QtWidgets.QFileDialog.getExistingDirectory(None, 'Select project folder:', 'F:\\', QtWidgets.QFileDialog.ShowDirsOnly)
        dirr = os.path.join(dirr,self.plainTextEdit.toPlainText())
        self.plainTextEdit_2.setPlainText(dirr)
        LocationPicked = True
        self.errorText("Hello World")


    def syncEditText(self):
        ProjectText = self.plainTextEdit.toPlainText()
        dirr = os.path.join(self.FileLocation,ProjectText)
        self.plainTextEdit_2.setPlainText(dirr)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(635, 588)
        MainWindow.setStyleSheet("background-color:rgb(34, 34, 34);\n"
                                 "color:#fff;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(100, 160, 411, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.plainTextEdit.setAutoFillBackground(True)
        self.plainTextEdit.setStyleSheet("color:#fff;\n"
                                         "border:none;\n"
                                         "outline:none;\n"
                                         "border-bottom: 1px solid rgb(86, 86, 86);\n"
                                         "padding:0px;\n"
                                         "margin:0px;")
        self.plainTextEdit.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        self.plainTextEdit.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        self.plainTextEdit.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setOverwriteMode(True)
        self.plainTextEdit.setPlaceholderText("")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(7, 546, 631, 20))
        self.progressBar.setProperty("value", 2)
        self.progressBar.setObjectName("progressBar")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(-3, 520, 671, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(260, 450, 101, 41))
        self.pushButton.setMinimumSize(QtCore.QSize(0, 41))
        self.pushButton.setMaximumSize(QtCore.QSize(101, 16777215))
        font = QtGui.QFont()
        font.setFamily("Montserrat SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("border:none;\n"
                                      "background-color: rgb(90, 90, 90);\n"
                                      "border-radius:5px;\n"
                                      "")
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.createProject)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 140, 71, 16))
        self.label_3.setAutoFillBackground(False)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(100, 210, 71, 16))
        self.label_4.setObjectName("label_4")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(100, 230, 411, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.plainTextEdit_2.setFont(font)
        self.plainTextEdit_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.plainTextEdit_2.setStyleSheet("color:#fff;\n"
                                           "border:none;\n"
                                           "outline:none;\n"
                                           "border-bottom: 1px solid rgb(86, 86, 86);\n"
                                           "padding:0px;\n"
                                           "margin:0px;")
        self.plainTextEdit_2.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_2.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_2.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.plainTextEdit_2.setPlainText(self.FileLocation)
        self.plainTextEdit_2.setOverwriteMode(True)
        self.plainTextEdit_2.setPlaceholderText("")
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.plainTextEdit.textChanged.connect(self.syncEditText)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(430, 230, 75, 23))
        self.pushButton_2.setStyleSheet("border-radius:5px;\n"
                                        "background-color:rgb(148, 148, 148);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.pickLocation)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(10, 0, 619, 37))
        self.label.setSizeIncrement(QtCore.QSize(2, 2))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.label.setFont(font)
        self.label.setStyleSheet("text-align: center;\n"
                                 "font-size: 27px;\n"
                                 "width:100%;\n"
                                 "height:fit-content;\n"
                                 "")
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label.setWordWrap(False)
        self.label.setIndent(0)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 30, 619, 36))
        self.label_2.setMinimumSize(QtCore.QSize(619, 36))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("padding:0;\n"
                                   "margin:0px;\n"
                                   "width:100%;\n"
                                   "height:fit-content;\n"
                                   "")
        self.label_2.setLocale(QtCore.QLocale(
            QtCore.QLocale.English, QtCore.QLocale.UnitedKingdom))
        self.label_2.setLineWidth(1)
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_2.setObjectName("label_2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(
            QtCore.QRect(130, 310, 163, 24))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.radioButton.setFont(font)
        self.radioButton.setStyleSheet("")
        self.radioButton.setChecked(True)
        self.radioButton.clicked.connect(self.checkNChange)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(
            self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(9)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setStyleSheet("")
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_2.clicked.connect(self.checkNChange)
        self.horizontalLayout.addWidget(self.radioButton_2)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(
            QtCore.QRect(330, 310, 160, 24))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioButton_4 = QtWidgets.QRadioButton(
            self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(9)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setStyleSheet("")
        self.radioButton_4.setChecked(True)
        self.radioButton_4.setObjectName("radioButton_4")
        self.horizontalLayout_2.addWidget(self.radioButton_4)
        self.radioButton_3 = QtWidgets.QRadioButton(
            self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setStyleSheet("")
        self.radioButton_3.setChecked(False)
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout_2.addWidget(self.radioButton_3)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 380, 611, 51))
        self.label_5.setStyleSheet("color:red;")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.plainTextEdit.raise_()
        self.progressBar.raise_()
        self.line.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.horizontalLayoutWidget.raise_()
        self.horizontalLayoutWidget_2.raise_()
        self.plainTextEdit_2.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Create"))
        self.label_3.setText(_translate("MainWindow", "Project Name"))
        self.label_4.setText(_translate("MainWindow", "File Location"))
        self.pushButton_2.setText(_translate("MainWindow", "Choose"))
        self.label.setAccessibleName(_translate("MainWindow", "head"))
        self.label.setText(_translate("MainWindow", "PROJECT CREATOR"))
        self.label_2.setText(_translate("MainWindow", "PYTHON & JAVASCRIPT"))
        self.radioButton.setText(_translate("MainWindow", "Python"))
        self.radioButton.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.radioButton_2.setText(_translate("MainWindow", "JavaScript"))
        self.radioButton_2.setShortcut(_translate("MainWindow", "Ctrl+J"))
        self.radioButton_4.setText(_translate("MainWindow", "Site"))
        self.radioButton_4.setShortcut(_translate("MainWindow", "Alt+S"))
        self.radioButton_3.setText(_translate("MainWindow", "Project"))
        self.radioButton_3.setShortcut(_translate("MainWindow", "Alt+P"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setWindowIcon(QtGui.QIcon('icon.png'))
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.setWindowTitle("Project Creator")
    MainWindow.show()
    sys.exit(app.exec_())
