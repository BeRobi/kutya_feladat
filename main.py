
from Kutya import Kutya

nev = ["Fifi", "Bruno", "Hektor", "Kajla", "Artúr"]
nem = ["szuka", "kan", "kan", "szuka", "kan"]
faj = ["husky", "labrador", "németjuhász", "tacskó", "bulldog"]
mar_mag = [42, 54, 68, 25, 38]
suly = [15, 21, 32, 5, 12]

# kutya = [kutya1, kutya2, kutya3, kutya4, kutya5]

# példányosítjuk az osztályt = konkrét egyed előfordulás, azaz objektum

kutya1 = Kutya("Fifi", "szuka", "husky", 42, 15)
kutya2 = Kutya("Bruno", "kan", "labrador", 54, 21)
kutya3 = Kutya("Hektor", "kan", "németjuhász", 68, 32)
kutya4 = Kutya("Kajla", "szuka", "tacskó", 25, 5)
kutya5 = Kutya("Artúr", "kan", "bulldog", 38, 12)

kutya = [kutya1, kutya2, kutya3, kutya4, kutya5]


print(kutya1)

print(kutya1.tev())
