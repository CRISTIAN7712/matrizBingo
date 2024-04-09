import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QTableWidget, QTableWidgetItem, QLabel, QLineEdit, QPushButton, QMessageBox
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
        self.table.setSelectionMode(QTableWidget.NoSelection)  # Hacer las celdas no seleccionables
        self.layout.addWidget(self.table)

        letras = ["B", "I", "N", "G", "O"]
        self.colores_filas = [QColor("#00A2FF"), QColor("#FF0000"), QColor("#00FFFB"), QColor("#17FF00"), QColor("#E8FF00")]

        self.table.setColumnCount(15)
        self.table.setHorizontalHeaderLabels([str(i) for i in range(1, 16)])
        self.table.setRowCount(len(letras))

        # Ajustar el tamaño de la fuente de las letras "BINGO"
        font = QFont("Arial", 24)  # Cambiar tamaño de fuente
        for i, letra in enumerate(letras):
            item_letra = QTableWidgetItem(letra)
            item_letra.setBackground(self.colores_filas[i])
            item_letra.setFont(font)  # Aplicar el estilo de fuente personalizado
            self.table.setVerticalHeaderItem(i, item_letra)

        for i in range(len(letras)):
            self.table.setRowHeight(i, 50)  # Ajustar la altura de la fila

        for i in range(len(letras)):
            for j in range(15):
                item_numero = QTableWidgetItem(str(i * 15 + j + 1))
                item_numero.setTextAlignment(Qt.AlignCenter)  # Centrar el texto dentro de la celda
                self.table.setItem(i, j, item_numero)
                item_numero.setFont(QFont("Arial", 16))  # Cambiar tamaño de fuente de los números

        # Ajustar automáticamente el tamaño de las columnas y filas
        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()

        # Ajustar el tamaño de las columnas
        for j in range(15):
            self.table.setColumnWidth(j, 70)  # Ajustar ancho de columnas

        # Obtener el tamaño preferido de la tabla y ajustar el tamaño de la ventana
        table_size = self.table.sizeHint()
        self.resize(table_size.width() + 850, table_size.height() + self.label.sizeHint().height() + 190)

        # Eliminar el botón de maximizar de la ventana
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, False)

        self.entry_numero = QLineEdit()
        self.layout.addWidget(self.entry_numero)

        self.btn_verificar = QPushButton("Verificar")
        self.btn_verificar.clicked.connect(self.verificar_numero)
        self.layout.addWidget(self.btn_verificar)

        self.btn_limpiar = QPushButton("Limpiar Tablero")
        self.btn_limpiar.clicked.connect(self.confirmar_limpiar_tablero)
        self.layout.addWidget(self.btn_limpiar)

        # Agregar texto adicional al final de la ventana
        hecho_por_label = QLabel("Hecho por: CRISTIAN7712")
        hecho_por_label.setAlignment(Qt.AlignCenter)
        hecho_por_label.setStyleSheet("color: rgba(0, 0, 0, 100);")  # Definir el color de texto opaco
        self.layout.addWidget(hecho_por_label)

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
        # Limpiar la casilla de entrada después de verificar
        self.entry_numero.setText("")

    def confirmar_limpiar_tablero(self):
        respuesta = QMessageBox.question(self, "Confirmar", "¿Estás seguro de que quieres limpiar el tablero?",
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if respuesta == QMessageBox.Yes:
            self.limpiar_tablero()

    def limpiar_tablero(self):
        for i in range(self.table.rowCount()):
            for j in range(self.table.columnCount()):
                item = self.table.item(i, j)
                item.setBackground(QColor("white"))  # Restablecer el color de fondo a blanco

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MatrizBingo()
    ventana.show()
    sys.exit(app.exec_())
