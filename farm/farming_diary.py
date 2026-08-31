from farm.corn import Corn
from farm.rice import Rice

print("\n📝 Day One: Corn\n")

# 1. Gün: Mısır ekme, sulama ve olgunlaşma kontrolü
corn = Corn()
print(f"Corn planted. Grains: {corn.grains}, Ripe: {corn.ripe()}")

corn.water()
print(f"Watered once. Grains: {corn.grains}, Ripe: {corn.ripe()}")

corn.water()
print(f"Watered twice. Grains: {corn.grains}, Ripe: {corn.ripe()}")


print("\n📝 Day Two: Rice\n")

# 2. Gün: Pirinç ekme, fideleme (transplant), sulama ve kontrol
rice = Rice()
print(f"Rice planted. Grains: {rice.grains}, Ripe: {rice.ripe()}")

rice.transplant()
print("Rice transplanted.")

while not rice.ripe():
    rice.water()
    print(f"Watered rice. Grains: {rice.grains}, Ripe: {rice.ripe()}")
