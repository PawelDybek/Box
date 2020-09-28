class Coffee_machine:
    state = {
        "water": 400,
        "milk": 540,
        "coffee beans": 120,
        "disposable cups": 9,
        "money": 550
    }

    def __init__(self, action):
        if action == "buy":
            self.buy_coffee()
        elif action == "fill":
            self.fill_machine()
        elif action == "take":
            self.take_money()
        elif action == "remaining":
            self.machine_state()

    def machine_state(self):
        print("The coffee machine has:")
        for key, value in self.state.items():
            print(value, "of", key)

    def make_espresso(self):
        if self.state["water"] < 250:
            print("Sorry, not enough water!")
        elif self.state["coffee beans"] < 16:
            print("Sorry, not enough coffee beans!")
        elif self.state["disposable cups"] < 1:
            print("Sorry, not enough disposable cups!")
        else:
            self.state["water"] -= 250
            self.state["coffee beans"] -= 16
            self.state["disposable cups"] -= 1
            self.state["money"] += 4

    def make_late(self):
        if self.state["water"] < 350:
            print("Sorry, not enough water!")
        elif self.state["milk"] < 75:
            print("Sorry, not enough milk!")
        elif self.state["coffee beans"] < 20:
            print("Sorry, not enough coffee beans!")
        elif self.state["disposable cups"] < 1:
            print("Sorry, not enough disposable cups!")
        else:
            self.state["water"] -= 350
            self.state["milk"] -= 75
            self.state["coffee beans"] -= 20
            self.state["disposable cups"] -= 1
            self.state["money"] += 7

    def make_cappuccino(self):
        if self.state["water"] < 200:
            print("Sorry, not enough water!")
        elif self.state["milk"] < 100:
            print("Sorry, not enough milk!")
        elif self.state["coffee beans"] < 12:
            print("Sorry, not enough coffee beans!")
        elif self.state["disposable cups"] < 1:
            print("Sorry, not enough disposable cups!")
        else:
            self.state["water"] -= 200
            self.state["milk"] -= 100
            self.state["coffee beans"] -= 12
            self.state["disposable cups"] -= 1
            self.state["money"] += 6

    def do_nothing(self):
        self.state["water"] -= 0
        self.state["milk"] -= 0
        self.state["coffee beans"] -= 0
        self.state["disposable cups"] -= 0
        self.state["money"] += 0

    def buy_coffee(self):
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        type_of_coffee = input()

        if type_of_coffee == "1":
            self.make_espresso()
        elif type_of_coffee == "2":
            self.make_late()
        elif type_of_coffee == "3":
            self.make_cappuccino()
        elif type_of_coffee == "back":
            self.do_nothing()

    def fill_machine(self):
        print("Write how many ml of water do you want to add:")
        self.state["water"] += int(input())

        print("Write how many ml of milk do you want to add:")
        self.state["milk"] += int(input())

        print("Write how many grams of coffee beans do you want to add:")
        self.state["coffee beans"] += int(input())

        print("Write how many disposable cups of coffee do you want to add:")
        self.state["disposable cups"] += int(input())

    def take_money(self):
        print("I gave you $" + str(self.state["money"]))
        self.state["money"] = 0


while True:
    print("Write action (buy, fill, take, remaining, exit):")
    order = input()

    coffee = Coffee_machine(order)

    if order == "exit":
        break
