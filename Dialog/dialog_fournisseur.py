# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot
# Importer la boite de dialogue
from PyQt5.QtGui import QStandardItemModel

import UI_PY.dialog_fournisseur
from PyQt5 import QtWidgets

from Classes.Fournisseur import Fournisseur
from Classes.Patient import Patient


######################################################
###### DÉFINITIONS DE LA CLASSE Fenetrelistview ######
######################################################


class Fenetrefournisseur(QtWidgets.QDialog, UI_PY.dialog_fournisseur.Ui_Dialog):
    def __init__(self, parent=None):
        """
        Constructeur de la fenêtre qui affiche la liste des étudiants
        """
        super(Fenetrefournisseur, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Boîte de dialogue Fournisseur")

        for elt in Patient.ls_patients:
            self.comboBox_numero_patient.addItem(elt.Numero_patient)

        self.model = QStandardItemModel()


    def on_pushButton_ajouter_patient_listview_clicked(self):

        for elt_patient in Patient.ls_patients:
            if elt_patient.Numero_patient == self.comboBox_numero_patient.currentText():
                for elt_num in elt_patient.Ls_patient:
                    item = QStandardItemModel(elt_num.Numero_patient)
                    self.model.appendRow(item)

    def on_pushButton_serialiser_clicked(self):

        F = Fournisseur()

        F.Code_fournisseur = self.lineEdit_code_fournisseur.text()
        F.Nom_compagnie = self.lineEdit_nom_compagnie.text().capitalize()

        if F.Code_fournisseur != "" and F.Nom_compagnie != "":
            Fournisseur.ls_fournisseur.append(F)
            F.serialiserFournisseur("." + F.Code_fournisseur + ".json")






