class TV:
    def __init__(self):
        self.is_on = False
        self.channel = 1
        self.channel_list = []
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
    def show_status(self):
        if self.is_on:
            if len(self.channel_list)!=0:
                for i in range(len(self.channel_list)):
                    if i+1 == self.channel:
                        print(f"TV is on, You are on channel: {self.channel} ({self.channel_list[i]})")
        else:
            print("TV is off")

TV_set = TV()
TV_set.turn_on()
TV_set.set_channels("TVP1,TVP2,Polsat,TVN,Filmbox,Discovery")
TV_set.show_channels()
TV_set.set_channel(6)
TV_set.show_status()
