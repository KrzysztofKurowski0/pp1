class TV:
    def __init__(self):
        self.is_on = False
        self.channel = 1
        self.channel_list = []
        self.volume = 0

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def set_channel(self,channel):
        self.channel = channel

    def set_channels(self,channel_list):
        for i in range(len(channel_list.split(","))):
            self.channel_list.append(channel_list.split(",")[i])

    def show_channels(self):
        if len(self.channel_list)!=0:
            x=1
            for i in self.channel_list:
                print(f"{x}. {i}")
                x+=1
        else:
            print("No channels available")

    def volume_up(self):
        if self.volume<10:
            self.volume+=1
        else:
            print("You can't increase the volume more!")
    
    def volume_down(self):
        if self.volume>0:
            self.volume-=1
        else:
            print("You can't decreace the volume more!")

    def show_status(self):
        if self.is_on:
            if len(self.channel_list)!=0:
                for i in range(len(self.channel_list)):
                    if i+1 == self.channel:
                        print(f"TV is on, You are on channel: {self.channel} ({self.channel_list[i]})\n Volume: {self.volume}")
        else:
            print("TV is off")

TV_set = TV()
TV_set.turn_on()
TV_set.set_channels("TVP1,TVP2,Polsat,TVN,Filmbox,Discovery")
TV_set.show_channels()
TV_set.set_channel(6)
TV_set.show_status()
TV_set.volume_up()
TV_set.volume_up()
TV_set.volume_up()
TV_set.volume_up()
TV_set.volume_up()
TV_set.volume_up()
TV_set.volume_up()
TV_set.volume_up()
TV_set.volume_up()
TV_set.volume_up()
TV_set.show_status()
TV_set.volume_up()

            