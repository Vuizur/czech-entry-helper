import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QVBoxLayout,
    QRadioButton,
    QPushButton,
    QWidget,
    QLineEdit,
    QButtonGroup,
    QCheckBox,
)

from czech_entry_helper.automatic_entry_creation import (
    create_noun_wiktionary_entry,
    create_wiktionary_entry,
)
import webbrowser


class WiktionaryApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Wiktionary Entry Creator")
        self.setGeometry(100, 100, 400, 200)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.word_label = QLabel("Word:")
        self.word_input = QLineEdit()
        self.layout.addWidget(self.word_label)
        self.layout.addWidget(self.word_input)

        self.pos_label = QLabel("Part of Speech:")
        self.pos_radio_group = QButtonGroup()
        self.pos_radio_adv = QRadioButton("Adverb")
        self.pos_radio_adj = QRadioButton("Adjective")
        self.pos_radio_noun = QRadioButton("Noun")
        self.pos_radio_verb = QRadioButton("Verb")
        self.pos_radio_group.addButton(self.pos_radio_adv)
        self.pos_radio_group.addButton(self.pos_radio_adj)
        self.pos_radio_group.addButton(self.pos_radio_noun)
        self.pos_radio_group.addButton(self.pos_radio_verb)
        self.layout.addWidget(self.pos_label)
        self.layout.addWidget(self.pos_radio_adv)
        self.layout.addWidget(self.pos_radio_adj)
        self.layout.addWidget(self.pos_radio_noun)
        self.layout.addWidget(self.pos_radio_verb)

        self.definition_label = QLabel("Definition:")
        self.definition_input = QLineEdit()
        self.layout.addWidget(self.definition_label)
        self.layout.addWidget(self.definition_input)

        self.comp_label = QLabel("Comparative:")
        self.comparative_checkbox = QCheckBox("Has comparative")
        self.layout.addWidget(self.comparative_checkbox)

        self.gender_label = QLabel("Gender:")
        self.gender_radio_group = QButtonGroup()
        self.m_button = QRadioButton("Male")
        self.n_button = QRadioButton("Neuter")
        self.f_button = QRadioButton("Feminine")
        self.gender_radio_group.addButton(self.m_button)
        self.gender_radio_group.addButton(self.n_button)
        self.gender_radio_group.addButton(self.f_button)
        self.layout.addWidget(self.gender_label)
        self.layout.addWidget(self.m_button)
        self.layout.addWidget(self.n_button)
        self.layout.addWidget(self.f_button)

        self.animate_checkbox = QCheckBox("Animate")
        self.layout.addWidget(self.animate_checkbox)

        self.create_button = QPushButton("Create Entry")
        self.create_button.clicked.connect(self.create_entry)
        self.layout.addWidget(self.create_button)

        self.central_widget.setLayout(self.layout)

    def create_entry(self):
        word = self.word_input.text().strip()
        definition = self.definition_input.text().strip()
        has_comparative = self.comparative_checkbox.isChecked()
        if self.pos_radio_adv.isChecked():
            create_wiktionary_entry(word, "adv", definition, has_comparative)
        elif self.pos_radio_adj.isChecked():
            create_wiktionary_entry(word, "adj", definition, has_comparative)
        elif self.pos_radio_verb.isChecked():
            raise NotImplementedError()
        elif self.pos_radio_noun.isChecked():
            if self.m_button.isChecked():
                gender = "m"
            elif self.n_button.isChecked():
                gender = "n"
            elif self.f_button.isChecked():
                gender = "f"
            else:
                return
            animacy = "an" if self.animate_checkbox.isChecked() else "in"
            create_noun_wiktionary_entry(word, definition, gender, animacy)

        link = (
            f"https://en.wiktionary.org/w/index.php?title={word}&action=edit&redlink=1"
        )
        webbrowser.open(link)


def run_app():
    app = QApplication(sys.argv)
    window = WiktionaryApp()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    run_app()
