from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets
import csv
import getpass as gt
from PyQt5 import QtWidgets
import sys

icon = r'C:\Users\azlotnik\PycharmProjects\dutgui\chipgui.png'

# *****************************************************************************************


PATH = r'C:\Users\azlotnik\OneDrive - Qualcomm\Desktop\pte_dut_database.csv'
DELETED_PATH = r'C:\Users\azlotnik\OneDrive - Qualcomm\Desktop\deleted_dut_database.csv'
UPDATED_PATH = r'C:\Users\azlotnik\OneDrive - Qualcomm\Desktop\updated_dut_database.csv'
# PATH = r'\\filer4\Public\zlal\pte_dut_database.csv'
# DELETED_PATH = r'\\filer4\Public\zlal\deleted_dut_database.csv'
rows = []
headers = ['dut_id', 'dut_type', 'revision', 'condition', 'location', 'info']
empty_result = ['', '', '', '', '', '']
empty_type_result = [['', '', '', '', '', '']]


# read file
def read_file():
    with open(PATH, 'r', encoding='utf-8-sig') as file:
        csvreader = csv.reader(file)
        header = next(csvreader)
        rows.extend(iter(csvreader))


# fill data when opening file
read_file()


# result to search by id
def search_by_id(serial):
    for row in rows:
        if serial == row[0]:
            return row
    return empty_result


# search all data
def search_all():
    return list(rows)


# refresh data
def refresh():
    global rows
    rows = []
    read_file()


# search by type result
def search_by_type(types):
    res = [row for row in rows if types.lower() == row[1].lower()]
    return res or empty_type_result


# search by revision
def revision_search(rev):
    res = [row for row in rows if rev.lower() == row[2].lower()]
    return res or empty_type_result


# search by condition
def condition_search(cond):
    res = [row for row in rows if cond.lower() == row[3].lower()]
    return res or empty_type_result


# search by location
def location_search(loc):
    res = [row for row in rows if loc.lower() == row[4].lower()]
    return res or empty_type_result


# write new dut in the end of file
def update_new_dut(up_data):
    with open(PATH, 'a+', encoding='utf-8-sig', newline='') as updated_file:
        writer = csv.writer(updated_file)
        writer.writerow(up_data)


