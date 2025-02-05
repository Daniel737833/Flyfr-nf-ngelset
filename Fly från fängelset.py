import random

def meny():
    while True:
        print("Huvudmeny:")
        print("1. Starta spelet")
        print("2. Avsluta")
        val = input("> ")
        if val == "1":
            main()
            break
        elif val == "2":
            print("Spelet avslutas.")
            exit()
        else:
            print("Ogiltigt val, försök igen.")


def intro():
    print("Välkommen till 'Fly från fängelset'!")
    print("Du är inlåst och måste hitta en väg ut.")
    print("Gör val för att lyckas fly. \n")


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
    print("\nGrattis! Du har lyckats fly!")


if __name__ == "__main__":
    main()
