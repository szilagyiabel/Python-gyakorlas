import random

def beolvas_kerdeseket(fajlnev):
    kerdesek = []
    with open(fajlnev, 'r', encoding='utf-8') as f:
        tartalom = f.read().split('\n\n')
        for blokk in tartalom:
            sorok = blokk.split('\n')
            kerdesek.append(sorok)
    return kerdesek

def beolvas_valaszokat(fajlnev):
    valaszok = {}
    with open(fajlnev, 'r', encoding='utf-8') as f:
        for sor in f:
            sorszam, valasz = sor.strip().split()
            valaszok[int(sorszam)] = valasz
    return valaszok

def main():
    kerdesek = beolvas_kerdeseket('KERDESEK.txt')
    valaszok = beolvas_valaszokat('VALASZOK.txt')

    darabszam = int(input("Hány kérdésre szeretnél válaszolni? "))
    kivalasztott_kerdesek = random.sample(kerdesek, darabszam)
    
    helyes_valaszok = 0
    for i, kerdes in enumerate(kivalasztott_kerdesek, start=1):
        for sor in kerdes:
            print(sor)
        helyes = valaszok[i]
        valasz = input("Válaszod: ").lower()
        
        if valasz == helyes:
            print("Helyes válasz!")
            helyes_valaszok += 1
        else:
            print(f"A válasz helytelen! A helyes válasz: {helyes}")
    
    teljesitmeny = (helyes_valaszok / darabszam) * 100
    
    print(f"\nElért százalék: {teljesitmeny}%")
    if teljesitmeny > 50:
        print("átmentél")
    else:
        print("megbuktál.")

main()
