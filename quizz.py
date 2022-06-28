quizz_data = {
    "Quel célèbre dictateur dirigea l’URSS du milieu des années 1920 à 1953 ?":
        ["staline"],
    "Dans quel pays peut-on trouver la Castille":
        ["espagne", "l'espagne"],
    "Quel est le nom du personnage principal de l'Oeuvre one piece":
        ["luffy", "monkey d luffy"],
    "Combien de couleur différente y a t-il sur le drapeau de l'afrique du sud":
        ["6", "six"],
    "combien font 12*9":
        ["108"],
    "Qui a dit le sort en est jeté (alea jacta est)":
        ["jules", "jules césar", "jules cesar", "cesar", "césar"],
    "qui a réalisé titanic ?":
        ["james cameron", "cameron", "james"],
    "Mon premier est la capitale de l’Italie., Mon second est une voyelle., Mon troisième est un fleuve d’Europe., Mon tout est une plante qui sent bon.":
        ["romarin", "le romarin", "romearhin"],
    "Quel nom porte l’habitat du castor ?":
        ["une hutte", "hutte"],
    "Quel est le 6e Président de la Ve République française ?":
        ["nicolas sarcozi", "sarcozi", "nicolas"],
    "Quelle est, à ce jour, la plus grande catastrophe nucléaire de l'histoire de l’humanité ?":
        ["tchernobyl"],
    "Quelle est la capitale de la Suisse ?":
        ["berne"],
    "Quel chanteur ou chanteuse est l’interprète de Shape Of You, sorti en 2017 ? ":
        ["ed sheeran", "edsheeran", "ed", "sheeran"],
    "À quel peintre attribue-t-on l’Origine du Monde ?":
        ["gustave courbet", "courbet", "gustave"],
    "Quel animal tue le plus d'hommes chaque année ? ":
        ["le moustique", "moustique"],
    "Quel est le langage informatique le plus utilisé au monde en 2022 ?":
        ["java", "le java"],
    "Complétez l'expression :Mettre du beurre dans les...":
        ["epindards", "épinards"],
    "Comment appelle-t-on l'explosion qui serait à l'origine de l'expansion de l'Univers ?":
        ["le big bang", "big bang"],
    "Comment s'appelle l'ami lapin de Bambi ?":
        ["pan pan"],
    "Que signifie en français le mot Guten Tag":
        ["bonjour"],
    "Dans quelle articulation du corps humain se situe la rotule ?":
        ["le genou", "genou"],
}

question = [str(x) for x in quizz_data.keys()]

reponse = [quizz_data[x] for x in question]
