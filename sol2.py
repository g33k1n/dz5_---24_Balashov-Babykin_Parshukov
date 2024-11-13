import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QGraphicsOpacityEffect
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt


class FoodMenuWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Food Menu")
        self.setGeometry(100, 100, 500, 400)

        # Стиль для раскраски
        self.setStyleSheet("""
            QWidget { background-color: #FFEB3B; color: #2C2C2C; }
            QLabel { font-size: 18px; font-weight: bold; margin: 10px; }
            QPushButton { background-color: #FF5722; color: white; padding: 10px; border-radius: 10px; font-size: 14px; }
            QPushButton:hover { background-color: #E64A19; }
        """)

        # Лейблы для картинок
        self.burger1_label = QLabel(self)
        pixmap_burger1 = QPixmap("burger1.jpg").scaled(150, 150, Qt.AspectRatioMode.KeepAspectRatio)
        self.burger1_label.setPixmap(pixmap_burger1)
        self.burger1_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.burger2_label = QLabel(self)
        pixmap_burger2 = QPixmap("burger2.jpg").scaled(150, 150, Qt.AspectRatioMode.KeepAspectRatio)
        self.burger2_label.setPixmap(pixmap_burger2)
        self.burger2_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.drink_label = QLabel(self)
        pixmap_drink = QPixmap("drink.jpg").scaled(150, 150, Qt.AspectRatioMode.KeepAspectRatio)
        self.drink_label.setPixmap(pixmap_drink)
        self.drink_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Кнопки для выбора
        self.burger1_button = QPushButton("Choose Burger 1")
        self.burger2_button = QPushButton("Choose Burger 2")
        self.drink_button = QPushButton("Choose Drink")

        # Подключение кнопок к методам
        self.burger1_button.clicked.connect(self.select_burger1)
        self.burger2_button.clicked.connect(self.select_burger2)
        self.drink_button.clicked.connect(self.select_drink)

        # Размещение элементов
        layout = QVBoxLayout()

        menu_layout = QHBoxLayout()
        menu_layout.addWidget(self.burger1_label)
        menu_layout.addWidget(self.burger2_label)
        menu_layout.addWidget(self.drink_label)

        buttons_layout = QVBoxLayout()
        buttons_layout.addWidget(self.burger1_button)
        buttons_layout.addWidget(self.burger2_button)
        buttons_layout.addWidget(self.drink_button)

        layout.addLayout(menu_layout)
        layout.addLayout(buttons_layout)

        self.setLayout(layout)

    def select_burger1(self):
        self.show_message("You selected Burger 1!")

    def select_burger2(self):
        self.show_message("You selected Burger 2!")

    def select_drink(self):
        self.show_message("You selected a Drink!")

    def show_message(self, message):
        QMessageBox.information(self, "Selection", message)


app = QApplication(sys.argv)
food_menu_window = FoodMenuWindow()
food_menu_window.show()
sys.exit(app.exec())
