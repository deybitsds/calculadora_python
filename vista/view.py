
import sys
from vista.main_window import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPropertyAnimation

from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt

class View(QtWidgets.QMainWindow):

    def __init__(self, controller = None):

        super().__init__()

        # instanciar la ventana principal
        self.ui = Ui_MainWindow() 
        self.ui.setupUi(self)

        # recuperar el controlador
        self.controller = controller

        # Eliminar barra y de título - opacidad
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)

        # Redimensionar ventana con tamaño de control 10 de redimensionamiento del widget.
        self.gripSize = 10
        # Crear control para usuario -> redimensionar
        self.grip = QtWidgets.QSizeGrip(self)
        # Ajustamos el tamaño visual del control de redimensionamiento.
        self.grip.resize(self.gripSize, self.gripSize)

        # Mover ventana -> usuario
        self.ui.fr_cerrar.mouseMoveEvent = self.mover_ventana

        # Gestion botones de Barra de control
        self.ui.bt_minimizar.clicked.connect(self.control_bt_minimizar)        
        self.ui.bt_reducir.clicked.connect(self.control_bt_normal)
        self.ui.bt_expandir.clicked.connect(self.control_bt_maximizar)
        self.ui.bt_cerrar.clicked.connect(lambda: self.close())

        # escondemos el boton reducir
        self.ui.bt_reducir.hide()

        # mostramos la ventana principal
        self.show()


    # funcion que actualiza el label input en base a la cadena principal del modelo
    def actualizar_input(self):

        # recuperamos del controlador el input
        cadena = self.controller.recuperar_input()
        
        # establecemos el label txt_input
        self.ui.txt_input.setText(cadena)


    # funcion que dado un resultado lo ingresa en el label output
    def mostrar_resultado(self, resultado):

        # establecemos el label txt_output
        self.ui.txt_output.setText(resultado)


    # funcion que establece el label output en "0" 
    def limpiar(self):

        # establecemos el label txt_output
        self.ui.txt_output.setText("0")


    # funcion que minimiza la app
    def control_bt_minimizar(self):

        # minimizar ventana principal
        self.showMinimized()        


    # funcion que reestablece el tamaño de la app
    def control_bt_normal(self):

        # mostrar ventana tamaño "normal"
        self.showNormal()        

        # intercalar vista
        self.ui.bt_reducir.hide()
        self.ui.bt_expandir.show()


    # funcion que maximiza la app
    def control_bt_maximizar(self): 

        # mostrar ventana tamaño "maximizado"
        self.showMaximized()
        # intercalar vista
        self.ui.bt_expandir.hide()
        self.ui.bt_reducir.show()

    
    # evento de redimensionar
    def resizeEvent(self, event):

        rect = self.rect()
        self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)

    
    # modulos mover la ventana
    def mousePressEvent(self, event):

        # recuperar la posicion global de la ventana
        self.clickPosition = event.globalPos()


    # modulo para la gestion del movimiento de la ventana
    def mover_ventana(self, event):

        # caso la ventana no este maximizada
        if not self.isMaximized():     
            # podemos redimensionar 
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.clickPosition)
                self.clickPosition = event.globalPos()
                event.accept()

        # caso la ventana este "muy arriba"
        if event.globalPos().y() <= 20:
            self.showMaximized()
        else:
            # caso ocurra ningun evento
            self.showNormal()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mi_app = View()
    mi_app.show()
    sys.exit(app.exec_())