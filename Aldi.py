# Fungsi Rekursif untuk Menghitung Bilangan Berpangkat
def pangkat(x,y):
   if y == 0:
      return 1
   else:
      return x * pangkat(x,y-1)

x = int(input("Masukan Nilai X : "))
y = int(input("Masukan Nilai Y : "))

print("%d dipangkatkan %d = %d" % (x,y,pangkat(x,y)))

# Menghitung Bilangan Faktorial Dengan Fungsi Rekursif di Python
def faktorial(a):
   if a == 1:
      return (a)
   else:
      return (a*faktorial(a-1))

bil = int(input("Masukan Bilangan : "))

print("%d! = %d" % (bil, faktorial(bil)))