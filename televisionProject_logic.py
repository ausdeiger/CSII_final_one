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
        self.current_channel_index = 5
        self.channels = [self.screen_nick, self.screen_tlc, self.screen_pbs, self.screen_bbc, self.screen_blank]
        self.show_only_current_channel()
        self.bar_curr_vol.setValue(0)
        self.bar_curr_chan.setValue(0)

        self.button_vol_up.clicked.connect(self.volume_up)
        self.button_vol_down.clicked.connect(self.volume_down)
        self.button_channel_up.clicked.connect(self.channel_up)
        self.button_channel_down.clicked.connect(self.channel_down)
        self.button_power.clicked.connect(self.power)
        self.button_mute.clicked.connect(self.mute)
        self.button_recall.clicked.connect(self.recall)
        self.button_power_indicator.setCheckable(True)
        self.button_power_indicator.setEnabled(False)

    def power(self) -> None:
        """
        Toggles On / Off Status
        """
        self.__status = not self.__status
        self.button_power_indicator.setChecked(self.__status)
        if not self.__status:
            self.__past_channel = self.current_channel_index
            self.current_channel_index = 5
            self.bar_curr_vol.setValue(0)
            self.bar_curr_chan.setValue(0)
        else:
            self.current_channel_index = self.__past_channel
            self.bar_curr_chan.setValue(self.current_channel_index)
            self.bar_curr_vol.setValue(self.__volume)
        self.show_only_current_channel()




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
            self.bar_curr_vol.setValue(self.__volume)


    def channel_up(self) -> None:
        """
        Method to increase the tv channel
        """
        if self.__status:
            self.__past_channel = self.__channel
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL
            self.current_channel_index = self.__channel
            self.show_only_current_channel()

    def channel_down(self) -> None:
        """
        Method to decrease the tv channel
        """
        if self.__status:
            self.__past_channel = self.__channel
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL
            self.current_channel_index = self.__channel
            self.show_only_current_channel()


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
            self.bar_curr_vol.setValue(self.__volume)


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
            self.bar_curr_vol.setValue(self.__volume)


    def recall(self) -> None:
        """
        Recalls previous channel
        """
        if self.__status:
            if self.__past_channel != self.__channel:
                self.__past_channel, self.__channel = self.__channel, self.__past_channel
                self.current_channel_index = self.__channel
                self.bar_curr_chan.setValue(self.__channel)
                self.show_only_current_channel()

    def show_only_current_channel(self):
        for i, screen in enumerate(self.channels):
            screen.setVisible(i == self.current_channel_index)
        if self.__status:
            self.bar_curr_chan.setValue(self.__channel)




    def __str__(self) -> str:
        """
        Output function
        :return: Television status list
        """
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'


