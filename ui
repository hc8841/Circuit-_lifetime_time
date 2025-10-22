import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QTextEdit, QTabWidget
)
from PyQt5.QtGui import QFont

class SimulatorWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simulador de Vida Útil de Circuito - v2.1")
        self.resize(800, 600)

        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        self.tab_simulador = QWidget()
        self.tab_manual = QWidget()
        self.tab_doacoes = QWidget()

        self.tabs.addTab(self.tab_simulador, "Simulador")
        self.tabs.addTab(self.tab_manual, "Manual")
        self.tabs.addTab(self.tab_doacoes, "Doações")

        # Layout principal do simulador (placeholder)
        layout_sim = QVBoxLayout()
        layout_sim.addWidget(QLabel("Aqui fica o simulador principal."))
        self.tab_simulador.setLayout(layout_sim)

        # Manual (placeholder)
        layout_manual = QVBoxLayout()
        manual_label = QLabel("Manual de uso: ajuste os parâmetros e clique em 'Simular'.")
        layout_manual.addWidget(manual_label)
        self.tab_manual.setLayout(layout_manual)

        # Aba de Doações
        layout_donate = QVBoxLayout()
        label_frase = QLabel(
            "💡 Dev Indie não sobrevive só comendo capacitor!\n"
            "Se quiser doar, pode. Se não quiser, tudo bem — é open source mesmo! kkkkk"
        )
        label_frase.setWordWrap(True)
        label_frase.setFont(QFont("Arial", 11))
        layout_donate.addWidget(label_frase)

        label_pix = QLabel("Chave Pix: 47991826484")
        label_pix.setFont(QFont("Courier", 10))
        layout_donate.addWidget(label_pix)

        btn_copy = QPushButton("Copiar chave Pix")
        btn_copy.clicked.connect(lambda: self.copy_pix(label_pix.text()))
        layout_donate.addWidget(btn_copy)

        layout_donate.addStretch()
        self.tab_doacoes.setLayout(layout_donate)

    def copy_pix(self, text):
        chave = text.replace("Chave Pix:", "").strip()
        cb = QApplication.clipboard()
        cb.setText(chave)
        QtWidgets.QMessageBox.information(self, "Pix copiado", "Chave Pix copiada para a área de transferência!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = SimulatorWindow()
    w.show()
    sys.exit(app.exec_())
