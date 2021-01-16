#
# Copyright 2019-2021 Manuel Barrette
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

""" Initialize windows and make the main window appear """
import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
import radiohm_main_window
import dialog_radiohm
import platform
import locale, ctypes

# Initialize windows
app = QApplication(sys.argv)
window = QMainWindow()
dialog = QDialog()

systeme_exploitation = platform.system()
if systeme_exploitation == 'Windows':
    langwin = ctypes.windll.kernel32
    langue_sys = locale.windows_locale[langwin.GetUserDefaultUILanguage()]
elif systeme_exploitation == 'Darwin' or 'Linux':
    langue_sys = locale.getdefaultlocale()[0]
langue_sys = langue_sys[0:2]
translator = QtCore.QTranslator()
if langue_sys == "fr":
    langue = "fr_CA"
else:
    langue = "en_CA"
translator.load(langue)
app.installTranslator(translator)

ui_Window = radiohm_main_window.Ui_MainWindow()
ui_Dial = dialog_radiohm.Ui_Dialog()

ui_Dial.setupUi(dialog)
ui_Window.setupUi(window, dialog, None)

# Make main window appear
window.show()
sys.exit(app.exec_())
