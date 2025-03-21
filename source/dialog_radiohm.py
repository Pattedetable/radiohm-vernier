#
# Copyright 2019-2025 Manuel Barrette
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


from PyQt6 import QtCore, QtGui, QtWidgets
import os

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        Dialog.resize(497, 256)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_image = QtWidgets.QLabel(Dialog)
        self.label_image.setObjectName("label_image")
        self.verticalLayout.addWidget(self.label_image)
        self.label_image.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        directory = "images"
        url_image = os.path.join(directory, "logo.png")
        image = QtGui.QPixmap(url_image)
        self.label_image.setPixmap(image)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setOpenExternalLinks(True)
        self.label.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.LinksAccessibleByMouse)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(lambda: Dialog.close())
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "À propos"))
        self.label.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Radiohm</span></p><p align=\"center\"><span style=\" font-size:12pt;\">Copyright 2019-2025 Manuel Barrette</p><p align=\"center\"><span style=\" font-size:12pt;\">License <a href=\"https://www.gnu.org/licenses/gpl-3.0.en.html\"><span style=\" text-decoration: underline; color:#0000ff;\">GNU GPLv3</span></a><span><span></p><p align=\"center\"><span style=\" font-size:12pt;\">Source code available on <a href=\"https://github.com/Pattedetable/radiohm-vernier\"><span style=\" text-decoration: underline; color:#0000ff;\">GitHub</span></a><span></p><p align=\"center\"><span style=\" font-size:10pt;\">This software uses libraries from <a href=\"https://www.qt.io/\"><span style=\" text-decoration: underline; color:#0000ff;\">Qt</span></a> under the GPL/LGPLv3, <a href=\"https://www.python.org/\"><span style=\" text-decoration: underline; color:#0000ff;\">Python</span></a>, <a href=\"http://www.numpy.org/\"><span style=\" text-decoration: underline; color:#0000ff;\">Numpy</span></a>, <a href=\"http://pyqtgraph.org/\"><span style=\" text-decoration: underline; color:#0000ff;\">PyQtGraph</span></a>, <a href=\"https://matplotlib.org/\"><span style=\" text-decoration: underline; color:#0000ff;\">Matplotlib</span></a></p> <p align=\"center\"><span style=\" font-size:10pt;\"> and <a href=\"https://pythonhosted.org/pyserial/\"><span style=\" text-decoration: underline; color:#0000ff;\">pySerial</span></a> (Copyright (c) 2001-2020 Chris Liechti <cliechti@gmx.net> All Rights Reserved.).<span></p></body></html>")
        self.pushButton.setText(_translate("Dialog", "Fermer"))
