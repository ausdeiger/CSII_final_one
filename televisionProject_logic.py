from PyQt6.QtWidgets import *
from televisionProject_gui import *


class Television(QMainWindow, Ui_remote):
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3


    def __init__(self) -> None:
        """
        Initializes television variables
        """
        super().__init__()
        self.setupUi(self)
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL
        self.__past_volume = self.__volume
        self.__past_channel = self.__channel

        self.button_vol_up.clicked.connect(self.volume_up)
        self.button_vol_down.clicked.connect(self.volume_down)
        self.button_channel_up.clicked.connect(self.channel_up)
        self.button_channel_down.clicked.connect(self.channel_down)
        self.button_power.clicked.connect(self.power)
        self.button_mute.clicked.connect(self.mute)
        self.button_recall.clicked.connect(self.recall)
        self.button_power_indicator.setEnabled(False)

    def power(self) -> None:
        """
        Toggles On / Off Status
        """
        self.__status = not self.__status
        self.button_power_indicator.setChecked(self.__status)


    def mute(self) -> None:
        """
        Toggles Mute Status
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__past_volume
            else:
                self.__muted = True
                self.__past_volume = self.__volume
                self.__volume = 0
            self.label_curr_vol.setText(str(self.__volume))


    def channel_up(self) -> None:
        """
        Method to increase the tv channel
        """
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL
            self.label_curr_chan.setText(str(self.__channel))

    def channel_down(self) -> None:
        """
        Method to decrease the tv channel
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL
            self.label_curr_chan.setText(str(self.__channel))


    def volume_up(self) -> None:
        """
        Method to increase tv volume
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__past_volume
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1
            self.__past_volume = self.__volume
            self.label_curr_vol.setText(str(self.__volume))


    def volume_down(self) -> None:
        """
        Method to decrease tv volume
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__past_volume
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
            self.__past_volume = self.__volume
            self.label_curr_vol.setText(str(self.__volume))


    def recall(self) -> None:
        """
        Recalls previous channel
        """
        if self.__status:
            if self.__past_channel != self.__channel:
                self.__past_channel, self.__channel = self.__channel, self.__past_channel
                self.label_curr_chan.setText(str(self.__channel))


    def __str__(self) -> str:
        """
        Output function
        :return: Television status list
        """
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'


