# 2-masala. berilgan sonlar to'plamidan eng kichigini toping

sonlar = [2,4,5,56,7,8,8,1,10]

kichikSon = sonlar[0] # kichikSon = 2

for son in sonlar:
    if kichikSon > son:
        kichikSon = son

print(kichikSon)

# min funksiyasi orqali topish

print(min(sonlar))

