# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Brouillon\dialog_recherche.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_Recherche(object):
    def setupUi(self, Dialog_Recherche):
        Dialog_Recherche.setObjectName("Dialog_Recherche")
        Dialog_Recherche.resize(849, 608)
        self.label_nom_fournisseur = QtWidgets.QLabel(Dialog_Recherche)
        self.label_nom_fournisseur.setGeometry(QtCore.QRect(40, 70, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_nom_fournisseur.setFont(font)
        self.label_nom_fournisseur.setObjectName("label_nom_fournisseur")
        self.comboBox_nom_fournisseur = QtWidgets.QComboBox(Dialog_Recherche)
        self.comboBox_nom_fournisseur.setGeometry(QtCore.QRect(40, 100, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_nom_fournisseur.setFont(font)
        self.comboBox_nom_fournisseur.setObjectName("comboBox_nom_fournisseur")
        self.comboBox_nom_fournisseur.addItem("")
        self.comboBox_nom_fournisseur.setItemText(0, "")
        self.comboBox_nom_fournisseur.addItem("")
        self.comboBox_nom_fournisseur.setItemText(1, "")
        self.comboBox_nom_fournisseur.addItem("")
        self.comboBox_nom_fournisseur.setItemText(2, "")
        self.listView_list_patients_fournisseur = QtWidgets.QListView(Dialog_Recherche)
        self.listView_list_patients_fournisseur.setGeometry(QtCore.QRect(40, 220, 701, 341))
        self.listView_list_patients_fournisseur.setObjectName("listView_list_patients_fournisseur")
        self.label_listview = QtWidgets.QLabel(Dialog_Recherche)
        self.label_listview.setGeometry(QtCore.QRect(50, 190, 771, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_listview.setFont(font)
        self.label_listview.setObjectName("label_listview")
        self.pushButton_afficher = QtWidgets.QPushButton(Dialog_Recherche)
        self.pushButton_afficher.setGeometry(QtCore.QRect(380, 100, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_afficher.setFont(font)
        self.pushButton_afficher.setObjectName("pushButton_afficher")

        self.retranslateUi(Dialog_Recherche)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Recherche)

    def retranslateUi(self, Dialog_Recherche):
        _translate = QtCore.QCoreApplication.translate
        Dialog_Recherche.setWindowTitle(_translate("Dialog_Recherche", "Dialog recherche"))
        self.label_nom_fournisseur.setText(_translate("Dialog_Recherche", "Nom fournisseur"))
        self.label_listview.setText(_translate("Dialog_Recherche", "Listview  affichant la liste des patients qui achètent des médicament du fournisseur via la pharmacie"))
        self.pushButton_afficher.setText(_translate("Dialog_Recherche", "Afficher"))
