from PyQt6.QtWidgets import QApplication

from televisionProject_logic import Television


def main():
    application = QApplication([])
    window = Television()
    window.show()
    application.exec()




if __name__ == '__main__':
    main()