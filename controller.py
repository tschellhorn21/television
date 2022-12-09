import os.path
from PyQt5.QtWidgets import *
from view import *
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Controller(QMainWindow, Ui_MainWindow):

    MIN_VOLUME = 0
    MAX_VOLUME = 100
    MIN_CHANNEL = 1
    MAX_CHANNEL = 3

    def __init__(self, *args, **kwargs) -> None:
        """
        This function controls the buttons on the gui and sets up the initial values.
        """
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.player = QMediaPlayer()
        self.__status = False
        self.__muted = False
        self.__volume = Controller.MIN_VOLUME
        self.__channel = Controller.MIN_CHANNEL
        self.power_button.clicked.connect(lambda: self.power())
        self.channelUp_button.clicked.connect(lambda: self.channel_up())
        self.channelDown_button.clicked.connect(lambda: self.channel_down())
        self.volumeUp_button.clicked.connect(lambda: self.volume_up())
        self.volumeDown_button.clicked.connect(lambda: self.volume_down())
        self.mute_button.clicked.connect(lambda: self.mute())

    def power(self) -> None:
        """
        This function controls the power button on the gui
        :return: None
        """
        if self.__status:
            self.__status = False
            self.tv_image.setPixmap(QtGui.QPixmap("pictures/off.png"))
            self.channel_num.setText("")
            self.volume_num.setText("")
            self.player.setVolume(Controller.MIN_VOLUME)
        else:
            self.__status = True
            self.volume_num.setText(f'{self.__volume}')
            self.player.setVolume(self.__volume)
            if self.__channel == 1:
                self.tv_image.setPixmap(QtGui.QPixmap("pictures/friends.png"))
                self.channel_num.setText(f'{self.__channel}')
                self.play_audio_friends()
            elif self.__channel == 2:
                self.tv_image.setPixmap(QtGui.QPixmap("pictures/spongebob.png"))
                self.channel_num.setText(f'{self.__channel}')
                self.play_audio_spongebob()
            elif self.__channel == 3:
                self.tv_image.setPixmap(QtGui.QPixmap("pictures/greys.png"))
                self.channel_num.setText(f'{self.__channel}')
                self.play_audio_greys()

    def mute(self) -> None:
        """
        This function controls the mute button on the gui.
        """
        self.player.setMuted(not self.player.isMuted())
        if self.__muted:
            self.__muted = False
            self.volume_num.setText(f'{self.__volume}')
        else:
            self.__muted = True
            self.volume_num.setText(f'{Controller.MIN_VOLUME}')

    def channel_up(self) -> None:
        """
        This function controls the channel up button and the channel number that is displayed.
        """
        if self.__status:
            if self.__channel == Controller.MAX_CHANNEL:
                self.__channel = Controller.MIN_CHANNEL
                self.tv_image.setPixmap(QtGui.QPixmap("pictures/friends.png"))
                self.channel_num.setText(f'{self.__channel}')
                self.play_audio_friends()
            else:
                self.__channel += 1
                if self.__channel == 2:
                    self.tv_image.setPixmap(QtGui.QPixmap("pictures/spongebob.png"))
                    self.channel_num.setText(f'{self.__channel}')
                    self.play_audio_spongebob()
                elif self.__channel == 3:
                    self.tv_image.setPixmap(QtGui.QPixmap("pictures/greys.png"))
                    self.channel_num.setText(f'{self.__channel}')
                    self.play_audio_greys()

    def channel_down(self) -> None:
        """
        This function controls the channel down button and the channel number that is displayed.
        """
        if self.__status:
            if self.__channel == Controller.MIN_CHANNEL:
                self.__channel = Controller.MAX_CHANNEL
                self.tv_image.setPixmap(QtGui.QPixmap("pictures/greys.png"))
                self.channel_num.setText(f'{self.__channel}')
                self.play_audio_greys()
            else:
                self.__channel -= 1
                if self.__channel == 1:
                    self.tv_image.setPixmap(QtGui.QPixmap("pictures/friends.png"))
                    self.channel_num.setText(f'{self.__channel}')
                    self.play_audio_friends()
                elif self.__channel == 2:
                    self.tv_image.setPixmap(QtGui.QPixmap("pictures/spongebob.png"))
                    self.channel_num.setText(f'{self.__channel}')
                    self.play_audio_spongebob()

    def volume_up(self) -> None:
        """
        This function controls the volume up button and the volume number that is displayed.
        """
        if self.__status:
            if self.__volume != Controller.MAX_VOLUME:
                self.__volume += 5
                self.volume_num.setText(f'{self.__volume}')
                self.player.setVolume(self.__volume + 5)

    def volume_down(self) -> None:
        """
        This function controls the volume down button and the volume number that is displayed.
        """
        if self.__status:
            if self.__volume != Controller.MIN_VOLUME:
                self.__volume -= 5
                self.volume_num.setText(f'{self.__volume}')
                self.player.setVolume(self.__volume - 5)

    def play_audio_friends(self) -> None:
        """
        This function controls playing the Friends theme song.
        """
        filepath = os.path.join(os.getcwd(), 'audio/Friends.mp3')
        url = QUrl.fromLocalFile(filepath)
        content = QMediaContent(url)
        self.player.setMedia(content)
        self.player.play()
        self.player.setVolume(self.__volume)

    def play_audio_greys(self) -> None:
        """
        This function controls playing the Grey's Anatomy theme song.
        """
        filepath = os.path.join(os.getcwd(), 'audio/Greys.mp3')
        url = QUrl.fromLocalFile(filepath)
        content = QMediaContent(url)
        self.player.setMedia(content)
        self.player.play()
        self.player.setVolume(self.__volume)

    def play_audio_spongebob(self) -> None:
        """
        This function controls playing the Spongebob theme song.
        """
        filepath = os.path.join(os.getcwd(), 'audio/Spongebob.mp3')
        url = QUrl.fromLocalFile(filepath)
        content = QMediaContent(url)
        self.player.setMedia(content)
        self.player.play()
        self.player.setVolume(self.__volume)
