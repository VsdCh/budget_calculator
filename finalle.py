from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import json

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("система для отслеживания личных доходов/расходов")
        Dialog.resize(487, 418)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(370, 370, 91, 31)
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.widget1 = QtWidgets.QWidget(Dialog)
        self.widget1.setGeometry(10, 10, 471, 31)
        self.widget1.setObjectName("widget1")
        
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        self.label_3 = QtWidgets.QLabel(self.widget1)
        self.label_3.setObjectName("label_3")
        self.label_3.setAlignment(QtCore.Qt.AlignHCenter)
        self.horizontalLayout_4.addWidget(self.label_3)

        self.label_4 = QtWidgets.QLabel(self.widget1)
        self.label_4.setObjectName("label_4")
        self.label_4.setAlignment(QtCore.Qt.AlignHCenter)
        self.horizontalLayout_4.addWidget(self.label_4)
        
        self.label_5 = QtWidgets.QLabel(self.widget1)
        self.label_5.setObjectName("label_5")
        self.label_5.setAlignment(QtCore.Qt.AlignHCenter)
        self.horizontalLayout_4.addWidget(self.label_5)
        
        self.widget2 = QtWidgets.QWidget(Dialog)
        self.widget2.setGeometry(10, 50, 471, 25)
        self.widget2.setObjectName("widget2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout_5.setContentsMargins(0, 0, 1, 0)
   
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
 
        self.pushButton = QtWidgets.QPushButton(self.widget2)
        self.pushButton.setMaximumSize(QtCore.QSize(300, 150))
        self.pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_5.addWidget(self.pushButton)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setGeometry(10, 50, 471, 331)
        self.scrollArea.setWidgetResizable(True)

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(0, 0, 467, 331)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.scrollLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.scrollLayout.setContentsMargins(0, 0, 0, 0)

        self.addButton = QtWidgets.QPushButton(Dialog)
        self.addButton.setGeometry(10, 390, 91, 31)
        self.addButton.setObjectName("addButton")
        self.addButton.setText("Добавить")
        self.addButton.clicked.connect(self.createRecord)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.records = []  
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.session_data = {}
        try:
            with open("session_data.json", "r") as file:
                self.session_data = json.load(file)
                total = self.session_data.get("total", 0)
                self.label_2.setText(str(total))
        except FileNotFoundError:
            pass 
        for record_data in self.session_data.get("records", []):
            self.createRecord(data=record_data)
            self.updateTotal()
        
        self.saveButton = QtWidgets.QPushButton(Dialog)
        self.saveButton.setGeometry(110, 390, 91, 31)
        self.saveButton.setObjectName("saveButton")
        self.saveButton.setText("Сохранить ")
        self.saveButton.clicked.connect(self.saveSessionData)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def saveSessionData(self):
        self.session_data["records"] = []
        for record in self.records:
            lineEdit = record.findChild(QtWidgets.QLineEdit, "lineEdit")
            lineEdit2 = record.findChild(QtWidgets.QLineEdit, "lineEdit_2")
            lineEdit3 = record.findChild(QtWidgets.QLineEdit, "lineEdit_3")

            try:
                line_edit_3_value = int(lineEdit3.text())
            except ValueError:
                line_edit_3_value = 0
                QtWidgets.QMessageBox.critical(None, "Ошибка", "Неверный тип данных в сумме.")
                return
                
            record_data = {
                "text": lineEdit.text(),
                "comment": lineEdit2.text(),
                "line_edit_3": int(lineEdit3.text())
            }
            self.session_data["records"].append(record_data)
        try:
            with open("session_data.json", "w") as file:
                json.dump(self.session_data, file)
                
        except Exception as e:
            error_message = f"An error occurred while saving data:\n{str(e)}"
            QMessageBox.critical(None, "Error", error_message)

        total = int(self.label_2.text())
        self.session_data["total"] = total
        
    def createRecord(self, data=None):
        newRecord = QtWidgets.QWidget()
        newRecord.setGeometry(0, 0, 467, 80)
        newRecord.setObjectName("newRecord")

        newRecordLayout = QtWidgets.QHBoxLayout(newRecord)

        label = QtWidgets.QLabel(newRecord)
        label.setObjectName("label")
        label.setText("Новая запись:")

        lineEdit = QtWidgets.QLineEdit(newRecord)
        lineEdit.setObjectName("lineEdit")
        lineEdit.setInputMask("99.99.9999")
        lineEdit2 = QtWidgets.QLineEdit(newRecord)
        lineEdit2.setObjectName("lineEdit_2")

        lineEdit3 = QtWidgets.QLineEdit(newRecord)
        lineEdit3.setObjectName("lineEdit_3")

        pushButton = QtWidgets.QPushButton(newRecord)
        pushButton.setObjectName("pushButton")
        pushButton.setText("Удалить")

        newRecordLayout.addWidget(label)
        newRecordLayout.addWidget(lineEdit)
        newRecordLayout.addWidget(lineEdit2)
        newRecordLayout.addWidget(lineEdit3)
        newRecordLayout.addWidget(pushButton)

        self.scrollLayout.addWidget(newRecord)

        if data:
            lineEdit.setText(data.get("text", ""))
            lineEdit2.setText(data.get("comment", ""))
            lineEdit3.setText(str(data.get("line_edit_3", 0)))

        self.records.append(newRecord)
        pushButton.clicked.connect(lambda: self.removeRecord(newRecord))
        lineEdit3.textChanged.connect(self.updateTotal)

    def removeRecord(self, record):
        self.records.remove(record) 
        record.deleteLater()  
        self.updateTotal()

    def updateTotal(self):
        total = 0
        for record in self.records:
            lineEdit3 = record.findChild(QtWidgets.QLineEdit, "lineEdit_3")
            if lineEdit3:
                try:
                    value = int(lineEdit3.text())
                    total += value
                    if value < 0:
                        lineEdit3.setStyleSheet("QLineEdit { color: red; }")
                    else:
                        lineEdit3.setStyleSheet("QLineEdit { color: green; }")
                except ValueError:
                    lineEdit3.setStyleSheet("")  # Вернуть стандартный стиль
                    pass  
        self.label_2.setText(str(total))

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "система для отслеживания личных доходов/расходов"))
        self.label.setText(_translate("Dialog", "остаток:"))
        self.label_2.setText(_translate("Dialog", "0"))
        self.label_3.setText(_translate("Dialog", "дата"))
        self.label_4.setText(_translate("Dialog", "комментарий"))
        self.label_5.setText(_translate("Dialog", "сумма"))
        self.pushButton.setText(_translate("Dialog", "удалить"))
        self.addButton.setText(_translate("Dialog", "Добавить"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()

    app.aboutToQuit.connect(ui.saveSessionData)
    sys.exit(app.exec_())
