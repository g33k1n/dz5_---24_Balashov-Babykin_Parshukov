import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, \
    QMessageBox, QFrame
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtCore import Qt


class StylishLoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Welcome Back!")
        self.setGeometry(100, 100, 350, 250)

        # Стиль
        self.setStyleSheet("""
            QWidget { background-color: #2E2E38; color: #F5F5F5; }
            QLabel { font-size: 14px; }
            QLineEdit { background-color: #3E3E4A; color: #F5F5F5; padding: 5px; border: none; }
            QPushButton { background-color: #4CAF50; color: white; padding: 10px; border-radius: 5px; }
            QPushButton:hover { background-color: #45A049; }
        """)

        # Лейблы и поля ввода
        self.username_label = QLabel("Username:")
        self.username_input = QLineEdit()
        self.password_label = QLabel("Password:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        # Кнопка входа
        self.login_button = QPushButton("Log In")
        self.login_button.clicked.connect(self.validate_login)

        # Макет окна
        layout = QVBoxLayout()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)
        self.setLayout(layout)

    def validate_login(self):
        # Проверка логина и пароля с новыми сообщениями
        if self.username_input.text() == "admin" and self.password_input.text() == "1234":
            self.profile_window = StylishProfileWindow()
            self.profile_window.show()
            self.close()
        else:
            QMessageBox.critical(self, "Access Denied", "Invalid username or password. Please try again.")


class StylishProfileWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Your Profile")
        self.setGeometry(100, 100, 450, 350)

        # Стиль
        self.setStyleSheet("""
            QWidget { background-color: #1E1E24; color: #FAFAFA; }
            QLabel { font-size: 14px; margin: 10px; }
        """)

        # Аватар и информация
        self.profile_pic = QLabel(self)
        pixmap = QPixmap("avatar1.jpg")
        self.profile_pic.setPixmap(pixmap.scaled(150, 150))

        self.name_label = QLabel("Имя")
        self.email_label = QLabel("Email")
        self.status_label = QLabel("Статус")

        layout = QHBoxLayout()
        layout.addWidget(self.profile_pic)
        data_layout = QVBoxLayout()
        data_layout.addWidget(self.name_label)
        data_layout.addWidget(self.email_label)
        data_layout.addWidget(self.status_label)
        # Размещение элементов в макете
        main_layout = QVBoxLayout()
        main_layout.addLayout(layout)  
        main_layout.addLayout(data_layout)
        self.setLayout(main_layout)

        self.setLayout(main_layout)


app = QApplication(sys.argv)
login_window = StylishLoginWindow()
login_window.show()
sys.exit(app.exec())
