# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'library.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import psycopg2 as pg2
import math
from list_item import *
from PyQt5.QtWidgets import QMessageBox


class Ui_LibraryFriend(object):
    def __init__(self, friend_id, friend_name, my_currency):
        super(Ui_LibraryFriend, self).__init__()
        self.friend_id = friend_id
        self.friend_name = friend_name
        self.my_currency = my_currency

        # dane do logowania do bazy danych
        self.db_host = 'packy.db.elephantsql.com'
        self.db_user = 'htcazxfd'
        self.db_name = 'htcazxfd'
        self.db_port = 5432
        self.db_psswd = 'UE5AaV5whqnbKyD5jL9MusNCvV1yaX7T'
        self.conn = None

        self.library_pages = []
        self.library_lists = []
        self.library_previous_buttons = []
        self.library_next_buttons = []
        self.library_current_page_labels = []
        self.library_current_page = 0

        self.currency_value = 1
        self.currency_name = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1240, 610)
        _translate = QtCore.QCoreApplication.translate
        self.library = QtWidgets.QWidget()
        self.library.setObjectName("library")
        self.stacked_library = QtWidgets.QStackedWidget(self.library)
        self.stacked_library.setGeometry(QtCore.QRect(440, 0, 281, 620))
        self.stacked_library.setObjectName("stacked_library")

        n = math.ceil(self.count_friend_games()/30)
        n = n if n > 0 else 1
        for i in range(n):
            self.library_pages.append(QtWidgets.QWidget())
            self.library_pages[i].setObjectName("stacked_library_page_{}".format(i+1))
            self.stacked_library.addWidget(self.library_pages[i])
            self.library_lists.append(QtWidgets.QListWidget(self.library_pages[i]))
            self.library_lists[i].setGeometry(QtCore.QRect(0, 0, 281, 580))
            self.library_lists[i].setObjectName("list_library_{}".format(i+1))
            if i > 0:
                self.library_previous_buttons.append(QtWidgets.QPushButton(self.library_pages[i]))
                self.library_previous_buttons[i-1].setGeometry(QtCore.QRect(0, 545, 89, 25))
                self.library_previous_buttons[i-1].setObjectName("library_previous_button_{}".format(i))
                self.library_previous_buttons[i-1].clicked.connect(self.library_previous_page)
                self.library_previous_buttons[i-1].setText(_translate("MainWindow", "Poprzednia"))
            if i < n-1:
                self.library_next_buttons.append(QtWidgets.QPushButton(self.library_pages[i]))
                self.library_next_buttons[i].setGeometry(QtCore.QRect(190, 545, 89, 25))
                self.library_next_buttons[i].setObjectName("library_next_button_{}".format(i+1))
                self.library_next_buttons[i].clicked.connect(self.library_next_page)
                self.library_next_buttons[i].setText(_translate("MainWindow", "Następna"))
            self.library_current_page_labels.append(QtWidgets.QLabel(self.library_pages[i]))
            self.library_current_page_labels[i].setGeometry(QtCore.QRect(110, 560, 67, 17))
            self.library_current_page_labels[i].setObjectName("library_current_page_label_{}".format(i+1))
            self.library_current_page_labels[i].setText(_translate("MainWindow", "Strona {}".format(i+1)))

        self.library_current_game_name = QtWidgets.QLabel(self.library)
        self.library_current_game_name.setGeometry(QtCore.QRect(730, 0, 491, 41))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.library_current_game_name.setFont(font)
        self.library_current_game_name.setObjectName("library_current_game_name")
        self.library_price_label = QtWidgets.QLabel(self.library)
        self.library_price_label.setGeometry(QtCore.QRect(740, 70, 67, 17))
        self.library_price_label.setObjectName("library_price_label")
        self.library_current_game_price = QtWidgets.QLabel(self.library)
        self.library_current_game_price.setGeometry(QtCore.QRect(800, 70, 100, 17))
        self.library_current_game_price.setObjectName("library_current_game_price")
        self.library_for_kids_label = QtWidgets.QLabel(self.library)
        self.library_for_kids_label.setGeometry(QtCore.QRect(920, 70, 161, 17))
        self.library_for_kids_label.setObjectName("library_for_kids_label")
        self.library_current_game_for_kids = QtWidgets.QLabel(self.library)
        self.library_current_game_for_kids.setGeometry(QtCore.QRect(1080, 70, 67, 17))
        self.library_current_game_for_kids.setObjectName("library_current_game_for_kids")
        self.library_release_date_label = QtWidgets.QLabel(self.library)
        self.library_release_date_label.setGeometry(QtCore.QRect(740, 100, 101, 17))
        self.library_release_date_label.setObjectName("library_release_date_label")
        self.library_current_game_release_date = QtWidgets.QLabel(self.library)
        self.library_current_game_release_date.setGeometry(QtCore.QRect(920, 100, 101, 17))
        self.library_current_game_release_date.setObjectName("library_current_game_release_date")
        self.library_genre_label = QtWidgets.QLabel(self.library)
        self.library_genre_label.setGeometry(QtCore.QRect(740, 130, 67, 17))
        self.library_genre_label.setObjectName("library_genre_label")
        self.library_current_game_genre = QtWidgets.QLabel(self.library)
        self.library_current_game_genre.setGeometry(QtCore.QRect(820, 130, 91, 17))
        self.library_current_game_genre.setObjectName("library_current_game_genre")
        self.library_author_label = QtWidgets.QLabel(self.library)
        self.library_author_label.setGeometry(QtCore.QRect(920, 130, 67, 17))
        self.library_author_label.setObjectName("library_author_label")
        self.library_current_game_author = QtWidgets.QLabel(self.library)
        self.library_current_game_author.setGeometry(QtCore.QRect(1000, 130, 211, 17))
        self.library_current_game_author.setObjectName("library_current_game_author")
        self.library_platform_label = QtWidgets.QLabel(self.library)
        self.library_platform_label.setGeometry(QtCore.QRect(740, 160, 171, 17))
        self.library_platform_label.setObjectName("library_platform_label")
        self.library_current_game_platform = QtWidgets.QLabel(self.library)
        self.library_current_game_platform.setGeometry(QtCore.QRect(920, 160, 241, 17))
        self.library_current_game_platform.setObjectName("library_current_game_platform")
        self.library_description_label = QtWidgets.QLabel(self.library)
        self.library_description_label.setGeometry(QtCore.QRect(740, 190, 101, 17))
        self.library_description_label.setObjectName("library_description_label")
        self.library_current_game_description = QtWidgets.QLabel(self.library)
        self.library_current_game_description.setGeometry(QtCore.QRect(740, 210, 471, 361))
        self.library_current_game_description.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.library_current_game_description.setWordWrap(True)
        self.library_current_game_description.setObjectName("library_current_game_description")
        self.library_owning_game_label = QtWidgets.QLabel(self.library)
        self.library_owning_game_label.setGeometry(QtCore.QRect(740, 40, 141, 17))
        self.library_owning_game_label.setObjectName("library_owning_game_label")
        self.library_filter_label = QtWidgets.QLabel(self.library)
        self.library_filter_label.setGeometry(QtCore.QRect(270, 10, 67, 17))
        self.library_filter_label.setObjectName("library_filter_label")
        self.library_filter_by_price_check = QtWidgets.QCheckBox(self.library)
        self.library_filter_by_price_check.setGeometry(QtCore.QRect(10, 260, 121, 23))
        self.library_filter_by_price_check.setObjectName("library_filter_by_price_check")
        self.library_filter_by_date_check = QtWidgets.QCheckBox(self.library)
        self.library_filter_by_date_check.setGeometry(QtCore.QRect(10, 320, 121, 23))
        self.library_filter_by_date_check.setObjectName("library_filter_by_date_check")
        self.library_filter_by_name_check = QtWidgets.QCheckBox(self.library)
        self.library_filter_by_name_check.setGeometry(QtCore.QRect(10, 200, 121, 23))
        self.library_filter_by_name_check.setObjectName("library_filter_by_name_check")
        self.library_filter_by_name_input = QtWidgets.QLineEdit(self.library)
        self.library_filter_by_name_input.setGeometry(QtCore.QRect(20, 230, 221, 25))
        self.library_filter_by_name_input.setObjectName("library_filter_by_name_input")
        self.library_filter_by_price_label_1 = QtWidgets.QLabel(self.library)
        self.library_filter_by_price_label_1.setGeometry(QtCore.QRect(10, 290, 31, 21))
        self.library_filter_by_price_label_1.setObjectName("library_filter_by_price_label_1")
        self.library_filter_by_price_label_2 = QtWidgets.QLabel(self.library)
        self.library_filter_by_price_label_2.setGeometry(QtCore.QRect(130, 290, 21, 21))
        self.library_filter_by_price_label_2.setObjectName("library_filter_by_price_label_2")
        self.library_filter_by_price_input_1 = QtWidgets.QLineEdit(self.library)
        self.library_filter_by_price_input_1.setGeometry(QtCore.QRect(40, 290, 81, 25))
        self.library_filter_by_price_input_1.setObjectName("library_filter_by_price_input_1")
        self.library_filter_by_price_input_2 = QtWidgets.QLineEdit(self.library)
        self.library_filter_by_price_input_2.setGeometry(QtCore.QRect(160, 290, 81, 25))
        self.library_filter_by_price_input_2.setObjectName("library_filter_by_price_input_2")
        self.library_filter_by_date_input_1 = QtWidgets.QDateEdit(self.library)
        self.library_filter_by_date_input_1.setGeometry(QtCore.QRect(40, 350, 110, 26))
        self.library_filter_by_date_input_1.setObjectName("library_filter_by_date_input_1")
        self.library_filter_by_date_label_1 = QtWidgets.QLabel(self.library)
        self.library_filter_by_date_label_1.setGeometry(QtCore.QRect(10, 350, 31, 31))
        self.library_filter_by_date_label_1.setObjectName("library_filter_by_date_label_1")
        self.library_filter_by_date_label_2 = QtWidgets.QLabel(self.library)
        self.library_filter_by_date_label_2.setGeometry(QtCore.QRect(10, 380, 21, 31))
        self.library_filter_by_date_label_2.setObjectName("library_filter_by_date_label_2")
        self.library_filter_by_date_input_2 = QtWidgets.QDateEdit(self.library)
        self.library_filter_by_date_input_2.setGeometry(QtCore.QRect(40, 380, 110, 26))
        self.library_filter_by_date_input_2.setObjectName("library_filter_by_date_input_2")
        self.library_filter_by_author_check = QtWidgets.QCheckBox(self.library)
        self.library_filter_by_author_check.setGeometry(QtCore.QRect(10, 410, 92, 23))
        self.library_filter_by_author_check.setObjectName("library_filter_by_author_check")
        self.library_filter_by_author_input = QtWidgets.QLineEdit(self.library)
        self.library_filter_by_author_input.setGeometry(QtCore.QRect(20, 440, 221, 25))
        self.library_filter_by_author_input.setObjectName("library_filter_by_author_input")
        self.library_filter_by_for_kids_check = QtWidgets.QCheckBox(self.library)
        self.library_filter_by_for_kids_check.setGeometry(QtCore.QRect(10, 470, 151, 23))
        self.library_filter_by_for_kids_check.setObjectName("library_filter_by_for_kids_check")
        self.library_sort_frame = QtWidgets.QFrame(self.library)
        self.library_sort_frame.setGeometry(QtCore.QRect(0, 0, 261, 171))
        self.library_sort_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.library_sort_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.library_sort_frame.setObjectName("library_sort_frame")
        self.library_sort_by_name_combobox = QtWidgets.QComboBox(self.library_sort_frame)
        self.library_sort_by_name_combobox.setGeometry(QtCore.QRect(140, 40, 111, 25))
        self.library_sort_by_name_combobox.setObjectName("library_sort_by_name_combobox")
        self.library_sort_by_name_combobox.addItem("")
        self.library_sort_by_name_combobox.addItem("")
        self.library_sort_by_price_check = QtWidgets.QCheckBox(self.library_sort_frame)
        self.library_sort_by_price_check.setGeometry(QtCore.QRect(10, 80, 121, 23))
        self.library_sort_by_price_check.setObjectName("library_sort_by_price_check")
        self.library_sort_by_date_combobox = QtWidgets.QComboBox(self.library_sort_frame)
        self.library_sort_by_date_combobox.setGeometry(QtCore.QRect(140, 120, 111, 25))
        self.library_sort_by_date_combobox.setObjectName("library_sort_by_date_combobox")
        self.library_sort_by_date_combobox.addItem("")
        self.library_sort_by_date_combobox.addItem("")
        self.library_sort_by_date_check = QtWidgets.QCheckBox(self.library_sort_frame)
        self.library_sort_by_date_check.setGeometry(QtCore.QRect(10, 120, 121, 23))
        self.library_sort_by_date_check.setObjectName("library_sort_by_date_check")
        self.library_sort_by_price_combobox = QtWidgets.QComboBox(self.library_sort_frame)
        self.library_sort_by_price_combobox.setGeometry(QtCore.QRect(140, 80, 111, 25))
        self.library_sort_by_price_combobox.setObjectName("library_sort_by_price_combobox")
        self.library_sort_by_price_combobox.addItem("")
        self.library_sort_by_price_combobox.addItem("")
        self.library_sort_label = QtWidgets.QLabel(self.library_sort_frame)
        self.library_sort_label.setGeometry(QtCore.QRect(20, 10, 81, 17))
        self.library_sort_label.setObjectName("library_sort_label")
        self.library_sort_by_name_check = QtWidgets.QCheckBox(self.library_sort_frame)
        self.library_sort_by_name_check.setGeometry(QtCore.QRect(10, 40, 121, 23))
        self.library_sort_by_name_check.setObjectName("library_sort_by_name_check")
        self.library_sort_by_name_check.setChecked(True)
        self.library_filter_by_genre_combobox = QtWidgets.QComboBox(self.library)
        self.library_filter_by_genre_combobox.setGeometry(QtCore.QRect(290, 70, 131, 25))
        self.library_filter_by_genre_combobox.setObjectName("library_filter_by_genre_combobox")
        self.library_filter_by_genre_check = QtWidgets.QCheckBox(self.library)
        self.library_filter_by_genre_check.setGeometry(QtCore.QRect(270, 40, 92, 23))
        self.library_filter_by_genre_check.setObjectName("library_filter_by_genre_check")
        self.library_filter_by_platform_label = QtWidgets.QLabel(self.library)
        self.library_filter_by_platform_label.setGeometry(QtCore.QRect(280, 120, 81, 17))
        self.library_filter_by_platform_label.setObjectName("library_filter_by_platform_label")
        self.library_filter_by_platform_origin_check = QtWidgets.QCheckBox(self.library)
        self.library_filter_by_platform_origin_check.setGeometry(QtCore.QRect(270, 140, 92, 23))
        self.library_filter_by_platform_origin_check.setObjectName("library_filter_by_platform_origin_check")
        self.library_filter_by_platform_steam_check = QtWidgets.QCheckBox(self.library)
        self.library_filter_by_platform_steam_check.setGeometry(QtCore.QRect(270, 170, 92, 23))
        self.library_filter_by_platform_steam_check.setObjectName("library_filter_by_platform_steam_check")
        self.library_filter_by_platform_egc_check = QtWidgets.QCheckBox(self.library)
        self.library_filter_by_platform_egc_check.setGeometry(QtCore.QRect(270, 230, 141, 23))
        self.library_filter_by_platform_egc_check.setObjectName("library_filter_by_platform_egc_check")
        self.library_filter_by_platform_uplay_check = QtWidgets.QCheckBox(self.library)
        self.library_filter_by_platform_uplay_check.setGeometry(QtCore.QRect(270, 200, 92, 23))
        self.library_filter_by_platform_uplay_check.setObjectName("library_filter_by_platform_uplay_check")
        self.library_filter_by_platform_bethesda_check = QtWidgets.QCheckBox(self.library)
        self.library_filter_by_platform_bethesda_check.setGeometry(QtCore.QRect(270, 290, 151, 23))
        self.library_filter_by_platform_bethesda_check.setObjectName("library_filter_by_platform_bethesda_check")
        self.library_filter_by_platform_gog_check = QtWidgets.QCheckBox(self.library)
        self.library_filter_by_platform_gog_check.setGeometry(QtCore.QRect(270, 260, 92, 23))
        self.library_filter_by_platform_gog_check.setObjectName("library_filter_by_platform_gog_check")
        self.library_filter_by_platform_blizzard_check = QtWidgets.QCheckBox(self.library)
        self.library_filter_by_platform_blizzard_check.setGeometry(QtCore.QRect(270, 320, 111, 23))
        self.library_filter_by_platform_blizzard_check.setObjectName("library_filter_by_platform_blizzard_check")
        self.library_filter_and_sort_button = QtWidgets.QPushButton(self.library)
        self.library_filter_and_sort_button.setGeometry(QtCore.QRect(280, 520, 121, 31))
        self.library_filter_and_sort_button.setObjectName("library_filter_and_sort_button")

        MainWindow.setCentralWidget(self.library)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stacked_library.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.complete_library_list()
        self.complete_genres()
        for each_list in self.library_lists:
            each_list.currentItemChanged.connect(self.selection_in_library)
        self.library_filter_and_sort_button.clicked.connect(self.filter_and_sort_library_list)

    def get_currency(self):
        try:
            self.conn = pg2.connect(host=self.db_host, database=self.db_name, user=self.db_user, password=self.db_psswd,
                                    port=self.db_port)
            c = self.conn.cursor()
            c.execute("""
                    SELECT c.value_in_pln, c.name
                    FROM currencies c
                    JOIN users u
                    ON u.currency = c.name
                    WHERE u.user_id = {};
            """.format(self.friend_id))
            val = c.fetchone()
            self.currency_value = val[0]
            self.currency_name = val[1]
            c.close()
            self.conn.commit()
            self.conn.close()
        except pg2.errors.RaiseException:
            self.something_is_wrong()

    def complete_genres(self):
        try:
            self.conn = pg2.connect(host=self.db_host, database=self.db_name, user=self.db_user, password=self.db_psswd,
                                    port=self.db_port)
            c = self.conn.cursor()
            c.execute("""
                    SELECT name
                    FROM genres;
            """)
            genres = c.fetchall()
            c.close()
            self.conn.commit()
            self.conn.close()

            for genre in genres:
                self.library_filter_by_genre_combobox.addItem(genre[0])
        except pg2.errors.RaiseException:
            self.something_is_wrong()

    def selection_in_library(self, arg=None):
        if arg is not None:
            myObject = arg.data(QtCore.Qt.UserRole)
            _translate = QtCore.QCoreApplication.translate
            myObject.get_info()
            self.get_currency()
            self.library_current_game_name.setText(_translate("MainWindow", "{}".format(myObject.name)))
            self.library_current_game_author.setText(_translate("MainWindow", "{}".format(myObject.author)))
            self.library_current_game_price.setText(
                _translate("MainWindow", "{} {}".format(round(float(myObject.price)*float(self.currency_value), 2),
                                                        self.currency_name)))
            self.library_current_game_genre.setText(_translate("MainWindow", "{}".format(myObject.genre)))
            self.library_current_game_for_kids.setText(_translate("MainWindow", "{}".format(myObject.for_kids)))
            self.library_current_game_release_date.setText(_translate("MainWindow", "{}".format(myObject.release_date)))
            self.library_current_game_platform.setText(_translate("MainWindow", "{}".format(myObject.platform)))
            self.library_current_game_description.setText(_translate("MainWindow", "{}".format(myObject.description)))

    def count_friend_games(self):
        try:
            self.conn = pg2.connect(host=self.db_host, database=self.db_name, user=self.db_user, password=self.db_psswd,
                                    port=self.db_port)
            c = self.conn.cursor()
            c.execute("""
                    SELECT count(*) FROM users_games WHERE user_id = {};
            """.format(self.friend_id))
            ret = c.fetchone()
            c.close()
            self.conn.commit()
            self.conn.close()
            return ret[0]
        except pg2.errors.RaiseException:
            self.something_is_wrong()

    def library_next_page(self):
        self.library_lists[self.library_current_page].clear()
        self.library_current_page += 1
        self.stacked_library.setCurrentIndex(self.library_current_page)
        self.complete_library_list()

    def library_previous_page(self):
        self.library_lists[self.library_current_page].clear()
        self.library_current_page -= 1
        self.stacked_library.setCurrentIndex(self.library_current_page)
        self.complete_library_list()

    def complete_library_list(self):
        name_order = ''
        price_order = ''
        date_order = ''
        name_where = ''
        price_where = ''
        date_where = ''
        author_where = ''
        for_kids_where = ''
        genre_where = ''
        platform_where = ''
        if self.library_sort_by_name_check.isChecked():
            name_order = 'g.name'
            if self.library_sort_by_name_combobox.currentIndex() == 0:
                name_order += ' ASC'
            else:
                name_order += ' DESC'
        if self.library_sort_by_price_check.isChecked():
            price_order = 'gp.price'
            if self.library_sort_by_price_combobox.currentIndex() == 0:
                price_order += ' ASC'
            else:
                price_order += ' DESC'
        if self.library_sort_by_date_check.isChecked():
            date_order = 'gp.release_date'
            if self.library_sort_by_date_combobox.currentIndex() == 0:
                date_order += ' ASC'
            else:
                date_order += ' DESC'
        if self.library_filter_by_name_check.isChecked():
            name_where = self.library_filter_by_name_input.text()
        if self.library_filter_by_price_check.isChecked():
            price_where_1 = self.library_filter_by_price_input_1.text()
            price_where_2 = self.library_filter_by_price_input_2.text()
            price_where = 'AND gp.price >= {} AND gp.price <= {}'.format(
                float(price_where_1) * float(self.currency_value), float(price_where_2) * float(self.currency_value))
        if self.library_filter_by_date_check.isChecked():
            date_where_1 = self.library_filter_by_date_input_1.text()
            date_where_2 = self.library_filter_by_date_input_2.text()
            date_where = "AND gp.release_date >= '{}' AND gp.release_date <= '{}'".format(date_where_1, date_where_2)
        if self.library_filter_by_author_check.isChecked():
            author_where = "AND g.author LIKE '%{}%'".format(self.library_filter_by_author_input.text())
        if self.library_filter_by_for_kids_check.isChecked():
            for_kids_where = "AND g.for_kids = 'True'"
        if self.library_filter_by_genre_check.isChecked():
            genre_where = "AND g.genre = '{}'".format(self.library_filter_by_genre_combobox.currentText())
        if self.library_filter_by_platform_bethesda_check.isChecked() or \
                self.library_filter_by_platform_blizzard_check.isChecked() or \
                self.library_filter_by_platform_egc_check.isChecked() or \
                self.library_filter_by_platform_gog_check.isChecked() or \
                self.library_filter_by_platform_origin_check.isChecked() or \
                self.library_filter_by_platform_steam_check.isChecked() or \
                self.library_filter_by_platform_uplay_check.isChecked():
            platform_where = "AND gp.plat_id IN ("
        if self.library_filter_by_platform_uplay_check.isChecked():
            platform_where += "3, "
        if self.library_filter_by_platform_steam_check.isChecked():
            platform_where += "1, "
        if self.library_filter_by_platform_origin_check.isChecked():
            platform_where += "2, "
        if self.library_filter_by_platform_gog_check.isChecked():
            platform_where += "5, "
        if self.library_filter_by_platform_egc_check.isChecked():
            platform_where += "4, "
        if self.library_filter_by_platform_blizzard_check.isChecked():
            platform_where += "6, "
        if self.library_filter_by_platform_bethesda_check.isChecked():
            platform_where += "7, "
        if self.library_filter_by_platform_bethesda_check.isChecked() or \
                self.library_filter_by_platform_blizzard_check.isChecked() or \
                self.library_filter_by_platform_egc_check.isChecked() or \
                self.library_filter_by_platform_gog_check.isChecked() or \
                self.library_filter_by_platform_origin_check.isChecked() or \
                self.library_filter_by_platform_steam_check.isChecked() or \
                self.library_filter_by_platform_uplay_check.isChecked():
            platform_where = platform_where[0:len(platform_where) - 2]
            platform_where += ")"

        try:
            self.conn = pg2.connect(host=self.db_host, database=self.db_name, user=self.db_user, password=self.db_psswd,
                                    port=self.db_port)
            c = self.conn.cursor()
            c.execute("""
                    DROP VIEW friend_library_games;
    
                    CREATE VIEW friend_library_games AS(
                    SELECT g.game_id, g.name, ROW_NUMBER() OVER(ORDER BY {}{}{}) AS number
                    FROM games_platforms gp
                    JOIN games g
                    ON g.game_id = gp.game_id
                    JOIN users_games ug
                    ON ug.gp_id = gp.gp_id
                    WHERE ug.user_id = {}
                    AND g.name LIKE '%{}%' {}{}{}{}{}{});
            """.format(date_order if date_order == '' or (name_order == '' and price_order == '')
                                         else date_order + ',',
                       price_order if price_order == '' or name_order == '' else price_order + ',',
                       name_order,
                       self.friend_id,
                       name_where,
                       price_where,
                       date_where,
                       author_where,
                       for_kids_where,
                       genre_where,
                       platform_where))
            c.close()
            self.conn.commit()

            c = self.conn.cursor()
            c.execute("""
                    SELECT game_id, name
                    FROM friend_library_games
                    WHERE number >= {} AND number <= {};
            """.format(30 * self.library_current_page + 1, 30 * (self.library_current_page + 1)))
            games = c.fetchall()
            c.close()
            self.conn.commit()
            self.conn.close()

            for game in enumerate(games):
                current_game = GameListItem(self.friend_id, my_id=game[1][0])
                current_game.name = game[1][1]
                item = QtWidgets.QListWidgetItem(current_game.name)
                item.setData(QtCore.Qt.UserRole, current_game)
                self.library_lists[self.library_current_page].insertItem(game[0], item)

            if self.library_lists[self.library_current_page].count() > 0:
                curr_item = self.library_lists[self.library_current_page].item(0)
                self.library_lists[self.library_current_page].setCurrentItem(curr_item)
        except pg2.errors.RaiseException:
            self.something_is_wrong()

    def filter_and_sort_library_list(self):
        if not self.library_sort_by_name_check.isChecked() and not self.library_sort_by_date_check.isChecked() and \
                not self.library_sort_by_price_check.isChecked():
            self.library_sort_by_name_check.setChecked(True)
        self.library_lists[self.library_current_page].clear()
        self.library_current_page = 0
        self.stacked_library.setCurrentIndex(self.library_current_page)
        self.complete_library_list()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Biblioteka gracza {}".format(self.friend_name)))
        self.library_release_date_label.setText(_translate("MainWindow", "Data premiery"))
        self.library_platform_label.setText(_translate("MainWindow", "Platforma"))
        self.library_for_kids_label.setText(_translate("MainWindow", "Czy gra jest dla dzieci?"))
        self.library_author_label.setText(_translate("MainWindow", "Autor"))
        self.library_current_game_name.setText(_translate("MainWindow", "Nazwa gry"))
        self.library_description_label.setText(_translate("MainWindow", "Krótki opis"))
        self.library_genre_label.setText(_translate("MainWindow", "Gatunek"))
        self.library_price_label.setText(_translate("MainWindow", "Cena"))
        self.library_filter_label.setText(_translate("MainWindow", "Filtracja"))
        self.library_filter_by_price_check.setText(_translate("MainWindow", "Cena"))
        self.library_filter_by_date_check.setText(_translate("MainWindow", "Data premiery"))
        self.library_filter_by_name_check.setText(_translate("MainWindow", "Nazwa"))
        self.library_filter_by_price_label_1.setText(_translate("MainWindow", "Od"))
        self.library_filter_by_price_label_2.setText(_translate("MainWindow", "do"))
        self.library_filter_by_date_input_1.setDisplayFormat(_translate("MainWindow", "dd-MM-yyyy"))
        self.library_filter_by_date_label_1.setText(_translate("MainWindow", "Od"))
        self.library_filter_by_date_label_2.setText(_translate("MainWindow", "do"))
        self.library_filter_by_date_input_2.setDisplayFormat(_translate("MainWindow", "dd-MM-yyyy"))
        self.library_filter_by_author_check.setText(_translate("MainWindow", "Autor"))
        self.library_filter_by_for_kids_check.setText(_translate("MainWindow", "Gry tylko dla dzieci"))
        self.library_sort_by_name_combobox.setItemText(0, _translate("MainWindow", "Od A do Z"))
        self.library_sort_by_name_combobox.setItemText(1, _translate("MainWindow", "Od Z do A"))
        self.library_sort_by_price_check.setText(_translate("MainWindow", "Cena"))
        self.library_sort_by_date_combobox.setItemText(0, _translate("MainWindow", "Rosnąco"))
        self.library_sort_by_date_combobox.setItemText(1, _translate("MainWindow", "Malejąco"))
        self.library_sort_by_date_check.setText(_translate("MainWindow", "Data premiery"))
        self.library_sort_by_price_combobox.setItemText(0, _translate("MainWindow", "Rosnąco"))
        self.library_sort_by_price_combobox.setItemText(1, _translate("MainWindow", "Malejąco"))
        self.library_sort_label.setText(_translate("MainWindow", "Sortowanie"))
        self.library_sort_by_name_check.setText(_translate("MainWindow", "Nazwa"))
        self.library_filter_by_genre_check.setText(_translate("MainWindow", "Gatunek"))
        self.library_filter_by_platform_label.setText(_translate("MainWindow", "Platforma"))
        self.library_filter_by_platform_origin_check.setText(_translate("MainWindow", "Origin"))
        self.library_filter_by_platform_steam_check.setText(_translate("MainWindow", "Steam"))
        self.library_filter_by_platform_egc_check.setText(_translate("MainWindow", "Epic Game Store"))
        self.library_filter_by_platform_uplay_check.setText(_translate("MainWindow", "Uplay"))
        self.library_filter_by_platform_bethesda_check.setText(_translate("MainWindow", "Bethesda Launcher"))
        self.library_filter_by_platform_gog_check.setText(_translate("MainWindow", "GOG"))
        self.library_filter_by_platform_blizzard_check.setText(_translate("MainWindow", "Blizzard.net"))
        self.library_filter_and_sort_button.setText(_translate("MainWindow", "Filtruj i sortuj"))

    @staticmethod
    def something_is_wrong():
        msg = QMessageBox()
        msg.setWindowTitle("Błąd")
        msg.setText("Coś poszło nie tak :(")
        msg.setIcon(QMessageBox.Critical)
        msg.setStandardButtons(QMessageBox.Abort)

        x = msg.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_LibraryFriend(162, "XD", 2)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
