# se importan las librerías a utilizar
import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QLineEdit
from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView

class Widgets(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("Christian Browser")
        self.widget = QWidget(self)
        
        # widget para el navegador
        self.webview = QWebEngineView()
        self.webview.load(QUrl("https://christiangr.me/"))
        self.webview.urlChanged.connect(self.url_changed)
        
        # botón atrás
        self.back_button = QPushButton("<")
        self.back_button.clicked.connect(self.webview.back)
        
        # botón adelante
        self.forward_button = QPushButton(">")
        self.forward_button.clicked.connect(self.webview.forward)
        
        # botón actualizar
        self.refresh_button = QPushButton("REFRESH")
        self.refresh_button.clicked.connect(self.webview.reload)
        
        # barra de direcciones
        self.url_text = QLineEdit()
        
        # botón go
        self.go_button = QPushButton("GO")
        self.go_button.clicked.connect(self.url_set)
        
        self.toplayout = QHBoxLayout()
        self.toplayout.addWidget(self.back_button)
        self.toplayout.addWidget(self.forward_button)
        self.toplayout.addWidget(self.refresh_button)
        self.toplayout.addWidget(self.url_text)
        self.toplayout.addWidget(self.go_button)
        
        self.layout = QVBoxLayout()
        self.layout.addLayout(self.toplayout)
        self.layout.addWidget(self.webview)
        
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)
    
    def url_changed(self, url):
        # actualiza la barra de direciones
        self.url_text.setText(url.toString())
    
    def url_set(self):
        # cargar la página de la barra de direciones
        self.webview.setUrl(QUrl(self.url_text.text()))
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Widgets()
    window.show()
    sys.exit(app.exec_())