class LotionBottle:
    def __init__(self, scent, volume_ml):
        self.scent = scent
        self.volume_ml = volume_ml
        self.is_open = False

    def open(self):
        self.is_open = True
        print("The bottle is now open.")

    def close(self):
        self.is_open = False
        print("The bottle is now closed.")

    def apply(self, amount):
        if not self.is_open:
            print("You need to open the bottle first.")
        elif amount > self.volume_ml:
            print("Not enough lotion left!")
        else:
            self.volume_ml -= amount
            print(f"Applied {amount}ml of lotion. {self.volume_ml}ml left.")

my_lotion = LotionBottle("lavender", 250)
print(type(my_lotion))
# Output: <class '__main__.LotionBottle'>

my_lotion.apply(50)
# Output: You need to open the bottle first.

my_lotion.open()
my_lotion.apply(50)
# Output: Applied 50ml of lotion. 200ml left.

print(my_lotion.scent)       # lavender
print(my_lotion.volume_ml)   # 200
print(my_lotion.is_open)     # True
