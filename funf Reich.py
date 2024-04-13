import random


class Stunden:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.arbeit = True

    def to_study(self):
        print("Uhr fur Studien ")
        self.progress += 0.12
        self.gladness -= 3

    def to_chill(self):
        print("Uhr fur schlaffen ")
        self.gladness += 3

    def to_sleep(self):
        print("Ich kuhlen ")
        self.gladness += 5
        self.progress -= 0.1

    def is_alive(self):
        if self.progress < -0.5:
            print('Aus der Schule geworfen')
            self.arbeit = False
        elif self.gladness <= 0:
            print("Sie haben im Alter von null Jahren eine Depression")
            self.arbeit = False
        elif self.progress > 5:
            print("Du genius")
            self.arbeit = False

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")

    def live(self, day):
        day = "Day" + str(day) + "of" + self.name + "life"
        print(f"{day:=^50}")
        live_cube = random.randint(1,3 )
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        self.end_of_day()
        self.is_alive()


student = Stunden(name="Sigma")

for day in range(365):
    if student.arbeit == False:
        break
    student.live(day)




























































































































































