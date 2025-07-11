import sys
from PyQt5.QtWidgets import QApplication
from gui.window import MikuWindow
from qasync import QEventLoop
import asyncio

if __name__ == "__main__":
    app = QApplication(sys.argv)
    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)

    window = MikuWindow()
    window.show()

    with loop:
        loop.run_forever()