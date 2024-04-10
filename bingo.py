import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QTableWidget, QTableWidgetItem, QLabel, QLineEdit, QPushButton, QMessageBox, QHeaderView, QHBoxLayout, QSpacerItem, QSizePolicy  # Importar QHBoxLayout, QSpacerItem, QSizePolicy
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
        self.colores_filas = [QColor("#000000"), QColor("#000000"), QColor("#000000"), QColor("#000000"), QColor("#000000")]

        self.table.setRowCount(len(letras))
        self.table.setColumnCount(15)

        # Ajustar el tamaño de la fuente de las letras "BINGO"
        font = QFont("Arial", weight=QFont.Bold)  # Especificar fuente negrita
        font.setPointSize(24)  # Tamaño de la fuente
        for i, letra in enumerate(letras):
            item_letra = QTableWidgetItem(letra)
            item_letra.setBackground(self.colores_filas[i])
            item_letra.setFont(font)  # Aplicar el estilo de fuente personalizado
            self.table.setVerticalHeaderItem(i, item_letra)

        for i in range(len(letras)):
            for j in range(15):
                item_numero = QTableWidgetItem(str(i * 15 + j + 1))
                item_numero.setTextAlignment(Qt.AlignCenter)  # Centrar el texto dentro de la celda
                self.table.setItem(i, j, item_numero)
                item_numero.setForeground(QColor("white"))
                item_numero.setFont(QFont("Arial", 16))  # Cambiar tamaño de fuente de los números

        # Ocultar los encabezados de las columnas
        self.table.horizontalHeader().hide()

        # Ajustar el tamaño de las filas y columnas automáticamente
        self.table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Habilitar el botón de maximizar en la ventana
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, True)

        # Crear un layout horizontal para colocar la etiqueta y el campo de entrada
        balota_layout = QHBoxLayout()

        # Agregar un espacio flexible al principio del layout horizontal
        balota_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

        # Crear la etiqueta "BALOTA:"
        self.label_balota = QLabel("BALOTA:")
        font = QFont("Arial", 14, weight=QFont.Bold)  # Ajustar tamaño y estilo de la fuente
        self.label_balota.setFont(font)
        balota_layout.addWidget(self.label_balota)

        # Crear el campo para escribir el número
        self.entry_numero = QLineEdit()
        self.entry_numero.setFixedWidth(100)  # Establecer un ancho fijo para el campo de entrada
        self.entry_numero.setFont(QFont("Arial", 12))  # Ajustar tamaño y estilo de la fuente
        balota_layout.addWidget(self.entry_numero)

        # Agregar un espacio flexible al final del layout horizontal para centrarlo
        balota_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

        # Agregar el layout horizontal al layout principal
        self.layout.addLayout(balota_layout)

        self.btn_verificar = QPushButton("Verificar")
        self.btn_verificar.clicked.connect(self.verificar_numero)
        self.btn_verificar.setFont(QFont("Arial", 14, weight=QFont.Bold))  # Ajustar tamaño y estilo de la fuente
        self.layout.addWidget(self.btn_verificar)

        self.btn_limpiar = QPushButton("Limpiar Tablero")
        self.btn_limpiar.clicked.connect(self.confirmar_limpiar_tablero)
        self.btn_limpiar.setFont(QFont("Arial", 14, weight=QFont.Bold))  # Ajustar tamaño y estilo de la fuente
        self.layout.addWidget(self.btn_limpiar)


        # Agregar texto adicional al final de la ventana
        hecho_por_label = QLabel("Hecho por: CRISTIAN7712")
        hecho_por_label.setAlignment(Qt.AlignCenter)
        hecho_por_label.setStyleSheet("color: rgba(0, 0, 0, 100);")  # Definir el color de texto opaco
        self.layout.addWidget(hecho_por_label)

        # Ajustar el tamaño de la ventana
        self.resize(800, 600)

    def closeEvent(self, event):
        """Evento de cierre de la ventana."""
        # Preguntar si el usuario está seguro de cerrar la ventana
        respuesta = QMessageBox.question(self, "Cerrar aplicación", "¿Está seguro de que desea salir de la aplicación?", 
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if respuesta == QMessageBox.Yes:
            event.accept()  # Aceptar el cierre de la ventana
        else:
            event.ignore()  # Ignorar el cierre de la ventana

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
        respuesta = QMessageBox.question(self, "Confirmar", "¿Está seguro de que desea limpiar el tablero?",
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
