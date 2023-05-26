# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot
# Importer la boite de dialogue
import UI_PY.dialog_patient
from PyQt5 import QtWidgets

# importation de la classe Patient
from Classes.Patient import Patient

from PyQt5.QtCore import pyqtSlot, QDate


######################################################
###### DÉFINITIONS DE LA CLASSE Fenetrelistview ######
######################################################
def verifier_num_patient(p_numero):
    """
    Cette fonction vérifie si le numero patient est déjà dans la liste ou non
    :param p_numero: numero patient
    :return: True = si trouvé ou False = pas trouvé
    """
    for elt in Patient.ls_patients:
        if elt.Numero_patient == p_numero:
            return True
    return False


def verifier_nom_patient(p_nom):
    """
    Cette fonction vérifie si le nom patient est déjà dans la liste ou non
    :param p_numero: nom patient
    :return: True = si trouvé ou False = pas trouvé
    """
    for elt in Patient.ls_patients:
        if elt.Nom == p_nom:
            return True
    return False


def verifier_prenom_patient(p_prenom):
    """
    Cette fonction vérifie si le prenom patient est déjà dans la liste ou non
    :param p_numero: prenom patient
    :return: True = si trouvé ou False = pas trouvé
    """
    for elt in Patient.ls_patients:
        if elt.Prenom == p_prenom:
            return True
    return False


def verifier_date_patient(p_date):
    """
    Cette fonction vérifie si le date naissance patient est déjà dans la liste ou non
    :param p_numero: date de naissance patient
    :return: True = si trouvé ou False = pas trouvé
    """
    for elt in Patient.ls_patients:
        if elt.Date_naiss == p_date:
            return True
    return False


class Fenetrepatient(QtWidgets.QDialog, UI_PY.dialog_patient.Ui_Dialog):

    def cacher_label_erreur(self):
        """
        Fonction qui permet de cacher tous les labels d'erreurs
        :return:
        """
        self.label_erreur_num_patient_existe.setVisible(False)
        self.label_errreur_num_patient_existe_pas.setVisible(False)
        self.label_erreur_num_patient_valider.setVisible(False)
        self.label_erreur_nom_patient.setVisible(False)
        self.label_erreur_prenom_patient.setVisible(False)
        self.label_erreur_date_naiss.setVisible(False)

    def __init__(self, parent=None):
        """
        Constructeur de la fenêtre qui affiche la liste des étudiants
        """
        super(Fenetrepatient, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Boîte de dialogue Patient")
        self.cacher_label_erreur()

    @pyqtSlot()
    def on_pushButton_Ajouter_patient_clicked(self):
        """
        Gestionnaire d'événement qui sert a ajouter les patients dans une liste
        """
        self.cacher_label_erreur()

        P = Patient()

        P.Numero_patient = self.lineEdit_numero_patient.text()
        P.Nom = self.lineEdit_nom_patient.text().capitalize()
        P.Prenom = self.lineEdit_prenom_patient.text().capitalize()
        P.Date_naiss = self.dateEdit_date_naiss_patient.date()

        verifier_num = verifier_num_patient(self.lineEdit_numero_patient.text())

        if verifier_num is True and P.Numero_patient != "":
            self.lineEdit_numero_patient.clear()
            self.label_erreur_num_patient_existe.setVisible(True)

        if P.Numero_patient == "":
            self.lineEdit_numero_patient.clear()
            self.label_erreur_num_patient_valider.setVisible(True)

        if P.Nom == "":
            self.lineEdit_nom_patient.clear()
            self.label_erreur_nom_patient.setVisible(True)

        if P.Prenom == "":
            self.lineEdit_prenom_patient.clear()
            self.label_erreur_prenom_patient.setVisible(True)

        if P.Date_naiss == None:
            self.dateEdit_date_naiss_patient.setDate(QDate(2000, 1, 1))
            self.label_erreur_date_naiss.setVisible(True)

        if P.Numero_patient != "" and P.Nom != "" and P.Prenom != "" and P.Date_naiss is not None and verifier_num is False:
            Patient.ls_patients.append(P)
            self.lineEdit_prenom_patient.clear()
            self.lineEdit_nom_patient.clear()
            self.lineEdit_numero_patient.clear()
            self.dateEdit_date_naiss_patient.setDate(QDate(2000, 1, 1))

    @pyqtSlot()
    def on_pushButton_supprimer_patient_clicked(self):
        """
        Gestionnaire d'événement qui sert a supprimer un patient dans sa liste
        :return:
        """
        self.cacher_label_erreur()

        P = Patient()

        P.Numero_patient = self.lineEdit_numero_patient.text()
        P.Nom = self.lineEdit_nom_patient.text().capitalize()
        P.Prenom = self.lineEdit_prenom_patient.text().capitalize()
        P.Date_naiss = self.dateEdit_date_naiss_patient.date()

        verifier_num = verifier_num_patient(self.lineEdit_numero_patient.text())
        verifier_nom = verifier_nom_patient(self.lineEdit_nom_patient.text().capitalize())
        verifier_prenom = verifier_prenom_patient(self.lineEdit_prenom_patient.text().capitalize())
        verifier_date = verifier_date_patient(self.dateEdit_date_naiss_patient.date())

        if verifier_num is False and P.Numero_patient != "":
            self.lineEdit_numero_patient.clear()
            self.label_errreur_num_patient_existe_pas.setVisible(True)

        if P.Numero_patient == "":
            self.lineEdit_numero_patient.clear()
            self.label_erreur_num_patient_valider.setVisible(True)

        if P.Nom == "":
            self.lineEdit_nom_patient.clear()
            self.label_erreur_nom_patient.setVisible(True)

        if P.Prenom == "":
            self.lineEdit_prenom_patient.clear()
            self.label_erreur_prenom_patient.setVisible(True)

        if P.Date_naiss == None:
            self.dateEdit_DNaissance.setDate(QDate(2000, 1, 1))
            self.label_erreur_date_naiss.setVisible(True)

        if P.Numero_patient != "" and P.Nom != "" and P.Prenom != "" and P.Date_naiss is not None \
                and verifier_num is True and verifier_nom is True \
                and verifier_prenom is True and verifier_date is True:

            for elt in Patient.ls_patients:
                if elt.Numero_patient == self.lineEdit_numero_patient.text() \
                        and elt.Nom == self.lineEdit_nom_patient.text().capitalize() \
                        and elt.Prenom == self.lineEdit_prenom_patient.text().capitalize() \
                        and elt.Date_naiss == self.dateEdit_date_naiss_patient.date():
                    Patient.ls_patients.remove(elt)
                    self.lineEdit_prenom_patient.clear()
                    self.lineEdit_nom_patient.clear()
                    self.lineEdit_numero_patient.clear()
                    self.dateEdit_date_naiss_patient.setDate(QDate(2000, 1, 1))
                    break

    @pyqtSlot()
    def on_pushButton_quitter_clicked(self):
        # fermer la fenêtre
        self.close()
