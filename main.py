
from controlador.controller import *
import traceback

class App:
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        control = Controller()
        sys.exit(app.exec_())	

if __name__ == "__main__":
    App()


