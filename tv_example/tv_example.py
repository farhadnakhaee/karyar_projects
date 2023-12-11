class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prv = None


class Channel:
    def __init__(self, channel_list):
        self.channel_list = channel_list
        self.head = Node(self.channel_list.pop(0))
        self.make_loop()

    def make_loop(self):
        current = self.head
        temp = None
        for i in self.channel_list:
            current.next = Node(i)
            current.prv = temp
            temp = current
            current = current.next
        current.prv = temp
        current.next = self.head
        self.head.prv = current


class TV:
    def __init__(self):
        self.isOn = False
        self.isMuted = False
        self.channel_list = self.search_channel()
        channel = Channel(self.channel_list)
        self.current_channel = channel.head
        self.volume = 10
        self.MAX_VOLUME = 20

    @staticmethod
    def search_channel():
        return [1, 2, 3, 4, 5, 6, 7, 8, 9, 20, 21, 25]

    @staticmethod
    def input_channel():
        channel = int(input("set channel: "))
        return channel

    def power(self):
        self.isOn = not self.isOn

    def volume_up(self):
        if self.volume < self.MAX_VOLUME:
            self.volume += 1

    def volume_down(self):
        if self.volume > 0:
            self.volume -= 1

    def channel_up(self):
        self.current_channel = self.current_channel.next

    def channel_down(self):
        self.current_channel = self.current_channel.prv

    def set_channel(self):
        channel = self.input_channel()
        if channel in self.channel_list:
            while channel != self.current_channel.value:
                self.channel_up()
        else:
            print("Channel isn't in list.")

    def show_info(self):
        print(f"volume: {self.volume}")
        print(f"current channel: {self.current_channel.value}")


if __name__ == "__main__":
    tv = TV()
    tv.channel_up()
    tv.show_info()
