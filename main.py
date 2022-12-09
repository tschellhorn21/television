from controller import *


def main() -> None:
    """
    This function sets up the gui.
    """
    app = QApplication([])
    window = Controller()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
