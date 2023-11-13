class TV:
    def __init__(self):
        self.isOn = False
        self.isMuted = False
        self.currentChannelIndex = 0
        self.channelsList = self.search_channel()
        self.volume = 10
        self.MAX_VOLUME = 20

    @staticmethod
    def search_channel():
        return [1, 2, 3, 4, 5, 6, 7, 8, 9, 20, 21, 25]

    def power(self):
        self.isOn = not self.isOn

    def volume_up(self):
        if self.volume < self.MAX_VOLUME:
            self.volume += 1

    def volume_down(self):
        if self.volume > 0:
            self.volume -= 1

    def channel_up(self):
        if self.currentChannelIndex < len(self.channelsList)-1:
            self.currentChannelIndex += 1

    def channel_down(self):
        if self.currentChannelIndex > 0:
            self.currentChannelIndex -= 1

    def set_channel(self):
        channel = self.input_channel()
        if channel in self.channelsList:
            self.currentChannelIndex = self.channelsList.index(channel)
        else:
            print("Channel isn't in list.")

    @staticmethod
    def input_channel():
        channel = int(input("set channel: "))
        return channel

    def show_info(self):
        print(f"volume: {self.volume}")
        print(f"current channel: {self.channelsList[self.currentChannelIndex]}")


if __name__ == "__main__":
    tv = TV()
    tv.set_channel()
    tv.volume_up()
    tv.show_info()
