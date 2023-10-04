import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QTextBrowser,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class MedicalChatbotUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Medical Chatbot")
        self.setGeometry(100, 100, 600, 600)

        self.init_ui()

    def init_ui(self):
        self.chat_history = QTextBrowser()
        self.input_box = QLineEdit()
        self.send_button = QPushButton("Send")

        layout = QVBoxLayout()
        layout.addWidget(self.chat_history)
        layout.addWidget(self.input_box)
        layout.addWidget(self.send_button)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

        self.send_button.clicked.connect(self.send_message)
        self.input_box.returnPressed.connect(self.send_message)

        self.chat_history.append("Chatbot: Hello! I'm your medical chatbot.")

    def send_message(self):
        user_input = self.input_box.text()
        self.chat_history.append("You: " + user_input)

        response = self.generate_response(user_input)
        self.chat_history.append("Chatbot: " + response)

        self.input_box.clear()

    def generate_response(self, user_input):
        if "symptoms" in user_input:
            return "It's important to consult a medical professional for accurate diagnosis."
        elif "fever" in user_input:
            return (
                "A fever could be a sign of an underlying infection. Rest and hydrate."
            )
        else:
            return "I'm not a substitute for a real doctor. Please consult a healthcare professional."


def main():
    app = QApplication(sys.argv)
    medical_chatbot_app = MedicalChatbotUI()
    medical_chatbot_app.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
