import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

class CustomSearchBrowser(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Custom Search Browser')
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.browser = QWebEngineView()
        self.layout.addWidget(self.browser)

        self.browser.load(QUrl.fromLocalFile(r'C:\Users\Liyander\Downloads\brow.html'))  # Load HTML file

if __name__ == '__main__':
    app = QApplication(sys.argv)
    browser = CustomSearchBrowser()
    browser.show()
    sys.exit(app.exec_())
