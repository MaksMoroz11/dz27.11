class Car:
    def __init__(self, id, model, plate):
        self.__id = id
        self.__model = model
        self.__plate = plate

    def get_info(self):
        return {'id': self.__id, 'model': self.__model, 'plate': self.__plate}

    @property
    def id(self):
        return self.__id

    @property
    def model(self):
        return self.__model

    @property
    def plate(self):
        return self.__plate

    @model.setter
    def model(self, value):
        self.__model = value

    @plate.setter
    def plate(self, value):
        self.__plate = value
