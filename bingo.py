import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QTableWidget, QTableWidgetItem, QLabel, QLineEdit, QPushButton, QMessageBox, QHeaderView, QHBoxLayout, QSpacerItem, QSizePolicy  
from PyQt5.QtGui import QColor, QFont
from PyQt5.QtCore import Qt

class MatrizBingo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bingo")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.label = QLabel("Registro de números de Bingo")
        self.layout.addWidget(self.label)

        self.table = QTableWidget()
        self.table.setSelectionMode(QTableWidget.NoSelection)  
        self.layout.addWidget(self.table)

        letras = ["B", "I", "N", "G", "O"]
        self.colores_filas = [QColor("#000000"), QColor("#000000"), QColor("#000000"), QColor("#000000"), QColor("#000000")]

        self.table.setRowCount(len(letras))
        self.table.setColumnCount(15)

        font = QFont("Arial", weight=QFont.Bold)  
        font.setPointSize(24)  
        for i, letra in enumerate(letras):
            item_letra = QTableWidgetItem(letra)
            item_letra.setBackground(self.colores_filas[i])
            item_letra.setFont(font)  
            self.table.setVerticalHeaderItem(i, item_letra)

        for i in range(len(letras)):
            for j in range(15):
                item_numero = QTableWidgetItem(str(i * 15 + j + 1))
                item_numero.setTextAlignment(Qt.AlignCenter)  
                self.table.setItem(i, j, item_numero)
                item_numero.setForeground(QColor("white"))
                item_numero.setFont(QFont("Arial", 16))  

        self.table.horizontalHeader().hide()
        self.table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.setWindowFlag(Qt.WindowMaximizeButtonHint, True)

        balota_layout = QHBoxLayout()

        balota_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

        self.label_balota = QLabel("BALOTA:")
        font = QFont("Arial", 14, weight=QFont.Bold)  
        self.label_balota.setFont(font)
        balota_layout.addWidget(self.label_balota)

        self.entry_numero = QLineEdit()
        self.entry_numero.setFixedWidth(100)  
        self.entry_numero.setFont(QFont("Arial", 12))  
        balota_layout.addWidget(self.entry_numero)

        balota_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

        self.layout.addLayout(balota_layout)

        self.btn_verificar = QPushButton("Verificar")
        self.btn_verificar.clicked.connect(self.verificar_numero)
        self.btn_verificar.setFont(QFont("Arial", 14, weight=QFont.Bold))  
        self.layout.addWidget(self.btn_verificar)

        self.btn_limpiar = QPushButton("Limpiar Tablero")
        self.btn_limpiar.clicked.connect(self.confirmar_limpiar_tablero)
        self.btn_limpiar.setFont(QFont("Arial", 14, weight=QFont.Bold))  
        self.layout.addWidget(self.btn_limpiar)

        # Botón para corregir el último valor digitado
        self.btn_corregir = QPushButton("Corregir último")
        self.btn_corregir.clicked.connect(self.corregir_ultimo)
        self.btn_corregir.setFont(QFont("Arial", 14, weight=QFont.Bold))  
        self.layout.addWidget(self.btn_corregir)

        hecho_por_label = QLabel("Hecho por: CRISTIAN7712")
        hecho_por_label.setAlignment(Qt.AlignCenter)
        hecho_por_label.setStyleSheet("color: rgba(0, 0, 0, 100);")  
        self.layout.addWidget(hecho_por_label)

        self.resize(800, 600)

        self.ultimo_numero = None  # Variable para almacenar el último número ingresado

    def closeEvent(self, event):
        respuesta = QMessageBox.question(self, "Cerrar aplicación", "¿Está seguro de que desea salir de la aplicación?", 
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if respuesta == QMessageBox.Yes:
            event.accept()  
        else:
            event.ignore()  

    def verificar_numero(self):
        numero = self.entry_numero.text()
        if not numero.isdigit() or int(numero) > 75:
            QMessageBox.warning(self, "Alerta", "El número debe ser un valor entero entre 1 y 75.")
            return
        
        for i in range(self.table.rowCount()):
            for j in range(self.table.columnCount()):
                item = self.table.item(i, j)
                if item.text() == numero:
                    item.setBackground(self.colores_filas[i])
        self.ultimo_numero = numero  # Almacenar el último número ingresado
        self.entry_numero.setText("")

    def confirmar_limpiar_tablero(self):
        respuesta = QMessageBox.question(self, "Confirmar", "¿Está seguro de que desea limpiar el tablero?",
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if respuesta == QMessageBox.Yes:
            self.limpiar_tablero()

    def limpiar_tablero(self):
        for i in range(self.table.rowCount()):
            for j in range(self.table.columnCount()):
                item = self.table.item(i, j)
                item.setBackground(QColor("white"))  

    # Método para corregir el último valor digitado
    def corregir_ultimo(self):
        if self.ultimo_numero:
            for i in range(self.table.rowCount()):
                for j in range(self.table.columnCount()):
                    item = self.table.item(i, j)
                    if item and item.text() == self.ultimo_numero and item.background() != QColor("white"):
                        item.setBackground(QColor("white"))  # Despintar el último número
            self.ultimo_numero = None  # Reiniciar la variable del último número
            texto_actual = self.entry_numero.text()
            nuevo_texto = texto_actual[:-1] if texto_actual else ""
            self.entry_numero.setText(nuevo_texto)
            self.entry_numero.setFocus()  # Establecer el foco en el campo de entrada

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MatrizBingo()
    ventana.show()
    sys.exit(app.exec_())
