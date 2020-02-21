# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import psycopg2 as pg2
from user_gui import Ui_UserGui
from register import Ui_Register
import sys
import requests
import datetime


class Ui_Login(object):
    def __init__(self):
        super(Ui_Login, self).__init__()
        self.user_gui = None
        self.response_currency = requests.get('https://api.exchangeratesapi.io/latest?base=PLN')

        # dane do logowania do bazy danych
        self.db_host = 'packy.db.elephantsql.com'
        self.db_user = 'htcazxfd'
        self.db_name = 'htcazxfd'
        self.db_port = 5432
        self.db_psswd = 'UE5AaV5whqnbKyD5jL9MusNCvV1yaX7T'
        self.conn = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(387, 223)
        self.window = MainWindow
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.username = QtWidgets.QLabel(self.centralwidget)
        self.username.setGeometry(QtCore.QRect(40, 40, 141, 17))
        self.username.setObjectName("username")
        self.result = QtWidgets.QLabel(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(40, 120, 141, 17))
        self.result.setObjectName("result")
        self.password = QtWidgets.QLabel(self.centralwidget)
        self.password.setEnabled(True)
        self.password.setGeometry(QtCore.QRect(40, 70, 67, 17))
        self.password.setObjectName("password")
        self.username_input = QtWidgets.QLineEdit(self.centralwidget)
        self.username_input.setGeometry(QtCore.QRect(190, 40, 150, 25))
        self.username_input.setFrame(True)
        self.username_input.setObjectName("username_input")
        self.password_input = QtWidgets.QLineEdit(self.centralwidget)
        self.password_input.setGeometry(QtCore.QRect(190, 70, 150, 25))
        self.password_input.setObjectName("password_input")
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 120, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.register_button = QtWidgets.QPushButton(self.centralwidget)
        self.register_button.setGeometry(QtCore.QRect(40, 120, 111, 25))
        self.register_button.setObjectName("register_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 387, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.clicked_log_in)
        self.register_button.clicked.connect(self.register_new_user)

    def download_currencies(self):
        if self.response_currency.status_code == 200:
            try:
                self.conn = pg2.connect(host=self.db_host, database=self.db_name, user=self.db_user, password=self.db_psswd,
                                        port=self.db_port)
                c = self.conn.cursor()
                c.execute("""
                        SELECT *
                        FROM currencies_download_date
                        WHERE date_of_download = CURRENT_DATE;
                """)
                date_of_update = c.fetchone()
                c.close()
                self.conn.commit()
                if date_of_update is None:
                    insert_values = ''
                    sorted_dict = sorted(self.response_currency.json()['rates'].items(), key=lambda x: x[0])
                    for currency, value in sorted_dict:
                        insert_values += "UPDATE currencies SET value_in_pln = {} WHERE name = '{}'; ".format(value, currency)

                    date_of_download = self.response_currency.json()['date']

                    c = self.conn.cursor()
                    c.execute("""
                            {}
                            INSERT INTO currencies_download_date (date_of_download)
                            VALUES ('{}');
                    """.format(insert_values, date_of_download))
                    c.close()
                    self.conn.commit()
                    self.conn.close()
            except pg2.errors.RaiseException:
                self.something_is_wrong()
        else:
            self.download_currencies_error()

    def download_currencies_error(self):
        self.conn = pg2.connect(host=self.db_host, database=self.db_name, user=self.db_user, password=self.db_psswd,
                                port=self.db_port)
        c = self.conn.cursor()
        c.execute("""
                SELECT date_of_download
                FROM currencies_download_date
                HAVING date_id = max(date_id);
        """)
        date_of_update = c.fetchone()
        c.close()
        self.conn.commit()
        self.conn.close()
        msg = QMessageBox()
        msg.setWindowTitle("Błąd")
        msg.setText("Błąd pobierania walut z ECB. Twoja biblioteka będzie korzystać z przeliczników walut z dnia {}".format(date_of_update))
        msg.setIcon(QMessageBox.Critical)
        msg.setStandardButtons(QMessageBox.Ok)

        x = msg.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Logowanie do biblioteki cyfrowej"))
        self.username.setText(_translate("MainWindow", "Nazwa użytkownika:"))
        self.password.setText(_translate("MainWindow", "Hasło:"))
        self.pushButton.setText(_translate("MainWindow", "Zaloguj"))
        self.register_button.setText(_translate("MainWindow", "Zarejestruj"))

    def clicked_log_in(self):
        _translate = QtCore.QCoreApplication.translate
        username = self.username_input.text()
        password = self.password_input.text()
        try:
            self.conn = pg2.connect(host=self.db_host, database=self.db_name, user=self.db_user, password=self.db_psswd,
                                    port=self.db_port)
            c = self.conn.cursor()
            c.execute("SELECT user_id FROM users WHERE username = '{}' AND psswd = '{}';".format(username, password))
            go = c.fetchone()
            if go is None:
                self.result.setText(_translate("MainWindow", "Błąd logowania!"))
            else:
                self.result.setText(_translate("MainWindow", "Zalogowano!"))
                self.open_user_gui(go[0])
            c.close()
            self.conn.commit()
            self.conn.close()
            self.username_input.setText(_translate('MainWindow', ''))
            self.password_input.setText(_translate('MainWindow', ''))
        except pg2.errors.RaiseException:
            self.something_is_wrong()

    def open_user_gui(self, user_id):
        self.download_currencies()
        self.window_user_gui = QtWidgets.QMainWindow()
        self.user_gui = Ui_UserGui(user_id)
        self.user_gui.setupUi(self.window_user_gui)
        self.window_user_gui.show()
        self.window.close()

    def register_new_user(self):
        self.window_register = QtWidgets.QMainWindow()
        self.register_gui = Ui_Register()
        self.register_gui.setupUi(self.window_register)
        self.window_register.show()
        self.window.close()

    @staticmethod
    def something_is_wrong():
        msg = QMessageBox()
        msg.setWindowTitle("Błąd")
        msg.setText("Coś poszło nie tak :(")
        msg.setIcon(QMessageBox.Critical)
        msg.setStandardButtons(QMessageBox.Abort)

        x = msg.exec_()


if __name__ == "__main__":
    app1 = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QMainWindow()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app1.exec_())
