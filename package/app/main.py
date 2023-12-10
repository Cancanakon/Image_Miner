import threading
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import Qt, QThreadPool, QRunnable, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QValidator
from package.ui.ui_image_miner import Ui_MainWindow
from simple_image_download import simple_image_download as simp
import sys


class Worker(QRunnable):
    def __init__(self, task_func, *args, **kwargs):
        super().__init__()
        self.task_func = task_func
        self.args = args
        self.kwargs = kwargs

    def run(self):
        self.task_func(*self.args, **self.kwargs)


class Main(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_getData.clicked.connect(self.getData_clicked)

        self.response = simp.simple_image_download()

        self.t1 = threading.Thread(target=self.thread_func)

    def thread_func(self):
        self.ui.lbl_searchKeyword.setText(self.keywordsText)
        self.ui.lbl_searchKeyword.setStyleSheet("color:orange;")
        self.ui.pb_loadingBar.setValue(0)
        self.ui.lbl_situation.setText("Getting data...")
        self.ui.lbl_situation_live.setText("Downloading...")

        for i,kw in enumerate(self.keywords):
            self.response.download(kw,self.targetNum)
            percentage = int((i + 1) / len(self.keywords) * 100)

            self.ui.pb_loadingBar.setValue(percentage)

        self.ui.lbl_situation.setText("Success! Armed for a new mission...")
        self.ui.lbl_searchKeyword.setStyleSheet("color:green;")
        self.ui.pb_loadingBar.setValue(100)
        self.ui.lbl_situation_live.setText("All Data Downloaded!")

    def getData_clicked(self):
        self.keywordsText = self.ui.edt_keywords.text()
        self.keywords = [self.keywordsText]
        self.targetNum = self.ui.sb_imageNumber.value()

        worker = Worker(self.thread_func)
        QThreadPool.globalInstance().start(worker)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Window Close', 'Are you sure you want to close the window?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            QThreadPool.globalInstance().waitForDone()
            event.accept()
            print('Window closed')
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Main()
    win.show()
    sys.exit(app.exec())
