
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPropertyAnimation

from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt

class View(QtWidgets.QMainWindow):
    def __init__(self, controller = None):
        super().__init__()
        self.ui = Ui_MainWindow() 
        self.ui.setupUi(self)

        self.controller = controller

        # Eliminar barra y de título - opacidad
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)

        # SizeGrip
        self.gripSize = 10
        self.grip = QtWidgets.QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)

        # Mover ventana
        self.ui.fr_cerrar.mouseMoveEvent = self.mover_ventana

        # Barra de control
        self.ui.bt_minimizar.clicked.connect(self.control_bt_minimizar)        
        self.ui.bt_reducir.clicked.connect(self.control_bt_normal)
        self.ui.bt_expandir.clicked.connect(self.control_bt_maximizar)
        self.ui.bt_cerrar.clicked.connect(lambda: self.close())

        self.ui.bt_reducir.hide()

        self.show()

    def actualizar_input(self):
        cadena = self.controller.recuperar_input()
        self.ui.txt_input.setText(cadena)

    def mostrar_resultado(self, resultado):
        self.ui.txt_output.setText(resultado)

    def limpiar(self):
        self.ui.txt_output.setText("0.0")

    def control_bt_minimizar(self):
        self.showMinimized()        

    def control_bt_normal(self): 
        self.showNormal()        
        self.ui.bt_reducir.hide()
        self.ui.bt_expandir.show()

    def control_bt_maximizar(self): 
        self.showMaximized()
        self.ui.bt_expandir.hide()
        self.ui.bt_reducir.show()

    # SizeGrip
    def resizeEvent(self, event):
        rect = self.rect()
        self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)

    # Mover ventana
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()
        
    def mover_ventana(self, event):
        if not self.isMaximized():            
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.clickPosition)
                self.clickPosition = event.globalPos()
                event.accept()

        if event.globalPos().y() <= 20:
            self.showMaximized()
        else:
            self.showNormal()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 660)
        MainWindow.setMinimumSize(QtCore.QSize(450, 660))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(67, 105, 128);")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.fr_cerrar = QtWidgets.QFrame(self.centralwidget)
        self.fr_cerrar.setMinimumSize(QtCore.QSize(450, 40))
        self.fr_cerrar.setMaximumSize(QtCore.QSize(16777215, 40))
        self.fr_cerrar.setStyleSheet("border:0px;")
        self.fr_cerrar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_cerrar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_cerrar.setObjectName("fr_cerrar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.fr_cerrar)
        self.horizontalLayout.setContentsMargins(5, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.icono = QtWidgets.QLabel(self.fr_cerrar)
        self.icono.setMinimumSize(QtCore.QSize(26, 26))
        self.icono.setMaximumSize(QtCore.QSize(26, 26))
        self.icono.setText("")
        self.icono.setPixmap(QtGui.QPixmap("vista/images/icon.png"))
        self.icono.setScaledContents(True)
        self.icono.setIndent(-1)
        self.icono.setObjectName("icono")
        self.horizontalLayout.addWidget(self.icono)
        self.titulo = QtWidgets.QLabel(self.fr_cerrar)
        self.titulo.setStyleSheet("border:none;\n"
"font: 12pt \"Montserrat\";\n"
"color: rgb(255, 255, 255);")
        self.titulo.setObjectName("titulo")
        self.horizontalLayout.addWidget(self.titulo)
        spacerItem = QtWidgets.QSpacerItem(295, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.bt_llaves2 = QtWidgets.QPushButton(self.fr_cerrar)
        self.bt_llaves2.setMinimumSize(QtCore.QSize(1, 1))
        self.bt_llaves2.setMaximumSize(QtCore.QSize(1, 1))
        self.bt_llaves2.setStyleSheet("QPushButton{\n"
"border:0px;\n"
"}")
        self.bt_llaves2.setText("")
        self.bt_llaves2.setObjectName("bt_llaves2")
        self.horizontalLayout.addWidget(self.bt_llaves2)
        self.bt_corchetes2 = QtWidgets.QPushButton(self.fr_cerrar)
        self.bt_corchetes2.setMinimumSize(QtCore.QSize(1, 1))
        self.bt_corchetes2.setMaximumSize(QtCore.QSize(1, 1))
        self.bt_corchetes2.setStyleSheet("QPushButton{\n"
"border:0px;\n"
"}")
        self.bt_corchetes2.setText("")
        self.bt_corchetes2.setObjectName("bt_corchetes2")
        self.horizontalLayout.addWidget(self.bt_corchetes2)
        self.bt_parentesis2 = QtWidgets.QPushButton(self.fr_cerrar)
        self.bt_parentesis2.setMinimumSize(QtCore.QSize(1, 1))
        self.bt_parentesis2.setMaximumSize(QtCore.QSize(1, 1))
        self.bt_parentesis2.setStyleSheet("QPushButton{\n"
"border:0px;\n"
"}")
        self.bt_parentesis2.setText("")
        self.bt_parentesis2.setObjectName("bt_parentesis2")
        self.horizontalLayout.addWidget(self.bt_parentesis2)
        self.bt_minimizar = QtWidgets.QPushButton(self.fr_cerrar)
        self.bt_minimizar.setMinimumSize(QtCore.QSize(40, 40))
        self.bt_minimizar.setMaximumSize(QtCore.QSize(40, 40))
        self.bt_minimizar.setStyleSheet("QPushButton{\n"
"border:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:0px;\n"
"background-color:rgb(139, 175, 191);\n"
"}")
        self.bt_minimizar.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("vista/images/minimizar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_minimizar.setIcon(icon)
        self.bt_minimizar.setIconSize(QtCore.QSize(40, 40))
        self.bt_minimizar.setObjectName("bt_minimizar")
        self.horizontalLayout.addWidget(self.bt_minimizar)
        self.bt_reducir = QtWidgets.QPushButton(self.fr_cerrar)
        self.bt_reducir.setMinimumSize(QtCore.QSize(40, 40))
        self.bt_reducir.setMaximumSize(QtCore.QSize(40, 40))
        self.bt_reducir.setStyleSheet("QPushButton{\n"
"border:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:0px;\n"
"background-color:rgb(139, 175, 191);\n"
"}")
        self.bt_reducir.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("vista/images/reducir.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_reducir.setIcon(icon1)
        self.bt_reducir.setIconSize(QtCore.QSize(40, 40))
        self.bt_reducir.setObjectName("bt_reducir")
        self.horizontalLayout.addWidget(self.bt_reducir)
        self.bt_expandir = QtWidgets.QPushButton(self.fr_cerrar)
        self.bt_expandir.setMinimumSize(QtCore.QSize(40, 40))
        self.bt_expandir.setMaximumSize(QtCore.QSize(40, 40))
        self.bt_expandir.setStyleSheet("QPushButton{\n"
"border:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:0px;\n"
"background-color:rgb(139, 175, 191);\n"
"}")
        self.bt_expandir.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("vista/images/expandir.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_expandir.setIcon(icon2)
        self.bt_expandir.setIconSize(QtCore.QSize(40, 40))
        self.bt_expandir.setObjectName("bt_expandir")
        self.horizontalLayout.addWidget(self.bt_expandir)
        self.bt_cerrar = QtWidgets.QPushButton(self.fr_cerrar)
        self.bt_cerrar.setMinimumSize(QtCore.QSize(40, 40))
        self.bt_cerrar.setMaximumSize(QtCore.QSize(40, 40))
        self.bt_cerrar.setStyleSheet("QPushButton{\n"
"border:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:0px;\n"
"background-color:#ff0000;\n"
"}")
        self.bt_cerrar.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("vista/images/cerrar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_cerrar.setIcon(icon3)
        self.bt_cerrar.setIconSize(QtCore.QSize(32, 32))
        self.bt_cerrar.setObjectName("bt_cerrar")
        self.horizontalLayout.addWidget(self.bt_cerrar)
        self.verticalLayout.addWidget(self.fr_cerrar)
        self.fr_input = QtWidgets.QFrame(self.centralwidget)
        self.fr_input.setMinimumSize(QtCore.QSize(450, 60))
        self.fr_input.setMaximumSize(QtCore.QSize(16777215, 60))
        self.fr_input.setStyleSheet("border:0px;")
        self.fr_input.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_input.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_input.setObjectName("fr_input")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.fr_input)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.txt_input = QtWidgets.QLabel(self.fr_input)
        self.txt_input.setStyleSheet("color:rgb(255,255,255);\n"
"font:  30pt \"Montserrat\";")
        self.txt_input.setText("")
        self.txt_input.setObjectName("txt_input")

        # Configurar alineación del texto a la derecha
        self.txt_input.setAlignment(QtCore.Qt.AlignRight)

        # Opcional: también puedes configurar la dirección del texto
        self.txt_input.setLayoutDirection(QtCore.Qt.RightToLeft)
        
        self.horizontalLayout_7.addWidget(self.txt_input)
        self.verticalLayout.addWidget(self.fr_input)
        self.fr_output = QtWidgets.QFrame(self.centralwidget)
        self.fr_output.setMinimumSize(QtCore.QSize(450, 80))
        self.fr_output.setMaximumSize(QtCore.QSize(16777215, 80))
        self.fr_output.setStyleSheet("border:0px;")
        self.fr_output.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_output.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_output.setObjectName("fr_output")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.fr_output)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.txt_output = QtWidgets.QLabel(self.fr_output)
        self.txt_output.setStyleSheet("color:rgb(255,255,255);\n"
"font:  Bold 45pt \"Montserrat\";")
        self.txt_output.setText("")
        self.txt_output.setObjectName("txt_output")

        # Configurar alineación del texto a la derecha
        self.txt_output.setAlignment(QtCore.Qt.AlignRight)

        # Opcional: también puedes configurar la dirección del texto
        self.txt_output.setLayoutDirection(QtCore.Qt.RightToLeft)

        self.horizontalLayout_8.addWidget(self.txt_output, 0, QtCore.Qt.AlignVCenter)
        self.verticalLayout.addWidget(self.fr_output)
        self.fr_clear = QtWidgets.QFrame(self.centralwidget)
        self.fr_clear.setMinimumSize(QtCore.QSize(450, 86))
        self.fr_clear.setMaximumSize(QtCore.QSize(1920, 117))
        self.fr_clear.setStyleSheet("border:0px;")
        self.fr_clear.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_clear.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_clear.setObjectName("fr_clear")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.fr_clear)
        self.horizontalLayout_6.setContentsMargins(4, 0, 4, 0)
        self.horizontalLayout_6.setSpacing(4)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.bt_rehacer = QtWidgets.QPushButton(self.fr_clear)
        self.bt_rehacer.setMinimumSize(QtCore.QSize(0, 80))
        self.bt_rehacer.setStyleSheet("QPushButton{\n"
"border:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:0px;\n"
"border-radius:20px;\n"
"background-color:rgb(139, 175, 191);\n"
"}")
        self.bt_rehacer.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("vista/images/redo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_rehacer.setIcon(icon4)
        self.bt_rehacer.setIconSize(QtCore.QSize(48, 48))
        self.bt_rehacer.setCheckable(False)
        self.bt_rehacer.setObjectName("bt_rehacer")
        self.horizontalLayout_6.addWidget(self.bt_rehacer)
        self.bt_deshacer = QtWidgets.QPushButton(self.fr_clear)
        self.bt_deshacer.setMinimumSize(QtCore.QSize(0, 80))
        self.bt_deshacer.setStyleSheet("QPushButton{\n"
"border:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:0px;\n"
"border-radius:20px;\n"
"background-color:rgb(139, 175, 191);\n"
"}")
        self.bt_deshacer.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("vista/images/undo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_deshacer.setIcon(icon5)
        self.bt_deshacer.setIconSize(QtCore.QSize(48, 48))
        self.bt_deshacer.setCheckable(False)
        self.bt_deshacer.setObjectName("bt_deshacer")
        self.horizontalLayout_6.addWidget(self.bt_deshacer)
        self.bt_limpiar = QtWidgets.QPushButton(self.fr_clear)
        self.bt_limpiar.setMinimumSize(QtCore.QSize(140, 70))
        self.bt_limpiar.setStyleSheet("QPushButton{\n"
"border-radius:20px;\n"
"border: 1px solid rgb(255, 255, 255);\n"
"color:rgb(255,255,255);\n"
"font:  20pt \"Montserrat\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:0px;\n"
"border-radius:20px;\n"
"background-color:rgb(255, 0, 0);\n"
"}")
        self.bt_limpiar.setObjectName("bt_limpiar")
        self.horizontalLayout_6.addWidget(self.bt_limpiar)
        self.bt_borrar = QtWidgets.QPushButton(self.fr_clear)
        self.bt_borrar.setMinimumSize(QtCore.QSize(0, 80))
        self.bt_borrar.setStyleSheet("QPushButton{\n"
"border:0px;\n"
"border-radius:20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:0px;\n"
"background-color:rgb(139, 175, 191);\n"
"}")
        self.bt_borrar.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("vista/images/borrar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_borrar.setIcon(icon6)
        self.bt_borrar.setIconSize(QtCore.QSize(48, 48))
        self.bt_borrar.setCheckable(False)
        self.bt_borrar.setObjectName("bt_borrar")
        self.horizontalLayout_6.addWidget(self.bt_borrar)
        self.verticalLayout.addWidget(self.fr_clear)
        self.fr_789 = QtWidgets.QFrame(self.centralwidget)
        self.fr_789.setMinimumSize(QtCore.QSize(450, 100))
        self.fr_789.setMaximumSize(QtCore.QSize(1920, 133))
        self.fr_789.setStyleSheet("border:0px;")
        self.fr_789.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_789.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_789.setObjectName("fr_789")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.fr_789)
        self.horizontalLayout_5.setContentsMargins(4, 0, 4, 0)
        self.horizontalLayout_5.setSpacing(4)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.bt_parentesis = QtWidgets.QPushButton(self.fr_789)
        self.bt_parentesis.setMinimumSize(QtCore.QSize(78, 92))
        self.bt_parentesis.setStyleSheet("QPushButton {\n"
"    background-color: rgb(26, 30, 39);\n"
"    border-radius: 15px;\n"
"    color: rgb(54, 105, 110);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(139, 175, 191);\n"
"}")
        self.bt_parentesis.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("vista/images/parentesis.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_parentesis.setIcon(icon7)
        self.bt_parentesis.setIconSize(QtCore.QSize(48, 48))
        self.bt_parentesis.setObjectName("bt_parentesis")
        self.horizontalLayout_5.addWidget(self.bt_parentesis)
        self.bt_7 = QtWidgets.QPushButton(self.fr_789)
        self.bt_7.setMinimumSize(QtCore.QSize(78, 92))
        self.bt_7.setStyleSheet("QPushButton {\n"
"    background-color: rgb(139, 175, 191);\n"
"    border-radius: 15px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 30pt \"Montserrat\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(26, 30, 39);\n"
"}")
        self.bt_7.setObjectName("bt_7")
        self.horizontalLayout_5.addWidget(self.bt_7)
        self.bt_8 = QtWidgets.QPushButton(self.fr_789)
        self.bt_8.setMinimumSize(QtCore.QSize(78, 92))
        self.bt_8.setStyleSheet("QPushButton {\n"
"    background-color: rgb(139, 175, 191);\n"
"    border-radius: 15px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 30pt \"Montserrat\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(26, 30, 39);\n"
"}")
        self.bt_8.setObjectName("bt_8")
        self.horizontalLayout_5.addWidget(self.bt_8)
        self.bt_9 = QtWidgets.QPushButton(self.fr_789)
        self.bt_9.setMinimumSize(QtCore.QSize(78, 92))
        self.bt_9.setStyleSheet("QPushButton {\n"
"    background-color: rgb(139, 175, 191);\n"
"    border-radius: 15px;\n"
"    color: rgb(255, 255, 255);\n"
"    font:  30pt \"Montserrat\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(26, 30, 39);\n"
"}")
        self.bt_9.setObjectName("bt_9")
        self.horizontalLayout_5.addWidget(self.bt_9)
        self.bt_sum = QtWidgets.QPushButton(self.fr_789)
        self.bt_sum.setMinimumSize(QtCore.QSize(78, 92))
        self.bt_sum.setStyleSheet("QPushButton {\n"
"    background-color: rgb(26, 30, 39);\n"
"    border-radius: 15px;\n"
"    color: rgb(54, 105, 110);\n"
"    font: 30pt \"Montserrat\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(139, 175, 191);\n"
"}\n"
"")
        self.bt_sum.setObjectName("bt_sum")
        self.horizontalLayout_5.addWidget(self.bt_sum)
        self.verticalLayout.addWidget(self.fr_789)
        self.fr_456 = QtWidgets.QFrame(self.centralwidget)
        self.fr_456.setMinimumSize(QtCore.QSize(450, 96))
        self.fr_456.setMaximumSize(QtCore.QSize(1920, 129))
        self.fr_456.setStyleSheet("border:0px;")
        self.fr_456.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_456.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_456.setObjectName("fr_456")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.fr_456)
        self.horizontalLayout_4.setContentsMargins(4, 0, 4, 0)
        self.horizontalLayout_4.setSpacing(4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.bt_llaves = QtWidgets.QPushButton(self.fr_456)
        self.bt_llaves.setMinimumSize(QtCore.QSize(78, 92))
        self.bt_llaves.setStyleSheet("QPushButton {\n"
"    background-color: rgb(26, 30, 39);\n"
"    border-radius: 15px;\n"
"    color: rgb(54, 105, 110);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(139, 175, 191);\n"
"}")
        self.bt_llaves.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("vista/images/llaves.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_llaves.setIcon(icon8)
        self.bt_llaves.setIconSize(QtCore.QSize(48, 48))
        self.bt_llaves.setObjectName("bt_llaves")
        self.horizontalLayout_4.addWidget(self.bt_llaves)
        self.bt_4 = QtWidgets.QPushButton(self.fr_456)
        self.bt_4.setMinimumSize(QtCore.QSize(78, 92))
        self.bt_4.setStyleSheet("QPushButton {\n"
"    background-color: rgb(139, 175, 191);\n"
"    border-radius: 15px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 30pt \"Montserrat\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(26, 30, 39);\n"
"}")
        self.bt_4.setObjectName("bt_4")
        self.horizontalLayout_4.addWidget(self.bt_4)
        self.bt_5 = QtWidgets.QPushButton(self.fr_456)
        self.bt_5.setMinimumSize(QtCore.QSize(78, 92))
        self.bt_5.setStyleSheet("QPushButton {\n"
"    background-color: rgb(139, 175, 191);\n"
"    border-radius: 15px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 30pt \"Montserrat\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(26, 30, 39);\n"
"}")
        self.bt_5.setObjectName("bt_5")
        self.horizontalLayout_4.addWidget(self.bt_5)
        self.bt_6 = QtWidgets.QPushButton(self.fr_456)
        self.bt_6.setMinimumSize(QtCore.QSize(78, 92))
        self.bt_6.setStyleSheet("QPushButton {\n"
"    background-color: rgb(139, 175, 191);\n"
"    border-radius: 15px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 30pt \"Montserrat\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(26, 30, 39);\n"
"}")
        self.bt_6.setObjectName("bt_6")
        self.horizontalLayout_4.addWidget(self.bt_6)
        self.bt_dif = QtWidgets.QPushButton(self.fr_456)
        self.bt_dif.setMinimumSize(QtCore.QSize(78, 92))
        self.bt_dif.setStyleSheet("QPushButton {\n"
"    background-color: rgb(26, 30, 39);\n"
"    border-radius: 15px;\n"
"    color: rgb(54, 105, 110);\n"
"    font:30pt \"Montserrat\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(139, 175, 191);\n"
"}\n"
"")
        self.bt_dif.setObjectName("bt_dif")
        self.horizontalLayout_4.addWidget(self.bt_dif)
        self.verticalLayout.addWidget(self.fr_456)
        self.fr_123 = QtWidgets.QFrame(self.centralwidget)
        self.fr_123.setMinimumSize(QtCore.QSize(450, 96))
        self.fr_123.setMaximumSize(QtCore.QSize(16777215, 129))
        self.fr_123.setStyleSheet("border:0px;")
        self.fr_123.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_123.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_123.setObjectName("fr_123")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.fr_123)
        self.horizontalLayout_3.setContentsMargins(4, 0, 4, 0)
        self.horizontalLayout_3.setSpacing(4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.bt_corchetes = QtWidgets.QPushButton(self.fr_123)
        self.bt_corchetes.setMinimumSize(QtCore.QSize(78, 92))
        self.bt_corchetes.setStyleSheet("QPushButton {\n"
"    background-color: rgb(26, 30, 39);\n"
"    border-radius: 15px;\n"
"    color: rgb(54, 105, 110);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(139, 175, 191);\n"
"}")
        self.bt_corchetes.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("vista/images/corchetes.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_corchetes.setIcon(icon9)
        self.bt_corchetes.setIconSize(QtCore.QSize(48, 48))
        self.bt_corchetes.setObjectName("bt_corchetes")
        self.horizontalLayout_3.addWidget(self.bt_corchetes)
        self.bt_1 = QtWidgets.QPushButton(self.fr_123)
        self.bt_1.setMinimumSize(QtCore.QSize(78, 92))
        self.bt_1.setStyleSheet("QPushButton {\n"
"    background-color: rgb(139, 175, 191);\n"
"    border-radius: 15px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 30pt \"Montserrat\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(26, 30, 39);\n"
"}")
        self.bt_1.setObjectName("bt_1")
        self.horizontalLayout_3.addWidget(self.bt_1)
        self.bt_2 = QtWidgets.QPushButton(self.fr_123)
        self.bt_2.setMinimumSize(QtCore.QSize(78, 92))
        self.bt_2.setStyleSheet("QPushButton {\n"
"    background-color: rgb(139, 175, 191);\n"
"    border-radius: 15px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 30pt \"Montserrat\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(26, 30, 39);\n"
"}")
        self.bt_2.setObjectName("bt_2")
        self.horizontalLayout_3.addWidget(self.bt_2)
        self.bt_3 = QtWidgets.QPushButton(self.fr_123)
        self.bt_3.setMinimumSize(QtCore.QSize(78, 92))
        self.bt_3.setStyleSheet("QPushButton {\n"
"    background-color: rgb(139, 175, 191);\n"
"    border-radius: 15px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 30pt \"Montserrat\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(26, 30, 39);\n"
"}")
        self.bt_3.setObjectName("bt_3")
        self.horizontalLayout_3.addWidget(self.bt_3)
        self.bt_mul = QtWidgets.QPushButton(self.fr_123)
        self.bt_mul.setMinimumSize(QtCore.QSize(78, 92))
        self.bt_mul.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.bt_mul.setStyleSheet("QPushButton {\n"
"    background-color: rgb(26, 30, 39);\n"
"    border-radius: 15px;\n"
"    color: rgb(54, 105, 110);\n"
"    font:30pt \"Montserrat\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(139, 175, 191);\n"
"}\n"
"")
        self.bt_mul.setObjectName("bt_mul")
        self.horizontalLayout_3.addWidget(self.bt_mul)
        self.verticalLayout.addWidget(self.fr_123)
        self.fr_0 = QtWidgets.QFrame(self.centralwidget)
        self.fr_0.setMinimumSize(QtCore.QSize(450, 102))
        self.fr_0.setMaximumSize(QtCore.QSize(16777215, 135))
        self.fr_0.setStyleSheet("border:0px;")
        self.fr_0.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_0.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_0.setObjectName("fr_0")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.fr_0)
        self.horizontalLayout_2.setContentsMargins(4, 0, 4, 4)
        self.horizontalLayout_2.setSpacing(4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.bt_pow = QtWidgets.QPushButton(self.fr_0)
        self.bt_pow.setMinimumSize(QtCore.QSize(78, 92))
        self.bt_pow.setStyleSheet("QPushButton {\n"
"    background-color: rgb(26, 30, 39);\n"
"    border-radius: 15px;\n"
"    color: rgb(54, 105, 110);\n"
"    font: 48pt \"DejaVu Sans\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(139, 175, 191);\n"
"}")
        self.bt_pow.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("vista/images/pow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_pow.setIcon(icon10)
        self.bt_pow.setIconSize(QtCore.QSize(40, 40))
        self.bt_pow.setObjectName("bt_pow")
        self.horizontalLayout_2.addWidget(self.bt_pow)
        self.bt_0 = QtWidgets.QPushButton(self.fr_0)
        self.bt_0.setMinimumSize(QtCore.QSize(78, 92))
        self.bt_0.setStyleSheet("QPushButton {\n"
"    background-color: rgb(139, 175, 191);\n"
"    border-radius: 15px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 30pt \"Montserrat\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(26, 30, 39);\n"
"}")
        self.bt_0.setObjectName("bt_0")
        self.horizontalLayout_2.addWidget(self.bt_0)
        self.bt_punto = QtWidgets.QPushButton(self.fr_0)
        self.bt_punto.setMinimumSize(QtCore.QSize(78, 92))
        self.bt_punto.setStyleSheet("QPushButton {\n"
"    background-color: rgb(139, 175, 191);\n"
"    border-radius: 15px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 30pt \"Montserrat\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(26, 30, 39);\n"
"}")
        self.bt_punto.setObjectName("bt_punto")
        self.horizontalLayout_2.addWidget(self.bt_punto)
        self.bt_div = QtWidgets.QPushButton(self.fr_0)
        self.bt_div.setMinimumSize(QtCore.QSize(78, 92))
        self.bt_div.setStyleSheet("QPushButton {\n"
"    background-color: rgb(26, 30, 39);\n"
"    border-radius: 15px;\n"
"    color: rgb(54, 105, 110);\n"
"    font:30pt \"Montserrat\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(139, 175, 191);\n"
"}\n"
"")
        self.bt_div.setObjectName("bt_div")
        self.horizontalLayout_2.addWidget(self.bt_div)
        self.bt_resul = QtWidgets.QPushButton(self.fr_0)
        self.bt_resul.setMinimumSize(QtCore.QSize(78, 92))
        self.bt_resul.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.bt_resul.setStyleSheet("QPushButton {\n"
"    background-color: rgb(54, 105, 110);\n"
"    border-radius: 15px;\n"
"    color: rgb(255, 255, 255);\n"
"    border: 1px solid rgb(255, 255, 255);\n"
"    font: Bold 30pt \"Montserrat\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(139, 175, 191);\n"
"}\n"
"")
        self.bt_resul.setObjectName("bt_resul")
        self.horizontalLayout_2.addWidget(self.bt_resul)
        self.verticalLayout.addWidget(self.fr_0)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.titulo.setText(_translate("MainWindow", " Calculadora"))
        self.bt_llaves2.setShortcut(_translate("MainWindow", "}"))
        self.bt_corchetes2.setShortcut(_translate("MainWindow", "Space"))
        self.bt_parentesis2.setShortcut(_translate("MainWindow", ")"))
        self.bt_rehacer.setShortcut(_translate("MainWindow", "Ctrl+Y"))
        self.bt_deshacer.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.bt_limpiar.setText(_translate("MainWindow", "CLEAR"))
        self.bt_limpiar.setShortcut(_translate("MainWindow", "Ctrl+Del"))
        self.bt_borrar.setShortcut(_translate("MainWindow", "Backspace"))
        self.bt_parentesis.setShortcut(_translate("MainWindow", "("))
        self.bt_7.setText(_translate("MainWindow", "7"))
        self.bt_7.setShortcut(_translate("MainWindow", "7"))
        self.bt_8.setText(_translate("MainWindow", "8"))
        self.bt_8.setShortcut(_translate("MainWindow", "8"))
        self.bt_9.setText(_translate("MainWindow", "9"))
        self.bt_9.setShortcut(_translate("MainWindow", "9"))
        self.bt_sum.setText(_translate("MainWindow", "+"))
        self.bt_sum.setShortcut(_translate("MainWindow", "+"))
        self.bt_llaves.setShortcut(_translate("MainWindow", "{"))
        self.bt_4.setText(_translate("MainWindow", "4"))
        self.bt_4.setShortcut(_translate("MainWindow", "4"))
        self.bt_5.setText(_translate("MainWindow", "5"))
        self.bt_5.setShortcut(_translate("MainWindow", "5"))
        self.bt_6.setText(_translate("MainWindow", "6"))
        self.bt_6.setShortcut(_translate("MainWindow", "6"))
        self.bt_dif.setText(_translate("MainWindow", "-"))
        self.bt_dif.setShortcut(_translate("MainWindow", "-"))
        self.bt_corchetes.setShortcut(_translate("MainWindow", "["))
        self.bt_1.setText(_translate("MainWindow", "1"))
        self.bt_1.setShortcut(_translate("MainWindow", "1"))
        self.bt_2.setText(_translate("MainWindow", "2"))
        self.bt_2.setShortcut(_translate("MainWindow", "2"))
        self.bt_3.setText(_translate("MainWindow", "3"))
        self.bt_3.setShortcut(_translate("MainWindow", "3"))
        self.bt_mul.setText(_translate("MainWindow", "x"))
        self.bt_mul.setShortcut(_translate("MainWindow", "*"))
        self.bt_pow.setShortcut(_translate("MainWindow", "Alt+9, Alt+4"))
        self.bt_0.setText(_translate("MainWindow", "0"))
        self.bt_0.setShortcut(_translate("MainWindow", "0"))
        self.bt_punto.setText(_translate("MainWindow", "."))
        self.bt_punto.setShortcut(_translate("MainWindow", "."))
        self.bt_div.setText(_translate("MainWindow", "/"))
        self.bt_div.setShortcut(_translate("MainWindow", "/"))
        self.bt_resul.setText(_translate("MainWindow", "="))
        self.bt_resul.setShortcut(_translate("MainWindow", "Return"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mi_app = View()
    mi_app.show()
    sys.exit(app.exec_())