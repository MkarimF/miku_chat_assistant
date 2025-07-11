import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt
import asyncio
from qasync import asyncSlot
from core.assistant import Assistant

class MikuWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.assistant = Assistant()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Miku Assistant")
        self.setGeometry(100, 100, 400, 300)

        self.label = QLabel("\ud83d\udda4 Miku is waiting \ud83d\udda4", self)
        self.label.setAlignment(Qt.AlignCenter)

        self.button_start = QPushButton("Start Voice Recognition", self)
        self.button_start.clicked.connect(self.start_voice)

        self.button_exit = QPushButton("Exit", self)
        self.button_exit.clicked.connect(self.close)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button_start)
        layout.addWidget(self.button_exit)

        self.setLayout(layout)

    @asyncSlot()
    async def start_voice(self):
        await self.assistant.run()