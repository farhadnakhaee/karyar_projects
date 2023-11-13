# decorator for volume size
def volume_check(method):
    def wrapper(self):

        if 0 < self.volume < self.MAX_VOLUME:
            method(self)
        else:
            print("Volume can't change. (max or min level)")

        return self
    return wrapper


def channel_check(method):
    def wrapper(self):

        if 0 < self.currentChannelIndex < len(self.channelsList):
            method(self)
        else:
            print("Channel is not in channel list")

        return self
    return wrapper


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
        # TODO: Get from CABLE!
        return [1, 2, 3, 4, 5, 6, 7, 8, 9, 20, 21, 25]

    def power(self):
        self.isOn = not self.isOn

    @volume_check
    def volume_up(self):
        self.volume += 1

    @volume_check
    def volume_down(self):
        self.volume -= 1

    @channel_check
    def channel_up(self):
        self.currentChannelIndex += 1

    @channel_check
    def channel_down(self):
        self.currentChannelIndex -= 1

    def set_channel(self):
        channel = self.input_channel()
        self.currentChannelIndex = self.channelsList.index(channel)

    @staticmethod
    def input_channel():
        channel = int(input("set channel: "))
        return channel

    def show_info(self):
        print(f"volume: {self.volume}")
        print(f"current channel: {self.channelsList[self.currentChannelIndex]}")


tv = TV()
tv.currentChannelIndex = 1
tv.channel_down()
tv.channel_down()
print(f"index: {tv.currentChannelIndex}   channel: {tv.channelsList[tv.currentChannelIndex]}")
