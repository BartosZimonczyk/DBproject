# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user_gui.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import psycopg2 as pg2
from list_item import *
import sys
import os
import math
from friend_library import Ui_LibraryFriend


class Ui_UserGui(object):
    def __init__(self, user_id):
        super(Ui_UserGui, self).__init__()
        self.user_id = user_id

        # dane do logowania do bazy danych
        self.db_host = 'packy.db.elephantsql.com'
        self.db_user = 'htcazxfd'
        self.db_name = 'htcazxfd'
        self.db_port = 5432
        self.db_psswd = 'UE5AaV5whqnbKyD5jL9MusNCvV1yaX7T'
        self.conn = None

        # listy z obiektami list i stron obsługujące sklep
        self.shop_pages = []
        self.shop_lists = []
        self.shop_previous_buttons = []
        self.shop_next_buttons = []
        self.shop_current_page_labels = []
        self.shop_current_page = 0

        # listy z obiektami list i stron obsługujące bibliotekę
        self.library_pages = []
        self.library_lists = []
        self.library_previous_buttons = []
        self.library_next_buttons = []
        self.library_current_page_labels = []
        self.library_current_page = 0

        self.current_friend_id = 0
        self.current_friend_name = None
        self.current_game = None

        self.only_int_validator = QtGui.QIntValidator(0, 999999)

    def setupUi(self, MainWindow):
        self.window = MainWindow
        _translate = QtCore.QCoreApplication.translate

        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1240, 660)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        # MainWindow.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(211, 215, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(211, 215, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(211, 215, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(211, 215, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Tabs = QtWidgets.QTabWidget(self.centralwidget)
        self.Tabs.setGeometry(QtCore.QRect(0, 0, 1231, 611))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Tabs.sizePolicy().hasHeightForWidth())
        self.Tabs.setSizePolicy(sizePolicy)
        self.Tabs.setMaximumSize(QtCore.QSize(1231, 611))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(211, 215, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(211, 215, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(211, 215, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(211, 215, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.Tabs.setPalette(palette)
        self.Tabs.setObjectName("Tabs")
        self.shop = QtWidgets.QWidget()
        self.shop.setObjectName("shop")
        self.stacked_shop = QtWidgets.QStackedWidget(self.shop)
        self.stacked_shop.setGeometry(QtCore.QRect(440, 0, 281, 620))
        self.stacked_shop.setObjectName("stacked_shop")

        n = math.ceil(self.count_all_games()/30)
        n = n if n > 0 else 1
        for i in range(n):
            self.shop_pages.append(QtWidgets.QWidget())
            self.shop_pages[i].setObjectName("stacked_shop_page_{}".format(i+1))
            self.stacked_shop.addWidget(self.shop_pages[i])
            self.shop_lists.append(QtWidgets.QListWidget(self.shop_pages[i]))
            self.shop_lists[i].setGeometry(QtCore.QRect(0, 0, 281, 580))
            self.shop_lists[i].setObjectName("list_shop_{}".format(i+1))
            if i > 0:
                self.shop_previous_buttons.append(QtWidgets.QPushButton(self.shop_pages[i]))
                self.shop_previous_buttons[i-1].setGeometry(QtCore.QRect(0, 545, 89, 25))
                self.shop_previous_buttons[i-1].setObjectName("shop_previous_button_{}".format(i))
                self.shop_previous_buttons[i-1].clicked.connect(self.shop_previous_page)
                self.shop_previous_buttons[i-1].setText(_translate("MainWindow", "Poprzednia"))
            if i < n-1:
                self.shop_next_buttons.append(QtWidgets.QPushButton(self.shop_pages[i]))
                self.shop_next_buttons[i].setGeometry(QtCore.QRect(190, 545, 89, 25))
                self.shop_next_buttons[i].setObjectName("shop_next_button_{}".format(i+1))
                self.shop_next_buttons[i].clicked.connect(self.shop_next_page)
                self.shop_next_buttons[i].setText(_translate("MainWindow", "Następna"))
            self.shop_current_page_labels.append(QtWidgets.QLabel(self.shop_pages[i]))
            self.shop_current_page_labels[i].setGeometry(QtCore.QRect(110, 560, 67, 17))
            self.shop_current_page_labels[i].setObjectName("shop_current_page_label_{}".format(i+1))
            self.shop_current_page_labels[i].setText(_translate("MainWindow", "Strona {}".format(i+1)))

        self.shop_current_game_name = QtWidgets.QLabel(self.shop)
        self.shop_current_game_name.setGeometry(QtCore.QRect(730, 0, 491, 41))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.shop_current_game_name.setFont(font)
        self.shop_current_game_name.setObjectName("shop_current_game_name")
        self.shop_price_label = QtWidgets.QLabel(self.shop)
        self.shop_price_label.setGeometry(QtCore.QRect(740, 70, 67, 17))
        self.shop_price_label.setObjectName("shop_price_label")
        self.shop_current_game_price = QtWidgets.QLabel(self.shop)
        self.shop_current_game_price.setGeometry(QtCore.QRect(800, 70, 100, 17))
        self.shop_current_game_price.setObjectName("shop_current_game_price")
        self.shop_for_kids_label = QtWidgets.QLabel(self.shop)
        self.shop_for_kids_label.setGeometry(QtCore.QRect(920, 70, 161, 17))
        self.shop_for_kids_label.setObjectName("shop_for_kids_label")
        self.shop_current_game_for_kids = QtWidgets.QLabel(self.shop)
        self.shop_current_game_for_kids.setGeometry(QtCore.QRect(1080, 70, 67, 17))
        self.shop_current_game_for_kids.setObjectName("shop_current_game_for_kids")
        self.shop_release_date_label = QtWidgets.QLabel(self.shop)
        self.shop_release_date_label.setGeometry(QtCore.QRect(740, 100, 101, 17))
        self.shop_release_date_label.setObjectName("shop_release_date_label")
        self.shop_current_game_release_date = QtWidgets.QLabel(self.shop)
        self.shop_current_game_release_date.setGeometry(QtCore.QRect(920, 100, 101, 17))
        self.shop_current_game_release_date.setObjectName("shop_current_game_release_date")
        self.shop_genre_label = QtWidgets.QLabel(self.shop)
        self.shop_genre_label.setGeometry(QtCore.QRect(740, 130, 67, 17))
        self.shop_genre_label.setObjectName("shop_genre_label")
        self.shop_current_game_genre = QtWidgets.QLabel(self.shop)
        self.shop_current_game_genre.setGeometry(QtCore.QRect(820, 130, 91, 17))
        self.shop_current_game_genre.setObjectName("shop_current_game_genre")
        self.shop_author_label = QtWidgets.QLabel(self.shop)
        self.shop_author_label.setGeometry(QtCore.QRect(920, 130, 67, 17))
        self.shop_author_label.setObjectName("shop_author_label")
        self.shop_current_game_author = QtWidgets.QLabel(self.shop)
        self.shop_current_game_author.setGeometry(QtCore.QRect(1000, 130, 211, 17))
        self.shop_current_game_author.setObjectName("shop_current_game_author")
        self.shop_platform_label = QtWidgets.QLabel(self.shop)
        self.shop_platform_label.setGeometry(QtCore.QRect(740, 160, 171, 17))
        self.shop_platform_label.setObjectName("shop_platform_label")
        self.shop_current_game_platform = QtWidgets.QLabel(self.shop)
        self.shop_current_game_platform.setGeometry(QtCore.QRect(920, 160, 241, 17))
        self.shop_current_game_platform.setObjectName("shop_current_game_platform")
        self.shop_description_label = QtWidgets.QLabel(self.shop)
        self.shop_description_label.setGeometry(QtCore.QRect(740, 190, 101, 17))
        self.shop_description_label.setObjectName("shop_description_label")
        self.shop_current_game_description = QtWidgets.QLabel(self.shop)
        self.shop_current_game_description.setGeometry(QtCore.QRect(740, 210, 471, 361))
        self.shop_current_game_description.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.shop_current_game_description.setWordWrap(True)
        self.shop_current_game_description.setObjectName("shop_current_game_description")
        self.shop_owning_game_label = QtWidgets.QLabel(self.shop)
        self.shop_owning_game_label.setGeometry(QtCore.QRect(740, 40, 141, 17))
        self.shop_owning_game_label.setObjectName("shop_owning_game_label")
        self.shop_buy_game_button = QtWidgets.QPushButton(self.shop)
        self.shop_buy_game_button.setGeometry(QtCore.QRect(1100, 10, 89, 25))
        self.shop_buy_game_button.setObjectName("shop_buy_game_button")
        self.shop_filter_label = QtWidgets.QLabel(self.shop)
        self.shop_filter_label.setGeometry(QtCore.QRect(270, 10, 67, 17))
        self.shop_filter_label.setObjectName("shop_filter_label")
        self.shop_filter_by_price_check = QtWidgets.QCheckBox(self.shop)
        self.shop_filter_by_price_check.setGeometry(QtCore.QRect(10, 260, 121, 23))
        self.shop_filter_by_price_check.setObjectName("shop_filter_by_price_check")
        self.shop_filter_by_date_check = QtWidgets.QCheckBox(self.shop)
        self.shop_filter_by_date_check.setGeometry(QtCore.QRect(10, 320, 121, 23))
        self.shop_filter_by_date_check.setObjectName("shop_filter_by_date_check")
        self.shop_filter_by_name_check = QtWidgets.QCheckBox(self.shop)
        self.shop_filter_by_name_check.setGeometry(QtCore.QRect(10, 200, 121, 23))
        self.shop_filter_by_name_check.setObjectName("shop_filter_by_name_check")
        self.shop_filter_by_name_input = QtWidgets.QLineEdit(self.shop)
        self.shop_filter_by_name_input.setGeometry(QtCore.QRect(20, 230, 221, 25))
        self.shop_filter_by_name_input.setObjectName("shop_filter_by_name_input")
        self.shop_filter_by_price_label_1 = QtWidgets.QLabel(self.shop)
        self.shop_filter_by_price_label_1.setGeometry(QtCore.QRect(10, 290, 31, 21))
        self.shop_filter_by_price_label_1.setObjectName("shop_filter_by_price_label_1")
        self.shop_filter_by_price_label_2 = QtWidgets.QLabel(self.shop)
        self.shop_filter_by_price_label_2.setGeometry(QtCore.QRect(130, 290, 21, 21))
        self.shop_filter_by_price_label_2.setObjectName("shop_filter_by_price_label_2")
        self.shop_filter_by_price_input_1 = QtWidgets.QLineEdit(self.shop)
        self.shop_filter_by_price_input_1.setGeometry(QtCore.QRect(40, 290, 81, 25))
        self.shop_filter_by_price_input_1.setObjectName("shop_filter_by_price_input_1")
        self.shop_filter_by_price_input_1.setValidator(self.only_int_validator)
        self.shop_filter_by_price_input_2 = QtWidgets.QLineEdit(self.shop)
        self.shop_filter_by_price_input_2.setGeometry(QtCore.QRect(160, 290, 81, 25))
        self.shop_filter_by_price_input_2.setObjectName("shop_filter_by_price_input_2")
        self.shop_filter_by_price_input_2.setValidator(self.only_int_validator)
        self.shop_filter_by_date_input_1 = QtWidgets.QDateEdit(self.shop)
        self.shop_filter_by_date_input_1.setGeometry(QtCore.QRect(40, 350, 110, 26))
        self.shop_filter_by_date_input_1.setObjectName("shop_filter_by_date_input_1")
        self.shop_filter_by_date_label_1 = QtWidgets.QLabel(self.shop)
        self.shop_filter_by_date_label_1.setGeometry(QtCore.QRect(10, 350, 31, 31))
        self.shop_filter_by_date_label_1.setObjectName("shop_filter_by_date_label_1")
        self.shop_filter_by_date_label_2 = QtWidgets.QLabel(self.shop)
        self.shop_filter_by_date_label_2.setGeometry(QtCore.QRect(10, 380, 21, 31))
        self.shop_filter_by_date_label_2.setObjectName("shop_filter_by_date_label_2")
        self.shop_filter_by_date_input_2 = QtWidgets.QDateEdit(self.shop)
        self.shop_filter_by_date_input_2.setGeometry(QtCore.QRect(40, 380, 110, 26))
        self.shop_filter_by_date_input_2.setObjectName("shop_filter_by_date_input_2")
        self.shop_filter_by_author_check = QtWidgets.QCheckBox(self.shop)
        self.shop_filter_by_author_check.setGeometry(QtCore.QRect(10, 410, 92, 23))
        self.shop_filter_by_author_check.setObjectName("shop_filter_by_author_check")
        self.shop_filter_by_author_input = QtWidgets.QLineEdit(self.shop)
        self.shop_filter_by_author_input.setGeometry(QtCore.QRect(20, 440, 221, 25))
        self.shop_filter_by_author_input.setObjectName("shop_filter_by_author_input")
        self.shop_filter_by_for_kids_check = QtWidgets.QCheckBox(self.shop)
        self.shop_filter_by_for_kids_check.setGeometry(QtCore.QRect(10, 470, 151, 23))
        self.shop_filter_by_for_kids_check.setObjectName("shop_filter_by_for_kids_check")
        self.shop_filter_by_owning_check = QtWidgets.QCheckBox(self.shop)
        self.shop_filter_by_owning_check.setGeometry(QtCore.QRect(10, 500, 151, 23))
        self.shop_filter_by_owning_check.setObjectName("shop_filter_by_owning_check")
        self.shop_sort_frame = QtWidgets.QFrame(self.shop)
        self.shop_sort_frame.setGeometry(QtCore.QRect(0, 0, 261, 171))
        self.shop_sort_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.shop_sort_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.shop_sort_frame.setObjectName("shop_sort_frame")
        self.shop_sort_by_name_combobox = QtWidgets.QComboBox(self.shop_sort_frame)
        self.shop_sort_by_name_combobox.setGeometry(QtCore.QRect(140, 40, 111, 25))
        self.shop_sort_by_name_combobox.setObjectName("shop_sort_by_name_combobox")
        self.shop_sort_by_name_combobox.addItem("")
        self.shop_sort_by_name_combobox.addItem("")
        self.shop_sort_by_price_check = QtWidgets.QCheckBox(self.shop_sort_frame)
        self.shop_sort_by_price_check.setGeometry(QtCore.QRect(10, 80, 121, 23))
        self.shop_sort_by_price_check.setObjectName("shop_sort_by_price_check")
        self.shop_sort_by_date_combobox = QtWidgets.QComboBox(self.shop_sort_frame)
        self.shop_sort_by_date_combobox.setGeometry(QtCore.QRect(140, 120, 111, 25))
        self.shop_sort_by_date_combobox.setObjectName("shop_sort_by_date_combobox")
        self.shop_sort_by_date_combobox.addItem("")
        self.shop_sort_by_date_combobox.addItem("")
        self.shop_sort_by_date_check = QtWidgets.QCheckBox(self.shop_sort_frame)
        self.shop_sort_by_date_check.setGeometry(QtCore.QRect(10, 120, 121, 23))
        self.shop_sort_by_date_check.setObjectName("shop_sort_by_date_check")
        self.shop_sort_by_price_combobox = QtWidgets.QComboBox(self.shop_sort_frame)
        self.shop_sort_by_price_combobox.setGeometry(QtCore.QRect(140, 80, 111, 25))
        self.shop_sort_by_price_combobox.setObjectName("shop_sort_by_price_combobox")
        self.shop_sort_by_price_combobox.addItem("")
        self.shop_sort_by_price_combobox.addItem("")
        self.shop_sort_label = QtWidgets.QLabel(self.shop_sort_frame)
        self.shop_sort_label.setGeometry(QtCore.QRect(20, 10, 81, 17))
        self.shop_sort_label.setObjectName("shop_sort_label")
        self.shop_sort_by_name_check = QtWidgets.QCheckBox(self.shop_sort_frame)
        self.shop_sort_by_name_check.setGeometry(QtCore.QRect(10, 40, 121, 23))
        self.shop_sort_by_name_check.setObjectName("shop_sort_by_name_check")
        self.shop_sort_by_name_check.setChecked(True)
        self.shop_filter_by_genre_combobox = QtWidgets.QComboBox(self.shop)
        self.shop_filter_by_genre_combobox.setGeometry(QtCore.QRect(290, 70, 131, 25))
        self.shop_filter_by_genre_combobox.setObjectName("shop_filter_by_genre_combobox")
        self.shop_filter_by_genre_check = QtWidgets.QCheckBox(self.shop)
        self.shop_filter_by_genre_check.setGeometry(QtCore.QRect(270, 40, 92, 23))
        self.shop_filter_by_genre_check.setObjectName("shop_filter_by_genre_check")
        self.shop_filter_by_platform_label = QtWidgets.QLabel(self.shop)
        self.shop_filter_by_platform_label.setGeometry(QtCore.QRect(280, 120, 81, 17))
        self.shop_filter_by_platform_label.setObjectName("shop_filter_by_platform_label")
        self.shop_filter_by_platform_origin_check = QtWidgets.QCheckBox(self.shop)
        self.shop_filter_by_platform_origin_check.setGeometry(QtCore.QRect(270, 140, 92, 23))
        self.shop_filter_by_platform_origin_check.setObjectName("shop_filter_by_platform_origin_check")
        self.shop_filter_by_platform_steam_check = QtWidgets.QCheckBox(self.shop)
        self.shop_filter_by_platform_steam_check.setGeometry(QtCore.QRect(270, 170, 92, 23))
        self.shop_filter_by_platform_steam_check.setObjectName("shop_filter_by_platform_steam_check")
        self.shop_filter_by_platform_egc_check = QtWidgets.QCheckBox(self.shop)
        self.shop_filter_by_platform_egc_check.setGeometry(QtCore.QRect(270, 230, 141, 23))
        self.shop_filter_by_platform_egc_check.setObjectName("shop_filter_by_platform_egc_check")
        self.shop_filter_by_platform_uplay_check = QtWidgets.QCheckBox(self.shop)
        self.shop_filter_by_platform_uplay_check.setGeometry(QtCore.QRect(270, 200, 92, 23))
        self.shop_filter_by_platform_uplay_check.setObjectName("shop_filter_by_platform_uplay_check")
        self.shop_filter_by_platform_bethesda_check = QtWidgets.QCheckBox(self.shop)
        self.shop_filter_by_platform_bethesda_check.setGeometry(QtCore.QRect(270, 290, 151, 23))
        self.shop_filter_by_platform_bethesda_check.setObjectName("shop_filter_by_platform_bethesda_check")
        self.shop_filter_by_platform_gog_check = QtWidgets.QCheckBox(self.shop)
        self.shop_filter_by_platform_gog_check.setGeometry(QtCore.QRect(270, 260, 92, 23))
        self.shop_filter_by_platform_gog_check.setObjectName("shop_filter_by_platform_gog_check")
        self.shop_filter_by_platform_blizzard_check = QtWidgets.QCheckBox(self.shop)
        self.shop_filter_by_platform_blizzard_check.setGeometry(QtCore.QRect(270, 320, 111, 23))
        self.shop_filter_by_platform_blizzard_check.setObjectName("shop_filter_by_platform_blizzard_check")
        self.shop_filter_and_sort_button = QtWidgets.QPushButton(self.shop)
        self.shop_filter_and_sort_button.setGeometry(QtCore.QRect(280, 520, 121, 31))
        self.shop_filter_and_sort_button.setObjectName("shop_filter_and_sort_button")

        self.Tabs.addTab(self.shop, "")
        self.friends = QtWidgets.QWidget()
        self.friends.setObjectName("friends")
        self.friends_label_birth = QtWidgets.QLabel(self.friends)
        self.friends_label_birth.setGeometry(QtCore.QRect(722, 80, 111, 17))
        self.friends_label_birth.setObjectName("friends_label_birth")
        self.friends_birth_date = QtWidgets.QLabel(self.friends)
        self.friends_birth_date.setGeometry(QtCore.QRect(832, 80, 101, 17))
        self.friends_birth_date.setObjectName("friends_birth_date")
        self.friends_label_creation = QtWidgets.QLabel(self.friends)
        self.friends_label_creation.setGeometry(QtCore.QRect(952, 80, 161, 17))
        self.friends_label_creation.setObjectName("friends_label_creation")
        self.friends_creation_date = QtWidgets.QLabel(self.friends)
        self.friends_creation_date.setGeometry(QtCore.QRect(1112, 80, 101, 17))
        self.friends_creation_date.setObjectName("friends_creation_date")
        self.open_friend_library_button = QtWidgets.QPushButton(self.friends)
        self.open_friend_library_button.setGeometry(QtCore.QRect(760, 210, 421, 51))
        self.open_friend_library_button.setObjectName("open_friend_library_button")
        self.friends_username_label = QtWidgets.QLabel(self.friends)
        self.friends_username_label.setGeometry(QtCore.QRect(722, 20, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.friends_username_label.setFont(font)
        self.friends_username_label.setObjectName("friends_username_label")
        self.friends_username = QtWidgets.QLabel(self.friends)
        self.friends_username.setGeometry(QtCore.QRect(972, 20, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.friends_username.setFont(font)
        self.friends_username.setObjectName("friends_username")
        self.friends_delete_friend_button = QtWidgets.QPushButton(self.friends)
        self.friends_delete_friend_button.setGeometry(QtCore.QRect(1010, 470, 171, 25))
        self.friends_delete_friend_button.setObjectName("friends_delete_friend_button")
        self.friends_list = QtWidgets.QListWidget(self.friends)
        self.friends_list.setGeometry(QtCore.QRect(422, 0, 291, 581))
        self.friends_list.setObjectName("friends_list")
        self.friends_since_label = QtWidgets.QLabel(self.friends)
        self.friends_since_label.setGeometry(QtCore.QRect(722, 120, 104, 17))
        self.friends_since_label.setObjectName("friends_since_label")
        self.friends_since_date = QtWidgets.QLabel(self.friends)
        self.friends_since_date.setGeometry(QtCore.QRect(832, 120, 101, 17))
        self.friends_since_date.setObjectName("friends_since_date")
        self.friends_sort_frame = QtWidgets.QFrame(self.friends)
        self.friends_sort_frame.setGeometry(QtCore.QRect(0, 0, 361, 171))
        self.friends_sort_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.friends_sort_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.friends_sort_frame.setObjectName("friends_sort_frame")
        self.friends_sort_by_name_combobox = QtWidgets.QComboBox(self.friends_sort_frame)
        self.friends_sort_by_name_combobox.setGeometry(QtCore.QRect(200, 40, 111, 25))
        self.friends_sort_by_name_combobox.setObjectName("friends_sort_by_name_combobox")
        self.friends_sort_by_name_combobox.addItem("")
        self.friends_sort_by_name_combobox.addItem("")
        self.friends_sort_by_birth_check = QtWidgets.QCheckBox(self.friends_sort_frame)
        self.friends_sort_by_birth_check.setGeometry(QtCore.QRect(10, 80, 181, 23))
        self.friends_sort_by_birth_check.setObjectName("friends_sort_by_birth_check")
        self.friends_sort_by_birth_combobox = QtWidgets.QComboBox(self.friends_sort_frame)
        self.friends_sort_by_birth_combobox.setGeometry(QtCore.QRect(200, 80, 111, 25))
        self.friends_sort_by_birth_combobox.setObjectName("friends_sort_by_birth_combobox")
        self.friends_sort_by_birth_combobox.addItem("")
        self.friends_sort_by_birth_combobox.addItem("")
        self.friends_sort_label = QtWidgets.QLabel(self.friends_sort_frame)
        self.friends_sort_label.setGeometry(QtCore.QRect(20, 10, 81, 17))
        self.friends_sort_label.setObjectName("friends_sort_label")
        self.friends_sort_by_name_check = QtWidgets.QCheckBox(self.friends_sort_frame)
        self.friends_sort_by_name_check.setGeometry(QtCore.QRect(10, 40, 121, 23))
        self.friends_sort_by_name_check.setObjectName("friends_sort_by_name_check")
        self.friends_sort_by_name_check.setChecked(True)
        self.friends_sort_button = QtWidgets.QPushButton(self.friends_sort_frame)
        self.friends_sort_button.setGeometry(QtCore.QRect(220, 124, 111, 31))
        self.friends_sort_button.setObjectName("friends_sort_button")

        self.Tabs.addTab(self.friends, "")
        self.library = QtWidgets.QWidget()
        self.library.setObjectName("library")
        self.stacked_library = QtWidgets.QStackedWidget(self.library)
        self.stacked_library.setGeometry(QtCore.QRect(440, 0, 281, 620))
        self.stacked_library.setObjectName("stacked_library")

        n = math.ceil(self.count_my_games()/30)
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
        self.library_delete_game_button = QtWidgets.QPushButton(self.library)
        self.library_delete_game_button.setGeometry(QtCore.QRect(1100, 10, 89, 25))
        self.library_delete_game_button.setObjectName("library_delete_game_button")
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
        self.library_filter_by_price_input_1.setValidator(self.only_int_validator)
        self.library_filter_by_price_input_2 = QtWidgets.QLineEdit(self.library)
        self.library_filter_by_price_input_2.setGeometry(QtCore.QRect(160, 290, 81, 25))
        self.library_filter_by_price_input_2.setObjectName("library_filter_by_price_input_2")
        self.library_filter_by_price_input_2.setValidator(self.only_int_validator)
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

        self.Tabs.addTab(self.library, "")
        self.settings = QtWidgets.QWidget()
        self.settings.setObjectName("settings")
        self.log_out_button = QtWidgets.QPushButton(self.settings)
        self.log_out_button.setGeometry(QtCore.QRect(670, 470, 89, 25))
        self.log_out_button.setObjectName("log_out_button")
        self.settings_add_money_label = QtWidgets.QLabel(self.settings)
        self.settings_add_money_label.setGeometry(QtCore.QRect(20, 20, 101, 21))
        self.settings_add_money_label.setObjectName("settings_add_money_label")
        self.settings_add_money_input = QtWidgets.QLineEdit(self.settings)
        self.settings_add_money_input.setGeometry(QtCore.QRect(20, 50, 113, 25))
        self.settings_add_money_input.setObjectName("settings_add_money_input")
        self.settings_add_money_input.setValidator(self.only_int_validator)
        self.settings_my_currency = QtWidgets.QLabel(self.settings)
        self.settings_my_currency.setGeometry(QtCore.QRect(140, 50, 71, 21))
        self.settings_my_currency.setObjectName("settings_my_currency")
        self.settings_change_currency_label = QtWidgets.QLabel(self.settings)
        self.settings_change_currency_label.setGeometry(QtCore.QRect(20, 90, 201, 17))
        self.settings_change_currency_label.setObjectName("settings_change_currency_label")
        self.settings_change_currency_combobox = QtWidgets.QComboBox(self.settings)
        self.settings_change_currency_combobox.setGeometry(QtCore.QRect(20, 120, 86, 25))
        self.settings_change_currency_combobox.setObjectName("settings_change_currency_combobox")
        self.settings_add_money_button = QtWidgets.QPushButton(self.settings)
        self.settings_add_money_button.setGeometry(QtCore.QRect(310, 50, 89, 25))
        self.settings_add_money_button.setObjectName("settings_add_money_button")
        self.settings_change_currency_button = QtWidgets.QPushButton(self.settings)
        self.settings_change_currency_button.setGeometry(QtCore.QRect(310, 120, 89, 25))
        self.settings_change_currency_button.setObjectName("settings_change_currency_button")
        self.settings_change_password_label = QtWidgets.QLabel(self.settings)
        self.settings_change_password_label.setGeometry(QtCore.QRect(20, 160, 91, 17))
        self.settings_change_password_label.setObjectName("settings_change_password_label")
        self.settings_change_password_old_input = QtWidgets.QLineEdit(self.settings)
        self.settings_change_password_old_input.setGeometry(QtCore.QRect(120, 190, 171, 25))
        self.settings_change_password_old_input.setObjectName("settings_change_password_old_input")
        self.settings_change_password_old_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.settings_change_password_button = QtWidgets.QPushButton(self.settings)
        self.settings_change_password_button.setGeometry(QtCore.QRect(310, 230, 89, 25))
        self.settings_change_password_button.setObjectName("settings_change_password_button")
        self.settings_change_mail_button = QtWidgets.QPushButton(self.settings)
        self.settings_change_mail_button.setGeometry(QtCore.QRect(310, 300, 89, 25))
        self.settings_change_mail_button.setObjectName("settings_change_mail_button")
        self.settings_change_mail_label = QtWidgets.QLabel(self.settings)
        self.settings_change_mail_label.setGeometry(QtCore.QRect(20, 270, 101, 17))
        self.settings_change_mail_label.setObjectName("settings_change_mail_label")
        self.settings_change_mail_input = QtWidgets.QLineEdit(self.settings)
        self.settings_change_mail_input.setGeometry(QtCore.QRect(20, 300, 171, 25))
        self.settings_change_mail_input.setObjectName("settings_change_mail_input")
        self.settings_change_password_new_input = QtWidgets.QLineEdit(self.settings)
        self.settings_change_password_new_input.setGeometry(QtCore.QRect(120, 230, 171, 25))
        self.settings_change_password_new_input.setObjectName("settings_change_password_new_input")
        self.settings_change_password_new_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.settings_change_password_old_label = QtWidgets.QLabel(self.settings)
        self.settings_change_password_old_label.setGeometry(QtCore.QRect(20, 190, 81, 21))
        self.settings_change_password_old_label.setObjectName("settings_change_password_old_label")
        self.settings_change_password_new_label = QtWidgets.QLabel(self.settings)
        self.settings_change_password_new_label.setGeometry(QtCore.QRect(20, 230, 81, 21))
        self.settings_change_password_new_label.setObjectName("settings_change_password_new_label")
        self.settings_account_creation_label = QtWidgets.QLabel(self.settings)
        self.settings_account_creation_label.setGeometry(QtCore.QRect(20, 340, 161, 17))
        self.settings_account_creation_label.setObjectName("settings_account_creation_label")
        self.settings_date_of_birth_label = QtWidgets.QLabel(self.settings)
        self.settings_date_of_birth_label.setGeometry(QtCore.QRect(20, 370, 161, 17))
        self.settings_date_of_birth_label.setObjectName("settings_date_of_birth_label")
        self.settings_account_creation = QtWidgets.QLabel(self.settings)
        self.settings_account_creation.setGeometry(QtCore.QRect(310, 340, 101, 17))
        self.settings_account_creation.setObjectName("settings_account_creation")
        self.settings_date_of_birth = QtWidgets.QLabel(self.settings)
        self.settings_date_of_birth.setGeometry(QtCore.QRect(310, 370, 101, 17))
        self.settings_date_of_birth.setObjectName("settings_date_of_birth")
        self.settings_add_friend_label = QtWidgets.QLabel(self.settings)
        self.settings_add_friend_label.setGeometry(QtCore.QRect(20, 430, 121, 17))
        self.settings_add_friend_label.setObjectName("settings_add_friend_label")
        self.settings_add_friend_input = QtWidgets.QLineEdit(self.settings)
        self.settings_add_friend_input.setGeometry(QtCore.QRect(20, 460, 171, 25))
        self.settings_add_friend_input.setObjectName("settings_add_friend_input")
        self.settings_add_friend_button = QtWidgets.QPushButton(self.settings)
        self.settings_add_friend_button.setGeometry(QtCore.QRect(310, 460, 89, 25))
        self.settings_add_friend_button.setObjectName("settings_add_friend_button")
        self.settings_currency_value_label = QtWidgets.QLabel(self.settings)
        self.settings_currency_value_label.setGeometry(QtCore.QRect(120, 120, 181, 21))
        self.settings_currency_value_label.setObjectName("settings_currency_value_label")
        self.Tabs.addTab(self.settings, "")
        self.username = QtWidgets.QLabel(self.centralwidget)
        self.username.setGeometry(QtCore.QRect(800, 0, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.username.setFont(font)
        self.username.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.username.setObjectName("username")
        self.wallet = QtWidgets.QLabel(self.centralwidget)
        self.wallet.setGeometry(QtCore.QRect(990, 0, 61, 17))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.wallet.setFont(font)
        self.wallet.setObjectName("wallet")
        self.wallet_amount = QtWidgets.QLabel(self.centralwidget)
        self.wallet_amount.setGeometry(QtCore.QRect(1060, 0, 101, 17))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.wallet_amount.setFont(font)
        self.wallet_amount.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.wallet_amount.setObjectName("wallet_amount")
        self.currency = QtWidgets.QLabel(self.centralwidget)
        self.currency.setGeometry(QtCore.QRect(1170, 0, 67, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.currency.setFont(font)
        self.currency.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.currency.setObjectName("currency")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 792, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.basic_info()
        self.retranslateUi(MainWindow)
        self.Tabs.setCurrentIndex(0)
        self.stacked_shop.setCurrentIndex(self.shop_current_page)
        self.stacked_library.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.open_friend_library_button.clicked.connect(self.open_friend_library)
        self.log_out_button.clicked.connect(self.log_out)
        self.settings_add_money_button.clicked.connect(self.add_money)
        self.settings_change_currency_button.clicked.connect(self.change_currency)
        self.settings_change_password_button.clicked.connect(self.change_password)
        self.settings_change_mail_button.clicked.connect(self.change_mail)
        self.settings_add_friend_button.clicked.connect(self.add_friend)
        self.settings_change_currency_combobox.currentIndexChanged.connect(self.settings_set_currency_value)
        self.friends_list.currentItemChanged.connect(self.selection_in_friends)
        self.friends_delete_friend_button.clicked.connect(self.delete_friend)
        self.friends_sort_button.clicked.connect(self.sort_friends_list)
        self.shop_buy_game_button.clicked.connect(self.buy_game)
        self.shop_filter_and_sort_button.clicked.connect(self.filter_and_sort_shop_list)
        for each_list in self.shop_lists:
            each_list.currentItemChanged.connect(self.selection_in_shop)
        self.library_delete_game_button.clicked.connect(self.delete_game)
        self.library_filter_and_sort_button.clicked.connect(self.filter_and_sort_library_list)
        for each_list in self.library_lists:
            each_list.currentItemChanged.connect(self.selection_in_library)
        self.complete_friends_list()
        self.complete_shop_list()
        self.complete_library_list()
        self.complete_currencies()
        self.complete_genres()

    def shop_next_page(self):
        self.shop_lists[self.shop_current_page].clear()
        self.shop_current_page += 1
        self.stacked_shop.setCurrentIndex(self.shop_current_page)
        self.complete_shop_list()

    def shop_previous_page(self):
        self.shop_lists[self.shop_current_page].clear()
        self.shop_current_page -= 1
        self.stacked_shop.setCurrentIndex(self.shop_current_page)
        self.complete_shop_list()

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

    def count_my_games(self):
        try:
            self.conn = pg2.connect(host=self.db_host, database=self.db_name, user=self.db_user, password=self.db_psswd,
                                    port=self.db_port)
            c = self.conn.cursor()
            c.execute("""
                    SELECT count(*) FROM users_games WHERE user_id = {};
            """.format(self.user_id))
            ret = c.fetchone()
            c.close()
            self.conn.commit()
            self.conn.close()
            return ret[0]
        except pg2.errors.RaiseException:
            self.something_is_wrong(1)

    def count_all_games(self):
        try:
            self.conn = self.conn = pg2.connect(host=self.db_host, database=self.db_name, user=self.db_user, password=self.db_psswd,
                                    port=self.db_port)
            c = self.conn.cursor()
            c.execute("""
                    SELECT count(*) FROM games_platforms;
            """)
            ret = c.fetchone()
            c.close()
            self.conn.commit()
            self.conn.close()
            return ret[0]
        except pg2.errors.RaiseException:
            self.something_is_wrong(2)

    # wpisuje wszystkie teksty do etykiet i przycisków
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Biblioteka cyfrowa gier"))
        self.friends_label_birth.setText(_translate("MainWindow", "Data urodzenia"))
        self.friends_label_creation.setText(_translate("MainWindow", "Data utworzenia konta"))
        self.friends_username_label.setText(_translate("MainWindow", "Informacje o użytkowniku"))
        self.friends_delete_friend_button.setText(_translate("MainWindow", "Usuń tego znajomego"))
        self.friends_since_label.setText(_translate("MainWindow", "Znajomy od"))
        self.open_friend_library_button.setText(_translate("MainWindow", "Otwórz bibliotekę gier tego użytkownika"))
        self.friends_sort_by_name_combobox.setItemText(0, _translate("MainWindow", "Od A do Z"))
        self.friends_sort_by_name_combobox.setItemText(1, _translate("MainWindow", "Od Z do A"))
        self.friends_sort_by_birth_check.setText(_translate("MainWindow", "Data urodzenia"))
        self.friends_sort_by_birth_combobox.setItemText(0, _translate("MainWindow", "Rosnąco"))
        self.friends_sort_by_birth_combobox.setItemText(1, _translate("MainWindow", "Malejąco"))
        self.friends_sort_label.setText(_translate("MainWindow", "Sortowanie"))
        self.friends_sort_button.setText(_translate("MainWindow", "Posortuj"))
        self.friends_sort_by_name_check.setText(_translate("MainWindow", "Nazwa"))
        self.Tabs.setTabText(self.Tabs.indexOf(self.shop), _translate("MainWindow", "Sklep"))
        self.Tabs.setTabText(self.Tabs.indexOf(self.friends), _translate("MainWindow", "Znajomi"))
        self.Tabs.setTabText(self.Tabs.indexOf(self.library), _translate("MainWindow", "Biblioteka"))
        self.Tabs.setTabText(self.Tabs.indexOf(self.settings), _translate("MainWindow", "Moje konto"))
        self.shop_price_label.setText(_translate("MainWindow", "Cena"))
        self.shop_for_kids_label.setText(_translate("MainWindow", "Czy gra jest dla dzieci?"))
        self.shop_release_date_label.setText(_translate("MainWindow", "Data premiery"))
        self.shop_genre_label.setText(_translate("MainWindow", "Gatunek"))
        self.shop_author_label.setText(_translate("MainWindow", "Autor"))
        self.shop_platform_label.setText(_translate("MainWindow", "Platforma"))
        self.shop_description_label.setText(_translate("MainWindow", "Krótki opis"))
        self.shop_buy_game_button.setText(_translate("MainWindow", "Kup tę grę"))
        self.shop_filter_label.setText(_translate("MainWindow", "Filtracja"))
        self.shop_filter_by_price_check.setText(_translate("MainWindow", "Cena"))
        self.shop_filter_by_date_check.setText(_translate("MainWindow", "Data premiery"))
        self.shop_filter_by_name_check.setText(_translate("MainWindow", "Nazwa"))
        self.shop_filter_by_price_label_1.setText(_translate("MainWindow", "Od"))
        self.shop_filter_by_price_label_2.setText(_translate("MainWindow", "do"))
        self.shop_filter_by_date_input_1.setDisplayFormat(_translate("MainWindow", "dd-MM-yyyy"))
        self.shop_filter_by_date_label_1.setText(_translate("MainWindow", "Od"))
        self.shop_filter_by_date_label_2.setText(_translate("MainWindow", "do"))
        self.shop_filter_by_date_input_2.setDisplayFormat(_translate("MainWindow", "dd-MM-yyyy"))
        self.shop_filter_by_author_check.setText(_translate("MainWindow", "Autor"))
        self.shop_filter_by_for_kids_check.setText(_translate("MainWindow", "Gry tylko dla dzieci"))
        self.shop_filter_by_owning_check.setText(_translate("MainWindow", "Tylko nieposiadane gry"))
        self.shop_sort_by_name_combobox.setItemText(0, _translate("MainWindow", "Od A do Z"))
        self.shop_sort_by_name_combobox.setItemText(1, _translate("MainWindow", "Od Z do A"))
        self.shop_sort_by_price_check.setText(_translate("MainWindow", "Cena"))
        self.shop_sort_by_date_combobox.setItemText(0, _translate("MainWindow", "Rosnąco"))
        self.shop_sort_by_date_combobox.setItemText(1, _translate("MainWindow", "Malejąco"))
        self.shop_sort_by_date_check.setText(_translate("MainWindow", "Data premiery"))
        self.shop_sort_by_price_combobox.setItemText(0, _translate("MainWindow", "Rosnąco"))
        self.shop_sort_by_price_combobox.setItemText(1, _translate("MainWindow", "Malejąco"))
        self.shop_sort_label.setText(_translate("MainWindow", "Sortowanie"))
        self.shop_sort_by_name_check.setText(_translate("MainWindow", "Nazwa"))
        self.shop_filter_by_genre_check.setText(_translate("MainWindow", "Gatunek"))
        self.shop_filter_by_platform_label.setText(_translate("MainWindow", "Platforma"))
        self.shop_filter_by_platform_origin_check.setText(_translate("MainWindow", "Origin"))
        self.shop_filter_by_platform_steam_check.setText(_translate("MainWindow", "Steam"))
        self.shop_filter_by_platform_egc_check.setText(_translate("MainWindow", "Epic Game Store"))
        self.shop_filter_by_platform_uplay_check.setText(_translate("MainWindow", "Uplay"))
        self.shop_filter_by_platform_bethesda_check.setText(_translate("MainWindow", "Bethesda Launcher"))
        self.shop_filter_by_platform_gog_check.setText(_translate("MainWindow", "GOG"))
        self.shop_filter_by_platform_blizzard_check.setText(_translate("MainWindow", "Blizzard.net"))
        self.shop_filter_and_sort_button.setText(_translate("MainWindow", "Filtruj i sortuj"))
        self.library_price_label.setText(_translate("MainWindow", "Cena"))
        self.library_for_kids_label.setText(_translate("MainWindow", "Czy gra jest dla dzieci?"))
        self.library_release_date_label.setText(_translate("MainWindow", "Data premiery"))
        self.library_genre_label.setText(_translate("MainWindow", "Gatunek"))
        self.library_author_label.setText(_translate("MainWindow", "Autor"))
        self.library_platform_label.setText(_translate("MainWindow", "Platforma"))
        self.library_description_label.setText(_translate("MainWindow", "Krótki opis"))
        self.library_delete_game_button.setText(_translate("MainWindow", "Usuń tę grę"))
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
        self.settings_add_money_label.setText(_translate("MainWindow", "Doładuj konto"))
        self.settings_my_currency.setText(_translate("MainWindow", "PLN"))
        self.settings_change_currency_label.setText(_translate("MainWindow", "Zmień walutę twojego konta"))
        self.settings_add_money_button.setText(_translate("MainWindow", "Zatwierdź"))
        self.settings_change_currency_button.setText(_translate("MainWindow", "Zatwierdź"))
        self.settings_change_password_label.setText(_translate("MainWindow", "Zmień hasło"))
        self.settings_change_password_button.setText(_translate("MainWindow", "Zatwierdź"))
        self.settings_change_mail_button.setText(_translate("MainWindow", "Zatwierdź"))
        self.settings_change_mail_label.setText(_translate("MainWindow", "Zmień e-mail"))
        self.settings_change_password_old_label.setText(_translate("MainWindow", "Stare hasło"))
        self.settings_change_password_new_label.setText(_translate("MainWindow", "Nowe hasło"))
        self.settings_account_creation_label.setText(_translate("MainWindow", "Data utworzenia konta:"))
        self.settings_date_of_birth_label.setText(_translate("MainWindow", "Data twoich urodzin:"))
        self.settings_add_friend_label.setText(_translate("MainWindow", "Dodaj znajomego"))
        self.settings_add_friend_button.setText(_translate("MainWindow", "Zatwierdź"))
        self.log_out_button.setText(_translate("MainWindow", "Wyloguj"))
        self.wallet.setText(_translate("MainWindow", "Portfel"))

        self.username.setText(_translate("MainWindow", "{}".format(self.info[0])))
        self.wallet_amount.setText(_translate("MainWindow", "{}".format(self.info[1])))
        self.currency.setText(_translate("MainWindow", "{}".format(self.info[2])))
        self.settings_my_currency.setText(_translate("MainWindow", "{}".format(self.info[2])))
        self.settings_account_creation.setText(_translate("MainWindow", "{}".format(self.info[5])))
        self.settings_date_of_birth.setText(_translate("MainWindow", "{}".format(self.info[4])))

    @staticmethod
    def settings_success_change():
        msg = QMessageBox()
        msg.setWindowTitle("Potwierdzenie")
        msg.setText("Zmiany na twoim koncie zostały zatwierdzone!")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)

        x = msg.exec_()

    # pobiera podstawowe dane użytkownika który się zalogował
    def basic_info(self):
        try:
            self.conn = pg2.connect(host=self.db_host, database=self.db_name, user=self.db_user, password=self.db_psswd,
                                    port=self.db_port)
            c = self.conn.cursor()
            c.execute("""
                    SELECT u.username, u.amount, u.currency, c.value_in_pln, u.date_of_birth, u.account_creation
                    FROM users u
                    JOIN currencies c
                    ON c.name = u.currency
                    WHERE user_id = {};
            """.format(self.user_id))
            self.info = c.fetchone()
            c.close()
            self.conn.commit()
            self.conn.close()
        except pg2.errors.RaiseException:
            self.something_is_wrong(3)

    def complete_currencies(self):
        try:
            self.conn = pg2.connect(host=self.db_host, database=self.db_name, user=self.db_user, password=self.db_psswd,
                                    port=self.db_port)
            c = self.conn.cursor()
            c.execute("""
                    SELECT name
                    FROM currencies;
            """)
            currencies = c.fetchall()
            c.close()
            self.conn.commit()
            self.conn.close()

            for currency in currencies:
                self.settings_change_currency_combobox.addItem(currency[0])
        except pg2.errors.RaiseException:
            self.something_is_wrong(4)

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
                self.shop_filter_by_genre_combobox.addItem(genre[0])
                self.library_filter_by_genre_combobox.addItem(genre[0])
        except pg2.errors.RaiseException:
            self.something_is_wrong(5)

    # wylogowuje użytkownika i wraca na ekran logowania
    def log_out(self):
        from login import Ui_Login
        self.window_login_gui = QtWidgets.QMainWindow()
        self.login_gui = Ui_Login()
        self.login_gui.setupUi(self.window_login_gui)
        self.window_login_gui.show()
        self.window.close()

    def delete_friend(self):
        try:
            self.conn = pg2.connect(host=self.db_host, database=self.db_name, user=self.db_user, password=self.db_psswd,
                                    port=self.db_port)
            c = self.conn.cursor()
            c.execute("""
                    DELETE FROM friends
                    WHERE (user_1 = {} AND user_2 = {}) OR (user_1 = {} AND user_2 = {})
            """.format(self.user_id, self.current_friend_id, self.current_friend_id, self.user_id))
            c.close()
            self.conn.commit()
            self.conn.close()
            self.delete_friend_success()
            self.friends_list.clear()
            self.complete_friends_list()
        except pg2.errors.RaiseException:
            self.something_is_wrong(6)

    def delete_friend_success(self):
        msg = QMessageBox()
        msg.setWindowTitle("Potwierdzenie")
        msg.setText("Usunięto użytkownika {} z twojej listy znajomych".format(self.current_friend_name))
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)

        x = msg.exec_()

    def delete_game(self):
        try:
            self.conn = pg2.connect(host=self.db_host, database=self.db_name, user=self.db_user, password=self.db_psswd,
                                    port=self.db_port)
            c = self.conn.cursor()
            c.execute("""
                    DELETE FROM users_games
                    WHERE user_id = {} AND gp_id = {};
            """.format(self.user_id, self.current_game.gp_id))
            c.close()
            self.conn.commit()
            self.conn.close()
            self.delete_game_success()
            self.library_lists[self.library_current_page].clear()
            self.complete_library_list()
            self.shop_lists[self.shop_current_page].clear()
            self.complete_shop_list()
        except pg2.errors.RaiseException:
            self.something_is_wrong(7)

    def delete_game_success(self):
        msg = QMessageBox()
        msg.setWindowTitle("Potwierdzenie")
        msg.setText("Usunięto grę {} z twojej biblioteki".format(self.current_game.name))
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)

        x = msg.exec_()

    def add_friend(self):
        friend = self.settings_add_friend_input.text()

        if friend == '':
            return

        _translate = QtCore.QCoreApplication.translate
        try:
            self.conn = pg2.connect(host=self.db_host, database=self.db_name, user=self.db_user, password=self.db_psswd,
                                    port=self.db_port)
            c = self.conn.cursor()
            c.execute("""
                    SELECT user_id 
                    FROM users 
                    WHERE username = '{}'
            """)
            friend_id = c.fetchone()
            friend_id = friend_id if friend_id is None else friend_id[0]
            c.close()
            self.conn.commit()
            if friend_id is not None:
                c = self.conn.cursor()
                c.execute("""
                        INSERT INTO friends (user_1, user_2, since)
                        VALUES ({}, {}, CURRENT_DATE)
                """.format(self.user_id, friend_id))
                c.close()
                self.conn.commit()
                self.conn.close()
                self.settings_add_friend_input.setText(_translate("MainWindow", ""))
                self.friends_list.clear()
                self.complete_friends_list()
            else:
                self.conn.close()
                self.settings_add_friend_input.setText(_translate("MainWindow", ""))
                self.add_friend_error(friend)
        except pg2.errors.RaiseException:
            self.add_friend_error(friend)

    @staticmethod
    def add_friend_success(friend):
        msg = QMessageBox()
        msg.setWindowTitle("Potwierdzenie")
        msg.setText("Dodano użytkownika {} do listy znajomych".format(friend))
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)

        x = msg.exec_()

    @staticmethod
    def add_friend_error(friend):
        msg = QMessageBox()
        msg.setWindowTitle("Potwierdzenie")
        msg.setText("Uzytkownik {} nie korzysta z tej biblioteki".format(friend))
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Ok)

        x = msg.exec_()

    def add_money(self):
        money = self.settings_add_money_input.text()

        if money == '':
            return

        _translate = QtCore.QCoreApplication.translate
        try:
            self.conn = pg2.connect(host=self.db_host, database=self.db_name, user=self.db_user, password=self.db_psswd,
                                    port=self.db_port)
            c = self.conn.cursor()
            c.execute("""
                    UPDATE users
                    SET amount = amount + {}
                    WHERE user_id = {};
            """.format(int(money), self.user_id))
            c.close()
            self.conn.commit()
            self.conn.close()

            self.basic_info()
            self.settings_success_change()
            self.wallet_amount.setText(_translate("MainWindow", "{}".format(self.info[1])))
            self.settings_add_money_input.setText(_translate("MainWindow", ""))
        except pg2.errors.RaiseException:
            self.something_is_wrong(8)

    def change_password(self):
        if self.settings_change_password_old_input.text() == '' and self.settings_change_password_new_input.text() == '':
            return

        _translate = QtCore.QCoreApplication.translate

        self.conn = pg2.connect(host=self.db_host, database=self.db_name, user=self.db_user, password=self.db_psswd,
                                port=self.db_port)
        c = self.conn.cursor()
        c.execute("""
                SELECT psswd
                FROM users
                WHERE user_id = {};
        """.format(self.user_id))
        psswd = c.fetchone()
        c.close()
        self.conn.commit()
        self.conn.close()

        if psswd[0] == self.settings_change_password_old_input.text():
            self.conn = pg2.connect(host=self.db_host, database=self.db_name, user=self.db_user, password=self.db_psswd,
                                    port=self.db_port)
            c = self.conn.cursor()
            c.execute("""
                UPDATE users
                SET psswd = '{}'
                WHERE user_id = {};
            """.format(self.settings_change_password_new_input.text(), self.user_id))
            c.close()
            self.conn.commit()
            self.conn.close()
            self.settings_success_change()
        else:
            self.change_password_error_msg()

        self.settings_change_password_old_input.setText(_translate("MainWindow", ""))
        self.settings_change_password_new_input.setText(_translate("MainWindow", ""))

    @staticmethod
    def change_password_error_msg():
        msg = QMessageBox()
        msg.setWindowTitle("Błąd zmiany hasła")
        msg.setText("Obecne hasło się nie zgadza")
        msg.setIcon(QMessageBox.Critical)
        msg.setStandardButtons(QMessageBox.Close)

        x = msg.exec_()

    def change_mail(self):
        if self.settings_change_mail_input.text() == '':
            return

        _translate = QtCore.QCoreApplication.translate
        try:
            self.conn = pg2.connect(host=self.db_host, database=self.db_name, user=self.db_user, password=self.db_psswd,
                                    port=self.db_port)
            c = self.conn.cursor()
            c.execute("""
                    UPDATE users
                    SET email = '{}'
                    WHERE user_id = {};
            """.format(self.settings_change_mail_input.text(), self.user_id))
            c.close()
            self.conn.commit()
            self.conn.close()

            self.settings_success_change()
            self.settings_change_mail_input.setText(_translate("MainWindow", ""))
        except pg2.errors.RaiseException:
            self.something_is_wrong(9)

    def settings_set_currency_value(self):
        _translate = QtCore.QCoreApplication.translate
        try:
            self.conn = pg2.connect(host=self.db_host, database=self.db_name, user=self.db_user, password=self.db_psswd,
                                    port=self.db_port)
            c = self.conn.cursor()
            c.execute("""
                    SELECT value_in_pln
                    FROM currencies
                    WHERE name = '{}';
            """.format(self.settings_change_currency_combobox.currentText()))
            value = c.fetchone()[0]
            c.close()
            self.conn.commit()
            self.conn.close()

            self.settings_currency_value_label.setText(_translate("MainWindow", "1 {} = {} {}".format(
                self.info[2], round(float(value)/float(self.info[3]), 4), self.settings_change_currency_combobox.currentText()
            )))
        except pg2.errors.RaiseException:
            self.something_is_wrong(10)

    # uzupełnia listę znajomych
    def complete_friends_list(self):
        name_order = ''
        birth_order = ''
        if self.friends_sort_by_name_check.isChecked():
            name_order = 'u.username'
            if self.friends_sort_by_name_combobox.currentIndex() == 0:
                name_order += ' ASC'
            else:
                name_order += ' DESC'
        if self.friends_sort_by_birth_check.isChecked():
            birth_order = 'u.date_of_birth'
            if self.friends_sort_by_birth_combobox.currentIndex() == 0:
                birth_order += ' ASC'
            else:
                birth_order += ' DESC'
        try:
            self.conn = pg2.connect(host=self.db_host, database=self.db_name, user=self.db_user, password=self.db_psswd,
                                    port=self.db_port)
            c = self.conn.cursor()
            c.execute("""
                    DROP VIEW users_id;
                    CREATE VIEW users_id AS (
                    SELECT user_1 FROM friends WHERE user_2 = {}
                    UNION
                    SELECT user_2 FROM friends WHERE user_1 = {});
                    SELECT * FROM users_id ORDER BY user_1 ASC;
            """.format(self.user_id, self.user_id))
            friends = c.fetchall()
            c.close()
            self.conn.commit()

            users_id_vector = ''
            for user in friends:
                users_id_vector += str(user[0]) + ', '
            users_id_vector = users_id_vector[0:len(users_id_vector)-2]
            c = self.conn.cursor()
            c.execute("""
                    SELECT u.username, u.user_id, ROW_NUMBER() OVER(ORDER BY {}{}) AS number
                    FROM users u
                    WHERE u.user_id IN ({}) 
                    ORDER BY number ASC;
            """.format(birth_order if name_order == '' or birth_order == '' else birth_order + ', ',
                       name_order,
                       users_id_vector))
            usernames = c.fetchall()
            c.close()
            self.conn.commit()
            self.conn.close()

            for friend in enumerate(friends):
                current_friend = FriendsListItem(friend[1][0], usernames[friend[0]][1])
                current_friend.username = usernames[friend[0]][0]
                item = QtWidgets.QListWidgetItem(current_friend.username)
                item.setData(QtCore.Qt.UserRole, current_friend)
                self.friends_list.insertItem(friend[0], item)

            if self.friends_list.count() > 0:
                curr_item = self.friends_list.item(0)
                self.friends_list.setCurrentItem(curr_item)
        except pg2.errors.RaiseException:
            self.something_is_wrong(11)

    def sort_friends_list(self):
        if not self.friends_sort_by_name_check.isChecked() and not self.friends_sort_by_birth_check.isChecked():
            self.friends_sort_by_name_check.setChecked(True)
        self.friends_list.clear()
        self.complete_friends_list()

    # uzupełnia listę sklepu na obecnej stronie
    def complete_shop_list(self):
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
        owning_where = ''
        if self.shop_sort_by_name_check.isChecked():
            name_order = 'g.name'
            if self.shop_sort_by_name_combobox.currentIndex() == 0:
                name_order += ' ASC'
            else:
                name_order += ' DESC'
        if self.shop_sort_by_price_check.isChecked():
            price_order = 'gp.price'
            if self.shop_sort_by_price_combobox.currentIndex() == 0:
                price_order += ' ASC'
            else:
                price_order += ' DESC'
        if self.shop_sort_by_date_check.isChecked():
            date_order = 'gp.release_date'
            if self.shop_sort_by_date_combobox.currentIndex() == 0:
                date_order += ' ASC'
            else:
                date_order += ' DESC'
        if self.shop_filter_by_name_check.isChecked():
            name_where = self.shop_filter_by_name_input.text()
        if self.shop_filter_by_price_check.isChecked():
            price_where_1 = self.shop_filter_by_price_input_1.text()
            price_where_2 = self.shop_filter_by_price_input_2.text()
            price_where_1 = price_where_1 if not price_where_1 == '' else '0'
            price_where_2 = price_where_2 if not price_where_2 == '' else '999999'
            price_where = 'AND gp.price >= {} AND gp.price <= {}'.format(
                float(price_where_1)*float(self.info[3]), float(price_where_2)*float(self.info[3]))
        if self.shop_filter_by_date_check.isChecked():
            date_where_1 = self.shop_filter_by_date_input_1.text()
            date_where_2 = self.shop_filter_by_date_input_2.text()
            date_where = "AND gp.release_date >= '{}' AND gp.release_date <= '{}'".format(date_where_1, date_where_2)
        if self.shop_filter_by_author_check.isChecked():
            author_where = "AND g.author LIKE '%{}%'".format(self.shop_filter_by_author_input.text())
        if self.shop_filter_by_for_kids_check.isChecked():
            for_kids_where = "AND g.for_kids = 'True'"
        if self.shop_filter_by_genre_check.isChecked():
            genre_where = "AND g.genre = '{}'".format(self.shop_filter_by_genre_combobox.currentText())
        if self.shop_filter_by_platform_bethesda_check.isChecked() or \
                self.shop_filter_by_platform_blizzard_check.isChecked() or \
                self.shop_filter_by_platform_egc_check.isChecked() or \
                self.shop_filter_by_platform_gog_check.isChecked() or \
                self.shop_filter_by_platform_origin_check.isChecked() or \
                self.shop_filter_by_platform_steam_check.isChecked() or \
                self.shop_filter_by_platform_uplay_check.isChecked():
                    platform_where = "AND gp.plat_id IN ("
        if self.shop_filter_by_platform_uplay_check.isChecked():
            platform_where += "3, "
        if self.shop_filter_by_platform_steam_check.isChecked():
            platform_where += "1, "
        if self.shop_filter_by_platform_origin_check.isChecked():
            platform_where += "2, "
        if self.shop_filter_by_platform_gog_check.isChecked():
            platform_where += "5, "
        if self.shop_filter_by_platform_egc_check.isChecked():
            platform_where += "4, "
        if self.shop_filter_by_platform_blizzard_check.isChecked():
            platform_where += "6, "
        if self.shop_filter_by_platform_bethesda_check.isChecked():
            platform_where += "7, "
        if self.shop_filter_by_platform_bethesda_check.isChecked() or \
                self.shop_filter_by_platform_blizzard_check.isChecked() or \
                self.shop_filter_by_platform_egc_check.isChecked() or \
                self.shop_filter_by_platform_gog_check.isChecked() or \
                self.shop_filter_by_platform_origin_check.isChecked() or \
                self.shop_filter_by_platform_steam_check.isChecked() or \
                self.shop_filter_by_platform_uplay_check.isChecked():
                    platform_where = platform_where[0:len(platform_where)-2]
                    platform_where += ")"
        if self.shop_filter_by_owning_check.isChecked():
            owning_where += "AND gp.gp_id NOT IN (SELECT gp_id FROM users_games WHERE user_id = {})".format(self.user_id)
        try:
            self.conn = pg2.connect(host=self.db_host, database=self.db_name, user=self.db_user, password=self.db_psswd,
                                    port=self.db_port)
            c = self.conn.cursor()
            c.execute("""
                    DROP VIEW shop_games;
                    
                    CREATE VIEW shop_games AS
                    (SELECT g.game_id, g.name, ROW_NUMBER() OVER(ORDER BY {}{}{}) AS number
                    FROM games g
                    JOIN games_platforms gp
                    ON g.game_id = gp.game_id
                    WHERE g.name LIKE '%{}%' {}{}{}{}{}{}{});
            """.format(date_order if date_order == '' or (name_order == '' and price_order == '')
                                         else date_order + ',',
                       price_order if price_order == '' or name_order == '' else price_order + ',',
                       name_order,
                       name_where,
                       price_where,
                       date_where,
                       author_where,
                       for_kids_where,
                       genre_where,
                       platform_where,
                       owning_where))
            c.close()
            self.conn.commit()

            c = self.conn.cursor()
            c.execute("""
                    SELECT game_id, name
                    FROM shop_games
                    WHERE number >= {} AND number <= {};
            """.format(30*self.shop_current_page + 1, 30*(self.shop_current_page + 1)))
            games = c.fetchall()
            self.conn.close()

            for game in enumerate(games):
                current_game = GameListItem(self.user_id, my_id=game[1][0])
                current_game.name = game[1][1]
                item = QtWidgets.QListWidgetItem(current_game.name)
                item.setData(QtCore.Qt.UserRole, current_game)
                self.shop_lists[self.shop_current_page].insertItem(game[0], item)

            curr_item = self.shop_lists[self.shop_current_page].item(0)
            self.shop_lists[self.shop_current_page].setCurrentItem(curr_item)
        except pg2.errors.RaiseException:
            self.something_is_wrong(12)

    #Autor kodu: Bartosz Zimończyk i Denis Syrkiewicz
    def filter_and_sort_shop_list(self):
        if not self.shop_sort_by_name_check.isChecked() and not self.shop_sort_by_date_check.isChecked() and \
            not self.shop_sort_by_price_check.isChecked():
                self.shop_sort_by_name_check.setChecked(True)
        self.shop_lists[self.shop_current_page].clear()
        self.shop_current_page = 0
        self.stacked_shop.setCurrentIndex(self.shop_current_page)
        self.complete_shop_list()

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
            price_where_1 = price_where_1 if not price_where_1 == '' else '0'
            price_where_2 = price_where_2 if not price_where_2 == '' else '999999'
            price_where = 'AND gp.price >= {} AND gp.price <= {}'.format(
                float(price_where_1) * float(self.info[3]), float(price_where_2) * float(self.info[3]))
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
                    DROP VIEW library_games;
                    
                    CREATE VIEW library_games AS(
                    SELECT ug.user_id, g.game_id, g.name, ROW_NUMBER() OVER(ORDER BY {}{}{}) AS number
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
                       self.user_id,
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
                    FROM library_games
                    WHERE number >= {} AND number <= {};
            """.format(30*self.library_current_page + 1, 30*(self.library_current_page + 1), self.user_id))
            games = c.fetchall()
            c.close()
            self.conn.commit()
            self.conn.close()

            for game in enumerate(games):
                current_game = GameListItem(self.user_id, my_id=game[1][0])
                current_game.name = game[1][1]
                item = QtWidgets.QListWidgetItem(current_game.name)
                item.setData(QtCore.Qt.UserRole, current_game)
                self.library_lists[self.library_current_page].insertItem(game[0], item)

            if self.library_lists[self.library_current_page].count() > 0:
                curr_item = self.library_lists[self.library_current_page].item(0)
                self.library_lists[self.library_current_page].setCurrentItem(curr_item)
        except pg2.errors.RaiseException:
            self.something_is_wrong(13)

    def filter_and_sort_library_list(self):
        if not self.library_sort_by_name_check.isChecked() and not self.library_sort_by_date_check.isChecked() and \
            not self.library_sort_by_price_check.isChecked():
                self.library_sort_by_name_check.setChecked(True)
        self.library_lists[self.library_current_page].clear()
        self.library_current_page = 0
        self.stacked_library.setCurrentIndex(self.library_current_page)
        self.complete_library_list()

    # funkcja przycisku otwierającego bibliotekę znajomego
    def open_friend_library(self):
        self.window_friend_library = QtWidgets.QMainWindow()
        self.friend_library = Ui_LibraryFriend(self.current_friend_id, self.current_friend_name, self.info[2])
        self.friend_library.setupUi(self.window_friend_library)
        self.window_friend_library.show()

    def buy_game(self):
        _translate = QtCore.QCoreApplication.translate
        self.conn = pg2.connect(host=self.db_host, database=self.db_name, user=self.db_user, password=self.db_psswd,
                                port=self.db_port)
        c = self.conn.cursor()
        try:
            c.execute("""
                    INSERT INTO transactions (user_id, amount, currency, gp_id)
                    VALUES ({}, {}, '{}', {});
            """.format(self.user_id, self.current_game.price, self.info[2], self.current_game.gp_id))
            c.close()
            self.conn.commit()
            self.conn.close()
            self.basic_info()
            self.wallet_amount.setText(_translate("MainWindow", "{}".format(self.info[1])))
            self.buy_game_success()
            self.selection_in_shop_own_game()
            self.disable_buy_game()
            self.library_lists[self.library_current_page].clear()
            self.complete_library_list()
        except pg2.errors.RaiseException:
            self.buy_game_error_msg()

    @staticmethod
    def buy_game_success():
        msg = QMessageBox()
        msg.setWindowTitle("Potwierdzenie")
        msg.setText("Gra została zakupiona!")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)

        x = msg.exec_()

    @staticmethod
    def buy_game_error_msg():
        msg = QMessageBox()
        msg.setWindowTitle("Błąd zakupu gry")
        msg.setText("Podczas zakupu wystąpił błąd!")
        msg.setIcon(QMessageBox.Critical)
        msg.setStandardButtons(QMessageBox.Close)

        x = msg.exec_()

    def disable_buy_game(self):
        self.shop_buy_game_button.setEnabled(not self.current_game.do_user_own_this())

    def change_currency(self, arg=None):
        if arg is not None:
            _translate = QtCore.QCoreApplication.translate
            currency = str(self.settings_change_currency_combobox.currentText())
            try:
                self.conn = pg2.connect(host=self.db_host, database=self.db_name, user=self.db_user, password=self.db_psswd,
                                        port=self.db_port)
                c = self.conn.cursor()
                c.execute("""
                        SELECT value_in_pln
                        FROM currencies
                        WHERE name = '{}'
                """.format(currency))
                value = c.fetchone()
                c.close()
                self.conn.commit()
                self.conn.close()

                self.conn = pg2.connect(host=self.db_host, database=self.db_name, user=self.db_user, password=self.db_psswd,
                                        port=self.db_port)
                c = self.conn.cursor()
                c.execute("""
                        UPDATE users
                        SET currency = '{}', amount = amount * {} * {}
                        WHERE user_id = {};
                """.format(currency, float(value[0]), 1/float(self.info[3]), self.user_id))
                c.close()
                self.conn.commit()
                self.conn.close()

                self.basic_info()
                self.settings_success_change()
                self.currency.setText(_translate("MainWindow", "{}".format(self.info[2])))
                self.wallet_amount.setText(_translate("MainWindow", "{}".format(self.info[1])))
                self.settings_my_currency.setText(_translate("MainWindow", "{}".format(self.info[2])))
                self.shop_lists[self.shop_current_page].clear()
                self.complete_shop_list()
                self.settings_set_currency_value()
            except pg2.errors.RaiseException:
                self.something_is_wrong(14)

    # funkcja która wyświetla dane znajomego
    def selection_in_friends(self, arg=None):
        if arg is not None:
            myObject = arg.data(QtCore.Qt.UserRole)
            _translate = QtCore.QCoreApplication.translate
            myObject.get_info()
            self.current_friend_id = myObject.my_id
            self.current_friend_name = myObject.username
            self.friends_birth_date.setText(_translate("MainWindow", "{}".format(myObject.date_of_birth)))
            self.friends_creation_date.setText(_translate("MainWindow", "{}".format(myObject.account_creation)))
            self.friends_username.setText(_translate("MainWindow", "{}".format(myObject.username)))
            self.friends_since_date.setText(_translate("MainWindow", "{}".format(myObject.since_date)))

    # funkcja która wyświetla dane gry ze sklepu
    def selection_in_shop(self, arg=None):
        if arg is not None:
            myObject = arg.data(QtCore.Qt.UserRole)
            _translate = QtCore.QCoreApplication.translate
            myObject.get_info()
            self.current_game = myObject
            self.shop_current_game_name.setText(_translate("MainWindow", "{}".format(myObject.name)))
            self.shop_current_game_author.setText(_translate("MainWindow", "{}".format(myObject.author)))
            self.shop_current_game_price.setText(
                _translate("MainWindow", "{} {}".format(round(float(myObject.price)/float(self.info[3]), 2),
                                                        self.info[2])))
            self.shop_current_game_genre.setText(_translate("MainWindow", "{}".format(myObject.genre)))
            self.shop_current_game_for_kids.setText(_translate("MainWindow", "{}".format(myObject.for_kids)))
            self.shop_current_game_release_date.setText(_translate("MainWindow", "{}".format(myObject.release_date)))
            self.shop_current_game_platform.setText(_translate("MainWindow", "{}".format(myObject.platform)))
            self.shop_current_game_description.setText(_translate("MainWindow", "{}".format(myObject.description)))
            self.selection_in_shop_own_game()
            self.disable_buy_game()

    def selection_in_shop_own_game(self):
        _translate = QtCore.QCoreApplication.translate
        if not self.current_game.do_user_own_this():
            self.shop_owning_game_label.setText(_translate("MainWindow", "Nie posiadasz tej gry"))
        else:
            self.shop_owning_game_label.setText(_translate("MainWindow", "Posiadasz tę grę"))

    # funkcja która wyświetla dane gry z biblioteki
    def selection_in_library(self, arg=None):
        if arg is not None:
            myObject = arg.data(QtCore.Qt.UserRole)
            _translate = QtCore.QCoreApplication.translate
            myObject.get_info()
            self.current_game = myObject
            self.library_current_game_name.setText(_translate("MainWindow", "{}".format(myObject.name)))
            self.library_current_game_author.setText(_translate("MainWindow", "{}".format(myObject.author)))
            self.library_current_game_price.setText(
                _translate("MainWindow", "{} {}".format(round(float(myObject.price)/float(self.info[3]), 2),
                                                        self.info[2])))
            self.library_current_game_genre.setText(_translate("MainWindow", "{}".format(myObject.genre)))
            self.library_current_game_for_kids.setText(_translate("MainWindow", "{}".format(myObject.for_kids)))
            self.library_current_game_release_date.setText(_translate("MainWindow", "{}".format(myObject.release_date)))
            self.library_current_game_platform.setText(_translate("MainWindow", "{}".format(myObject.platform)))
            self.library_current_game_description.setText(_translate("MainWindow", "{}".format(myObject.description)))

    @staticmethod
    def something_is_wrong(number):
        msg = QMessageBox()
        msg.setWindowTitle("Błąd")
        msg.setText("Coś poszło nie tak :( \n Numer błędu: {}".format(number))
        msg.setIcon(QMessageBox.Critical)
        msg.setStandardButtons(QMessageBox.Abort)

        x = msg.exec_()


if __name__ == "__main__":
    ap = QtWidgets.QApplication(sys.argv)
    UserGui = QtWidgets.QMainWindow()
    uii = Ui_UserGui(162)
    uii.setupUi(UserGui)
    UserGui.show()
    sys.exit(ap.exec_())








































