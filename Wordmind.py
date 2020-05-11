import random

poging_teller = 0

def random_woord():         #Deze functie kiest een random woord.
    display_woord = ""
    woorden = ["appel", "aarde", "adres", "boten", "bloed", "brand", "dalen", "dames", "droom", "enger", "elder", "enkel",
    "friet", "feest", "fruit", "gaven", "grote", "graaf", "heren", "haken", "hotel", "ieder", "icoon", "inzet",
    "jaren", "jacht", "joint", "koken", "kopje", "kudde", "links", "lijst", "luier", "maand", "markt", "macht",
    "nieuw", "negen", "namen", "onder", "ovaal", "ophef", "plein", "pegel", "preek", "robot", "regio", "rokje",
    "staal", "speel", "stand", "typen", "treur", "teler", "uiten", "ultra", "uniek", "video", "vuren", "vanaf",
    "wagen", "wazig", "wrede", "zesde", "zadel", "zweer"]
    geheim_woord = random.choice(woorden)
    woordlen = len(geheim_woord)
    for n in range(woordlen):
        display_woord += "-"
    print("Geheim woord: ", display_woord)
    return geheim_woord, woordlen

def input_woord():          #Deze functie laat de gebruiker een woord invoeren en returned de waarde.
    global poging_teller
    gerade_woord = ""
    poging_teller += 1
    gerade_woord = input("Wat is het geheime woord? ")
    return gerade_woord

def woord_controle(geheim_woord, gerade_woord, woordlen):           #Deze functie controleerd welke letters kloppen.
    global poging_teller
    teller = 0
    display_woord = ""
    if len(gerade_woord) == woordlen:
        for i in gerade_woord:
            if gerade_woord[teller] == geheim_woord[teller]:
                display_woord += geheim_woord[teller]
                teller += 1
            elif gerade_woord[teller] in geheim_woord:
                display_woord += "?"
                teller += 1
            elif gerade_woord[teller] != geheim_woord[teller]:
                display_woord += "-"
                teller += 1
        print("Geheim woord: ", display_woord)
    else:
        print("Het geraden woord heeft niet evenveel letters als het geheime woord.")
        teller += 1
        for n in range(woordlen):
            display_woord += "-"



def main():                 #Deze functie zorgt ervoor dat je opnieuw kan spelen als je dat wilt.
    global poging_teller
    naam = input("Wat is je naam? ")
    nog_een_keer_spelen = ""
    gerade_woord = ""
    while nog_een_keer_spelen != "n":
        nog_een_keer_spelen = ""
        poging_teller = 0
        geheim_woord, woordlen = random_woord()
        while gerade_woord != geheim_woord:
            gerade_woord = input_woord()
            woord_controle(geheim_woord, gerade_woord, woordlen)
        print("Het raden koste", poging_teller, "poging(en).")
        nog_een_keer_spelen = input("Wil je nog een keer spelen? j/n ")
    print("Tot ziens!")

main()                      #Deze lijn code start het programma.