def update_dut_info(info):
    for row in range(len(rows)):
        if rows[row][0] == info[0]:
            rows[row] = info
    with open(PATH, 'w', encoding='utf-8-sig', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        writer.writerows(rows)


# Check if dut already in database
def existed_dut(num):
    for r in rows:
        if num == r[0]:
            return True


# Check if dut not in database
def not_existed_dut(num):
    flag = any(num == r[0] for r in rows)
    return not flag


# delete selected dut from database
def delete_selected_dut(dut_num):
    for row_num in range(len(rows)):
        if rows[row_num][0] == dut_num:
            try:
                deleted_dut = rows.pop(row_num) + [gt.getuser()]
                with open(PATH, 'w', encoding='utf-8-sig', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(headers)
                    writer.writerows(rows)
                with open(DELETED_PATH, 'a+', encoding='utf-8-sig', newline='') as updated_file:
                    writer = csv.writer(updated_file)
                    writer.writerow(deleted_dut)
                return True
            except:
                return False


# *****************************************************************************************
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("DUT Database by Alex&Roman")
        MainWindow.setFixedHeight(930)
        MainWindow.setFixedWidth(785)
        # MainWindow.resize(785, 930)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 10, 751, 331))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        # Condition combo box
        cond_list = ['', 'Good', 'Problematic', 'Bad']
        self.condition_box = QtWidgets.QComboBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.condition_box.setFont(font)
        self.condition_box.setObjectName("conditionBox")
        self.condition_box.addItems(cond_list)
        self.gridLayout.addWidget(self.condition_box, 2, 1, 1, 1)

        # Info text line
        self.info_text = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.info_text.sizePolicy().hasHeightForWidth())
        self.info_text.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.info_text.setFont(font)
        self.info_text.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.info_text, 5, 1, 1, 2)

        # Clear button
        self.clear_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.clear_button.setFont(font)
        self.clear_button.setObjectName("pushButton")
        self.gridLayout.addWidget(self.clear_button, 6, 0, 1, 1)

        # Show all button
        self.show_all_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.show_all_button.setFont(font)
        self.show_all_button.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.show_all_button, 6, 2, 1, 1)

        # Refresh button
        self.refresh_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.refresh_button.setFont(font)
        self.refresh_button.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.refresh_button, 6, 1, 1, 1)

        # Dut id text
        self.id_text = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.id_text.sizePolicy().hasHeightForWidth())
        self.id_text.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.id_text.setFont(font)
        self.id_text.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.id_text, 0, 1, 1, 1)

        # Info label
        self.info_label = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.info_label.sizePolicy().hasHeightForWidth())
        self.info_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.info_label.setFont(font)
        self.info_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.info_label.setObjectName("label")
        self.gridLayout.addWidget(self.info_label, 5, 0, 1, 1)

        # status label
        self.status_label = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.status_label.sizePolicy().hasHeightForWidth())
        self.status_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.status_label.setFont(font)
        self.status_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.status_label.setObjectName("status")
        self.gridLayout.addWidget(self.status_label, 0, 2, 1, 1)

        # Update DUT info button
        self.update_info_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.update_info_button.setFont(font)
        self.update_info_button.setObjectName("pushButton_12")
        self.gridLayout.addWidget(self.update_info_button, 5, 3, 1, 1)

        # Create new DUT button
        self.create_new_dut_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.create_new_dut_button.setFont(font)
        self.create_new_dut_button.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.create_new_dut_button, 0, 3, 1, 1)

        # Revision text line
        revisions = ['None', 'A', "B", 'C', 'D', 'E', "F", 'G', 'H', 'I', 'J', 'K', 'Other']
        self.rev_box = QtWidgets.QComboBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rev_box.setFont(font)
        self.rev_box.setObjectName("revBox")
        self.rev_box.addItems(revisions)
        self.gridLayout.addWidget(self.rev_box, 3, 1, 1, 1)

        # DUT ID button
        self.dut_id_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dut_id_button.setFont(font)
        self.dut_id_button.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.dut_id_button, 0, 0, 1, 1)

        # Type combo box
        corners_types = ['None', 'NN/TT', 'FF1p5', 'FF3p0', 'SS1p5', 'SS3p0']
        self.type_box = QtWidgets.QComboBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.type_box.setFont(font)
        self.type_box.setObjectName("comboBox")
        self.type_box.addItems(corners_types)
        self.gridLayout.addWidget(self.type_box, 1, 1, 1, 1)

        # Type button
        self.type_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.type_button.setFont(font)
        self.type_button.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.type_button, 1, 0, 1, 1)

        # Revision button
        self.rev_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rev_button.setFont(font)
        self.rev_button.setObjectName("pushButton_10")
        self.gridLayout.addWidget(self.rev_button, 3, 0, 1, 1)

        # Location combo box
        locations = ['', 'LAB 054', 'LAB 1160', 'RFALAB-2000', 'RFALAB-2001', 'RFALAB-2002', 'RFALAB-2003',
                     'RFALAB-2004', 'RFALAB-2005', 'RFALAB-2006', 'RFALAB-2009', 'RFALAB-2010', 'Soldering Station 054',
                     "Monica's cubic", 'Unknown']
        self.location_box = QtWidgets.QComboBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.location_box.setFont(font)
        self.location_box.setObjectName("comboBox_3")
        self.location_box.addItems(locations)
        self.gridLayout.addWidget(self.location_box, 4, 1, 1, 1)

        # Update dut button
        self.update_dut_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.update_dut_button.sizePolicy().hasHeightForWidth())
        self.update_dut_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.update_dut_button.setFont(font)
        self.update_dut_button.setObjectName("pushButton_11")
        self.gridLayout.addWidget(self.update_dut_button, 6, 3)

        # condition button search
        self.condition_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.condition_button.setFont(font)
        self.condition_button.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.condition_button, 2, 0, 1, 1)

        # location button search
        self.location_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.location_button.setFont(font)
        self.location_button.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.location_button, 4, 0, 1, 1)

        # delete dut button
        self.delete_dut_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.delete_dut_button.setFont(font)
        self.delete_dut_button.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.delete_dut_button, 1, 3, 1, 1)

        # Table
        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(20, 350, 751, 551))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.table.setFont(font)
        self.table.setObjectName("tableWidget")
        self.table.setColumnCount(0)
        self.table.setRowCount(0)
        self.table.setColumnCount(6)
        self.table.setRowCount(0)
        self.table.setSortingEnabled(True)
        self.table.setEditTriggers(QtWidgets.QTableWidget.EditTrigger.NoEditTriggers)
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.table.horizontalHeader().setStretchLastSection(True)
        table_headers = ['ID', 'Type', 'Revision', 'Condition', 'Location', 'Info']
        self.table.setHorizontalHeaderLabels(table_headers)
        row_num = self.table.rowCount()

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 785, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow",
                                             "DUT Database                                                                                                                                        by Alex&Roman"))
        MainWindow.setWindowIcon(QtGui.QIcon(icon))
        self.clear_button.setText(_translate("MainWindow", "Clear"))
        self.show_all_button.setText(_translate("MainWindow", "Show All"))
        self.refresh_button.setText(_translate("MainWindow", "Refresh"))
        self.info_label.setText(_translate("MainWindow", "Info"))
        self.status_label.setText(_translate("MainWindow", ""))
        self.update_info_button.setText(_translate("MainWindow", "Update Info"))
        self.create_new_dut_button.setText(_translate("MainWindow", "Create New DUT"))
        self.dut_id_button.setText(_translate("MainWindow", "DUT ID"))
        self.type_button.setText(_translate("MainWindow", "Type"))
        self.rev_button.setText(_translate("MainWindow", "Revision"))
        # self.update_loc_button.setText(_translate("MainWindow", "Update Location"))
        self.update_dut_button.setText(_translate("MainWindow", "Update DUT"))
        self.condition_button.setText(_translate("MainWindow", "Condition"))
        self.location_button.setText(_translate("MainWindow", "Location"))
        self.delete_dut_button.setText(_translate("MainWindow", "Delete DUT"))

    # Show all data in table
    def show_all_data(self):
        self.table.setSortingEnabled(False)
        self.table.setRowCount(0)
        res = search_all()
        for result in range(len(res)):
            row_position = self.table.rowCount()
            self.table.insertRow(row_position)
            for col in range(6):
                new_item = QTableWidgetItem(res[result][col])
                self.table.setItem(row_position, col, new_item)
                new_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.table.resizeRowsToContents()
        self.status_label.setText('All Data Shown')
        self.table.setSortingEnabled(True)

    # Clear screen
    def clear_screen(self):
        self.table.setSortingEnabled(False)
        self.table.setRowCount(0)
        self.id_text.setText('')
        self.type_box.setCurrentText('None')
        self.condition_box.setCurrentText('')
        self.location_box.setCurrentText('')
        self.rev_box.setCurrentText('None')
        self.info_text.setText('')
        self.status_label.setText('Cleared')
        self.table.setSortingEnabled(True)

    # Refresh data in table
    def refresh_data(self):
        self.table.setSortingEnabled(False)
        refresh()
        self.show_all_data()
        self.status_label.setText('Refreshed')
        self.table.setSortingEnabled(True)

    # Search functions

    # Search by ID
    def id_search(self):
        self.table.setSortingEnabled(False)
        self.table.setRowCount(0)
        row_position = self.table.rowCount()
        id_num = self.id_text.text()
        res = search_by_id(id_num)
        self.type_box.setCurrentText(res[1])
        self.rev_box.setCurrentText(res[2])
        self.condition_box.setCurrentText(res[3])
        self.location_box.setCurrentText(res[4])
        self.info_text.setText(res[5])
        self.table.insertRow(row_position)
        for cell in range(len(res)):
            new_item = QTableWidgetItem(res[cell])
            self.table.setItem(row_position, cell, new_item)
            new_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        self.table.resizeRowsToContents()
        self.status_label.setText('Search finished')
        self.table.setSortingEnabled(True)

    # Search by type
    def type_search(self):
        self.table.setSortingEnabled(False)
        self.table.setRowCount(0)
        type_id = self.type_box.currentText()
        res = search_by_type(type_id)
        if len(res) > 0:
            for result in range(len(res)):
                row_position = self.table.rowCount()
                self.table.insertRow(row_position)
                for col in range(6):
                    new_item = QTableWidgetItem(res[result][col])
                    self.table.setItem(row_position, col, new_item)
                    new_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.table.resizeRowsToContents()
        self.status_label.setText('Search finished')
        self.table.setSortingEnabled(True)

    # Search by revision
    def rev_search(self):
        self.table.setSortingEnabled(False)
        self.table.setRowCount(0)
        rev = self.rev_box.currentText()
        res = revision_search(rev)
        if len(res) > 0:
            for result in range(len(res)):
                row_position = self.table.rowCount()
                self.table.insertRow(row_position)
                for col in range(6):
                    new_item = QTableWidgetItem(res[result][col])
                    self.table.setItem(row_position, col, new_item)
                    new_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.table.resizeRowsToContents()
        self.status_label.setText('Search finished')
        self.table.setSortingEnabled(True)

    # Condition search
    def cond_search(self):
        self.table.setSortingEnabled(False)
        self.table.setRowCount(0)
        con = self.condition_box.currentText()
        res = condition_search(con)
        if len(res) > 0:
            for result in range(len(res)):
                row_position = self.table.rowCount()
                self.table.insertRow(row_position)
                for col in range(6):
                    new_item = QTableWidgetItem(res[result][col])
                    self.table.setItem(row_position, col, new_item)
                    new_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.table.resizeRowsToContents()
        self.status_label.setText('Search finished')
        self.table.setSortingEnabled(True)

    # Search by location
    def loc_search(self):
        self.table.setSortingEnabled(False)
        self.table.setRowCount(0)
        loc = self.location_box.currentText()
        res = location_search(loc)
        if len(res) > 0:
            for result in range(len(res)):
                row_position = self.table.rowCount()
                self.table.insertRow(row_position)
                for col in range(6):
                    new_item = QTableWidgetItem(res[result][col])
                    self.table.setItem(row_position, col, new_item)
                    new_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.table.resizeRowsToContents()
        self.status_label.setText('Search finished')
        self.table.setSortingEnabled(True)

    # -------------------------------------------------------------------------------------------

    # write new dut
    def get_new_dut_data(self):
        invalid_data = False
        idtext = self.id_text.text()
        type_text = self.type_box.currentText()
        revision_text = self.rev_box.currentText()
        condition_text = self.condition_box.currentText()
        location_text = self.location_box.currentText()
        infotext = self.info_text.text()
        user = gt.getuser()
        dut_data = [idtext, type_text, revision_text, condition_text, location_text, infotext, user]
        if existed_dut(idtext):
            self.exist_error()
            return
        if not (idtext[:2] == 'BA' and idtext[2:].isdigit() and len(idtext) == 8):
            self.unexpected_data()
            return
        for text in dut_data:
            if not text.isascii():
                invalid_data = True
                self.unexpected_data()
                break
        if not invalid_data:
            try:
                self.new_dut_button_clicked(dut_data)
            except:
                self.error_file_opened()

    # message before update new dut
    def new_dut_button_clicked(self, dat):
        dlg = QtWidgets.QMessageBox()
        dlg.setWindowTitle("Submitting New DUT")
        dlg.setText("Do you want to submit new DUT to database?")
        dlg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
        dlg.setIcon(QtWidgets.QMessageBox.Icon.Question)
        button = dlg.exec()
        if button == QtWidgets.QMessageBox.StandardButton.Yes:
            update_new_dut(dat)
            self.refresh_data()
            self.status_label.setText('New DUT was added to database')

    # message before update existing dut
    def update_dut_button_clicked(self, dat):
        dlg = QtWidgets.QMessageBox()
        dlg.setWindowTitle("Update existing DUT")
        dlg.setText("Do you want to update DUT information?")
        dlg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
        dlg.setIcon(QtWidgets.QMessageBox.Icon.Question)
        button = dlg.exec()
        if button == QtWidgets.QMessageBox.StandardButton.Yes:
            update_dut_info(dat)
            self.refresh_data()
            self.status_label.setText('DUT information was updated')

    # error message
    def error_file_opened(self):
        dlg = QtWidgets.QMessageBox()
        dlg.setWindowTitle("Error")
        dlg.setText("Please close the database file")
        dlg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        dlg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
        button = dlg.exec()

    # invalid data error
    def unexpected_data(self):
        dlg = QtWidgets.QMessageBox()
        dlg.setWindowTitle("Error")
        dlg.setText("Invalid data. Please check your input")
        dlg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        dlg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
        button = dlg.exec()

    # dut already exist
    def exist_error(self):
        dlg = QtWidgets.QMessageBox()
        dlg.setWindowTitle("Error")
        dlg.setText("This DUT already in database")
        dlg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        dlg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
        button = dlg.exec()

    # dut not exist
    def not_exist_error(self):
        dlg = QtWidgets.QMessageBox()
        dlg.setWindowTitle("Error")
        dlg.setText("This DUT doesn't exist. Try to submit new DUT")
        dlg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        dlg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
        button = dlg.exec()

    # get info to update existing dut
    def get_update_info(self):
        invalid_data = False
        idtext = self.id_text.text()
        type_text = self.type_box.currentText()
        revision_text = self.rev_box.currentText()
        condition_text = self.condition_box.currentText()
        location_text = self.location_box.currentText()
        infotext = self.info_text.text()
        user = gt.getuser()
        dut_data = [idtext, type_text, revision_text, condition_text, location_text, infotext, user]
        if not (idtext[:2] == 'BA' and idtext[2:].isdigit() and len(idtext) == 8):
            self.unexpected_data()
            return
        if not_existed_dut(idtext):
            self.not_exist_error()
            return
        for text in dut_data:
            if not text.isascii():
                invalid_data = True
                self.unexpected_data()
                break
        if not invalid_data:
            try:
                self.update_dut_button_clicked(dut_data)
            except:
                self.error_file_opened()

    # select row data by mouse
    def selection_change(self, selected, deselected):
        selected_row = None
        index_list = []
        for x in selected.indexes():
            index_list.append(x.row())
        if len(index_list) == 1:
            selected_row = index_list[0]
            index = self.table.model().index(selected_row, 0)
            row_data = index.data()
            res = search_by_id(row_data)
            self.id_text.setText(res[0])
            self.type_box.setCurrentText(res[1])
            self.rev_box.setCurrentText(res[2])
            self.condition_box.setCurrentText(res[3])
            self.location_box.setCurrentText(res[4])
            self.info_text.setText(res[5])

    # deleting dut
    def delete_dut_button_clicked(self, dat):
        dlg = QtWidgets.QMessageBox()
        dlg.setWindowTitle("Deleting DUT")
        dlg.setText(f"Do you want to delete DUT {dat} from database?")
        dlg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
        dlg.setIcon(QtWidgets.QMessageBox.Icon.Question)
        button = dlg.exec()
        if button == QtWidgets.QMessageBox.StandardButton.Yes:
            dlg2 = QtWidgets.QMessageBox()
            dlg2.setWindowTitle("Deleting DUT")
            dlg2.setText("Are you sure?")
            dlg2.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
            dlg2.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            button2 = dlg2.exec()
            if button2 == QtWidgets.QMessageBox.StandardButton.Yes:
                result_delete = delete_selected_dut(dat)
                if result_delete:
                    self.refresh_data()
                    self.status_label.setText(f'DUT {dat} was deleted from database')
                else:
                    self.status_label.setText(f'Error while deleting DUT {dat}')

    # delete dut function
    def delete_dut(self):
        dut_num = self.id_text.text()
        self.delete_dut_button_clicked(dut_num)

    # mouse
    def mouse(self):
        self.table.selectionModel().selectionChanged.connect(self.selection_change)

    # Connect buttons to functions
    def button_connect(self):
        self.show_all_button.clicked.connect(self.show_all_data)
        self.clear_button.clicked.connect(self.clear_screen)
        self.refresh_button.clicked.connect(self.refresh_data)
        self.dut_id_button.clicked.connect(self.id_search)
        self.type_button.clicked.connect(self.type_search)
        self.rev_button.clicked.connect(self.rev_search)
        self.location_button.clicked.connect(self.loc_search)
        self.condition_button.clicked.connect(self.cond_search)
        self.delete_dut_button.clicked.connect(self.delete_dut)
        self.update_dut_button.clicked.connect(self.get_update_info)
        self.update_info_button.clicked.connect(self.get_update_info)
        self.create_new_dut_button.clicked.connect(self.get_new_dut_data)


# *****************************************************
def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.button_connect()
    ui.mouse()
    MainWindow.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
