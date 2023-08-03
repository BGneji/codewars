"""Building blocks"""

# class Block:
#
#     def __init__(self, mylist):
#         self.mylist = mylist
#         self.width = mylist[0]
#         self.length = mylist[1]
#         self.height = mylist[2]
#
#     def get_width(self):
#         return self.width
#
#     def get_length(self):
#         return self.length
#
#     def get_height(self):
#         return self.height
#
#     def get_volume(self):
#         return self.height * self.width * self.length
#
#     def get_surface_area(self):
#         return 2 * (self.width * self.height + self.width * self.length + self.length * self.height)
#
#
# block1 = Block([2, 2, 2])
# print(block1.get_width())
# print(block1.get_surface_area())

"""Refactored Greeting"""

# class Person:
#
#     def __init__(self, my_name):
#         self.name = my_name
#
#     def greet(self, your_name):
#         return "Hello %s, my name is %s" % (your_name, self.name)
#
#
# jack = Person("Jack")
# jill = Person("Jill")
# print(jack.greet('Jill'))
# print(jack.greet('Mary'))
# print(jill.greet('Jack'))
# print(jill.name)


# class Song:
#     def __init__(self, title, artist):
#         self.title = title
#         self.artist = artist
#         self._seen = set()
#
#     def __str__(self):
#         return f'Песня: {self.title} Артист: {self.artist }'
#
#     def how_many(self, people):
#         tmp = set(map(str.lower, people))
#         res = len(tmp - self._seen)
#         self._seen.update(tmp)
#         return res
#
#
#
# mount_moose = Song('Mount Moose', 'The Snazzy Moose')
#
# print((mount_moose.title))
# print((mount_moose.artist))
# print(mount_moose.how_many(['John', 'Fred', 'BOb', 'carl', 'RyAn']))
# print(mount_moose.how_many(['JoHn', 'Luke', 'AmAndA']))

"""Person Class Bug"""
# class Person:
#
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#
#     def __str__(self):
#         return f'{self.first_name} {self.last_name}'
#
#     @property
#     def full_name(self):
#         return (f'{self.first_name} {self.last_name}')
#
#
#
#
#
# person = Person('Yukihiro', 'Matsumoto', 47)
# print(person.full_name)
# print(person.age)

"""Building Spheres"""
import math


class Sphere(object):
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass
        self.pi = math.pi

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_surface_area(self):
        surface_area = 4 * self.pi * (self.radius ** 2)
        return float(f'{surface_area:.5f}')

    def get_volume(self):
        volume = 4 / 3 * self.pi * (self.radius ** 3)
        return float(f'{volume:.5f}')

    def get_density(self):
        density = self.mass / self.get_volume()
        return float(f'{density:.5f}')


ball = Sphere(2, 50)
print(ball.get_radius())
print(ball.get_volume())
print(ball.get_surface_area())
print(ball.get_density())
