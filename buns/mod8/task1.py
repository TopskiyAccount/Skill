class Transport:
    def __init__(self, coordinates, speed, brand, year, number):
        self._coordinates = coordinates
        self._speed = speed
        self._brand = brand
        self._year = year
        self._number = number

    @property
    def coordinates(self):
        return self._coordinates

    @coordinates.setter
    def coordinates(self, value):
        self._coordinates = value

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        self._speed = value

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        self._brand = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        self._year = value

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        self._number = value

    def __str__(self):
        return f"Coordinates: {self.coordinates}, Speed: {self.speed}, Brand: {self.brand}, Year: {self.year}, Number: {self.number}"

    def isInArea(self, pos_x, pos_y, length, width):
        return (pos_x <= self.coordinates[0] <= pos_x + length and
                pos_y <= self.coordinates[1] <= pos_y + width)


class Passenger:
    def __init__(self, passengers_capacity, number_of_passengers):
        self._passengers_capacity = passengers_capacity
        self._number_of_passengers = number_of_passengers

    @property
    def passengers_capacity(self):
        return self._passengers_capacity

    @passengers_capacity.setter
    def passengers_capacity(self, value):
        self._passengers_capacity = value

    @property
    def number_of_passengers(self):
        return self._number_of_passengers

    @number_of_passengers.setter
    def number_of_passengers(self, value):
        self._number_of_passengers = value


class Cargo:
    def __init__(self, carrying):
        self._carrying = carrying

    @property
    def carrying(self):
        return self._carrying

    @carrying.setter
    def carrying(self, value):
        self._carrying = value


class Plane(Transport):
    def __init__(self, coordinates, speed, brand, year, number, height):
        super().__init__(coordinates, speed, brand, year, number)
        self._height = height


class Auto(Transport):
    pass


class Ship(Transport):
    def __init__(self, coordinates, speed, brand, year, number, port):
        super().__init__(coordinates, speed, brand, year, number)
        self._port = port


class Car(Auto):
    pass


class Bus(Auto, Passenger):
    pass


class CargoAuto(Auto, Cargo):
    pass


class Boat(Ship):
    pass


class PassengerShip(Ship, Passenger):
    pass


class CargoShip(Ship, Cargo):
    pass
