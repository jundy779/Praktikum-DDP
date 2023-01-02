# from Person import *
from Person import Person

class Student(Person):
  # Manggil constructor class person
  def __init__(self, name, address, age, nim, jurusan):
    super().__init__(name, address, age)
    self.nim = nim
    self.jurusan = jurusan
    