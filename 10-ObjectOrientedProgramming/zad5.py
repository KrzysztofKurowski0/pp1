class TV:
    def __init__(self):
        self.is_on = False
        self.channel = 1
    def turn_on(self):
        self.is_on = True
    def turn_off(self):
        self.is_on = False
    def set_channel(self,channel):
        self.channel = channel
    def show_status(self):
        if self.is_on:
            print("TV is on")
            print(f"TV is on channel {self.channel}")
        else:
            print("TV is off")

TV_set = TV()
TV_set.show_status()
TV_set.turn_on()
TV_set.set_channel(5)
TV_set.show_status()
TV_set.turn_off()
TV_set.show_status()