#
# Copyright 2019-2023 Manuel Barrette
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#


import serial, io
import serial.tools.list_ports
from PyQt6 import QtGui, QtWidgets
import pyqtgraph as pg
import numpy as np
import matplotlib.pyplot as plt
from pyqtgraph.Qt import QtCore
import platform, os, time
import locale, ctypes

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, Dialog, ui_Dialog, parent):

#        self.app = app
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.btn = QtWidgets.QPushButton(self.centralwidget)
        self.gridLayout.addWidget(self.btn, 0, 0, 1, 1)

        self.btn2 = QtWidgets.QPushButton(self.centralwidget)
        self.gridLayout.addWidget(self.btn2, 1, 0, 1, 1)

        self.btn3 = QtWidgets.QPushButton(self.centralwidget)
        self.gridLayout.addWidget(self.btn3, 4, 0, 1, 1)

        self.btn4 = QtWidgets.QPushButton(self.centralwidget)
        self.gridLayout.addWidget(self.btn4, 2, 0, 1, 1)

        self.btn5 = QtWidgets.QPushButton(self.centralwidget)
        self.gridLayout.addWidget(self.btn5, 5, 0, 1, 1)

        #spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        #self.gridLayout.addItem(spacerItem, 15, 0, 1, 1)

        self.plot = pg.PlotWidget()
        self.gridLayout.addWidget(self.plot, 0, 1, 6, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1001, 25))
        self.menubar.setObjectName("menubar")
        self.menu_aide = QtWidgets.QMenu(self.menubar)
        self.menu_aide.setObjectName("menu_aide")
        MainWindow.setMenuBar(self.menubar)
        self.action_translate = QtWidgets.QMenu(MainWindow)
        self.action_translate.setObjectName("action_translate")
        self.menu_aide.addMenu(self.action_translate)

        self.action_fr = QtGui.QAction(MainWindow)
        self.action_fr.setObjectName("action_fr")
        self.action_translate.addAction(self.action_fr)
        self.action_en = QtGui.QAction(MainWindow)
        self.action_en.setObjectName("action_en")
        self.action_translate.addAction(self.action_en)

        self.action_propos = QtGui.QAction(MainWindow)
        self.action_propos.setObjectName("action_propos")
        self.menu_aide.addAction(self.action_propos)

        self.menubar.addAction(self.menu_aide.menuAction())

        # Initial parameters

        self.retranslateUi(MainWindow)

        self.E = 4.996 # Voltage de la source

        self.baud     = 9600                          # baud rate
#        self.filename = 'data.txt'                # log file to save data in
        fps = 100
        self.flagUpdate = False

        self.connexion = True

        self.plot.showGrid(x = True, y = True)
        self.xdata = []
        self.ydata = []

        self.courbe = self.plot.plot(pen=1)

        self.compteur = 0
        self.flagConnexion = 0

        self.connexionold = 0
#        self.outFile = open(self.filename,'w')
        self.timer_recherche = QtCore.QTimer()
        self.timer_recherche.timeout.connect(lambda: self.searchThread(fps))
        self.timer_recherche.start(1000)

        self.timer_lecture = QtCore.QTimer()
        self.timer_lecture.timeout.connect(lambda: self.update(fps))
#        self.timer_lecture.start(int(1000/fps))


        # Buttons triggers
        self.action_propos.triggered.connect(lambda: Dialog.show())
        self.action_fr.triggered.connect(lambda: self.traduire(MainWindow, Dialog, ui_Dialog, "fr_CA"))
        self.action_en.triggered.connect(lambda: self.traduire(MainWindow, Dialog, ui_Dialog, "en_CA"))
        self.btn.clicked.connect(lambda: self.toggleUpdate())
        self.btn2.clicked.connect(lambda: self.effacer())
        self.btn3.clicked.connect(lambda: self.graphique())
        self.btn4.clicked.connect(lambda: self.enregistrer())
        self.btn5.clicked.connect(lambda: self.fermerEtAfficher())


    def retranslateUi(self, MainWindow):
        self._translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(self._translate("MainWindow", "Radiohm"))
        self.btn.setText(self._translate("MainWindow", "Mettre à jour"))
        self.btn2.setText(self._translate("MainWindow", "Effacer"))
        self.btn4.setText(self._translate("MainWindow", "Enregistrer"))
        nom_bouton = self._translate("MainWindow", "Graphique à partir") + " \n " + self._translate("MainWindow", "d'un fichier")
        self.btn3.setText(nom_bouton)
        self.btn5.setText(self._translate("MainWindow", "Quitter"))
        self.menu_aide.setTitle(self._translate("MainWindow", "Options"))
        self.action_propos.setText(self._translate("MainWindow", "À propos"))
        self.action_translate.setTitle(self._translate("MainWindow", "Langue"))
        self.action_fr.setText(self._translate("MainWindow", "Français"))
        self.action_en.setText(self._translate("MainWindow", "English"))
        self.plot.setLabel('left', text=self._translate("MainWindow", "Intensité (u.a.)"))
        self.plot.setLabel('bottom', text=self._translate("MainWindow", "Position"), units='m')


    def traduire(self, MainWindow, Dialog, ui_Dialog, langue):
        directory = "locales"
        self.translator = QtCore.QTranslator()
        self.translator.load(langue, directory)
        QtCore.QCoreApplication.installTranslator(self.translator)
        self.retranslateUi(MainWindow)
        ui_Dialog.retranslateUi(Dialog)


    def fermerEtAfficher(self):
        app = QtWidgets.QApplication.instance()
        app.closeAllWindows()


    def toggleUpdate(self):
        self.flagUpdate = not self.flagUpdate
        if self.flagUpdate:
            self.btn.setText(self._translate("MainWindow", "Arrêter"))
            if self.device:
                self.serialPort.reset_input_buffer()
                line = self.serialPort.readline() # Jeter la premiere ligne car souvent incomplete
        else:
            self.btn.setText(self._translate("MainWindow", "Mettre à jour"))
        return None


    def effacer(self):
        self.xdata = []
        self.ydata = []
        self.courbe.setData(self.xdata, self.ydata)
