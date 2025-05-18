class LotionBottle:
    def _init_(self, scent, volume_ml):
        self.scent = scent
        self.volume_ml = volume_ml
        self.is_open = False

    def open(self):
        self.is_open = True
        print("The bottle is now open.")