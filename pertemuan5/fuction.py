'''
    *
'''

def hello():
    print("hello, world")
    
hello()
hello()
hello()
hello()

# function dengan parameter

def sayHello(name):
    print(f"Hello, nama saya {name}")
    
    
sayHello("Budi")
sayHello("Joko")

def tambah(bilanganPertama, bilanganKedua):
    total = bilanganPertama + bilanganKedua
    print(total)
    
tambah(10, 5)

'''
    * Challenge
'''
# Buat fungsi yang bisa membuat perkalian
# Buat fungsi yang bisa membuat pembagian
def perkalian(bilanganPertama, bilanganKedua):
    total = bilanganPertama * bilanganKedua
    print(total)
    
perkalian(10, 10)

def pembagian(bilanganPertama, bilanganKedua):
    total = bilanganPertama / bilanganKedua
    print(total)
    
pembagian(100, 2)