from PySide2.QtWidgets import QApplication, QMainWindow
from Interfacegrafica import Ui_MainWindow
from PySide2.QtCore import Slot
from estudiante import Estudiante
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.registros = []
        self.regcount = 0

        self.ui.Registro.clicked.connect(self.registrar)
    @Slot()
    def registrar(self):
        print(f"Nombre:{self.ui.nombre.text()}\nCorreo:{self.ui.correo.text()}\nContrasena:{self.ui.contrasena.text()}")
        tmp = Estudiante(self.ui.nombre.text(),self.ui.correo.text(), self.ui.contrasena.text())
        print(tmp)

        self.registros.append(tmp)


    """@Slot()
    def mostrartxt(self):
        for i in self.registros:
            print(i)"""

if __name__ == '__main__':
    app = QApplication()

    window = MainWindow()
    window.show()

    app.exec_()