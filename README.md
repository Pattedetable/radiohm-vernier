# Radiohm

![screenshot](https://raw.githubusercontent.com/Pattedetable/radiohm-vernier/master/images/radiohm_screenshot.png)

_The English version follows_

## Français

Ce programme a pour but de faire l'acquisition de données de l'intensité lumineuse en fonction de la position dans une expérience d'interférence et de diffraction.

![screenshot](https://raw.githubusercontent.com/Pattedetable/radiohm-vernier/master/images/montage.jpg)

L'acquisition passe par une carte Arduino Uno avec le script ```radiohm.ino```.  Le calcul de la position se fait avec un vernier numérique.  Un détecteur de lumière est fixé à celui-ci.  Dans le graphique, la position est représentée sur l'axe des x, et l'intensité lumineuse (en fait la différence de potentiel aux bornes du détecteur) sur l'axe des y.

![screenshot](https://raw.githubusercontent.com/Pattedetable/radiohm-vernier/master/images/montage_breadboard.jpg)

Le programme est disponible pour Linux, MacOS et Windows.  Il s'agit en même temps d'un projet personnel d'apprentissage de programmation.  Si vous trouvez des erreurs, sentez-vous bien à l'aise de les souligner à partir de l'onglet "Issues" sur [GitHub](https://github.com/Pattedetable/radiohm-vernier).

Le fichier utilisé pour démarrer le programme est ```radiohm.py```.


### Utilisation

Afin d'utiliser ce programme, vous aurez besoin des logiciels suivants :

  * Python 3

Si vous utilisez Linux, Python sera généralement déjà installé.  Si ce n'est pas déjà fait, vous pouvez installer Python 3 à partir des dépôts de logiciels de votre distribution.

Que vous utilisiez Linux, MacOS ou Windows, vous pouvez aussi installer Python à partir du [site officiel](https://www.python.org/).  Sélectionnez ensuite le paquet correspondant à votre système d'exploitation.

Vous aurez aussi besoin des modules Python suivants :

  * Numpy
  * Matplotlib
  * PyQt6
  * pyqtgraph (>=0.12)
  * pyserial

Si vous utilisez Linux, il est fort probable qu'ils se trouvent dans les dépôts logiciels de votre distribution.

Pour tous les systèmes d'exploitation supportés, à partir de la version 3.4, Python inclus de plus `pip`, un gestionnaire de paquet qui permet d'installer des modules pour Python.  Pour vérifer la version de Python installée sur votre système, ouvrez un terminal (Linux, MacOS) ou une invite de commande (Windows) et tappez :

```python --version```

Si le numéro de version affiché à l'écran commence par 2, dans tout ce qui suit, utilisez `python3` au lieu de `python`, et `pip3` au lieu de `pip`.

Vous pouvez vous servir de `pip` pour installer les divers modules nécessaires.  Par exemple, pour installer Numpy, entrez dans un terminal (ou invite de commande) :

```pip install numpy```

Une fois ces modules installés, dans le terminal sous Linux et MacOS ou l'invite de commande sous Windows, entrez :

```python radiohm.py```

Sous Windows, vous pouvez aussi double-cliquer sur le fichier ```radiohm.py```.


### License

Le programme est distribué sous la licence GNU GPLv3.  Pour le texte complet, référez-vous au fichier `LICENSE`.
La version courte de cette licence est que vous êtes libre d'utiliser ce logiciel, d'en modifier le code source, ainsi que de le redistribuer, que ce soit sous sa version originale ou modifiée.  Cependant, vous devez donner ces mêmes droits aux personnes qui utiliseront votre logiciel redistribué.

Le code source est disponible sur [GitHub](https://github.com/Pattedetable/radiohm).

Ce logiciel utilise des bibliothèques de Qt sous la licence LGPLv3, ainsi que de Python, Numpy et Matplotlib.


## English

This software serves to gather data of the intensity of the light as a function of position in a diffraction and interference experiment.

![screenshot](https://raw.githubusercontent.com/Pattedetable/radiohm-vernier/master/images/montage.jpg)

The data is gathered through an Arduino Uno board with the ```radiohm.ino``` script on it.  The position is computed using a digital caliper.  A light detector is fixed to it.  On the graph, the position is represented on the x axis, while the intensity of the light (in fact the voltage of the detector) is represented on the y axis.

![screenshot](https://raw.githubusercontent.com/Pattedetable/radiohm-vernier/master/images/montage_breadboard.jpg)

This program is available for Linux, MacOS and Windows.  It is also a personal learning project.  Please report any errors you find using the "Issues" tab on [GitHub](https://github.com/Pattedetable/radiohm-vernier).

The file used to start the program is ```radiohm.py```.


### Usage

You will need some software to use this program, namely:

  * Python 3

If you are using Linux, Python will generally already be installed.  If not, you can install it from your distribution's repositories.

You can also install Python from the [official website](https://www.python.org/).  Once there, select the appropriate package for your operating system.

You will also need the following Python modules:

  * Numpy
  * Matplotlib
  * PyQt6
  * pyqtgraph (>= 0.12)
  * pyserial

On Linux, you will most likely find these modules in your distribution's repositories.

On all supported operating systems, starting with version 3.4, Python includes `pip`, a package manager for Python which can be used to install the necessary modules.  To check the version of Python that is installed on your system, open a terminal (Linux, MacOS) or a command prompt (Windows) and type in:

```python --version```

If the version number displayed on screen begins with 2, replace `python` with `python3` and `pip` with `pip3` in every command that follows.

You can then use `pip` to install the necessary modules.  For instance, to install Numpy on Linux, acquire administrator rights and then type in a terminal:

```python pip install numpy```

On Windows, administrator rights are not required, and the command is instead:

```pip install numpy```

Once these are installed, open a terminal on Linux or MacOS (or command prompt on Windows) and enter:

```python radiohm.py```

Moreover, on Windows, you can simply double-click on the ```radiohm.py``` file.


### License

This program is distributed under the GNU GPLv3 licence.  The details of this license can be found in the `LICENSE` file.
The short version is that you are free to use this software, to modify its source code, and to redistribute it in either its original or modified form.  However, you have to give those same rights to the users of the redistributed software.

The source code is available on [GitHub](https://github.com/Pattedetable/radiohm).

This software uses libraries from Qt under the LGPLv3, Python, Numpy and Matplotlib.
