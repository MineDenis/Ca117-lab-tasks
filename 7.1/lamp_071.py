import sys

class Lamp:
    def __init__(self, on=False):
        self.on = on

    def turn_on(self):
        self.on = True

    def turn_off(self):
        self.on = False

    def toggle(self):
        self.on = not self.on

def main():
    lamp1 = Lamp()
    print(lamp1.on)
    lamp1.turn_off()
    print(lamp1.on)
    lamp1.turn_on()
    lamp1.turn_on()
    print(lamp1.on)
    lamp1.turn_off()
    print(lamp1.on)
    lamp1.turn_off()
    print(lamp1.on)
    lamp1.toggle()
    print(lamp1.on)
    lamp1.toggle()
    lamp1.toggle()
    print(lamp1.on)

    lamp2 = Lamp(True)
    print(lamp2.on)
    lamp2.turn_on()
    lamp2.turn_on()
    print(lamp2.on)
    lamp1.turn_off()
    print(lamp2.on)
    lamp2.toggle()
    print(lamp2.on)

if __name__ == '__main__':
    main()
