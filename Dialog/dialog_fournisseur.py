# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot
# Importer la boite de dialogue
from PyQt5.QtGui import QStandardItemModel

import UI_PY.dialog_fournisseur
from PyQt5 import QtWidgets
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
            self.comboBox_numero_patient(elt.Numero_patient)

        self.model = QStandardItemModel()


    def on_pushButton_ajouter_patient_listview_clicked(self):

        for elt_patient in Patient.ls_patients:
            if elt_patient.Numero_patient ==
