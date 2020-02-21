# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import psycopg2 as pg2
from PyQt5.QtWidgets import QMessageBox


class Ui_Register(object):
    def __init__(self):
        super(Ui_Register, self).__init__()

        # dane do logowania do bazy danych
        self.db_host = 'packy.db.elephantsql.com'
        self.db_user = 'htcazxfd'
        self.db_name = 'htcazxfd'
        self.db_port = 5432
        self.db_psswd = 'UE5AaV5whqnbKyD5jL9MusNCvV1yaX7T'
        self.conn = None

    def setupUi(self, MainWindow):
        self.window = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(342, 390)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.register_username_label = QtWidgets.QLabel(self.centralwidget)
        self.register_username_label.setGeometry(QtCore.QRect(10, 10, 181, 17))
        self.register_username_label.setObjectName("register_username_label")
        self.register_password_label = QtWidgets.QLabel(self.centralwidget)
        self.register_password_label.setGeometry(QtCore.QRect(10, 80, 81, 17))
        self.register_password_label.setObjectName("register_password_label")
        self.register_username_input = QtWidgets.QLineEdit(self.centralwidget)
        self.register_username_input.setGeometry(QtCore.QRect(10, 40, 201, 25))
        self.register_username_input.setObjectName("register_username_input")
        self.register_password_input = QtWidgets.QLineEdit(self.centralwidget)
        self.register_password_input.setGeometry(QtCore.QRect(10, 110, 201, 25))
        self.register_password_input.setObjectName("register_password_input")
        self.register_mail_label = QtWidgets.QLabel(self.centralwidget)
        self.register_mail_label.setGeometry(QtCore.QRect(10, 150, 121, 17))
        self.register_mail_label.setObjectName("register_mail_label")
        self.register_mail_input = QtWidgets.QLineEdit(self.centralwidget)
        self.register_mail_input.setGeometry(QtCore.QRect(10, 180, 201, 25))
        self.register_mail_input.setObjectName("register_mail_input")
        self.register_date_of_birth_label = QtWidgets.QLabel(self.centralwidget)
        self.register_date_of_birth_label.setGeometry(QtCore.QRect(10, 220, 211, 17))
        self.register_date_of_birth_label.setObjectName("register_date_of_birth_label")
        self.register_date_of_birth_input = QtWidgets.QDateEdit(self.centralwidget)
        self.register_date_of_birth_input.setGeometry(QtCore.QRect(10, 250, 110, 25))
        self.register_date_of_birth_input.setObjectName("register_date_of_birth_input")
        self.register_button = QtWidgets.QPushButton(self.centralwidget)
        self.register_button.setGeometry(QtCore.QRect(100, 290, 151, 31))
        self.register_button.setObjectName("register_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 342, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.register_button.clicked.connect(self.register_new_user)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Rejestracja"))
        self.register_username_label.setText(_translate("MainWindow", "Podaj nazwę użytkownika"))
        self.register_password_label.setText(_translate("MainWindow", "Podaj hasło"))
        self.register_mail_label.setText(_translate("MainWindow", "Podaj swój email"))
        self.register_date_of_birth_label.setText(_translate("MainWindow", "Podaj datę swojego urodzenia"))
        self.register_button.setText(_translate("MainWindow", "Zarejestruj"))
        self.register_date_of_birth_input.setDisplayFormat(_translate("MainWindow", "dd-MM-yyyy"))

    def register_new_user(self):
        username = self.register_username_input.text()
        password = self.register_password_input.text()
        mail = self.register_mail_input.text()
        date_of_birth = self.register_date_of_birth_input.text()
        try:
            self.conn = pg2.connect(host=self.db_host, database=self.db_name, user=self.db_user, password=self.db_psswd,
                                    port=self.db_port)
            c = self.conn.cursor()
            c.execute("""
                    INSERT INTO users (username, psswd, email, date_of_birth, amount, account_creation)
                    VALUES ('{}', '{}', '{}', '{}', 0, CURRENT_DATE)
            """.format(username, password, mail, date_of_birth))
            c.close()
            self.conn.commit()
            self.conn.close()
            self.register_success()
        except pg2.errors.RaiseException:
            self.register_error()

    def register_success(self):
        msg = QMessageBox()
        msg.setWindowTitle("Potwierdzenie")
        msg.setText("Udało Ci się zarejestrować do biblioteki gier")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)

        msg.buttonClicked.connect(self.open_login)
        x = msg.exec_()

    def register_error(self):
        _translate = QtCore.QCoreApplication.translate
        msg = QMessageBox()
        msg.setWindowTitle("Błąd rejestracji")
        msg.setText("Nie udało Ci się zarejestrować do biblioteki gier")
        msg.setIcon(QMessageBox.Critical)
        msg.setStandardButtons(QMessageBox.Retry)

        self.register_date_of_birth_input.setDate(QtCore.QDate(2000, 1, 1))
        self.register_username_input.clear()
        self.register_password_input.clear()
        self.register_mail_input.clear()
        x = msg.exec_()

    def open_login(self):
        from login import Ui_Login
        self.window_login = QtWidgets.QMainWindow()
        self.login_gui = Ui_Login()
        self.login_gui.setupUi(self.window_login)
        self.window_login.show()
        self.window.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Register()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
