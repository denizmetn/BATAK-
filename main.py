# Puanlama sistemi
#   - Oyuncu tahmin ettiği eli alırsa "tahmin x 10" puan kazanır (3 tahmin edip tam 3 el almışsa 30 puan)
#   - Fazladan aldığı her el için 1 puan eklenir (3 tahmin edip 5 aldıysa: 32)
#   - Tahmininden az el alırsa "tahmin x 10" puan kaybeder (3 tahmin edip 2 aldıysa: -30)

import random

A = ['♠', '♣', '♥', '♦']
B = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

x = int(input("oyun kaç el oynansın : "))
for i in range(x):
    oyuncu1 = 0
    oyuncu2 = 0
    oyuncu3 = 0
    oyuncu4 = 0

    o1 = 0
    o2 = 0
    o3 = 0
    o4 = 0
    deste = []
    for i in A:
        for j in B:
            deste.append(i+j)

    oyuncular = {}
    oyuncu_sira = []
    print("OYUNCULARIN İSİMLERİNİ GİRİN:")
    for i in range(4):
        oyuncular.setdefault(input("Oyuncu " + str(i+1) + ": "), {}.fromkeys(A))

    for oyuncu in oyuncular:
        oyuncu_sira.append(oyuncu)
        for i in A:
            oyuncular[oyuncu][i] = []
        for i in range(13):
            kart = random.choice(deste)
            oyuncular[oyuncu][kart[0]].append(kart[1:])
            deste.remove(kart)

    print("\nDAĞITILAN KARTLAR:")
    for oyuncu in oyuncular:
        print(oyuncu + ":")
        for karttip in oyuncular[oyuncu]:
            oyuncular[oyuncu][karttip].sort(key=B.index)
            print(karttip, oyuncular[oyuncu][karttip])
    oyuncu1t = int(input(f"{oyuncu_sira[0]} tahminen kaç el kazanır : "))
    oyuncu2t = int(input(f"{oyuncu_sira[1]} tahminen kaç el kazanır : "))
    oyuncu3t = int(input(f"{oyuncu_sira[2]} tahminen kaç el kazanır : "))
    oyuncu4t = int(input(f"{oyuncu_sira[3]} tahminen kaç el kazanır : "))

    print("\nOYUN BAŞLADI...")
    oyun_skor = dict()
    macaAtildi = False
    sira = random.randrange(4)
    for el in range(13):
        print(str(el+1) + ". el:")
        oynayan = 0
        oynanan_kartlar = []
        while oynayan < 4:
            oyuncu = oyuncu_sira[sira]
            if oynayan == 0:
                while True:
                    if macaAtildi:
                        kart_tipi = random.choice(A)
                    else:
                        kart_tipi = random.choice(A[1:])
                    if len(oyuncular[oyuncu_sira[sira]][kart_tipi]):
                        break
                oyuncu_kart = (oyuncu, kart_tipi, oyuncular[oyuncu][kart_tipi].pop())
            else:
                if len(oyuncular[oyuncu][kart_tipi]):
                    oyuncu_kart = (oyuncu, kart_tipi, oyuncular[oyuncu][kart_tipi].pop())
                elif len(oyuncular[oyuncu]['♠']):
                    oyuncu_kart = (oyuncu, '♠', oyuncular[oyuncu]['♠'].pop(0))
                    macaAtildi = True
                else:
                    kart_tipleri = A[1:].copy()
                    for tip in kart_tipleri:
                        if len(oyuncular[oyuncu][tip]):
                            oyuncu_kart = (oyuncu, tip, oyuncular[oyuncu][tip].pop(0))
                            break
            print(oyuncu_kart[0], oyuncu_kart[1] + oyuncu_kart[2])
            oynanan_kartlar.append(oyuncu_kart)
            oynayan += 1
            sira += 1
            if sira >= 4:
                sira -= 4

        en_buyuk = oynanan_kartlar[0]
        for kart in oynanan_kartlar[1:]:
            if kart[1] == en_buyuk[1] and B.index(kart[2]) > B.index(en_buyuk[2]):
                en_buyuk = kart
            elif en_buyuk[1] != '♠' and kart[1] == '♠':
                en_buyuk = kart
        print("eli kazanan:", en_buyuk[0])
        sira = oyuncu_sira.index(en_buyuk[0])
        oyun_skor[en_buyuk[0]] = oyun_skor.setdefault(en_buyuk[0], 0) + 1
        if en_buyuk[0] == 'oyuncu1' :
            o1 += 1
        if en_buyuk[0] == 'oyuncu2' :
            o2 += 1
        if en_buyuk[0] == 'oyuncu3' :
            o3 += 1
        if en_buyuk[0] == 'oyuncu4' :
            o4 += 1

        if o1 == oyuncu1t :
            oyuncu1p = oyuncu1t * 10
        if o1 > oyuncu1t :
            oyuncu1p = oyuncu1t * 10 + (o1 - oyuncu1t)
        if o1 < oyuncu1t :
             oyuncu1p = oyuncu1t * (-10)

        if o2 == oyuncu2t :
            oyuncu2p = oyuncu2t * 10
        if o2 > oyuncu2t :
            oyuncu2p = oyuncu2t * 10 + (o2 - oyuncu2t)
        if o2 < oyuncu2t :
             oyuncu2p = oyuncu2t * (-10)

        if o3 == oyuncu3t :
            oyuncu3p = oyuncu3t * 10
        if o3 > oyuncu3t :
            oyuncu3p = oyuncu3t * 10 + (o3 - oyuncu3t)
        if o3 < oyuncu3t :
             oyuncu3p = oyuncu3t * (-10)

        if o4 == oyuncu4t :
            oyuncu4p = oyuncu4t * 10
        if o4 > oyuncu4t :
            oyuncu4p = oyuncu4t * 10 + (o4 - oyuncu4t)
        if o4 < oyuncu4t :
             oyuncu4p = oyuncu4t * (-10)

    print("SKOR:", oyun_skor)
    print(f"{oyuncu_sira[0]}'in puanı : ", oyuncu1p)
    print(f"{oyuncu_sira[1]}'nin puanı : ", oyuncu2p)
    print(f"{oyuncu_sira[2]}'ün puanı : ", oyuncu3p)
    print(f"{oyuncu_sira[3]}'ün puanı : ", oyuncu4p)

