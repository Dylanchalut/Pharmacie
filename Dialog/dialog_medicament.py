# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot
# Importer la boite de dialogue
import UI_PY.dialog_medicament
from PyQt5 import QtWidgets

from Classes.Analgesique import Analgesique
from Classes.Antibiotique import Antibiotique
from Classes.Corticoide import Corticoide
from Classes.Medicament import Medicament
######################################################
###### DÉFINITIONS DE LA CLASSE Fenetrelistview ######
######################################################
def verifier_code_medicament(p_code):
    """
    Cette fonction vérifie si le code médicament est déjà dans la liste ou non
    :param p_code: le code du médicament
    :return: True = si trouvé ou False = pas trouvé
    """
    for elt in Medicament.ls_medicaments:
        if elt.Code_medicament == p_code:
            return True
    return False


class Fenetremedicament(QtWidgets.QDialog, UI_PY.dialog_medicament.Ui_Dialog_Medicament):

    def cacher_label_erreur(self, B):
        """
        Fonction qui permet de cacher tous les labels d'erreurs
        :param B: le paramètre B est pour qu'ensuite marquer True ou False
        """
        self.label_erreur_code_medicament_existe_pas.setVisible(B)
        self.label_erreur_code_medicamen_existe.setVisible(B)
        self.label_erreur_code_medicament_invalide.setVisible(B)
        self.label_erreur_nom_commercial.setVisible(B)
        self.label_erreur_dose_quot_max.setVisible(B)
        self.label_erreur_nom_chimique.setVisible(B)
        self.label_erreur_prix.setVisible(B)
        self.label_erreur_duree_prise_max.setVisible(B)

    def cacher_label_duree_prise_max(self, B):
        """
        Fonction qui permet de cacher tous les chose reliée a la duree prise max
        :param B: le paramètre B est pour qu'ensuite marquer True ou False
        """
        self.label_duree_prise_maximale.setVisible(B)
        self.lineEdit_duree_prise_max.setVisible(B)
        self.label_antibiotique.setVisible(B)

    def cacher_label_dose_quot_max(self, B):
        """
        Fonction qui permet de cacher tous les chose reliée à la dose quotidien max
        :param B: le paramètre B est pour qu'ensuite marquer True ou False
        """
        self.label_dose_quot_max.setVisible(B)
        self.lineEdit_dose_quot_max.setVisible(B)
        self.label_analgesique.setVisible(B)

    def cacher_label_effet_medicament(self,B):
        """
        Fonction qui permet de cacher tous les chose reliée a la comboBox effet médicament
        :param B: le paramètre B est pour qu'ensuite marquer True ou False
        """
        self.comboBox_effet_medicament.setVisible(B)
        self.label_effet_medicament.setVisible(B)
        self.label_corticoide.setVisible(B)





    def __init__(self, parent=None):
        """
        Constructeur de la fenêtre qui affiche la liste des étudiants
        """
        super(Fenetremedicament, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Boîte de dialogue Médicament")
        self.cacher_label_erreur(False)
        self.cacher_label_dose_quot_max(False)
        self.cacher_label_effet_medicament(False)
        self.cacher_label_duree_prise_max(True)

        #Permet de savoir quelle catégorie il a choisie
        self.comboBox_categorie.currentIndexChanged.connect(self.affiche_widget)


    def affiche_widget(self):
        """
        Fonction pour afficher les widget personnaliser selon quelle index de la comboBox catégorie
        est choisi.
        """
        if self.comboBox_categorie.currentText() == "Antibiotique":
            self.cacher_label_duree_prise_max(True)
            self.cacher_label_dose_quot_max(False)
            self.cacher_label_effet_medicament(False)

        elif self.comboBox_categorie.currentText() == "Analgésique":
            self.cacher_label_duree_prise_max(False)
            self.cacher_label_dose_quot_max(True)
            self.cacher_label_effet_medicament(False)

        else:
            self.cacher_label_duree_prise_max(False)
            self.cacher_label_dose_quot_max(False)
            self.cacher_label_effet_medicament(True)

    def Gestionner_categorie(self, p_categorie_m):
        """
        Fonction qui permet de rendre le code plus condenser
        permet aussi de prendre les paramètre principal
        :param p_categorie_m: ComboBox catégorie
        :return:
        """
        if p_categorie_m == "Antibiotique":
            M = Antibiotique()
        elif p_categorie_m == "Analgésique":
            M = Analgesique()
        else:
            M = Corticoide()

        M.Code_medicament = self.lineEdit_code_medicament.text()
        M.Nom_chimique = self.lineEdit_nom_chimique.text().capitalize()
        M.Nom_commercial = self.lineEdit_nom_commercial.text().capitalize()
        try:
            M.Prix = int(self.lineEdit_prix.text())
        except:
            self.label_erreur_prix.setVisible(True)

        M.Categorie = self.comboBox_categorie.currentText()

        verifier_code = verifier_code_medicament(self.lineEdit_code_medicament.text())

        if M.Code_medicament != "" and verifier_code is True:
            self.lineEdit_code_medicament.clear()
            self.label_erreur_code_medicamen_existe.setVisible(True)
        if M.Code_medicament == "":
            self.lineEdit_code_medicament.clear()
            self.label_erreur_code_medicament_invalide.setVisible(True)
        if M.Nom_chimique == "":
            self.lineEdit_nom_chimique.clear()
            self.label_erreur_nom_chimique.setVisible(True)

        if M.Nom_commercial == "":
            self.lineEdit_nom_commercial.clear()
            self.label_nom_commercial.setVisible(True)

        if M.Prix == 0:
            self.lineEdit_prix.clear()
            self.label_erreur_prix.setVisible(True)

        if M.Code_medicament != "" and M.Nom_chimique != "" and M.Nom_commercial != "" \
            and M.Prix != 0 and verifier_code is False:
            self.lineEdit_code_medicament.clear()
            self.lineEdit_nom_chimique.clear()
            self.lineEdit_nom_commercial.clear()
            self.lineEdit_prix.clear()



    @pyqtSlot()
    def on_pushButton_ajouter_clicked(self):
        """
       Gestionnaire d'événement qui ajoute les médicament dans une liste
        """
        self.cacher_label_erreur(False)

        if self.comboBox_categorie.currentText() == "Antibiotique":
            M = Antibiotique()

            self.Gestionner_categorie(self.comboBox_categorie.currentText())
            try:
                M.Duree_prix_max = int(self.lineEdit_duree_prise_max.text())
            except:
                self.label_erreur_duree_prise_max.setVisible(True)

            if M.Duree_prix_max == 0:
                self.lineEdit_duree_prise_max.clear()
                self.label_erreur_duree_prise_max.setVisible(True)

            if M.Duree_prix_max != 0 and self.Gestionner_categorie(self.comboBox_categorie.currentText()):
                Medicament.ls_medicaments.append(M)
                self.lineEdit_duree_prise_max.clear()

        elif self.comboBox_categorie.currentText() == "Analgésique":
            M = Analgesique()
            try:
                M.Dose_quot_max = int(self.lineEdit_dose_quot_max.text())
            except:
                self.label_erreur_dose_quot_max.setVisible(True)

            if M.Dose_quot_max == 0:
                self.lineEdit_dose_quot_max.clear()
                self.label_erreur_dose_quot_max.setVisible(True)

            if M.Dose_quot_max != 0 and self.Gestionner_categorie(self.comboBox_categorie.currentText()):
                Medicament.ls_medicaments.append(M)
                self.lineEdit_dose_quot_max.clear()

        else:
            M = Corticoide()

            M.Effet_medic = self.comboBox_effet_medicament.currentText()

            if self.Gestionner_categorie(self.comboBox_categorie.currentText()):
                Medicament.ls_medicaments.append(M)










