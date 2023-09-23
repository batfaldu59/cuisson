import time
import beepy


def effectuer_cuisson(choix_cuisson):
    duree = choix_cuisson
    print("Cuisson en cours: ", end="", flush=True)
    print()
    while True:
        for i in range(DUREE_PROGRESSION):
            time.sleep(1)
            print(".", end="", flush=True)
            duree -= 1
            if duree <= 0:
                break
        if duree <= 0:
            break
        min = duree // 60
        sec = duree - min * 60
        print()
        print(f"Temps restant: {min:02d}:{sec:02d}", end="", flush=True)



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


def obtenir_temps(duree):
    min = duree // 60
    sec = duree - min * 60
    temps = ""
    min_unit = "minutes"
    sec_unit = "secondes"
    if min == 1:
        min_unit = "minute"
    if sec == 1:
        sec_unit = "secconde"
    if min > 0:
        temps += f"{min} {min_unit}"
    if sec > 0:
        if len(temps) > 0:
            temps += " "
        temps += f"{sec} {sec_unit}"
    return temps






# --------------------- Programme principale



CUISSONS = (
    ("Oeufs à la coque", 3*60),
    ("Oeufs mollets", 6*60),
    ("Oeufs dur", 9*60)
)

# nombre depoint à affichier
DUREE_PROGRESSION = 10
title = "Choix de cuisson"


print("-"*len(title), title, "-"*len(title))
index = 1
for cuisson in CUISSONS:
    print(f"{index}) {cuisson[0]} ({obtenir_temps(cuisson[1])})")
    index += 1

choix = demander_choix_cuisson(1, len(CUISSONS))
choix_cuisson = CUISSONS[choix-1][1]
effectuer_cuisson(choix_cuisson)
print()
print("Cuisson términée!")
beepy.beep(sound="ping")


