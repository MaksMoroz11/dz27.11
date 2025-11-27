import csv
from os import path as ops
from modules.Car import Car


COLUMNS = ['id', 'model', 'plate']


class CarsRepository:
    def __init__(self, path):
        self.__cars = []
        self.__path = path
        if not ops.exists(path):
            with open(path, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, COLUMNS)
                writer.writeheader()

    def update(self, new_car = None):
        if new_car is not None:
            for car in range(len(self.__cars)):
                if self.__cars[car].id == new_car.id:
                    self.__cars[car].model = new_car.model
                    self.__cars[car].plate = new_car.plate
                    break
        with open(self.__path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, COLUMNS)
            writer.writeheader()
            writer.writerows([car.get_info() for car in self.__cars])

    def create(self, new_car):
        found_same_car = False
        for car in self.__cars:
            if car.id == new_car.id:
                found_same_car = True
                break

        if not found_same_car:
            self.__cars.append(new_car)
            self.update()

    def read(self):
        self.__cars.clear()
        with open(self.__path, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, COLUMNS)
            for row in reader:
                id, model, plate = row['id'], row['model'], row['plate']
                if id.isdigit():
                    self.__cars.append(Car(int(id), model, plate))

    def delete(self, id):
        for i in range(len(self.__cars)):
            if self.__cars[i].id == id:
                self.__cars.pop(i)
                break
        self.update()

if __name__ == '__main__':
    cars_repo = CarsRepository('cars.csv')
    cars_repo.read()
    cars_repo.create(Car(2, 'Cadillac', 'Phoenix'))
    cars_repo.create(Car(1, 'Mercedes', 'White'))
    cars_repo.delete(1)
    cars_repo.update(Car(2, 'Cadillac', 'Blackjack'))
