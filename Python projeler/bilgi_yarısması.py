def tahmini_kontrol_et(tahmin, cevap):
    global puan
    hala_tahmin_ediyor = True
    deneme = 0
    while hala_tahmin_ediyor and deneme < 3:
        if tahmin.lower() == cevap.lower():
            print("Doğru Cevap!")
            puan = puan + 1
            hala_tahmin_ediyor = False
        else:
            if deneme < 2:
                tahmin = input("Üzgünüm, yanlış cevap. Tekrar deneyin: ")
            deneme = deneme + 1
    if deneme == 3:
        print("Doğru cevap: ", cevap)


puan = 0
print("Hayvanı Tahmin Et!")
tahmin1 = input("Hangi ayı Kuzey Kutbu'nda yaşar? ")
tahmini_kontrol_et(tahmin1, "kutup ayısı")
tahmin2 = input("Dünyanın en hızlı kara hayvanı hangisidir? ")
tahmini_kontrol_et(tahmin2, "çita")
tahmin3 = input("Dünyanın en büyük hayvanı hangisidir? ")
tahmini_kontrol_et(tahmin3, "mavi balina")
print("Puanınız: " + str(puan))
