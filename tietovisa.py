print(">>>> Tervetuloa Tietovisaan! <<<<")
print(" ")
print("Testaa tietosi tässä BTS aiheisessa visassa!")
print(" ")
print("Aloitetaan helpolla kysymyksellä...")
print(" ")


kysymys1 = str(input("Kuinka monta jäsentä BTS:ssä on? "))
if kysymys1 == "7":
    print("Aivan oikein! Olet varmasti tutustunut ryhmään jonkin verran.")
else:
    print("Väärin... Oijoi...")
    

kysymys2 = str(input("Kuka on ryhmän nuorin jäsen? "))
if kysymys2 == "Jungkook":
    print("O-o-o-oikein!! 우리 막내 <3")
else:
    print("Väärin! Oletko varmasti oikean visan äärellä?")


kysymys3 = str(input("Minä vuonna BTS on aloittanut julkaisemaan musiikkia? "))
if kysymys3 == "2013":
    print("Correct! Toivon, että olisin tutustunut heihin jo silloin :)")
else:
    print("Nyt hei... Yritä edes...")

print("Nyt on pisteiden aika... Jännittävää")
# kaikki oikein vaihtoehdot
if kysymys1 == "7" and kysymys2 == "Jungkook" and kysymys3 == "2013":
    print("Vastasit kaikkiin kysymyksiin oikein! 3/3 suoritus! Mahtavaa <3")
# 2 oikein
elif kysymys1 == "7" and kysymys2 == "Jungkook":
    print("Kaksi kolmesta oikein! Ihan hyvin")
elif kysymys1 == "7" and kysymys3 == "2013":
    print("2/3,  numerot selkeesti hallussa. Ei kyllä varmaan mikään muu...")
elif kysymys2 == "Jungkook" and kysymys3 == "2013":
    print("Kaks kautta kolme oikein. Menettelee")
# 1 oikein
elif kysymys1 == "7":
    print("Yksi oikein... Ootko ihan tosissasi?")
elif kysymys2 == "Jungkook":
    print("1/3 oikein... Tiedät sentään, kuka on ryhmän nuorin...")
elif kysymys3 == "2013":
    print("Yksi kolmesta oikein... Ei kannata kehuskella")
else:
    print("0/3... Nolla kautta kolme... Tiputettiinko sut vauvana? Olisiko sun äiti ylpeä tästä tuloksesta? Sietäisit hävetä!")

print(" ")
print(">>>> Kiitos osallistumisesta Tietovisaan! <<<<")
