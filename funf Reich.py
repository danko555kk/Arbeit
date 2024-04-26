import random


class Stunden:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 50
        self.dry = 50
        self.arbeit = True

    def to_study(self):
        print("Time to eat the dry food ")
        self.progress += 30
        self.gladness -= 10
        self.dry -= 30

    def to_chill(self):
        print("DRINK DRINK DRINK")
        self.dry += 100

    def to_sleep(self):
        print("I will play with someone!")
        self.gladness += 75
        self.progress -= 40
		self.dry -= 75

	def to_doy(self):
        print("ZzzzzZzzzz")
        self.gladness += 3
        self.progress = 100
		
    def is_alive(self):
        if self.progress < -1:
            print('Your dog die of tired')
            self.arbeit = False
        elif self.gladness <= 0:
            print("Your dog become human emo")
            self.arbeit = False
        elif self.progress > 500:
            print("Your dog was so energy, that broke window and die")
            self.arbeit = False
        elif self.dry <= 0:
            print("Your dog die of dry")
            self.arbeit = False
    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Hunger = {round(self.progress, 2)}")
		print(f"Thirst = {round(self.dry, 2)}")

    def live(self, day):
        day = "Day" + str(day) + "of" + self.name + "life"
        print(f"{day:=^50}")
        live_cube = random.randint(1,4 )
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
		elif live_cube == 4:
            self.to_doy()
        self.end_of_day()
        self.is_alive()


student = Stunden(name="Sigma")

for day in range(365):
    if student.arbeit == False:
        break
    student.live(day)




























































































































































