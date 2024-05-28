
from vista.view import *
from modelo.model import *

class Controller:
    def __init__(self):
        self.view = View(self)
        self.model = Model()

        # Gestion de botones
        self.view.ui.bt_0.clicked.connect(self.view.actualizar_input)
        self.view.ui.bt_1.clicked.connect(self.view.actualizar_output)
        self.view.ui.bt_2.clicked.connect(self.view.actualizar_output)
        self.view.ui.bt_3.clicked.connect(self.view.actualizar_output)
        self.view.ui.bt_4.clicked.connect(self.view.actualizar_output)
        self.view.ui.bt_5.clicked.connect(self.view.actualizar_output)
        self.view.ui.bt_6.clicked.connect(self.view.actualizar_output)
        self.view.ui.bt_7.clicked.connect(self.view.actualizar_output)
        self.view.ui.bt_8.clicked.connect(self.view.actualizar_output)
        self.view.ui.bt_9.clicked.connect(self.view.actualizar_output)
        self.view.ui.bt_punto.clicked.connect(self.view.actualizar_output)


    def recuperar_input(self):
        return self.model.recuperar_input()

    def recuperar_output(self):
        return self.model.recuperar_output()
    

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    control = Controller()
    sys.exit(app.exec_())	