import time
import beepy


def effectuer_cuisson(index_choix):
    duree = CUISSONS[index_choix-1][1] * 60
    print("Cuisson en cours: ", end="", flush=True)
    print()
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


def demander_choix_cuisson(min, max):
    choix_str = input(f"Votre choix (entre {min} et {max}): ")
    try:
        choix_int = int(choix_str)
        if not min <= choix_int <= max:
            print(f"ERREUR: votre choix doit être entre {min} et {max}")
            return demander_choix_cuisson(min, max)
        return choix_int
    except ValueError:
        print("ERREUR: vous ne pouvez rentrer qu'une valeur numérique")
        return demander_choix_cuisson(min, max)


# --------------------- Programme principale


CUISSONS = (
    ("Oeufs à la coque", 3),
    ("Oeufs mollets", 6),
    ("Oeufs dur", 9)
)
title = "Choix de cuisson"


print("-"*len(title), title, "-"*len(title))
index = 1
for cuisson in CUISSONS:
    print(f"{index}) {cuisson[0]} ({cuisson[1]} min)")
    index += 1

valeur_max_choix = index - 1
choix = demander_choix_cuisson(1, valeur_max_choix)
effectuer_cuisson(choix)
print("Cuisson términée!")
beepy.beep(sound="ping")


