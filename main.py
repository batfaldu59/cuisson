import time
import beepy


def cuisson(nb_minute_cuisson):
    duree = nb_minute_cuisson * 60
    print("Cuisson en cours: ", end="", flush=True)

    while duree > 0:
        print("Temps restant: ", end="", flush=True)
        min = duree // 60
        sec = duree - min * 60
        print(f" {min:02d}:{sec:02d}", end="", flush=True)
        for i in range(10):
            time.sleep(1)
            print(".", end="", flush=True)
        print()
        duree -= 10

# --------------------- Programme principale


choix = ""
while choix != "a" and choix != "b" and choix != "c":
    title = "Choix de cuisson"
    print("-"*len(title), title, "-"*len(title))
    print("a - Oeufs à la coque (3min)")
    print("b - Oeufs mollets (6 min)")
    print("c - Oeufs dur (9 min)")
    choix = input("Votre choix: ")
    if choix != "a" and choix and "b" and choix != "c":
        print("ERREUR: le choix doit être soit a, b ou c")
    elif choix == "a":
        cuisson(3)
    elif choix == "b":
        cuisson(6)
    else:
        cuisson(9)


print("Cuisson términée!")
beepy.beep(sound="ping")


