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