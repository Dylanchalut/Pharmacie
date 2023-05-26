# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot
# Importer la boite de dialogue
import UI_PY.dialog_medicament
from PyQt5 import QtWidgets
from Classes.Medicament import Medicament
######################################################
###### DÉFINITIONS DE LA CLASSE Fenetrelistview ######
######################################################
def verifier_code_medicament(p_code):
    for elt in Medicament.ls_medicaments:
        if elt.Code_medicament == p_code:
            return True
    return False


class Fenetremedicament(QtWidgets.QDialog, UI_PY.dialog_medicament.Ui_Dialog_Medicament):

    def cacher_label_erreur(self):
        self.label_erreur_code_medicament_existe_pas.setVisible(False)
        self.label_erreur_code_medicamen_existe.setVisible(False)
        self.label_erreur_code_medicament_invalide.setVisible(False)
        self.label_erreur_nom_commercial.setVisible(False)
        self.label_erreur_dose_quot_max.setVisible(False)
        self.label_erreur_nom_chimique.setVisible(False)
        self.label_erreur_prix.setVisible(False)
        self.label_erreur_duree_prise_max.setVisible(False)




    def __init__(self, parent=None):
        """
        Constructeur de la fenêtre qui affiche la liste des étudiants
        """
        super(Fenetremedicament, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Boîte de dialogue Médicament")

