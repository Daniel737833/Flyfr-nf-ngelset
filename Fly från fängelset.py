import random

def intro():
    print("Välkommen till 'Fly från fängelset'!")
    print("Du är inlåst och måste hitta en väg ut.")
    print("Gör val för att lyckas fly. \n")


def visa_instruktioner():
    while True:
        print("\nFly från fängelset - En textbaserad äventyrsspel")
        print("\nBeskrivning:")
        print("'Fly från fängelset' är ett textbaserat äventyrsspel där du spelar som en fånge som försöker rymma.")
        print("Genom att navigera genom olika rum och göra rätt val kan du lyckas ta dig ut.")
        print("Spelet innehåller olika utmaningar, inklusive ett bossrum där du måste besegra en vaktchef för att vinna.\n")
        
        print("Hur man spelar")
        print("--------------")
        print("Spelaren måste göra val för att ta sig vidare genom olika rum.")
        print("I huvudmenyn kan du välja att starta ett nytt spel, ändra svårighetsgrad,")
        print("visa instruktioner eller avsluta spelet.")
        print("I varje rum ges spelaren ett antal alternativ att välja mellan.")
        print("Om spelaren gör rätt val, går de vidare till nästa rum.")
        print("Om spelaren gör ett felaktigt val, måste de försöka igen tills rätt val görs.")
        print("I det sista rummet möter du en boss som du måste besegra i en strid.\n")
        
        print("Kontroller")
        print("----------")
        print("Använd nummer för att göra val i spelet, exempelvis '1' eller '2'.\n")
        
        print("Svårighetsgrader")
        print("---------------")
        print("Lätt – För en enklare spelupplevelse.")
        print("Normal – Balanserad svårighetsgrad.")
        print("Svår – Utmanande, där val och strategier är avgörande.\n")
        
        print("Avsluta spelet")
        print("--------------")
        print("Vill du inte spela längre så kan du när som helst skriva 'SLUTA',")
        print("vilket tar dig tillbaka till huvudmenyn.\n")
        
        print("Tryck [B] för att gå tillbaka till huvudmenyn.")
        val = input("> ").lower()
        if val == "b":
            return


def meny():
    while True:
        print("\nHuvudmeny:")
        print("1. Starta nytt spel")
        print("2. Välj svårighetsgrad")
        print("3. Visa instruktioner")
        print("4. Avsluta")
        print("Vad vill du göra:")
        val = input("> ")
        
        if val == "1":
            main()
            break
        elif val == "2":
            valj_svarighetsgrad()
        elif val == "3":
            visa_instruktioner()
        elif val == "4":
            print("Spelet avslutas.")
            exit()
        else:
            print("Ogiltigt val, försök igen.")


def valj_svarighetsgrad():
    global svårighetsgrad
    print("\nVälj svårighetsgrad:")
    print("1. Lätt")
    print("2. Normal")
    print("3. Svår\n")
    print("Tryck [B] för att gå tillbaka till huvudmenyn.")
    val = input("> ")
    if val == "b":
            return
    
    if val == "1":
        svårighetsgrad = "Lätt"
        print("Svårighetsgrad inställd på Lätt.\n")
    elif val == "2":
        svårighetsgrad = "Normal"
        print("Svårighetsgrad inställd på Normal.\n")
    elif val == "3":
        svårighetsgrad = "Svår"
        print("Svårighetsgrad inställd på Svår.\n")
    else:
        print("Ogiltigt val, försöker igen.")
        valj_svarighetsgrad()


def rum_1():
    print("Rum 1: Din cell")
    print("Dörren är låst. Vad gör du?")
    print("1. Leta efter en nyckel")
    print("2. Ropa på hjälp")
    val = input("> ")
    if val == "1":
        print("Du hittar en nyckel!")
        return True
    else:
        print("Inget händer. Försök igen.")
        return False


def rum_2():
    print("\nRum 2: Korridoren")
    print("En vakt står vid dörren.")
    print("1. Smyga förbi")
    print("2. Distrahera vakten")
    val = input("> ")
    if val == "2":
        print("Vakten blir distraherad, du smyger förbi!")
        return True
    elif val == "1":
        print("Vakten ser dig! Du blir tillbakaskickad till din cell.")
        main()
        return False
    else:
        print("Vakten ser dig. Försök igen.")
        return False


def rum_3():
    print("\nRum 3: Fångarnas samlingsrum")
    print("Här finns en annan fånge som kan hjälpa dig.")
    print("1. Prata med fången")
    print("2. Försök ta en annan väg")
    val = input("> ")
    if val == "1":
        print("Fången ger dig en viktig kod till nästa dörr!")
        return True
    else:
        print("Du hittar ingen annan väg. Försök igen.")
        return False


def rum_4():
    print("\nRum 4: Förvaringsrummet")
    print("Här finns en låst dörr med en kodlås.")
    print("1. Försök knäcka koden")
    print("2. Leta efter något som kan hjälpa dig")
    val = input("> ")
    if val == "2":
        print("Du hittar en lapp med koden och öppnar dörren!")
        return True
    else:
        print("Koden fungerar inte. Försök igen.")
        return False


def rum_5():
    print("\nRum 5: Laserfällan")
    print("Du står inför en korridor fylld med laserstrålar.")
    print("1. Försök krypa under lasrarna")
    print("2. Leta efter en avstängningsknapp")
    val = input("> ")
    if val == "2":
        print("Du hittar knappen och stänger av lasrarna!")
        return True
    else:
        print("Lasrarna träffar dig! Försök igen.")
        return False


def rum_6():
    print("\nRum 6: Utgången")
    print("En låst dörr leder ut.")
    print("1. Använd nyckeln")
    print("2. Leta efter en annan väg")
    val = input("> ")
    if val == "1":
        print("Dörren öppnas, du är fri!")
        return True
    else:
        print("Du hittar ingen annan väg. Försök igen.")
        return False

def rum_7():
    print("\nRum 7: Bossrummet")
    print("Du har nästan lyckats fly, men en vaktchef står i vägen!")
    boss_hp = 30
    player_hp = 25
    while boss_hp > 0 and player_hp > 0:
        print(f"\nDitt HP: {player_hp} | Bossens HP: {boss_hp}")
        print("1. Slå med näven (5 skada)")
        print("2. Specialattack (10 skada, 50% chans att missa)")
        val = input("> ")
        if val == "1":
            boss_hp -= 5
            print("Du träffar bossen!")
        elif val == "2":
            if random.random() > 0.5:
                boss_hp -= 10
                print("Din specialattack träffar hårt!")
            else:
                print("Din attack missar!")
        else:
            print("Ogiltigt val, försök igen.")
            continue
        
        if boss_hp > 0:
            skada = random.randint(3, 7)
            player_hp -= skada
            print(f"Bossen attackerar dig och gör {skada} skada!")
    
    if player_hp <= 0:
        print("Bossen besegrar dig! Du skickas tillbaka till din cell.")
        main()
        return False
    else:
        print("Du besegrar bossen och flyr! Du är fri!")
        return True


def main():
    intro()
    while not rum_1():
        pass
    while not rum_2():
        pass
    while not rum_3():
        pass
    while not rum_4():
        pass
    while not rum_5():
        pass
    while not rum_6():
        pass
    while not rum_7():
        pass
    print("\nGrattis! Du har lyckats fly!")


if __name__ == "__main__":
    svårighetsgrad = "Normal"
    meny()