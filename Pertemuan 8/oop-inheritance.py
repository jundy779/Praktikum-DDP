class Person():
  # Definitions awal Variable
  nama = ""
  address = ""
  age = 0
  
  # Constructor :=> Pembungkus
  def __init__(self, name, address, age):
      self.name = name
      self.address = address
      self.age = age
      
  
  
    # Method / Fuction
  def sayHello(self):
      print("Hello nama saya ", self.name, "usia saya ", self.age, "alamat saya di ", self.address)
:=> nurunin sifat dari kelas Person
# Extend 
  
class Student(Person):
  # Manggil constructor class person
  def __init__(self, name, address, age, nim, jurusan):
    super().__init__(name, address, age)
    self.nim = nim
    self.jurusan = jurusan
    
# Instance object
  
jundi = Student("jundi", "Bogor, Jabar", 20, "0110122233", "Sistem Informasi")

jundi.sayHello()
print("Nim: ", jundi.nim)
print("Jurusan: ", jundi.jurusan)