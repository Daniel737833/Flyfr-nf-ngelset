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
    print("Du vaknar i en mörk, kall cell. Stenväggarna är kalla och en liten spricka i dörren släpper in ett svagt ljus.")
    print("Du ser ett rostigt dörr hantag i hörnet. På golvet finns en matbricka med möglig mat")
    print("Dörren är låst. Vad gör du?")
    print("1. Leta efter en nyckel")
    print("2. Ropa på hjälp")
    val = input("> ")
    if val == "1":
        print("Du rotar runt på golvet och under matbrickan hittar du en rostig nyckel!")
        return True
    else:
        print("Dina rop ekar genom cellen, men ingen svarar.")
        print("Istället kommer det in en vakt som börjar slå dig med en batong.")
        print("Därefter smäller han dörren bakom sig och stänger in dig igen i cellen. Försök igen")
        return False

def rum_2():
    print("Du smyger ut ur cellen och befinner dig i ett svagt upplyst korridor.")
    print("Golvets betong är kall under dina fötter, och du hör fotsteg.")
    print("Du ser en vakt som står vid dörren längre fram, vänd bort från dig.")
    print("\nRum 2: Korridoren")
    print("Vad vill du göra?")
    print("1. Smyga förbi")
    print("2. Distrahera vakten")
    val = input("> ")
    if val == "2":
        print("Du kastar en sten mot väggen längre bort. Vakten vänder sig om för att undersöka, och du smyger snabbt förbi!")
        return True
    elif val == "1":
        print("Du försöker smyga förbi, men vakten hör dina steg och griper dig! Du förs tillbaka till din cell.")
        main()
        return False
    else:
        print("Vakten ser dig. Försök igen.")
        return False

def rum_3():
    print("Du kommer in i ett stort rum där flera fångar sitter och viskar till varandra.")
    print("En fånge signalerar åt dig med handen att komma närmare.")
    print("\nRum 3: Fångarnas samlingsrum")
    print("Vad vill du göra?")
    print("1. Prata med fången")
    print("2. Försök ta en annan väg")
    val = input("> ")
    if val == "1":
        kod = random.randint(1000, 9999)
        print(f"Fången ser sig omkring och viskar: 'Jag har sett koden till förvaringsrummet. Den är {kod}.')")
        while True:
            kod_input = input("Ange koden för att gå vidare: ")
            if kod_input == str(kod):
                print("Rätt kod! Du får passera.")
                return True
            else:
                print("Fel kod, försök igen.")
    else:
        print("Du försöker hitta en annan väg, men rummet har bara en utgång. Försök igen.")
        return False


def rum_4():
    print("Du smyger in i ett stökigt kontor, fullt av papper och mappar som ligger huller om buller.")
    print("Den enda vägen vidare är en låst dörr med ett kodlås.")
    print("Någonstans här inne bland alla papper och mappar finnas en kod som kan hjälpa dig.")
    print("\nRum 4: Kontorrummet")
    print("Vad vill du göra?")
    print("1. Försök gissa koden")
    print("2. Rota igenom alla papper och mappar")
    val = input("> ")
    if val == "2":
        print("Du rotar igenom alla papper och mappar och hittar en kod.")
        print("Du använder koden för att låsa upp dörren och du smyger vidare!")
        return True
    else:
        print("Du försöker gissa koden men misslyckas, försök igen.")
        return False


def rum_5():
    print("Du kommer in i en smal, mörk korridor där röda laserstrålar skär genom luften i olika mönster.")
    print("Väggarna är täckta av metall, och golvet har skrapmärken från tidigare försök att ta sig igenom.")
    print("Du börjar att inse ett felaktigt steg kan aktivera ett larm eller något ännu värre.")
    print("\nRum 5: Laserfällan")
    print("Vad vill du göra?")
    print("1. Försök krypa under lasrarna")
    print("2. Leta efter en avstängningsknapp")
    val = input("> ")
    if val == "2":
        print("Du undersöker väggarna och ser en liten panel med kablar, där du hittar en knapp.")
        print("Du trycker försiktigt på knappen och hör ett ljud där lasrarna långsamt börjar slockna.")
        return True
    else:
        print("Du försöker krypa under lasrarna, men en av strålarna träffar din arm och en högljudd siren går igång!")
        print("Försök igen.")
        return False


def rum_6():
    print("Du smyger in i ett mörkt rum fyllt med skärmar som övervakar hela fängelset.")
    print("På ett bord ligger en terminal med ett kortläsarsystem som låser upp nästa dörr.")
    print("Men var är nyckelkortet?")
    print("\nRum 6: Övervakningsrummet")
    print("Vad vill du göra?")
    print("1. Leta i skrivbordslådorna")
    print("2. Försök att slå dig igenom dörren")
    val = input("> ")
    if val == "1":
        print("Du öppnar skrivbordslådorna och hittar ett nyckelkort!")
        print("Du använder kortet på terminalen och dörren låses upp.")
        return True
    else:
        print("Du försöker bryta upp dörren men misslyckas. Försök igen.")
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