#        self.outFile.seek(0)
#        self.outFile.truncate()
        self.compteur = 0
        return None


    def enregistrer(self):
        extension = self._translate("MainWindow", "Données") + " (*.txt)"
        systeme_exploitation = platform.system()
        if systeme_exploitation == "Linux":
            fichier = QtWidgets.QFileDialog.getSaveFileName(None, self._translate("MainWindow", "Enregistrer sous..."), '', extension, options=QtWidgets.QFileDialog.Option.DontUseNativeDialog)
        else:
            fichier = QtWidgets.QFileDialog.getSaveFileName(None, self._translate("MainWindow", "Enregistrer sous..."), '', extension)
        nom_fichier = fichier[0]
        if nom_fichier != "" and nom_fichier[-4:] != ".txt":
            nom_fichier = nom_fichier + ".txt"
        fichier = open(nom_fichier, 'w')
        for i in range(0,self.compteur):
            sortie = str(self.xdata[i]) + " " + str(self.ydata[i]) + "\n"
            fichier.write(sortie)
        fichier.close()

#    def enregistrer(self):
#        extension = self._translate("MainWindow", "Données") + " (*.txt)"
#        fichier = QtGui.QFileDialog.getSaveFileName(None, self._translate("MainWindow", "Enregistrer sous..."), '', extension)
#        nom_fichier = fichier[0]
#        if nom_fichier != "" and nom_fichier[-4:] != ".txt":
#            nom_fichier = nom_fichier + ".txt"
#        systeme_exploitation = platform.system()
#        if systeme_exploitation == 'Windows':
#            commande = 'copy ' + self.filename + ' "' + nom_fichier + '"'
#        else:
#            commande = 'cp ' + self.filename + ' "' + nom_fichier + '"'
#        print(commande)
#        os.system(commande)

    def graphique(self):

        extension = self._translate("MainWindow", "Données") + " (*.txt)"
        systeme_exploitation = platform.system()
        if systeme_exploitation == "Linux":
            fichier = QtWidgets.QFileDialog.getOpenFileName(None, self._translate("MainWindow", "Ouvrir..."), "", extension, options=QtWidgets.QFileDialog.Option.DontUseNativeDialog)
        else:
            fichier = QtWidgets.QFileDialog.getOpenFileName(None, self._translate("MainWindow", "Ouvrir..."), "", extension)
        try:
            lecture = open(fichier[0])
            xdata = []
            ydata = []

            for line in lecture:
                x, y = line.split(" ", 1)
                x = float(x)
                y = float(y)
                xdata.append(x)
                ydata.append(y)

            plt.xlabel(self._translate("MainWindow", "Position") + " (m)")
            plt.ylabel(self._translate("MainWindow", "Intensité (u.a.)"))

            plt.plot(xdata, ydata)

            plt.show()
        except(FileNotFoundError):
            pass


    def findDevice(self):
        ports = list(serial.tools.list_ports.comports())
        systeme_exploitation = platform.system()
        for p in ports:
            if systeme_exploitation == 'Windows':
                if "Arduino" in p.description or "USB Serial Device" in p.description or "Périphérique série USB" in p.description:
                    print(p.device)
                    return p.device
            elif systeme_exploitation == 'Linux' and "Arduino" in p.manufacturer:
                print(p.device)
                return p.device
            elif systeme_exploitation == 'Darwin' and "Arduino" in str(p.manufacturer):
                print(p.device)
                return p.device


    def searchThread(self, fps):
        self.device = self.findDevice()
        if self.device:
            print("Connecte")
            time.sleep(1)
            self.serialPort = serial.Serial(self.device,self.baud)
            self.timer_recherche.stop()
            self.timer_lecture.start(int(1000/fps))


    def update(self, fps):
        try:
            line = self.serialPort.readline()
            if self.flagUpdate == True:
                self.compteur = self.compteur + 1
#                line = self.serialPort.readline()
                line2 = line.rstrip()
                ligne = line2.decode("utf-8")
                x, y = ligne.split(" ", 1)
                x = float(x)
                y = float(y) # Unités arbitraires
#                x = self.E*x/1023
                y = self.E*y/1023
#                y -= (x - 0.007)
#                x = 1/self.a*(x*self.RV*self.R/(self.E*self.RV-x*self.RV-self.R*x) - self.b)/100
                x = x/1000.0
                self.xdata.append(x)
                self.ydata.append(y)
#                donnees = str(x) + " " + str(y) + "\n"
#                self.outFile.write(donnees)
                self.courbe.setData(self.xdata, self.ydata)
        except serial.serialutil.SerialException:
            print("Deconnecte")
            self.timer_lecture.stop()
            self.timer_recherche.start(1000)
            self.device = False
