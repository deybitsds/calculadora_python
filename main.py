
from controlador.controller import *

class App:
    def __init__(self):
        # Crear una instancia de la aplicación Qt
        app = QtWidgets.QApplication(sys.argv)
        
        # Crear una instancia de la clase Controller
        control = Controller()
        
        # Ejecutar el bucle principal de la aplicación y salir cuando se cierre
        sys.exit(app.exec_())

if __name__ == "__main__":
    App()
