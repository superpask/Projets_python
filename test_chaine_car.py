import re


phrase = "Bonjour tout le monde."
nouvelle_phrase = phrase.replace("jour", "soir")
print(nouvelle_phrase)


lettre_a_chercher = "o"
phrase = "Bonjour tout le monde"
resultat = phrase.count(lettre_a_chercher)
print(resultat)