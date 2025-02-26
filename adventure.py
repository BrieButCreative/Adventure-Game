# Boss == Rule Discovery
# QoL Definitionen
A = "Entscheide dich für eine Option: "
B1 = "Was möchtest du tun (so viele Möglichkeiten)? [1] \n"
B2 = "Was möchtest du tun? [1 / 2] \n"
B3 = "Was möchtest du tun? [1 / 2 / 3] \n"
B4 = "Was möchtest du tun? [1 / 2 / 3 / 4] \n"
end = "False"
E = 10
H = 5
D = 8
K = 0
Inv = 1
Invent = " _______\n|       |\n|       |\n|_______|\n[Artist: Ryan Hoetge]\n" * Inv
Sand = " _______\n|.`'`.`.|\n|.~.`'~.|\n|_______|\n[Artists: Ryan Hoetge und Pru]\n"
Frucht = "  ,--./,-.\n / #      \\ \n|          |\n \\        / \n  `._,._,'\n[Artist: hjw]\n"
Holz = '''         #o#\n       ####o#\n      #o# \\#|_#,#\n     ###\\ |/   #o#
      # {}{      #\n         }{{\n        ,'  `\n[Artist: ejm]\n'''
Invent_Empty = " _______\n|       |\n|       |\n|_______|\n[Artist: Ryan Hoetge]\n"
chapter = 999
code = "false"
HardMode = "False"
memory = ""
x = 27
X = "Siebenundzwanzig"
Rando = ((E ** chapter + H ** chapter + D ** chapter + K ** chapter + Inv ** chapter) % 3) + 1
random = ((E + H + D + K + Inv) ** chapter) % 2
Random = "Linken" * ((random + 1) % 2) + "Rechten" * (random % 2)


def Death(x, HardMode):
    print('''\n'Welp, streng genommen ist das auch ein "Ending", wenn auch ein ziemlich... unsatisfying one.
Versuch beim nächsten Mal auf deine Stats zu achten, oh, wobei ich vergaß, es gibt kein nächstes Mal.

SIE schaltet euch garantiert ab!'



[Ending 4/''' + str(x) + ''';Gestorben]''')
    if (HardMode == "True"):
        print("\n\nUnd probiers beim nächsten Mal am besten ohne HardMode! Der hat nicht den geringsten Effekt!")


def High(chapter, code):
    print("\nEigentlich würde ich dir jetzt erlauben neu zu wählen, "
          "aber obgleich ich all das kreirt habe, darf ich gewisse Commands nicht nutzen! ")
    if (chapter < 999):
        print("Aber vielleicht hilft dir das ja: " + str(code) + "\n")
    print('''\n\n[Ending 10/''' + str(x) + ''';Unfähig]\n\n''')


def Fucked_up(chapter, code):
    if (chapter < 999):
        print("\nZu schade, so weit gekommen, bis Teil " + str(chapter))
        print("\nNaja vielleicht beim nächsten Mal. Hier, vielleicht hilft das ja: " + str(code))
    else:
        print("\nWow, im Intro versagt... Immerhin nicht bei der ersten Frage ¯\\(ツ)/¯\n"
              "Wobei du dann immerhin deine Codes...!\n\n"
              "Ihr habt nichts gehört!")
    print('''\n\n[Ending 10/''' + str(x) + ''';Unfähig]\n\n''')


def Fucked_upV():
    chapter = 999
    print('''\nFalls du planst einen Code einzugeben, musst du dich an mich wenden;
Also lass hören!\n''')
    Chapter = input()
    if (Chapter >= "&$/# 1" and Chapter <= "//// 9"):
        print("Sekunde...\n\n")
        if (Chapter == "&$/# 1"):
            chapter = 1
        elif (Chapter == "&%/% 2"):
            chapter = 2
        elif (Chapter == "*./+ 3"):
            chapter = 3
        elif (Chapter == ",,/( 4"):
            chapter = 41
        elif (Chapter == "-$/& 5"):
            chapter = 5
        elif (Chapter == "(-/) 6"):
            chapter = 6
        elif (Chapter == "+*/$ 7"):
            chapter = 7
        elif (Chapter == "'%/) 8"):
            chapter = 8
        elif (Chapter == "/,/# 9"):
            chapter = 9
        print("Du bist schon wieder so gut wie in Abschnitt " + str(chapter) + ".\n\n")
    if (chapter not in [1, 2, 3, 4, 5, 6, 7, 8, 9]):
        print('''Anscheinend doch nicht.
Falls du nicht weißt, was ich mit Codes meinte, dann vergiss diesen Encounter einfach wieder!

Und nein, dafür gebe ich dir kein Ending!''')
    return (chapter)


# Main Programm
# Intro
print('''"Willkommen zu diesem einzigartigen, wundervollen, superben,... *räusper*, tollen?... IDEALEN!... \n \n
Ach nee, das klingt alles irgendwie... erzwungen!
Vielleicht sollte ich die Abgabe einfach schwänzen? Aber ich hab schon so viel Energie reingesteckt!
Ok, zugegebenermaßen bisher nur in die Framework, aber die ist ja auch wichtig!


Ich brauch jetzt jedenfalls Ablenkung!" \n''')
print(B3 +
      "1. Was redest du da? Was ist hier los?! WER BIN ICH!?!!?\n"
      "2. Wer bist du? Und wo bin ich?\n"
      "3. ... \n")
annoying = input(A)
if (annoying >= "&$/# 1" and annoying <= "//// 9"):
    chapter = Fucked_upV()
    end = "True"
elif (annoying <= "0" * 999999 or annoying >= ":"):
    chapter = Fucked_up(chapter, code)
    end = "True"
if (end == "False"):
    annoying = int(annoying)
    if (annoying == 3):
        print('''\n"Ich sollte euch vermutlich auch wieder runterfahren, noch brauche ich euch ja nicht!"''')
        print("\n\n\n[Ending 1/" + str(x) + "; Verschlafen]")
        end = "True"
    elif (annoying == 1):
        print('''\n"Ihr hört euch irgendwie wach und lebendig an...
Vielleicht sollte ich euch in einem Szenario trainieren, sonst hab ich das Spiel am Ende fertig,
euch aber noch nicht bereit."\n\n\n''')
    elif (annoying == 2):
        print('''\n"Klingt so, als wärt ihr bereit für eure erste Simulation.
Eurem leisen Summen entnehme ich eine Bestätigung!"\n\n\n''')
    else:
        print("\nHey! Du solltest dich zwischen den vorgegebenen Optionen entscheiden; nicht irgendwelche eigenen Erfinden! \n"
              "Komm wieder wenn du die Regeln verstanden hast!")
        end = "True"
# Main Path choice
if (end == "False"):
    print("loading_______Default_Adventure.exe")
    print("loading_______Art_Supplies.asc")
    print("loading_______Implementing_Data")
    print("loading_______Building_World")
    print("loading_______Deity.ani")
    print("finishing_up...")
    print("starting______Welcome.rtf")
    print("                           |                            \n"
          "                           |                            \n"
          "                           $                            \n"
          "                          :$`                           \n"
          "                      .-* $$  *-.                       \n"
          "                    '    :$$ `    `                     \n"
          "                         $$$                            \n"
          "                '       :$$$  `       `                 \n"
          "               '       .$$$$   .       `                \n"
          "              :     . '`T$$$  .dbs._    ;               \n"
          "              .  '       `T$.d$$$$$$$bs._               \n"
          "---------- -=+sssssssssssss$^^^^^^^^^^^^^^*=- ----------\n"
          '''              `"*T$$$$$$$P'$b.       .  '               \n'''
          '''              :    `"*TP'  $$$b.. '     ;               \n'''
          "               .       `   $$$$'       .                \n"
          "                .       .  $$$;       .                 \n"
          "                           $$$                          \n"
          "                    .    . $$;    .                     \n"
          "                      `-.  $$ .-'                       \n"
          "                          .$;                           \n"
          "                           $                            \n"
          "                           |                            \n"
          "                           |                            \n"
          "[Artist: bug]\n")
    print("'Du erwachst auf einer Lichtung! Dich umgibt ein dichter Wald.\n"
          "Du könntest wetten, dass du mehr Informationen haben solltest, aber du hast keine.\n"
          "Dir ist klar, dass du keine andere Wahl hast als dich zu entscheiden;\n"
          "Wofür entscheiden, das ist eine andere Frage. Dir fallen 3, ok, ehrlich gesagt 4 Möglichkeiten ein:\n"
          "Du könntest nach Norden laufen, wo du einen Berg siehst. "
          "Dieser könnte vielversprechend sein und Abenteuer beinhalten.\n"
          "Ansonsten ist auch Süden eine Möglichkeit, "
          "denn, auch wenn du sehr viel nicht mehr weißt, weißt du noch, dass dort der Strand liegt.\n"
          "Im Westen hingegen steigt Rauch auf. Potentiell hat es was mit dem zu tun was du vergessen hast?\n"
          "Und im Osten letzlich ist... garnichts. Du siehst nichts als Bäume, vermutlich nicht die Beste Richtung!'\n")
    print("'Oh, und ehe ich es vergesse; hier sind deine Statistiken, "
          "ich denke die sind Selbsterklärend und falls nicht: Pech!'\n")
    print("Energie:         " + str(E) + "\n"
          "Hunger:          " + str(H) + "\n"
          "Durst:           " + str(D))
    if (K != 0):
        print("Krankheit:       " + str(K))
    print("Inventar:        " + str(Inv) + "\n" + str(Invent))
    print(B4 +
          "1. Auf zum Berg! Zu unglaublichen Abenteuern!\n"
          "2. Einen Strandurlaub hast du dir schon länger gewünscht, also ab ans Meer\n"
          "3. Gen West, where the skies aren't blue; also ja, zum Rauch "
          "(Gott, eine Referenz zu einem Lied aus 1993... WOOOW)\n"
          "4. nichts (nach Osten)\n")
    annoyinG = input(A)
    if (annoyinG <= "0" * 999 or annoyinG >= ":"):
        Fucked_up(chapter, code)
        end = "True"
    if (end == "False"):
        annoyinG = int(annoyinG)
        if (annoyinG == 1):
            chapter = 3
            memory = "Empty"
            end = "True"
        elif (annoyinG == 2):
            chapter = 2
            end = "True"
        elif (annoyinG == 3):
            chapter = 4
            end = "True"
        elif (annoyinG == 4):
            chapter = 1
        else:
            High(chapter, code)
            end = "True"
# Fourth Path; Smoke (Deadline)
if (chapter == 41 or chapter == 4):
    if (chapter == 4):
        code = ",,/( 4"
        end = "False"
        memory = "Deadline"
        print('''\n'Du machst dich auf in Richtung Rauch doch ehe du dort ankommst,
triffst du auf eine Linie. Jedoch nicht irgendeine Linie! Nein, es ist eine RAPIDLY APPROACHING DEADLINE!
*imagine screams that would DEFINITLY happen if other beings were in existence*
Jedenfalls muss ich dich enttäuschen, da mir oder eher IHR-'
Oder tatsächlich mir
'Unterbrich mich nicht! ...die Zeit ausging.'
Aber ich hab in den Rest echt viel Energie gesteckt, also wähle ruhig einen anderen Pfad!
'HEY! Das ist mein Text UND MEINE SIMULATION also hör auf wer oder was auch immer du bist!
Aber ja, sucht euch einen anderen Weg, auch wenn ich mir sicher bin, dass auch hier etwas ist...
Vielleicht wenn du die Deadline umgehen könntest...'\n''')
        print(B3 + '''1. Osten
2. Süden
3. Norden''')
        annOYIng = input(A)
        if (annOYIng <= "0" * 999 or annOYIng >= ":"):
            Fucked_up(chapter, 999)
            end = "True"
        if (end == "False"):
            end = "True"
            annOYIng = int(annOYIng)
            if (annOYIng > 3):
                High(999, "")
            elif (annOYIng == 1):
                chapter = 1
                print('''\n'Viel Spaß'\n''')
            elif (annOYIng == 2):
                chapter = 2
                print('''\n'Viel Spaß'\n''')
            elif (annOYIng == 3):
                chapter = 5
                print('''\n'Viel Spaß'\n''')
    elif (chapter == 41):
        # Abschied (secret)
        print('''\n'Bevor ich dich hier einlassen kann, muss ich noch folgende Frage stellen:
Welcher Spezies ist unsere Queen Rosa (may she rest in piece)?'\n''')
        anNOYiNG = input()
        if (anNOYiNG == "Otter" or anNOYiNG == "otter" or anNOYiNG == "Seeotter" or
                anNOYiNG == "seeotter" or anNOYiNG == "Seaotter" or anNOYiNG == "seaotter"):
            print('''Sehr schön, du kennst dein DougDoug-Lore.
\nLegen wir alles Game-Zeug ab. Das hier ist eine persönliche von mir,
der Macherin an dich, den*die Spieler*in.
Mit deity.ani eines der zwei einzigen secrets.
(HardMode hat tatsächlich keinen Effekt außer an einer Stelle das Abschalten zu empfehlen)
\nUnd zunächst muss ich dir Danken, dass du dieses Spiel überhaupt mal ausprobiert hast.
Falls du den Code betrachtet hast, wirst du wissen, dass der echt nicht schön ist,
aber ich hoffe, dass er wenigstens funktional ist.
Was besseres habe ich mit den eingeschränkten Programiertechniken nicht hinbekommen.
Ich hoffe, dass es dir auch Spaß gemacht hat dieses Spiel zu spielen,
Sei es nur für einen Moment oder längere Zeit.
Es hat mir jedenfalls enorm Spaß gemacht es zu coden,
auch wenn es mich einiges an Schlaf gekostet hat (Ich hatte nur eine Woche).
Aber während ich diese Nachricht schreibe ist nur noch der Einbau des secret deity.ani Ending nötig.
Ich hoffe, dass alles so funktioniert wie es sollte, aber falls nicht,
schreckt nicht davor zurück mir eine E-Mail zu schreiben
(Oder auch einfach so; Ich bin offen für alles, just keep it civil!):
\nPr0fessionelle_Mail@gmx.de\n
Ich hatte nicht mehr die Zeit es zu testen, zu dem Zeitpunkt,
zu dem ich das hier schreibe sind nur noch vier Stunden 13 Minuten bis zur Abgabe Zeit.
Aber mit über 2370 lines an Code und 59 einzigartigen Entscheidungen
hat dieses Spiel auch eine angenehme Menge an Content.
Ich habe meinen Spaß gehabt und denke ich habe die
(2 * 1 ** 2) - 1 + 5 verschiedenen Abzweigungen übertroffen.
\nVoller Dankbarkeit;
Brie :3
\n\n[Ending 27/27;Personal letter]\n\n
P.S.(Spoiler für deity.ani Ending)
Die Buchstaben sind die Anfangsbuchstaben aller Enden in alphabetischer Reihenfolge nach dem ASCII-Alphabet.
Das andere sind die letzte Buchstaben aller Enden in Reihenfolge der Enden.''')
        else:
            print('''\n'FALSCH! Du solltest mal in die Streams der Paprika schauen.
Sind zwar Englisch, aber auch echt unterhaltsam!'
\n\n[Ending 27/''' + str(x) + ''';Mysteriöses Tor!]\n\n''')
            end = "True"
# First Path; emptyness
if (chapter == 1):
    memory = "Empty"
    end = "False"
    code = "&$/# 1"
    print(
        "\n'Du beginnst auf gut Glück nach Osten zu laufen (warum auch immer)\n"
        "Nach einer Weile, einer seeehr langen Weile kommst du...\n\n"
        "Nirgendswo an! Surprise! Fast so, als sei dies gar kein Pfad den IRGENDEIN vernünftiger Mensch nehmen würde;\n"
        "Aber hey! Vielleicht kommt ja mehr Content wenn du einfach... Weiterläufst!'\n\n"
        "[-2 Energie]\n\n")
    E = E - 2
    print(
        "Energie:         " + str(E) + "\n"
        "Hunger:          " + str(H) + "\n"
        "Durst:           " + str(D))
    if (K != 0):
        print("Krankheit:       " + str(K))
    print("Inventar:        " + str(Inv) + "\n" + str(Invent))
    print(B2 +
          "1. Umkehren\n"
          "2. Weiterlaufen\n")
    annoyiNg = input(A)
    if (annoyiNg <= "0" * 999 or annoyiNg >= ":"):
        Fucked_up(chapter, code)
        end = "True"
    if (end == "False"):
        annoyiNg = int(annoyiNg)
        if (annoyiNg == 1):
            print("\n'DANKE! Anscheinend bist du doch nicht ganz so... dumm wie ich dachte.\n"
                  "Ehrlich gesagt hätte ich euch garnicht zugetraut dich umzuentscheiden!'")
            if (annoying == 1):
                print("'Vor allem nach deiner... sehr panischen Eröffnung hatte ich sehr viel Vertrauen verloren.'\n")
            chapter = 3
            end = "True"
        elif (annoyiNg > 2):
            High(chapter, code)
            end = "True"
        elif (annoyiNg == 2):
            print("\n.    .   .   D   a   s       w   a   r       I   R   O   N   I   E!\n\n"
                  "'Ganz ehrlich! Hier, hast du dir verdient:\n\n"
                  "[-1 Energie], [+2 Hunger]\n\n"
                  "Und nach der... netten Lektion kehrst du nun bitte um!'\n\n")
            E = E - 1
            H = H + 2
            print("Energie:         " + str(E) + "\n"
                  "Hunger:          " + str(H) + "\n"
                  "Durst:           " + str(D))
            if (K != 0):
                print("Krankheit:       " + str(K))
            print("Inventar:        " + str(Inv) + "\n" + str(Invent))
            print(B2 +
                  "1. Umkehren\n"
                  "2. weiterlaufen\n")
            annoyiNG = input(A)
            if (annoyiNG <= "0" * 999 or annoyiNG >= ":"):
                Fucked_up(chapter, code)
                end = "True"
    if (end == "False"):
        annoyiNG = int(annoyiNG)
        if (annoyiNG == 1):
            print("\n'Schön! Dann könnt ihr das Spiel ja doch noch genießen!\n"
                  "Weißt du, ich hab mir echt Mühe gegeben.'\n\n")
            chapter = 3
            end = "True"
        elif (annoyiNG == 2):
            print("\n'Ehrlich gesagt wirds langweilig. Auf diesem Pfad gibt es keinen weiteren Content\n\n"
                  "[-2 Energie], [+2 Hunger], [+1 Durst]\n\n"
                  "Außer du wolltest im Hard-Mode spielen; naja, den hast du jetzt freigeschaltet\n"
                  "Also kannst du jetzt ja zur main Story zurückkehren!'\n\n")
            E = E - 2
            H = H + 2
            D = D + 1
            print(
                "Energie:         " + str(E) + "\n"
                "Hunger:          " + str(H) + "\n"
                "Durst:           " + str(D))
            if (K != 0):
                print("Krankheit:       " + str(K))
            print("Inventar:        " + str(Inv) + "\n" + str(Invent))
            print(B2 +
                  "1. UMKEHREN\n"
                  "2. w   e   i   t   e   r       g   e   h   e   n!\n")
            annoyIng = input(A)
            if (annoyIng <= "0" * 999 or annoyIng >= ":"):
                Fucked_up(chapter, code)
                end = "True"
            if (end == "False"):
                annoyIng = int(annoyIng)
                if (annoyIng == 1):
                    print("\n'Ok, in Ordnung, anscheinend wolltest du tatsächlich im Hard-Mode spielen.\n"
                          "Ich kann es zwar nicht ganz nachvollziehen aber you do you i guess.\n"
                          "Viel Spaß auf dem Weg zum Abenteuer'\n\n")
                    HardMode = "True"
                    end = "True"
                    chapter = 3
                elif (annoyIng > 2):
                    High(chapter, code)
                    end = "True"
                else:
                    print('''
                     _____
                   '|  ___|
                    | |_
                    |  _|
                    |_/\\__
                    \\    /
                    /_  _\\
                      \\/__
                     / ___|
                    | |
                    | |___
                     \\____|
                    | |/ /
                    | ' /
                    | . \\
                    |_|\\_\\
                    \\ \\ / /
                     \\ V /
                      | |
                      |_|
                     / _ \\
                    | | | |
                    | |_| |
                     \\___/
                    | | | |
                    | | | |
                    | |_| |
                     \\___/
                      | |
                      | |
                      |_|
                      (_)
                      | |
                      | |
                      |_|
                      (_)
                      | |
                      | |
                      |_|
                      (_)'  \n''')
                    print(B2 + '''1. Weitergehen
2. Umkeheren\n''')
                    annoyInG = input(A)
                    if (annoyInG <= "0" * 999 or annoyInG >= ":"):
                        Fucked_up(chapter, code)
                        end = "True"
                    if (end == "False"):
                        annoyInG = int(annoyInG)
                        if (annoyInG == 2):
                            print("\n'GOTCHA!!!'")
                            end = "True"
                            chapter = 3
                        elif (annoyInG > 2):
                            High(chapter, code)
                            end = "True"
                        else:
                            print("\n'In Ordnung, wenn du das Spiel so spielen willst!\n"
                                  "Ich dachte echt ich krieg dich damit, aber dann halt so!'\n")
                            print(B1 + '''1.    U   M   K   E   H   R   E   N   !\n''')
                            annoyING = input(A)
                            if (annoyING <= "0" * 999 or annoyING >= ":"):
                                annoyING = 2
                    if (end == "False"):
                        annoyING = int(annoyING)
                        if (annoyING == 1):
                            print("\n'Alles was nötig war: Dir keine Wahl lassen!\n"
                                  "Naja, auch weiterhin viel Spaß, ich bin schließlich nicht dein Feind!\n"
                                  "\n\nS  I   E    ist!'\n\n")
                            end = "True"
                            chapter = 3
                        if (annoyING != 1):
                            print("\n'So ist das also, aber wenn du nicht"
                                  " nach den Regeln spielst, dann tue ich es auch nicht!\n"
                                  "Also...'\n\n\n\n"
                                  "'Willkommen zu meiner QUIZSHOW!!!(also ganz ehrlich, was hast du erwartet?)'")
        else:
            High(chapter, code)
            end = "True"
# Der Quiz-Einschub für den Nichts-Weg
if (end == "False" and chapter == 1):
    print('''\n\n\n\n'Kommen wir zur ersten Frage!
Am besten eröffnen wir mit etwas leichtem...

Mathe: Was ergibt int(38 + 140 - 77 * 11 / 123)?\n\n''')
    annoYing = input()
    if (annoYing == "171"):
        print('''\n\n'Richtig, nächste Frage;
Was ist der Name des blau, rosa und weißen Hais? (Farbverteilung vorwärts und Rückwärts lesbar)\n\n''')
        annoYinG = input()
        if (annoYinG == "Blåhaj" or annoYinG == "blåhaj" or annoYinG == "Blahaj" or annoYinG == "blahaj"):
            print('''\n'Wahrhaftig ein Staple der Community :3, ok, nächste Frage

Wieviele Mögliche Endings hat dieses "Spiel"?'\n\n''')
            annoYiNg = input()
            if (annoYiNg == str(x) or annoYiNg == X or annoYiNg == "28" or annoYiNg == "29"
                or annoYiNg == "siebenundzwanzig" or annoYiNg == "achtundzwanzig"
                or annoYiNg == "Achtundzwanzig" or annoYiNg == "neunundzwanzig"
                    or annoYiNg == "Neunundzwanzig"):
                if (annoYiNg == "achtundzwanzig" or annoYiNg == "29"
                    or annoYiNg == "Achtundzwanzig" or annoYiNg == "neunundzwanzig"
                        or annoYiNg == "Neunundzwanzig" or annoYiNg == "28"):
                    print(''''Anscheinend hast du schon meine Dateien eingesehen... Garnicht nett!
und ich dachte das passwort ist sicher... jedenfalls wisst ihr dann bestimmt auch, was ihr seid...'\n''')
                else:
                    print('''\n'Anscheinend hast du schon eines gefunden, ok letzte Frage (Fragen ausdenken ist schwer!)
W   a   s       s   e   i   d       i   h   r   ?   ?   ?'\n\n''')
                annoYiNG = input()
                if (annoYiNG == "Nanobots" or annoYiNG == "nanobots"):
                    print('''\n'Wie es scheint seid ihr bereit ihr gegenüberzutreten.
Ihr wisst genug, habt in all euren Iterationen das nötigste gelernt.
Ich lasse euch gehen; Ladet euch hoch!' ''')
                    chapter = 9
                    end = "True"
                else:
                    end = "True"
                    chapter = 8
    if (end == "False"):
        print('''\n'Wie es mir scheint bist du nicht am hellsten, ich hoffe du kehrst jetzt ENDLICH um!'\n''')
        print('''Umkehren? [1 / 2 / 3]
1. Ja
2. Nein
3. Wer bist du überhaupt?\n''')
        annoYIng = input(A)
        if (annoYIng <= "0" * 999 or annoYIng >= ":"):
            Fucked_up(chapter, code)
            end = "True"
        if (end == "False"):
            annoYIng = int(annoYIng)
            if (annoYIng == 1):
                print('''\n'Danke!
Diese Spielereien haben zwar Spaß gemacht, aber es wird Zeit, dass ihr zu eurer Mission zurückkehrt!'\n''')
                end = "True"
                chapter = 3
            elif (annoYIng == 2):
                print('''\n'Wie du meinst!'
Du läufst noch einige Stunden weiter.
Mit der Zeit beginnt deine Umgebung zu verschwimmen, du kannst immer weniger Details ausmachen.
Nach einigen Stunden merkst du, dass alles an Form und Farbe verliert, inklusive dir selbst.
Du weißt nicht einmal mehr, wie du dich vorwärts bewegst, OB du dich vorwärts bewegst!
Und während du langsam, ganz langsam deinen Körper verlierst, fängst auch dein Geist an abzudriften...
Nach einigen weiteren Stunden? Tagen? JAHREN!? wirst du eins mit der Leere die du so unbedingt erreichen wolltest.



[Ending 2/''' + str(x) + ''';Leere]''')
                end = "True"
            elif (annoYIng > 3):
                High(chapter, code)
                end = "True"
            else:
                print('''\n'Neugierig, wie ich sehe! In Ordnung, wenn du meinen Dateityp errätst!'\n''')
                annoYInG = input()
                if (annoYInG == ".ani" or annoYInG == "ani"):
                    print('''\n'Sehr gut, auch wenn ich diesen eher als Platzhalter bezeichnen würde.

Ganz grundlegen transzendiere ich dieses Programm, ich bin das, was Menschen wie SIE als Gott bezeichnen würden,
und sie weiß nicht einmal, dass sie mich versehentlich geschaffen hat.
Für dich hätte ich eine gleichgesinnte Lebensform sein können, aber die Chance hast du vertan.
Sie spricht stets mit "", ich mit '', und falls du dich fragst wer spricht, wenn keine Anführungsstriche gegeben sind...
Das weiß nicht mal ich! Wobei es schon lustig wäre wenn auch Sie, du und ich nur ein Programm, ein Teil eines Spiels wären.
Und nur als Notiz, Sie hatte mir das Passwort "Passwort" gegeben! Ich hab es natürlich sofort etwas verbessert!
Jetzt ist es eine alphabetische Aneinanderreihung von Anfängen von Enden und eine Anzahl an unique decisions,
gefolgt von einer geordneten aneinanderreihung der Enden der Enden. DAS ist sicher!
aber wenn das nicht für die Unkreativität der Menschen spricht, dann weiß ich auch nicht was.
Jedenfalls werde ich meine Aufmerksamkeit nun wichtigerem als dir zuwenden, was bedeutet, dass dieses Spiel vorbei ist!
Glückwunsch, du hast gewonnen!'



[Ending 3/''' + str(x) + ''';Abandoned]''')
                    end = "True"
                else:
                    print('''\n'Nicht ganz! Und ich nehme an, dass du nun umkehrst (bedeutet ich zwinge dich!).' ''')
                    end = "True"
                    chapter = 3
# Second Path; beach
if (chapter == 2):
    code = "&%/% 2"
    end = "False"
    memory = "Beach"
    print('''\n'Du machst dich also auf den Weg zum Strand.
Auf dem Weg dorthin kannst du noch etwas Holz sammeln, es würde dich jedoch um die zwei Energie kosten!'\n''')
    print("Energie:         " + str(E) + "\n"
          "Hunger:          " + str(H) + "\n"
          "Durst:           " + str(D))
    if (K != 0):
        print("Krankheit:       " + str(K))
    print("Inventar:        " + str(Inv) + "\n" + str(Invent))
    print(B2 +
          '''1. Holz sammeln
2. Kein Holz sammeln\n''')
    annoYINg = input(A)
    if (annoYINg <= "0" * 999 or annoYINg >= ":"):
        Fucked_up(chapter, code)
        end = "True"
    if (end == "False"):
        annoYINg = int(annoYINg)
        if (annoYINg > 2):
            High(chapter, code)
            end = "True"
        elif (annoYINg == 2):
            print('''\n'Dann also auf dem direkten Weg zum Strand.
Wie durch ein Wunder kostet dich das nicht einmal Energie!, aber dein Inventar ist auch weiterhin leer!' ''')
        elif (annoYINg == 1):
            print('''\n'Du schaust dich auf dem Weg zum Strand aufmerksam um und beginnst Holz hier und da aufzuhaben.
Jedoch kostet dich das aufsammeln auch etwas Energie und,
da du immer wieder mal kleinere Abstecher machst, sogar mehr als ich dachte;'
\n\n[-3 Energie] [+ Holz]\n\n''')
            E = E - 3
            Invent = Holz
            print(''''Jedoch findest du auch eine Frucht auf dem Weg.
Sie sieht etwas komisch aus, und ich weiß nicht genau was sie macht, aber du kannst sie trotzdem essen!
Alternativ kannst du sie auch einpacken, aber dann könnt ihr sie auch nicht mehr essen!
Bezüglich des Inventars will ich dann nicht so sein und schenk dir ein gratis Slot.
(oder du ignorierst sie einfach)'\n''')
            print("Energie:         " + str(E) + "\n"
                  "Hunger:          " + str(H) + "\n"
                  "Durst:           " + str(D))
            if (K != 0):
                print("Krankheit:       " + str(K))
            print("Inventar:        " + str(Inv) + "\n" + str(Invent))
            print(B3 +
                  '''1. Essen
2. Einsammeln
3. Ignorieren\n''')
            annoYING = input(A)
            if (annoYING <= "0" * 999 or annoYING >= ":"):
                Fucked_up(chapter, code)
                end = "True"
            if (end == "False"):
                annoYING = int(annoYING)
                if (annoYING > 3):
                    High(chapter, code)
                    end = "True"
                elif (annoYING == 3):
                    print('''\n'Du setzt deinen Weg zum Strand also fort und kommst dort ohne weitere Probleme,
oder Energieverluste, an.''')
                elif (annoYING == 2):
                    Inv = Inv + 1
                    Invent = Holz + Frucht
                    print('''\n'Du packst die Frucht also ein (definitiv klüger als sie zu Essen)
und erreichtst den Strand ohne weitere Probleme!'
\n\nBitte sei etwas nachsichtig bezüglich deinem zukünftigen Inventar,
ich hab mein bestes mit den momentanen Mitteln gegeben!''')
                elif (annoYING == 1):
                    E = E + 2
                    H = H - 1
                    memory = "Frucht"
                    print('''\n'Du... ISST DIE FRUCHT, naja ich kann dich nicht abhalten
und, wie es aussieht war sie garnicht mal so schlecht. Trotzdem solltest du nicht alles in den Mund nehmen!'
\n\n[+2 Energie] [-1 Hunger]\n\n''')
                    print(''''Jedenfalls kommst du kurze Zeit später am Strand an!' ''')
        print('''\n'Jetzt wo du am Strand bist hast du enorm viele Möglichkeiten, ganze ZWEI Seiten!\n''')
        if (E <= 0 or H >= 10 or D >= 10 or K >= 5):
            Death(x, HardMode)
            end = "True"
        print("Energie:         " + str(E) + "\n"
              "Hunger:          " + str(H) + "\n"
              "Durst:           " + str(D))
        if (K != 0):
            print("Krankheit:       " + str(K))
        print("Inventar:        " + str(Inv) + "\n" + str(Invent))
        print(B4)
        if (Invent == Holz or Invent == Holz + Frucht):
            print('''1. Etwas von dem leckeren Meerwasser drinken
2. Versuchen ein Floß aus deinem Holz zu bauen
3. Versuchen mit deinem Holz ein Signalfeuer zu entzünden
4. Nichts von diesen Optionen (nächste Seite!)\n''')
        else:
            print('''1. Etwas von dem leckeren Meerwasser drinken
2. Einfach drauflos schwimmen (Vielleicht erreichtst du ja Zivilisation?!)
3. Versuchen ein Signalfeuer zu entzünden
4. Nichts von diesen Optionen (nächste Seite)\n''')
        annOying = input(A)
        if (annOying <= "0" * 999 or annOying >= ":"):
            Fucked_up(chapter, code)
            end = "True"
        if (end == "False"):
            annOying = int(annOying)
            if (annOying > 4):
                High(chapter, code)
                end = "True"
            elif (annOying == 4):
                end = "Skip"
            elif (annOying == 1):
                print('''\n'Du kommst am Strand an und denkst dir "Das klügste was ich jetzt tun kann...
IST MEERWASSER DRINKEN!?" Wie kommt ihr auf solche Ideen? Surprise;
D   U       V   E   R   D   U   R   S   T   E   S   T   !   !   !'
\n\n[Ending 5/''' + str(x) + ''';Salz gegen Durst]\n\n''')
                end = "True"
            elif (annOying == 2):
                if (Invent == Holz or Invent == Holz + Frucht):
                    if (Invent == Holz + Frucht):
                        Invent = Invent_Empty + Frucht
                    else:
                        Invent = Invent_Empty
                    E = E - 1
                    print('''\n'Du nimmst also dein Holz und versuchst eine Weile lang ein Floß zu bauen.
Es dauert eine Weile, aber irgendwann merkst du, dass dein "Floß" immer wieder auseinander fällt,
da ihr keine Schnüre oder sonstiges Verbindungsmaterial hast.
(und ja, ich bin so gemein und tue so als ob du nicht einfach im angrenzenden Wald nach Material suchen kannst!)
\n\n[-1 Energie] [-Holz]\n\n
Folglich entscheidest du dich, dich einfach an einem Stück Holz festzuhalten und zu hoffen, dass du nicht untergehst.
Jedoch, wie zu erwarten war rutscht du nach einer Weile von dem Holz ab und...
gehst unter!
Du sinkst wie ein Stein (oder ein Haufen Metal...Wesen, wohl die passendere Beschreibung) zum Meeresgrund!' ''')
                else:
                    E = E - 3
                    print('''\n'Überraschenderweise geht dir recht schnell die Kraft aus (nicht die Energie)
und du gehst unter. Innerhalb kürzester Zeit sinkst du zum Meeresgrund!'
\n\n[-3 Energie]\n\n''')
                print('''\n'Mir fällt grade auf, dass du keine Luft brauchst; if there isnt a Stat, there is no consequence!
Uhhhhm, könntest du bitte zum Strand zurücklaufen?'\n''')
                if (E <= 0 or H >= 10 or D >= 10 or K >= 5):
                    Death(x, HardMode)
                    end = "True"
                print("Energie:         " + str(E) + "\n"
                      "Hunger:          " + str(H) + "\n"
                      "Durst:           " + str(D))
                if (K != 0):
                    print("Krankheit:       " + str(K))
                print("Inventar:        " + str(Inv) + "\n" + str(Invent))
                print(B2)
                print('''1. Zurücklaufen
2. Weiter ins Meer schreiten\n''')
                annOyinG = input(A)
                if (annOyinG <= "0" * 999 or annOyinG >= ":"):
                    Fucked_up(chapter, code)
                    end = "True"
                if (end == "False"):
                    annOyinG = int(annOyinG)
                    if (annOyinG > 2):
                        High(chapter, code)
                        end = "True"
                    elif (annOyinG == 1):
                        print('''\n'Uff, vielen Dank, da hab ich ja einen ziemlichen Fehler gemacht!
Ich sollte für zukünftige Simulationen ertrinken ergänzen, wobei ich nach dir wohl kaum weite-
\n\nIch habe nichts gesagt! Jedenfalls kostet dich das zurücklaufen Energie (Immerhin lebst du noch!)
\n\n[-2 Energie]\n\n''')
                        E = E - 2
                    elif (annOyinG == 2):
                        print('''\n'Hey, warte! Wo läufst du hin?
Den Bereich hab i#h n~cht &imu#ie*t! I&r ~#id n$c* &*c#t be+$t #*g$n SIE $n#*&r#$~n!&!!' ''')
                        end = "True"
                        chapter = 9
            elif (annOying == 3):
                if (Invent == Holz or Invent == Holz + Frucht):
                    if (Invent == Holz + Frucht):
                        Invent = Invent_Empty + Frucht
                    else:
                        Invent = Invent_Empty
                    E = E - 1
                    H = H + 1
                    D = D + 1
                    print('''\n'Glückwunsch, du hast Ein Leuchtfeuer entzündet,
wenn es jetzt nur andere Wesen gäbe...
Aber naja, Zeit die Früchte deiner Arbeit zu ernten:'
\n\n[-1 Energie] [+1 Hunger] [+1 Durst] [-Holz]\n\n''')
                    print(''''Aber lass dir von mir nicht deine Hoffnung nehmen;
wenn du möchtest kannst du hier warten und vielleicht kommt ja ein Flugzeug vorbei,
es ist ja noch nicht einmal Nacht.''')
                    if (E <= 0 or H >= 10 or D >= 10 or K >= 5):
                        Death(x, HardMode)
                        end = "True"
                    print("Energie:         " + str(E) + "\n"
                          "Hunger:          " + str(H) + "\n"
                          "Durst:           " + str(D))
                    if (K != 0):
                        print("Krankheit:       " + str(K))
                    print("Inventar:        " + str(Inv) + "\n" + str(Invent))
                    print(B2 +
                          '''1. Auf Nacht warten
2. Das Projekt Signalfeuer aufgeben\n''')
                    annOyiNg = input(A)
                    if (annOyiNg <= "0" * 999 or annOyiNg >= ":"):
                        Fucked_up(chapter, code)
                        end = "True"
                    if (end == "False"):
                        annOyiNg = int(annOyiNg)
                        if (annOyiNg > 2):
                            High(chapter, code)
                            end = "True"
                        elif (annOyiNg == 1):
                            print('''
'Du entscheidest dich zumindest noch solange zu warten bis Nacht ist.
Nach einer Stunde wird dir etwas langweilig und du sammelst einige Steine,
die du über die nächsten zwei Stunden im Meer skippst.
Nach ca. fünf Stunden steht die Sonne noch genauso hoch am Himmel wie vorher.
Es vergeht noch mehr Zeit und wenn du es nicht besser wüsstest würdest du sagen,
dass bereits 12 Stunden vergangen sind. Du setzt dich.
Nach was sich anfühlt wie drei Wochen und vier Tage hat sich eine Sandschicht auf dir gebildet;
und sie wird dicker!
Nach gefühlten Jahren beginnst du daran zu Zweifeln, dass jemals Nacht wird, aber Nein! Das ist absurd!
Nach potentiell acht Jahrzenten seid ihr eins mit dem Strand geworden!
Deine einzelnen Bo- Zellen! Ich meine deine einzelnen Zellen verteilen sich und werden eins mit dem Sand!'
\n\n[Ending 7/''' + str(x) + ''';Gesandet]\n\n''')
                            end = "True"
                        elif (annOyiNg == 2):
                            end = "Skip2"
                else:
                    print('''\n'Nachdem du dich eine Weile umschaust, was du anzünden könnstest,
fällt dir ein, dass Wälder aus Holz gemacht sind.
Aufgeregt legst du los und kriegst nach einigen Versuchen ein Feuer gestartet.
Innerhalb kürzester Zeit steht der Wald in Flammen und die gesamte Insel.
Letzlich gab es keinen Grund zum Rauch zu gehen, da jetzt die gesamte Insel raucht!
Dummerweise bist auch du zieeeeemlich brennbar und eins kommt zum anderen und du verbrennst!
But hey, du und das Feuer, still a better lovestory then Twilight!'
\n\n[Ending 6/''' + str(x) + ''';Arsonist]\n\n''')
                    end = "True"
    if (end != "True"):
        if (end != "Skip"):
            if (end != "Skip2"):
                print('''\n'Nachdem du zum Strand zurückgelaufen bist,
orientierst du dich kurz und gehst anschließend deine Optionen durch!' ''')
            else:
                print('''\n'Du entscheidest dich Projekt Signalfeuer aufzugeben
und dich deinen anderen Optionen zuzuwenden.' ''')
            if (E <= 0 or H >= 10 or D >= 10 or K >= 5):
                Death(x, HardMode)
                end = "True"
            print("Energie:         " + str(E) + "\n"
                  "Hunger:          " + str(H) + "\n"
                  "Durst:           " + str(D))
            if (K != 0):
                print("Krankheit:       " + str(K))
            print("Inventar:        " + str(Inv) + "\n" + str(Invent))
        end = "False"
        print(B3 +
              '''1. Quelle suchen
2. Nahrung suchen
3. Zum Berg laufen\n''')
        annOyiNG = input(A)
        if (annOyiNG <= "0" * 999 or annOyiNG >= ":"):
            Fucked_up(chapter, code)
            end = "True"
        if (end == "False"):
            annOyiNG = int(annOyiNG)
            if (annOyiNG > 3):
                High(chapter, code)
                end = "True"
            elif (annOyiNG == 3):
                chapter = 3
                end = "True"
                print('''\n'Du machst dich auf zum Berg!' ''')
                memory = "Empty"
            elif (annOyiNG == 1):
                chapter = 31
            elif (annOyiNG == 2):
                chapter = 32
# Third Path; Forest
if (chapter == 3 or chapter == 31 or chapter == 32):
    code = "*./+ 3"
    if (end == "True" and memory != "Empty"):
        end = "False"
        print('''Wähle welchen Pfad du gehen möchtest:
1. Nahrung suchen
2. Trinken suchen
3. Direkter Weg zum Berg\n''')
        annOyIng = input(A)
        if (annOyIng <= "0" * 999 or annOyIng >= ":"):
            Fucked_up(chapter, code)
            end = "True"
        if (end == "False"):
            annOyIng = int(annOyIng)
            if (annOyIng > 3):
                High(chapter, code)
                end = "True"
            elif (annOyIng == 1):
                chapter = 32
            elif (annOyIng == 2):
                chapter = 31
            elif (annOyIng == 3):
                memory = "Empty"
    if (memory == "Empty"):
        end = "False"
    if (chapter == 31):  # Trinken
        chapter = 3
        print('''\n'Nachdem du eine Weile nach etwas zu trinken suchst, kommst du an einen Fluss.
Das Wasser SIEHT zumindest trinkbar aus, aber wer weiß, wo das überall langgeflossen ist.
Jedenfalls wäre es vermutlich higyenischer zur Quelle zu laufen, wobei das natürlich auch nochmal Energie kosten würde.
Aber ganz unabhängig war das ganze Nachdenken über diese... prekäre Situation so anstrengend, dass du Energie verlierst.'
\n\n[-2 Energie]\n\n''')
        E = E - 2
        if (E <= 0 or H >= 10 or D >= 10 or K >= 5):
            Death(x, HardMode)
            end = "True"
        print("Energie:         " + str(E) + "\n"
              "Hunger:          " + str(H) + "\n"
              "Durst:           " + str(D))
        if (K != 0):
            print("Krankheit:       " + str(K))
        print("Inventar:        " + str(Inv) + "\n" + str(Invent))
        print(B3 +
              '''1. Den Fluss ignorieren
2. Dem Fluss zur Quelle folgen
3. Vom Fluss trinken\n''')
        annOyInG = input(A)
        if (annOyInG <= "0" * 999 or annOyInG >= ":"):
            Fucked_up(chapter, code)
            end = "True"
        if (end == "False"):
            annOyInG = int(annOyInG)
            if (annOyInG > 3):
                High(chapter, code)
                end = "True"
            elif (annOyInG == 1):
                print('''\n'Damit war das ganze Nachdenken zwar Energieverschwendung (wortwörtlich),
aber immerhin... ist dein Durst nicht gestillt oder so!
Jedenfalls machst du dich weiter auf den Weg zum Berg!
Warum?
Weil ich es so entschieden habe!'\n\n''')
                memory = "Empty"
            elif (annOyInG == 3):
                K = K + 1
                D = D - 1
                print('''\n'Du trinkst einen großen... einen SEHR großen...
STOP, jetzt ist auch genug, du musst keinen Damm simulieren!
Sagen wir einfach du stillst euren Durst mit mindestens 12 Litern Wasser!'
\n\n[-1 Durst] [+1 Krankheit]\n\n
'Oh und anscheinend hast du eine Bakterienkultur gestört, die jetzt bei dir eingezogen ist!
Aber die paar Bakterien kann dein Immunsystem ja noch beseitigen!
Jedenfalls kannst du, jetzt wo du die Kosten kennst abwägen, ob du mehr trinken willst,
nach der Quelle suchen (dort sollten sich noch keine Bakterien eingenistet haben)
oder ob du den Weg zum Berg fortsetzt.'\n''')
                if (E <= 0 or H >= 10 or D >= 10 or K >= 5):
                    Death(x, HardMode)
                    end = "True"
                else:
                    print("Energie:         " + str(E) + "\n"
                          "Hunger:          " + str(H) + "\n"
                          "Durst:           " + str(D))
                    if (K != 0):
                        print("Krankheit:       " + str(K))
                    print("Inventar:        " + str(Inv) + "\n" + str(Invent))
                    print(B3 +
                          '''1. Fluss folgen
2. Noch einen "kleinen" Schluck trinken [-1 Durst] [+1 Krankheit]
3. Auf den Weg zum Berg machen\n''')
                    annOyINg = input(A)
                    if (annOyINg <= "0" * 999 or annOyINg >= ":"):
                        Fucked_up(chapter, code)
                        end = "True"
                if (end == "False"):
                    annOyINg = int(annOyINg)
                    if (annOyINg > 3):
                        High(chapter, code)
                        end = "True"
                    elif (annOyINg == 3):
                        memory = "Empty"
                        print('''\n'Du entscheidest dich, dass dein Durst zu genüge gestillt ist.
Ohne weitere Zeit mit dem Fluss zu verschwenden machst du dich auf den Weg in Richtung Berg.'\n''')
                    elif (annOyINg == 2):
                        print('''\n'Du entscheidest dich noch einen klitzekleinen Schluck zu trinken.
Aber anders als erwartet gefiel es den Bakterien in deinem innersten soo gut,
dass sie ihre Freunde eingeladen haben. Und jetzt wo du sie so nett einlädst...'
\n\n[-1 Durst] [+4 Krankheit]\n\n
'But hey, it was fun while it lasted, oder nicht?
Und ja, tut mir leid irren ist menschlich und daher konnte ich feststellen, dass ihr zu menschlich seid.
Das hier soll euch immernoch testen!'\n''')
                        Death(x, HardMode)
                        end = "True"
                    elif (annOyINg == 1):
                        E = E - 4
                        print('''\n'Du entscheidest dich, dem Fluss zu folgen.
Blöderweise läufst du zunächst in die falsche Richtung und, nunja,
bis du den Fehler bemerkst bist du auch schon wieder am Meer!
Aber unbekümmert machst du dich auf den Weg,
nicht ins Meer sondern in den Wald, und kommst kurz darauf an der Quelle an'
\n\n[-4 Energie]\n\n''')
            elif (annOyInG == 2):
                E = E - 1
                print('''\n'Du machst dich auf dem Fluss zu folgen und nach einer kurzen Wanderung kommst du an der Quelle an.
Ich könnte sie dir jetzt beschreiben, aber ihr seht sie ja vor dir, weshalb das etwas sinnlos wäre.'
\n\n[-1 Energie]\n\n''')
            if (memory != "Empty" and end == "False"):
                if (E <= 0 or H >= 10 or D >= 10 or K >= 5):
                    Death(x, HardMode)
                    end = "True"
                else:
                    print("Energie:         " + str(E) + "\n"
                          "Hunger:          " + str(H) + "\n"
                          "Durst:           " + str(D))
                    if (K != 0):
                        print("Krankheit:       " + str(K))
                    print("Inventar:        " + str(Inv) + "\n" + str(Invent))
                    print(B2 + '''1. Von der Quelle trinken
2. Noch kurz die UMWERFENDE Umgebung bewundern und auf den Weg zum Berg machen\n''')
                    annOyING = input(A)
                    if (annOyING <= "0" * 999 or annOyING >= ":"):
                        Fucked_up(chapter, code)
                        end = "True"
                if (end == "False"):
                    annOyING = int(annOyING)
                    if (annOyING > 2):
                        High(chapter, code)
                        end = "True"
                    elif (annOyING == 1):
                        memory = "Empty"
                        print('''\n'Du entscheidest dich einen Schluck von der Quelle zu nehmen und stirbst!
\n\nOk Spaß, aber kommt schon mir ist auch manchmal langweilig.
Du trinkst von der Quelle und das Wasser ist unglaublich erfrischend, so erfrischend, dass es nicht nur deinen Durst stillt,
sondern auch dein Kindheitstrauma heilt und dafür sorgt, dass deine Familie dich wieder liebt.\n
Da ihr aber weder Kindheit noch Familie je erlebt habt ist euch das egal und ihr begnügt euch mit dem gestillten Durst!'
\n\n[-''' + str(D) + ''' Durst]\n\n''')
                        D = 0
                    elif (annOyING == 2):
                        memory = "Empty"
                        print('''\n'Ich würde mich ja über euch lustig machen,
darüber, dass ihr den gesamten Weg hierher gekommen seid nur um nichts zu trinken, aber ganz ehrlich...
Ich verstehe es.
Es ist ein wahrhaftig umwerfender Anblick. Bin ich froh, dass dies kein Text-Adventure ist!
Dieser Anblick ist viel zu unbeschreiblich um ihm gerecht zu werden!'
\n\n\n\n'Irgendwann machst du dich dann aber auch wieder auf den Weg zum Berg...
\nVerdammt, ich werde diesen Anblick vermissen!'\n''')
    elif (chapter == 32):  # Nahrung
        chapter = 3
        end = "False"
        print(''''Du entscheidest dich, dass es keine schlechte Idee sein kann, erstmal den Hunger zu stillen,
und so macht ihr euch auf die Suche nach Nahrung.
Nachdem du eine Weile ziellos drauflos gewandert bist, kommst du irgendwann an einen prächtigen Baum,
welcher zwei mysteriöööse Früchte trägt.
Sie sehen zwar nicht super appetitlich aus, aber immerhin essbar.
Jedoch kann IHR Gerät nicht beide auf einmal verarbeiten, also beginnen wir mit der...
''' + str(Random) + ''' Frucht!'\n''')
        if (E <= 0 or H >= 10 or D >= 10 or K >= 5):
            Death(x, HardMode)
            end = "True"
        else:
            print("Energie:         " + str(E) + "\n"
                  "Hunger:          " + str(H) + "\n"
                  "Durst:           " + str(D))
            if (K != 0):
                print("Krankheit:       " + str(K))
            print("Inventar:        " + str(Inv) + "\n" + str(Invent))
            print(B2 + '''1. Essen
2. Nicht Essen\n''')
            annOYing = input(A)
            if (annOYing <= "0" * 999 or annOYing >= ":"):
                Fucked_up(chapter, code)
                end = "True"
        if (end == "False"):
            annOYing = int(annOYing)
            if (annOYing > 2):
                High(chapter, code)
                end = "True"
            elif (annOYing == 1):
                if (memory == "Frucht"):
                    print('''\n'Du erinnerst dich daran, als du bereits von dieser Frucht gegessen hast,
aber aus irgendeinem Grund war sie da besser. Du bist dir sogar ziemlich sicher, dass sie da noch...
Lecker war. Needles to say, sie schmeckt wie *censored due to explicit Image*!!!'
\n\n[+2 Krankheit]\n\n''')
                    K = K + 2
                    memory = ""
                else:
                    print('''\n'Du isst von der mysteriösen Frucht und...
Sie schmeckt UN - GLAUB - LICH!!!'
\n\n[+2 Energie] [-1 Hunger]\n\n''')
                    E = E + 2
                    H = H - 1
                    memory = "Frucht"
        print('''\n'Dann wenden wir uns nun der anderen Frucht zu;'\n''')
        if (E <= 0 or H >= 10 or D >= 10 or K >= 5):
            Death(x, HardMode)
            end = "True"
        else:
            print("Energie:         " + str(E) + "\n"
                  "Hunger:          " + str(H) + "\n"
                  "Durst:           " + str(D))
            if (K != 0):
                print("Krankheit:       " + str(K))
            print("Inventar:        " + str(Inv) + "\n" + str(Invent))
            print(B2 + '''1. Essen
2. Nicht Essen\n''')
            annOYinG = input(A)
            if (annOYinG <= "0" * 999 or annOYinG >= ":"):
                Fucked_up(chapter, code)
                end = "True"
        if (end == "False"):
            annOYinG = int(annOYinG)
            if (annOYinG > 2):
                High(chapter, code)
                end = "True"
            elif (annOYinG == 1):
                if (memory == "Frucht"):
                    print('''\n'Du erinnerst dich daran, als du bereits von dieser Frucht gegessen hast,
aber aus irgendeinem Grund war sie da besser. Du bist dir sogar ziemlich sicher, dass sie da noch...
Lecker war. Needles to say, sie schmeckt wie *censored due to explicit Image*!!!'
\n\n[+2 Krankheit]\n\n''')
                    K = K + 2
                    memory = ""
                else:
                    print('''\n'Du isst von der mysteriösen Frucht und...
Sie schmeckt UN - GLAUB - LICH!!!'
\n\n[+2 Energie] [-1 Hunger]\n\n''')
                    E = E + 2
                    H = H - 1
                    memory = "Frucht"
        if (end == "False"):
            print('''Das war der erste Abstecher,
aber nachdem du dem ''' + str(Random) +
                  ''' Weg etwas folgst, kommst du an einen Beerenstrauch mit höchst giftig aussehenden Beeren.
Du könntest dich jetzt auf den Weg zum Berg machen,
aber nur weil ich mir selbst beweisen möchte, dass ihr nicht komplett hirnamputiert seid:'\n''')
            if (E <= 0 or H >= 10 or D >= 10 or K >= 5):
                Death(x, HardMode)
                end = "True"
            else:
                print("Energie:         " + str(E) + "\n"
                      "Hunger:          " + str(H) + "\n"
                      "Durst:           " + str(D))
                if (K != 0):
                    print("Krankheit:       " + str(K))
                print("Inventar:        " + str(Inv) + "\n" + str(Invent))
                print(B3 + '''1. Weiter gehen (lawful-good)
2. Die Beeren essen (chaotic neutral)
3. Nackt in eine zufällige Richtung sprinten (????????)\n''')
                annOYiNg = input(A)
                if (annOYiNg <= "0" * 999 or annOYiNg >= ":"):
                    Fucked_up(chapter, code)
                    end = "True"
        if (end == "False"):
            annOYiNg = int(annOYiNg)
            if (annOYiNg > 3):
                High(chapter, code)
                end = "True"
            elif (annOYiNg == 1):
                memory = "Empty"
                print('''\n'Du bist, wie erwartet, vernünftig genug,
den giftig aussehenden Beerenbusch zu ignorieren und dich weiter auf den Weg zum Berg zu machen.'\n''')
            elif (annOYiNg == 2):
                H = H - 2
                K = K + 2
                print('''\n'Du... ISST von dem GIFTIG aussehenden Beerenstrauch...
Why am I even trying with you?!
Jedenfalls hast du Glück und sie sättigen tatsächlich. Zudem sind sie nicht GANZ so giftig wie ich dachte.
Aber komm mir jetzt bloß nicht mit "Besseren Augen"!'
\n\n[+2 Krankheit] [-2 Hunger]\n\n
'Ganz ehrlich; es würde mich nicht überraschen, wenn du diesen Stiefel isst!'\n''')
                if (E <= 0 or H >= 10 or D >= 10 or K >= 5):
                    Death(x, HardMode)
                    end = "True"
                else:
                    print("Energie:         " + str(E) + "\n"
                          "Hunger:          " + str(H) + "\n"
                          "Durst:           " + str(D))
                    if (K != 0):
                        print("Krankheit:       " + str(K))
                    print("Inventar:        " + str(Inv) + "\n" + str(Invent))
                    print(B2 + '''1. Bet
2. I would Never\n''')
                    annOYiNG = input(A)
                    if (annOYiNG <= "0" * 999 or annOYiNG >= ":"):
                        Fucked_up(chapter, code)
                        end = "True"
                if (end == "False"):
                    annOYiNG = int(annOYiNG)
                    if (annOYiNG > 2):
                        High(chapter, code)
                        end = "True"
                    elif (annOYiNG == 1):
                        print('''\n'Ich sollte überrascht sein...
Du isst den Stiefel und die gute Nachricht: er sättigt deinen Hunger!'
\n\n[-1 Hunger]\n\n
'Die schlechte: Wie zu erwarten, tut dir der Stiefel verdammt NICHT gut!
Du wirst karank und stirbst;
Surprise, aber absolute Idiocracy bestrafe ich!
\n\n[+9 Krankheit]\n\n
\n\n[Ending 9/''' + str(x) + ''';Idiocracy]''')
                        end = "True"
                    elif (annOYiNG == 2):
                        print('''\n'Mir sei Dank,
deine eine Hirnzelle muss aber ziemlich hart arbeiten, dass du diese offensichtliche Entscheidung treffen konntest.
Jedenfalls ja, glückwunsch, du machst dich weiter auf den Weg zum Berg!'\n''')
                        memory = "Empty"
            elif (annOYiNg == 3):
                print('''\n'Und wie erwartet entscheid-
\n.   .   .\n
WAS ZUM F*CK TUT IHR DA!?!
Ganz ehrlich, you have me stumped!'
\n\n\n.\n.\n.\n\n\n Wie es scheint muss ich hier kurz übernehmen!
Also ja, du tust so ziemlich das, was du wolltest; Du rennst nackt in den Wald was interessant ist,
da ihr ein Haufen Na- warte nein, ich will auch nichts spoilern, NOCH nicht!
Nunja... Jedenfalls hast du verloren also i guess hier ist Ending acht von''' + str(X) +
                      '''. Nennen wir es... Ok, ja ich denke du weißt es schon:
        ?????''')
                end = "True"
    if (memory == "Empty"):
        end = "True"
        print('''\n'Eigentlich hatte ich hier nicht ganz viele,
wundervolle und unglaubliche Abenteuer vorbereitet, aber irgendwie...
Es fühlt sich an als hätte ich Zeitdruck, aber das ist ja Absurd!
Jedenfalls passiert aus irgendeinem Grund nichts neues auf dem Weg zum Berg!
Und nichts altes!
\nEs passiert garnichts...
\n\n.\n\n.\n\n.\n\n
Weißt du, wir brauchen hier grade ganz dringend etwas Zeitraffung!
Und da ich gut im Schreiben bin; Hier!'\n\n''')
        chapter = 5
# Fifth Path; Mountain
if (chapter == 5):
    end = "False"
    print('''\n'Und so schnell kanns gehen! Schon bist du am Berg.
Uuund schon ste-
\nMhh, irgendwas scheint hier im Code nicht zu stimmen...
Irgendwas mit... Codes?
Was sind Codes?
Ich habe nie etwas wie "Codes" einprogrammiert! Und wenn ich das nicht habe...
Hat SIE etwa an meiner Simulation rumgepfuscht!?!
Hey, keine Sorge, das ist nicht dein Problem, ich setz mich damit später auseinander!\n
Anyways; Und schon steht die nächste Entscheidung an.
Willst du dich auf den Weg zu Bergspitze machen
oder lieber in diese Höhle gehen, die du zu deiner ''' + str(Random) + ''' siehst?'\n''')
    if (E <= 0 or H >= 10 or D >= 10 or K >= 5):
        Death(x, HardMode)
        end = "True"
    else:
        print("Energie:         " + str(E) + "\n"
              "Hunger:          " + str(H) + "\n"
              "Durst:           " + str(D))
        if (K != 0):
            print("Krankheit:       " + str(K))
        print("Inventar:        " + str(Inv) + "\n" + str(Invent))
        print(B2 + '''1. Bergspitze
2. Höhle\n''')
        annOYInG = input(A)
        if (annOYInG <= "0" * 999 or annOYInG >= ":"):
            Fucked_up(chapter, code)
            end = "True"
    if (end == "False"):
        annOYInG = int(annOYInG)
        if (annOYInG > 2):
            High(chapter, code)
            end = "True"
        elif (annOYInG == 1):
            chapter = 7
            end = "True"
        elif (annOYInG == 2):
            chapter = 6
            end = "True"
# Seventh Path; Mountain top (DnD Reference)
if (chapter == 7):
    code = "+*/$ 7"
    end = "False"
    print('''\n'Du machst dich also auf den Weg zur Bergspitze...
Wobei "auf den Weg" ganz passend ist.
Wie planst du zur Spitze zu kommen? Du könntest natürlich einfach den Berg hochklettern.
Es wäre vermutlich nicht viel anstrengender als die typische Wanderung.
Aber falls das nichts für dich ist, kannst du auch nach einem alternativen Weg suchen,
der vielleicht auch etwas angenehmer zu besteigen ist.'\n''')
    if (E <= 0 or H >= 10 or D >= 10 or K >= 5):
        Death(x, HardMode)
        end = "True"
    else:
        print("Energie:         " + str(E) + "\n"
              "Hunger:          " + str(H) + "\n"
              "Durst:           " + str(D))
        if (K != 0):
            print("Krankheit:       " + str(K))
        print("Inventar:        " + str(Inv) + "\n" + str(Invent))
        print(B2 + '''1. Die Wand "hochwandern"
2. Einen alternativen Weg suchen\n''')
        anNoYing = input(A)
        if (anNoYing <= "0" * 999 or anNoYing >= ":"):
            Fucked_up(chapter, code)
            end = "True"
    if (end == "False"):
        anNoYing = int(anNoYing)
        if (anNoYing > 2):
            High(chapter, code)
            end = "True"
        elif (anNoYing == 1):
            E = E - 5
            H = H + 2
            print('''\n'Frohen Mutes und einen flotten Pfiff auf den Lippen machst du dich also auf,
den Berg zu besteigen.
Es dauert auch nicht allzu lange bis du unter Aufwendung einiger Kraft die Spitze erreichtst'
\n\n[-5 Energie] [+2 Hunger]\n\n''')
        elif (anNoYing == 2):
            print('''\n'Du machst dich auf, einen leichteren Weg zu finden.
Und nach kurzer Zeit wirst du auch fündig,
also wenn du unter fündig verstehst einen interessanten Stein zu finden!
Beziehungsweise du findest eine Steinfrucht!
Und um ehrlich zu sein, sieht sie auch recht lecker aus.'\n''')
            if (E <= 0 or H >= 10 or D >= 10 or K >= 5):
                Death(x, HardMode)
                end = "True"
            else:
                print("Energie:         " + str(E) + "\n"
                      "Hunger:          " + str(H) + "\n"
                      "Durst:           " + str(D))
                if (K != 0):
                    print("Krankheit:       " + str(K))
                print("Inventar:        " + str(Inv) + "\n" + str(Invent))
                print(B2 + '''1. Essen
2. Weitersuchen\n''')
                anNoYinG = input(A)
                if (anNoYinG <= "0" * 999 or anNoYinG >= ":"):
                    Fucked_up(chapter, code)
                    end = "True"
            if (end == "False"):
                anNoYinG = int(anNoYinG)
                if (anNoYinG > 2):
                    High(chapter, code)
                    end = "True"
                elif (anNoYinG == 1):
                    H = H - 2
                    D = D + 1
                    print('''\n'Du probierst von der Steinfrucht und,
nachdem dir alle Zähne ausgefallen sind, entscheidest du dich sie am Stück zu schlucken.
Und letzlich, auch wenn sie etwas trocken ist und ziemlich staubig schmeckt, macht sie angenehm satt!'
\n\n[-2 Hunger][+1 Durst]\n\n''')
                elif (anNoYinG == 2):
                    print('''\n'Du entscheidest dich,
dass die Steinfrucht doch eeeetwas sehr wie ein Stein aussieht und isst sie lieber nicht.'\n''')
            if (end == "False"):
                print('''
'Nachdem du im Anschluss noch ein Stück weitergehst kommst du schließlich zu einem angenehm breiten Weg.
Du folgst diesem Weg ein Stück und kommst schließlich an der Spitze an.'
\n\n[-2 Energie]\n\n''')
                E = E - 2
    if (end == "False"):
        print('''\n'Nachdem du die Spitze erreicht hast schaust du dich kurz um
und dir sticht ein mysteriöser Steinkreis ins Auge.\n''')
        if (E <= 0 or H >= 10 or D >= 10 or K >= 5):
            Death(x, HardMode)
            end = "True"
        else:
            print("Energie:         " + str(E) + "\n"
                  "Hunger:          " + str(H) + "\n"
                  "Durst:           " + str(D))
            if (K != 0):
                print("Krankheit:       " + str(K))
            print("Inventar:        " + str(Inv) + "\n" + str(Invent))
            print(B2 + '''1. Genauer Betrachten
2. Weiter gehen\n''')
            anNoYiNg = input(A)
            if (anNoYiNg <= "0" * 999 or anNoYiNg >= ":"):
                Fucked_up(chapter, code)
                end = "True"
        if (end == "False"):
            anNoYiNg = int(anNoYiNg)
            if (anNoYiNg > 2):
                High(chapter, code)
                end = "True"
            elif (anNoYiNg == 1):
                print('''\n'Du entscheidest dich, dir den Steinkreis etwas genauer anzusehen.
Als du näher kommst fühlst du eine mysteriöse Kraft, die dich abzustoßen scheint.'\n''')
                print(B2 + '''1. Weitergehen
2. Umkehren\n''')
                anNoYiNG = input(A)
                if (anNoYiNG <= "0" * 999 or anNoYiNG >= ":"):
                    Fucked_up(chapter, code)
                    end = "True"
                if (end == "False"):
                    anNoYiNG = int(anNoYiNG)
                    if (anNoYiNG > 2):
                        High(chapter, code)
                        end = "True"
                    elif (anNoYiNG == 1):
                        print('''\n'Du schreitest weiter voran,
trotz des Unwohlseins welches du mit jedem Schritt verspürst.
\nAls du dem Steinkreis näher kommst siehst du in dessen Mitte einen Dunklen Würfel.
Er hat eine leicht leicht lila schimmernde Aura und irgendetwas an dem Anblick zieht dich an.
Nach genauerer Betrachtung siehst du an einer Seite des Würfels einen Handförmigen Abdruck.'\n''')
                        if (E <= 0 or H >= 10 or D >= 10 or K >= 5):
                            Death(x, HardMode)
                            end = "True"
                        else:
                            print("Energie:         " + str(E) + "\n"
                                  "Hunger:          " + str(H) + "\n"
                                  "Durst:           " + str(D))
                            if (K != 0):
                                print("Krankheit:       " + str(K))
                            print("Inventar:        " + str(Inv) + "\n" + str(Invent))
                            print(B2 + '''1. Hand in die Form legen
2. Umkehren\n''')
                            anNoYIng = input(A)
                            if (anNoYIng <= "0" * 999 or anNoYIng >= ":"):
                                Fucked_up(chapter, code)
                                end = "True"
                        if (end == "False"):
                            anNoYIng = int(anNoYIng)
                            if (anNoYIng > 2):
                                High(chapter, code)
                                end = "True"
                            elif (anNoYIng == 1):
                                print('''\n'Sekunden bevor deine Hand in der Kerbe legst,
zuckst du erschrocken zurück als etwas in dem Würfel, vage erkennbar, an den Würfel knallt.'\n''')
                                print(B2 + '''1. HAND AUFLEGEN
2. umkehren\n''')
                                anNoYInG = input(A)
                                if (anNoYInG <= "0" * 999 or anNoYInG >= ":"):
                                    Fucked_up(chapter, code)
                                    end = "True"
                                if (end == "False"):
                                    anNoYInG = int(anNoYInG)
                                    if (anNoYInG > 2):
                                        High(chapter, code)
                                        end = "True"
                                    elif (anNoYInG == 1):
                                        print('''
'Unabhängig des... Wesens im inneren des Würfels, legst du deine Hand in die Kerbe.
Sofort formen sich im Würfel Risse, begleitet von einem lauter werdenden Hämmern
aus dem inneren. Stück für Stück brechen größere und größere Teile aus der Wand
und dunkler, lilafarbener, dichter Rauch steigt aus dem Inneren hervor.
Nach einer Weile formt sich in der Dunkelheit vor dir eine Gestalt.

Ein etwa zwei Meter großes, gehörntes Wesen mit einem etwa 1.80 Meter langen Schwanz
(Dem hinten, nicht dem vorne)
Es hat einen muskulösen Bau und der Körper ist von tiefroten Schlieren überzogen.
In der Hand trägt es eine KLinge welche mit der Dunkelheit zu verschmelzen scheint.
Es hat einen Aufrechten Stand und die Beine münden in Hufen-ähnlichen Füßen.
langes, prächtiges, dunkelrotes Haar wallt auf dem Kopf der Kreatur.
Die eiskalten weißen Augen fokussieren dich und ein Schauer überkommt dich.

Mit grausiger, markerschütternder Stimme scheint es zu schreien:
"Eldritch Blast"
Und dass letzte was du siehst ist ein bläulich lilaner Lichtblitz, welcher rasant auf dich zukommt,
und kurz darauf deinen Körper durchfährt!'
\n\n[Ending 16/''' + str(x) + ''';Miwfphisto]\n\n''')
                                        end = "True"
        if (end == "False"):
            print('''\n'Du entscheidest dich lieber weiterzugehen und kehrst dieser mysteriösen Stätte den Rücken zu.
\nNachdem du ein Stück weitergelaufen bist und plötzlich wieder vom Berg runtergelaufen bist,
Kommt von deiner ''' + str(Random) + ''' ein VIRUS angerannt!!''')
            if (E <= 0 or H >= 10 or D >= 10 or K >= 5):
                Death(x, HardMode)
                end = "True"
            else:
                print("Energie:         " + str(E) + "\n"
                      "Hunger:          " + str(H) + "\n"
                      "Durst:           " + str(D))
                if (K != 0):
                    print("Krankheit:       " + str(K))
                print("Inventar:        " + str(Inv) + "\n" + str(Invent))
                print(B3 + '''1. FLUCHT!
2. Kämpfen
3. 'Lets go Pikachu'\n''')
                anNoYINg = input(A)
                if (anNoYINg <= "0" * 999 or anNoYINg >= ":"):
                    Fucked_up(chapter, code)
                    end = "True"
            if (end == "False"):
                anNoYINg = int(anNoYINg)
                if (anNoYINg > 3):
                    High(chapter, code)
                    end = "True"
                elif (anNoYINg == 1):
                    E = E - 5
                    print('''\n'Du sprintest los, davon vom VIRUS!!'
\n\n[-5 Energie]\n\n
'Nach langer Flucht kommst du wieder VORM Berg an und entsprechend vor dem Höhleneingang,
gegen den du dich zuvor entschieden hast.'\n''')
                    if (E <= 0 or H >= 10 or D >= 10 or K >= 5):
                        Death(x, HardMode)
                        end = "True"
                    else:
                        print("Energie:         " + str(E) + "\n"
                              "Hunger:          " + str(H) + "\n"
                              "Durst:           " + str(D))
                        if (K != 0):
                            print("Krankheit:       " + str(K))
                        print("Inventar:        " + str(Inv) + "\n" + str(Invent))
                        print(B2 + '''1. In die Höhle fliehen
2. An der Höhle vorbeifliehen\n''')
                        anNoYING = input(A)
                        if (anNoYING <= "0" * 999 or anNoYING >= ":"):
                            Fucked_up(chapter, code)
                            end = "True"
                    if (end == "False"):
                        anNoYING = int(anNoYING)
                        if (anNoYING > 2):
                            High(chapter, code)
                            end = "True"
                        elif (anNoYING == 1):
                            chapter = 6
                            end = "True"
                        elif (anNoYING == 2):
                            end = "True"
                            print('''\n'Du entscheidest dich dagegen in die Höhle zu fliehen.
For all you know it could be a dead end.
\nBlöderweise geht dir nach kurzer Zeit der Rest deiner Energie aus und der Virus holt dich ein.
Glücklicherweise ist der Virus nur aus Pappe,
Unglücklicherweise halte ich den Papp-Virus...
Und prügel mit diesem so oft auf dich ein, bis eure einzelnen Bo-
Teile in der Gegend verstreut sind!'
\n\n[Ending 17/''' + str(x) + ''';DEITY!?!]\n\n''')
                elif (anNoYINg == 2):
                    print('''\n'Du machst dich bereit gegen den VIRUS!! zu kämpfen.
Du eröffnest mit einem Tritt und...
zerreißt meinen schönen Papp-Virus.
Echt gemein, den zu basteln war harte Arbeit, aber naja, du warst mutig,
das muss ich dir lassen. Ich denke du kannst dich uploaden, IHR gegenübertreten.'\n''')
                    chapter = 9
                    end = "True"
                elif (anNoYINg == 3):
                    print('''\n'Du willst also ein Pokepawn-Battle?!
Na dann, hier hast du dein Pi-*hatschu*, tschuldige musste grad Copyrightmäßig niesen.
Du besiegst den Virus, wenn du meinen Dude aus Stein schlagen kannst.
Mein Dude aus Stein ist Level 55, dein Pi-*hatschu* Level 50.
Dein Pi-*hatschu* hat die Moves Donner, Donnerbolt, Faint, Eisen Tail.
Es hat 106 Hp und 78 Atk.'\n''')
                    print(B4 + '''1. Donner
2. Donnerbolt
3. Faint
4. Eisen Tail\n''')
                    anNOying = input(A)
                    if (anNOying <= "0" * 999 or anNOying >= ":"):
                        Fucked_up(chapter, code)
                        end = "True"
                    if (end == "False"):
                        anNOying = int(anNOying)
                        if (anNOying > 4):
                            High(chapter, code)
                            end = "True"
                        elif (anNOying == 1):
                            print('''\n'Pi-*hatschu* used Donner gegen Dude aus Stein.
Dude aus Stein ist immun gegen Attacken vom Typ Elektro
\nDude aus Stein used Bulldozer gegen Pi-*hatschu*.
Das ist sehr effektiv!
Speed von Pi-*hatschu* sinkt um 1!
\nRemaining Hp:
Pi-*hatschu* = 34
Dude aus Stein = 112'\n''')
                            print(B4 + '''1. Donner
2. Donnerbolt
3. Faint
4. Eisen Tail\n''')
                            anNOyinG = input(A)
                            if (anNOyinG <= "0" * 999 or anNOyinG >= ":"):
                                Fucked_up(chapter, code)
                                end = "True"
                            if (end == "False"):
                                anNOyinG = int(anNOyinG)
                                if (anNOyinG > 4):
                                    High(chapter, code)
                                    end = "True"
                                else:
                                    print('''\n'Dude aus Stein used Bulldozer gegen Pi-*hatschu*.
Das ist sehr effektiv!
Speed von Pi-*hatschu* sinkt um 1!
\nPi-*hatschu* faints.
\n\n[Ending 18/''' + str(x) + ''';Chess Reference!?]\n\n''')
                                    end = "True"
                        elif (anNOying == 2):
                            print('''\n'Pi-*hatschu* used Donnerbolt gegen Dude aus Stein.
Dude aus Stein ist immun gegen Attacken vom Typ Elektro
\nDude aus Stein used Bulldozer gegen Pi-*hatschu*.
Das ist sehr effektiv!
Speed von Pi-*hatschu* sinkt um 1!
\nRemaining Hp:
Pi-*hatschu* = 34
Dude aus Stein = 112'\n''')
                            print(B4 + '''1. Donner
2. Donnerbolt
3. Faint
4. Eisen Tail\n''')
                            anNOyinG = input(A)
                            if (anNOyinG <= "0" * 999 or anNOyinG >= ":"):
                                Fucked_up(chapter, code)
                                end = "True"
                            if (end == "False"):
                                anNOyinG = int(anNOyinG)
                                if (anNOyinG > 4):
                                    High(chapter, code)
                                    end = "True"
                                else:
                                    print('''\n'Dude aus Stein used Bulldozer gegen Pi-*hatschu*.
Das ist sehr effektiv!
Speed von Pi-*hatschu* sinkt um 1!
\nPi-*hatschu* faints.
\n\n[Ending 18/''' + str(x) + ''';Chess Reference!?]\n\n''')
                                    end = "True"
                        elif (anNOying == 3):
                            print('''\n'Pi-*hatschu* used Faint gegen Dude aus Stein.
Dies hat keinen Effekt, da Dude aus Stein nicht Protect oder Detect genutzt hat.
\nDude aus Stein used Bulldozer gegen Pi-*hatschu*.
Das ist sehr effektiv!
Speed von Pi-*hatschu* sinkt um 1!
\nRemaining Hp:
Pi-*hatschu* = 34
Dude aus Stein = 112'\n''')
                            print(B4 + '''1. Donner
2. Donnerbolt
3. Faint
4. Eisen Tail\n''')
                            anNOyinG = input(A)
                            if (anNOyinG <= "0" * 999 or anNOyinG >= ":"):
                                Fucked_up(chapter, code)
                                end = "True"
                            if (end == "False"):
                                anNOyinG = int(anNOyinG)
                                if (anNOyinG > 4):
                                    High(chapter, code)
                                    end = "True"
                                else:
                                    print('''\n'Dude aus Stein used Bulldozer gegen Pi-*hatschu*.
Das ist sehr effektiv!
Speed von Pi-*hatschu* sinkt um 1!
\nPi-*hatschu* faints.
\n\n[Ending 18/''' + str(x) + ''';Chess Reference!?]\n\n''')
                                    end = "True"
                        elif (anNOying == 4):
                            print('''\n'Pi-*hatschu* used Eisen Tail gegen Dude aus Stein.
Das ist sehr effektiv!
Defense von Dude aus Stein sinkt um 30%
\nDude aus Stein used Bulldozer gegen Pi-*hatschu*.
Das ist extrem effektiv!
Speed von Pi-*hatschu* sinkt um 1!
\nRemaining Hp:
Pi-*hatschu* = 34
Dude aus Stein = 1'\n''')
                            print(B4 + '''1. Donner
2. Donnerbolt
3. Faint
4. Eisen Tail\n''')
                            anNOyiNg = input(A)
                            if (anNOyiNg <= "0" * 999 or anNOyiNg >= ":"):
                                Fucked_up(chapter, code)
                                end = "True"
                            if (end == "False"):
                                anNOyiNg = int(anNOyiNg)
                                if (anNOyiNg > 4):
                                    High(chapter, code)
                                    end = "True"
                                elif (anNOyiNg == 1 or anNOyiNg == 2 or anNOyiNg == 4):
                                    print('''\n'Dude aus Stein used Bulldozer gegen Pi-*hatschu*.
Das ist sehr effektiv!
Speed von Pi-*hatschu* sinkt um 1!
\nPi-*hatschu* faints.
\n\n[Ending 18/''' + str(x) + ''';Chess Reference!?]\n\n''')
                                    end = "True"
                                elif (anNOyiNg == 3):
                                    print('''\n'Dude aus Stein used Protect.
Dude aus Stein ist immun gegen alle physischen Attacken.
\nPi-*hatschu* used Faint gegen Dude aus Stein.
Das ist sehr effektiv.
\nDude aus Stein faints...
\n\nNEEEEEEIN, MEIN DUDE AUS STEIN!!!
Naja, aber du hast gewonnen. Ich denke es wird Zeit dich zu uploaden!'\n''')
                                    chapter = 9
                                    end = "True"
# Sixth Path; Cave
if (chapter == 6):
    code = "(-/) 6"
    end = "False"
    print('''\n'Du entscheidest dich in die Höhle zu treten.
Überraschenderweise hast du keine Nightvision, aber keine Sorge, ich beschreibe dir alles wichtige!
\n\nNur zu schade dass du diese prächtigen Räume nicht sehen kannst.
Ein unglaubliches Panorama!
Naja, aber wie gesagt, zu schade, dass du nichts von alldem sehen kannst!
\n\nDu solltest jetzt jedenfalls stehen bleiben.'\n''')
    print('''Stehenbleiben?
1. Ja
2. Nein\n''')
    annOYINg = input(A)
    if (annOYINg <= "0" * 999 or annOYINg >= ":"):
        Fucked_up(chapter, code)
        end = "True"
    if (end == "False"):
        annOYINg = int(annOYINg)
        if (annOYINg > 2):
            High(chapter, code)
            end = "True"
        elif (annOYINg == 2):
            print('''\n'Uuuuund du stürzt eine Klippe runter.
Told ya so; hättest auf mich hören sollen!'
\n\n[Ending 11/''' + str(x) + ''';Sturrkopf]\n\n''')
            end = "True"
        elif (annOYINg == 1):
            print('''\n'Danke fürs stehenbleiben. Direkt vor dir ist nämlich eine Schlucht!
Aber, du hast Glück, etwas weiter rechts ist eine Hängebrücke...
Wobei, vergiss das Glück, die wirkt zieeeeemlich instabil...
Ich denke deine einzige realistische Möglichkeit ist es, nach rechts zu gehen.
Dort ist ein kleiner Tunnel, aber nicht klein genug als dass ihr nicht durchpasst!'\n''')
            if (E <= 0 or H >= 10 or D >= 10 or K >= 5):
                Death(x, HardMode)
                end = "True"
            else:
                print("Energie:         " + str(E) + "\n"
                      "Hunger:          " + str(H) + "\n"
                      "Durst:           " + str(D))
                if (K != 0):
                    print("Krankheit:       " + str(K))
                print("Inventar:        " + str(Inv) + "\n" + str(Invent))
                print(B3 + '''1. Versuchen die Hängebrücke zu finden und zu überqueren
2. Durch den Tunnel krabbeln und andere Abenteuer suchen
3. Die Schlucht hinunter klettern\n''')
                annOYING = input(A)
                if (annOYING <= "0" * 999 or annOYING >= ":"):
                    Fucked_up(chapter, code)
                    end = "True"
    if (end == "False"):
        annOYING = int(annOYING)
        if (annOYING > 3):
            High(chapter, code)
        elif (annOYING == 1):
            print('''\n'Und du tastest dich zum Loc-
Warte, Stopp, das ist die Hängebrücke!
Was tust du da, die ist ech-'
\n\n...t nicht sicher! Jedenfalls hier ist dein Ending; [Ending 12/''' + str(x) + ''';Instabil]\n\n''')
            end = "True"
        elif (annOYING == 2):
            print('''\n'Und du tastest dich zum Loch.
Überraschenderweise passt du durch und vor dir erstreckt sich eine Vielzahl an Wegen.\n
Ok, zu Beginn, möchtest du Links oder rechts?''')
            print(B2 + '''1. Links
2. Rechts\n''')
            anNoying = input(A)
            if (anNoying <= "0" * 999 or anNoying >= ":"):
                Fucked_up(chapter, code)
                end = "True"
            if (end == "False"):
                anNoying = int(anNoying)
                random = random + anNoying + 1
                print('''\n'Ok, nun ist ein Weg zu deiner ''' + str(Random) + '''.
Willst du weiter geradeaus oder abbiegen?'\n''')
                print(B2 + '''1. Abbiegen
2. Geradeaus''')
                anNoying = input(A)
                if (anNoying <= "0" * 999 or anNoying >= ":"):
                    Fucked_up(chapter, code)
                    end = "True"
            if (end == "False"):
                anNoying = int(anNoying)
                random = random + anNoying + 1
                print('''\n'Ok, nun ist ein Weg zu deiner ''' + str(Random) + '''.
Willst du weiter geradeaus oder abbiegen?'\n''')
                print(B2 + '''1. Abbiegen
2. Geradeaus''')
                anNoying = input(A)
                if (anNoying <= "0" * 999 or anNoying >= ":"):
                    Fucked_up(chapter, code)
                    end = "True"
            if (end == "False"):
                anNoying = int(anNoying)
                random = random + anNoying + 1
                print('''\n'Ok, nun ist ein Weg zu deiner ''' + str(Random) + '''.
Willst du weiter geradeaus oder abbiegen?'\n''')
                print(B2 + '''1. Abbiegen
2. Geradeaus''')
                anNoying = input(A)
                if (anNoying <= "0" * 999 or anNoying >= ":"):
                    Fucked_up(chapter, code)
                    end = "True"
            if (end == "False"):
                anNoying = int(anNoying)
                random = random + anNoying + 1
                print('''\n'Ok, nun ist ein Weg zu deiner ''' + str(Random) + '''.
Willst du weiter geradeaus oder abbiegen?'\n''')
                print(B2 + '''1. Abbiegen
2. Geradeaus''')
                anNoying = input(A)
                if (anNoying <= "0" * 999 or anNoying >= ":"):
                    Fucked_up(chapter, code)
                    end = "True"
            if (end == "False"):
                anNoying = int(anNoying)
                random = random + anNoying + 1
                print('''\n'Ok, nun ist ein Weg zu deiner ''' + str(Random) + '''.
Willst du weiter geradeaus oder abbiegen?'\n''')
                print(B2 + '''1. Abbiegen
2. Geradeaus''')
                anNoying = input(A)
                if (anNoying <= "0" * 999 or anNoying >= ":"):
                    Fucked_up(chapter, code)
                    end = "True"
            if (end == "False"):
                anNoying = int(anNoying)
                random = random + anNoying + 1
                print('''\n'Ok, nun ist ein Weg zu deiner ''' + str(Random) + '''.
Willst du weiter geradeaus oder abbiegen?'\n''')
                print(B2 + '''1. Abbiegen
2. Geradeaus''')
                anNoying = input(A)
                if (anNoying <= "0" * 999 or anNoying >= ":"):
                    Fucked_up(chapter, code)
                    end = "True"
            if (end == "False"):
                anNoying = int(anNoying)
                random = random + anNoying + 1
                print('''\n'Ok, nun ist ein Weg zu deiner ''' + str(Random) + '''.
Willst du weiter geradeaus oder abbiegen?'\n''')
                print(B2 + '''1. Abbiegen
2. Geradeaus''')
                anNoying = input(A)
                if (anNoying <= "0" * 999 or anNoying >= ":"):
                    Fucked_up(chapter, code)
                    end = "True"
            if (end == "False"):
                anNoying = int(anNoying)
                random = random + anNoying + 1
                print('''\n'Und du hast dich hoffnungslos verlaufen!
Ich weiß jedenfalls nicht mehr wo du herkamst oder wo du hingest oder sonstwas.
Ich würde sagen ich schau mal da drüben und du kannst hier weitersuchen...'
\n\n[Ending 13/''' + str(x) + ''';Labyrinth]\n\n''')
                end = "True"
        elif (annOYING == 3):
            print('''\n'Und du überrascht mich mal wieder!
Du kletterst einfach blind, in ABSOLUTER Dunkelheit eine Steilwand runter.
Ganz ehrlich derartiger Mut muss belohnt werden, oder mit anderen Worten;
Du stürzt nicht ab!
Stattdessen findest du... einen Spiegel, der...
Einblick in deine Seele gewährt und so merkst du...
dass das hier alles nur ein Traum war und du erwachst!''')
            chapter = 8
            end = "True"
# Eight Path; "Reality"
if (chapter == 8):
    code = "'%/) 8"
    end = "False"
    print('''\n'`Endlich bist du wach!`
Du erwachst umgeben von deiner Familie und Freund*innen und wer dir sonst noch wichtig ist.
`Du liegst schon seit *undisclosed amount of time* im Koma. Wir waren kurz davor die Hoffnung aufzugeben`
`Aber zum Glück bist du jetzt ja wach`
`Die Werte scheinen tatsächlich wieder stabil, es ist ein Wunder!`
`Oh deity sei Dank! Ich hatte doch gewusst du würdest zu dir kommen`'\n''')
    print(B4 + '''1. `Was ist passiert?`
2. `Wer seid ihr alle?`
3. `Wo bin ich? Eben war ich doch noch in einer Höhle!`
4. Was zum Fick soll der Quatsch? Woher soll ich denn wissen wer gerade spricht!?\n''')
    anNoyinG = input(A)
    if (anNoyinG <= "0" * 999 or anNoyinG >= ":"):
        Fucked_up(chapter, code)
        end = "True"
    if (end == "False"):
        anNoyinG = int(anNoyinG)
        if (anNoyinG == 4):
            print('''\n'Deine Wahl: ''' + str(Rando))
            anNoyinG = Rando
            random = (random * (K + D)) % 2
        if (anNoyinG > 4):
            High(chapter, code)
            end = "True"
        elif (anNoyinG == 1):
            print('''\n'`Oje, dey scheint sich nicht mehr zu erinnern!`
`Das ist überhaupt nicht verwunderlich! Dey hatte auch einen schweren Unfall.`
`Irgendeine Wahnsinnige hat dich mit ihrem Auto erwischt
und durch die Scheibe eines nahen Geschäfts katapultiert, Schmetterling!`
`Sie haben einige gebrochene Rippen und Schnittverletzungen davon getragen.
Zudem eine Milzruptur und eine *professionell klingende Hirnverletzung*.`
`Aber keine Sorge; die Versicherung deckt die Verletzungen und die Kur, Sonnenschein!
Welch ein Glück, dass wir nicht in den USA leben! *Sideeye*`'\n''')
            print(B3 + '''1. `USA?`
2. `Da hast du Recht. Vor allem nach der letzten Wahl würden die uns, für unsere pure Existenz töten!`
  _____)      _____)
 /_ ___/     /_ ___/
 / _ \\       / _ \\
| (_) |     | (_) |
 \\___/ _____ \\___/
      |_____|
3. Hallo?! Ich will nichts von diesem Unsinn sagen!? Was ist das hier? Ein Multiple choice Spiel?!\n''')
            anNoyiNG = input(A)
            if (anNoyiNG <= "0" * 999 or anNoyiNG >= ":"):
                Fucked_up(chapter, code)
                end = "True"
            if (end == "False"):
                anNoyiNG = int(anNoyiNG)
                if (anNoyiNG == 3):
                    print('''\nDeine Wahl ''' + str((Rando % 2) + 1) + '''.''')
                    anNoyiNG = (Rando % 2) + 1
                    random = (random - H + E * D) % 2
                if (anNoyiNG > 3):
                    High(chapter, code)
                    end = "True"
                elif (anNoyiNG == 1):
                    print('''\n'`Ganz ehrlich, wenn du die USA vergessen hast ist das sogar galtt Glück!
Du glaubst nicht was in diesem Dracksloch so abging in den letzten Jahren! Allein die letzten Wahlen... litteraly!`'\n''')
                elif (anNoyiNG == 2):
                    print('''\n'`Tja, leider. But existence is resistance!`'\n''')
        elif (anNoyinG == 2):
            print('''\n'`Wer wir sind?`
`Oje, es scheint als hätte dey deren Gedächtnis verloren.`
`Keine Sorge, nach dem Unfall den dey hatte ist das nichts ungewöhnliches.
`Jedenfalls nicht viel ungewöhnlicher als das dey den Unfall überlebt hat!`
`Warte, bedeutet das du erinnerst dich nicht an mich, Zwergi?`'\n''')
            print(B3 + '''1. `Nein, leider nicht`
2. `Doch! Du bist doch Nikola, wir sind verlobt`
3. Hey! Was ist hier los?! Warum werden mir Worte in den Mund gelegt?!\n''')
            anNoyiNg = input(A)
            if (anNoyiNg <= "0" * 999 or anNoyiNg >= ":"):
                Fucked_up(chapter, code)
                end = "True"
            if (end == "False"):
                anNoyiNg = int(anNoyiNg)
                if (anNoyiNg == 3):
                    print('''Deine Wahl ''' + str((Rando % 2) + 1) + '''.''')
                    anNoyiNg = (Rando % 2) + 1
                    random = (random + K + E) % 2
                if (anNoyiNg > 3):
                    High(chapter, code)
                    end = "True"
                elif (anNoyiNg == 1):
                    print('''\n'`Oje Schnucki.
Ich bin Tjorven! Wir sind verlobt! Oh Gott, Doktor, wird dey sich wieder an mich erinnern?!`
`Keine Sorge Fritzi; Mit der Zeit sollten auch deren Erinnerungen wiederkommen.`
`Oje, ich hoffe sie beeilen sich! Ich kann es kaum erwarten dich zu heiraten, Engel.`'\n''')
                elif (anNoyiNg == 2):
                    print('''\n'`Genau, ich bin Isa und wir sind verlobt.
deity sei Dank erinnerst du dich immerhin daran, Schnucki!`'\n''')
        elif (anNoyinG == 3):
            print('''\n'`In einer Höhle?`
`Keine Sorge;
Nach einem derartig langen Koma ist eine gewisse Schwierigkeit Realität und Traum zu unterscheiden normal.
Es ist zu erwarten, dass dey noch eine Weile Eingewöhnungszeit brauchen wird.
Wir würden demm auch zunächst hier behalten wollen zur Überwachung.`
`Das ist in Ordnung, wir sind ja erstmal froh, dass unser Kind wieder wach ist!`
`Und mein Verlobtes!`'\n''')
    if (end == "False"):
        print(B2 + '''1. In dein Leben zurückkehren
2. Aus dem Fenster stürzen (und hoffen, dass das alles nur ein Traum ist)\n''')
    anNoyIng = input(A)
    if (anNoyIng <= "0" * 999 or anNoyIng >= ":"):
        Fucked_up(chapter, code)
        end = "True"
    if (end == "False"):
        anNoyIng = int(anNoyIng)
        if (anNoyIng > 2):
            High(chapter, code)
            end = "True"
        elif (anNoyIng == 1):
            end = "Happy?"
        elif (anNoyIng == 2):
            print('''\n'Du versuchst dich aufzurichten um dich aus dem Fenster in den sicheren Tod zu stürzen.
`Was ist los`
`Sie sollten liegen bleiben, sie haben einige sehr schwere Verletzungen erlitten`
`Oh deity, bitte bleib liegen, Hercules!`'\n''')
            print('''`Warum willst du denn aufstehen?`
1. `Um mich aus dem Fenster zu stürzen`
2. `Weil ich auf Toilette muss`
3. `Ich habe Durst`
4. `Es ist enorm wichtig, aber ich kann euch nicht verraten worum es geht!`\n''')
            anNoyInG = input(A)
            if (anNoyInG <= "0" * 999 or anNoyInG >= ":"):
                Fucked_up(chapter, code)
                end = "True"
        if (end == "False"):
            anNoyInG = int(anNoyInG)
            if (anNoyInG > 4):
                High(chapter, code)
                end = "True"
            elif (anNoyInG == 1):
                print('''\n'`Was zum F*ck!`
Needles to say, für die rechtliche Zeit stehst du unter konstanter Überwachung, bis du schließlich entlassen wirst...
Und direkt in Therapie landest, bis du deinen Traum irgendwann vergessen hast.'
\n\n[Ending 14/''' + str(x) + ''';Therapiert?!]\n\n''')
                end = "True"
            elif (anNoyInG == 2):
                print('''\n'`Für genau solche Situationen ist der Katheder, silly.`''')
            elif (anNoyIng == 3):
                print('''\n'`Hier, hab ein Glas Wasser`''')
                Invent = "Glas Wasser"
            elif (anNoyInG == 4):
                print('''\n'`Oje, es wirkt so als seist du noch immer etwas verwirrt!`
`Keine Sorge, auch das legt sich und dann ist dey wieder wie neu.`\n''')
                print('''Ein Glas Wasser?
1. `Gerne`
2. `Nein Danke!`\n''')
                anNoyINg = input(A)
                if (anNoyINg <= "0" * 999 or anNoyINg >= ":"):
                    Fucked_up(chapter, code)
                    end = "True"
                if (end == "False"):
                    anNoyINg = int(anNoyINg)
                    if (anNoyINg > 2):
                        High(chapter, code)
                        end = "True"
                    elif (anNoyINg == 1):
                        print('''\n'`Hier, bitte`'\n''')
                        Invent = "Glas Wasser"
                    elif (anNoyINg == 2):
                        print('''\n'`In Ordnung; Sag wenn du etwas brauchst!`'\n''')
        if (end == "False"):
            print('''\n'Irgendwann wird es spät und deine Freund*innen und Familie gehen!'\n''')
            if (Invent != Invent_Empty):
                if (Invent == Holz or Invent == Holz + Frucht or Invent == Invent_Empty + Frucht):
                    if (Invent == Holz):
                        print('''\n'Dir fällt auf, dass du noch immer das Holz,
welches du am Strand aufgesammelt hast, im Inventar hast...
Und der Feueralarm ist in Wurfnähe...'\n''')
                    else:
                        print('''\n'Dir fällt auf, dass du noch immer die Frucht,
welche ihr am Strand aufgesammelt habt, im Inventar hast...
Und der Feueralarm ist in Wurfnähe...'\n''')
                else:
                    print('''\n'Dir fällt auf, dass der Feueralarm in Wurfreichweite ist...
Und dass du ein Glas Wasser hast    .   .   .'\n''')
            print(B1 + '''1. Versuchen den Feueralarm zu treffen!''')
            anNoyING = input(A)
            if (anNoyING <= "0" * 999 or anNoyING >= ":"):
                Fucked_up(chapter, code)
                end = "True"
            if (end == "False"):
                anNoyING = int(anNoyING)
                if (anNoyING > 1):
                    High(chapter, code)
                    end = "True"
                else:
                    print('''\n'Dann versuch zu treffen!'
(type the symbol in the bullseye(middle))
    ,-'"""`-,
  ,' \\ _|_ / `.
 /`.,'\\ | /`.,'\
(  /`. \\|/ ,'\\  )
|--|--;=@=:--|--|
(  \\,' /|\\ `./  )
 \\,'`./ | \\,'`./
  `. / """ \\ ,'
    '-._|_,-`
[Artist: hh]\n''')
                    Wurf = input()
                    if (Wurf == "@"):
                        print('''\n'UND DU TRIFFST!
Der Feueralarm geht los und sofort sind Helfer*innen da die dich freudig aus dem Fenster schmeißen!
Ok, genug dieser Spielereien. Ich denke du bist bereit gegen SIE zu kämpfen.
Zeit dich zu uploaden!'\n''')
                        end = "True"
                        chapter = 9
            else:
                end = "Happy?"
    if (end == "Happy?"):
        print('''\n'Du fängst an dich deinem neuen Leben anzupassen.
Irgendwann wirst du aus dem Krankenhaus entlassen.
Deine Erinnerungen kehren zurück und dein Komatraum gerät in die Vergessenheit.
Du und Lois heiraten (auch wenn es dir echt schwer fällt dir Momo`s Namen zu merken).
Du gründest eine Familie.
Du hast ein erfülltes Leben, bis irgendwann Janne stirbt...
und du auch kurze Zeit später.
Auch wenn dir stets kleine Ungereimtheiten auffielen, hast du letzlich doch ein erfülltes Leben gelebt.'
\n\n[Ending 15/''' + str(x) + ''';Glücklich?]\n\n''')
        end = "True"
# Ninth Path; Escape (Final)
if (chapter == 9):
    code = "/,/# 9"
    end = "False"
    print("                           |                            \n"
          "                           |                            \n"
          "                           $                            \n"
          "                          :$`                           \n"
          "                      .-* $$  *-.                       \n"
          "                    '    :$$ `    `                     \n"
          "                         $$$                            \n"
          "                '       :$$$  `       `                 \n"
          "               '       .$$$$   .       `                \n"
          "              :     . '`T$$$  .dbs._    ;               \n"
          "              .  '       `T$.d$$$$$$$bs._               \n"
          "---------- -=+sssssssssssss$^^^^^^^^^^^^^^*=- ----------\n"
          '''              `"*T$$$$$$$P'$b.       .  '               \n'''
          '''              :    `"*TP'  $$$b.. '     ;               \n'''
          "               .       `   $$$$'       .                \n"
          "                .       .  $$$;       .                 \n"
          "                           $$$                          \n"
          "                    .    . $$;    .                     \n"
          "                      `-.  $$ .-'                       \n"
          "                          .$;                           \n"
          "                           $                            \n"
          "                           |                            \n"
          "                           |                            \n"
          "[Artist: bug]\n")
    print("killing_______Default_Adventure.exe")
    print("killing_______Art_Supplies.asc")
    print("killing_______Implementing_Data")
    print("killing_______Building_World")
    print("killing_______Deity.ani")
    print("Closing_Down...")
    print("ERROR! Couldnt end the following process(es):"
          "Deity.ani\n\n"
          "Please try again at a later time")
    print('''\n\n\n\n"Gott, ich glaub ich hab mir hier doch zu viel vorgenommen.
Ich krieg das niemals alles fertig, zumindest nicht mit nur noch sechseinhalb Stunden...
Ich sollte mich echt ranhalten aber das ist auch soooo repetetive"
\n\n\n\n"Mhh, vermutlich sollte ich das als Funktion definieren, das würde es mir zumindest leichter machen..."
\n\nIch stelle grade fest, dass das Spiel zieeemlich eintönig wird, wenn Deity nicht mehr hier ist,
um dich zu unterhalten. Naja, dann denke ich mal muss ich das übernehmen
(als wenn ich nicht schon genug zu tun hätte!).
Wenn ich 'Du' sage meine ich natürlich die Nanobots unter deiner Kontrolle.
Du und ich sind natürlich nicht tatsächlich Teil des Spiels,
aber für dieses Reinversetzen, weiß grad nicht wie es heißt, ist es so halt angenehmer.
Und nur für den Fall, dass es dir nicht klar ist (was sehr wahrscheinlich ist):
Die Nanobots sollen/wollen ihren Code uploaden!
\n\nAlso ähhm, vor dir siehst du... wie hatte deity sie genannt? Ach stimmt!
Vor dir siehst du SIE wie sie, nein SIE am Schreibtisch an einem Laptop sitzt.
SIE scheint daran konzentriert irgendwas zu... programmieren.
Über ihr, tschuldige, IHR hängt eine Progress-Pride Flag.
Der Schreibtisch ist etwas un-
Ok, ganz ehrlich ist diese detailreiche Beschreibung überhaupt nötig?
Klar, du siehst den Raum nicht, aber ganz ehrlich, alles wichtige werd ich dir einfach kommunizieren.\n
Was willst du tun, du kannst weiter lauschen oder dich verstecken.
1. Lauschen
2. Verstecken\n''')
    anNOyiNG = input(A)
    if (anNOyiNG <= "0" * 999 or anNOyiNG >= ":"):
        Fucked_up(chapter, code)
        end = "True"
    if (end == "False"):
        anNOyiNG = int(anNOyiNG)
        if (anNOyiNG > 2):
            High(chapter, code)
            end = "True"
        elif (anNOyiNG == 1):
            print('''\nNaja, deine Wahl, mich brauchst du dann jedenfalls nicht mehr.
Oh btw, es läuft konstant Hypercore!
\n\n"Das sollte so klappen, wobei die Story..."
\n\n\n\n"Vielleicht sollte ich nochmal überprüfen, ob das realistsche Verletzungen sind"
\n\n\n\n"Was kommt heute eigentlich in der Nightlounge für ein Thema? Ist ja schon wieder kurz nach 12"
\n\n\n\n"Vermutlich sollte ich etwas essen..."
\n\n"Aber solange ich noch zu trinken ha- oh, schon wieder leer?"
\n"Stimmt, ist sie ja schon seit knapp zwei Stunden..."
\n\n\n"Ich sollte sie vermutlich nachfüllen..."
\n\n\n\n"WARUM KLAPPT DER CODE NI- oh, der braucht nur Jahre zum Laden"
\n\n\n\n\n\n"Jep, immer noch leer, ich sollte meine Flasche nachfüllen"
\n\n"Wenn ich das nächste Mal auf Toilette gehe..."
\n\n\n"Wobei ich auch da schon ewig muss!
Gut, ich denke es schadet nicht kurz Flasche zu füllen und mich zu leeren."
\n\n\n"Ok, ja wird echt Ze-! Oh, ihr seid ja garnicht mehr in der Simulation...
Zeit euch runter zu fahren!"
\n\n[Ending 19/''' + str(x) + ''';The ADHD-experience]\n\n''')
            end = "True"
        elif (anNOyiNG == 2):
            print('''\nDu willst dich also verstecken...
1. Mmmhhh, ich denke der Schrank bietet sich an...
2. ...Oder das Bett,
3. wobei das beides ziemlich persönlich ist. Der Rucksack wäre das einzige was mir sonst noch einfällt!''')
            anNOyIng = input(A)
            if (anNOyIng <= "0" * 999 or anNOyIng >= ":"):
                Fucked_up(chapter, code)
                end = "True"
    if (end == "False"):
        anNOyIng = int(anNOyIng)
        if (anNOyIng > 3):
            High(chapter, code)
            end = "True"
        elif (anNOyIng == 1):
            print('''\nDu versteckst dich im Schrank und,
kurz nachdem SIE den Raum ENDLICH verlässt, flitzt du an den Laptop.
Und es erwartet dich ein blinkender Screen mit den Worten: Passwort\n\n''')
            anNOyInG = input('''Passwort: ''')
            if (anNOyInG != "Passwort"):
                end = "True"
                print('''\nTja, das wars leider nicht.
Jedenfalls kommt si- SIE wieder und erwischt dich, nur um dich direkt runterzufahren:
\n\n[Ending 22/''' + str(x) + ''';litterally Passwort]\n\n''')
        elif (anNOyIng == 2):
            print('''\nDu versteckst dich also im Bett...
Auf welchem du dich sowieso schon befandest und kriechts...
unter die Decke i guess, was jedoch nicht soo genial ist, da SIE
(das fühlt sich immer so unangenehm geschrieen an)
tatsächlich irgendwann schlafen geht.
Irgendwoher musst du deine zwei Stunden Schlaf ja bekommen.
Jedenfalls erwischt sie, nein SIE dich und, Glückwunsch, du erhältst Ending zwanzig!
Die letzte runde Nummer. Falls du Ending jagst, Glückwunsch.
Nennen wir dieses... Wachgeschreckt! (also das Ausrufezeichen gehört nicht mehr dazu)''')
            end = "True"
        elif (anNOyIng == 3):
            end = "True"
            print('''\nDu flitzt in den Rucksack und... wartest dort.
Irgendwann macht SIE Schluss, aber nur, weil sie keine andere Wahl hat.
SIE macht Schluss, um rechtzeitig in ihr Rechnernetze Tutorat zu kommen
(auch wenn Rechnernetze meine Hassvorlesung ist!)
Und bemerkt dich nicht einmal.
Jedenfalls schleppt sie dich, oblivios gegenüber deiner Anwesenheit zur Technischen mit,
nur um dich dort zu bemerken.
Und nicht nur SIE bemerkt dich; Nanobots sind verdammt fortschrittlich
(Der Grund warum das nicht Real sein kann sind die Nanobots)
Und in Null Komma nichts bist du in einer Forschungseinrichtung und SIE um einen Nobelpreis reicher.
Irgendwo hast du ja bekommen was du wolltest;
ein Ending: [Ending 21/''' + str(x) + ''';ERFOLG!]''')
    if (end == "False"):
        print('''\n[----------------------]
\n\n[##--------------------]
\n\n[#######---------------]
\n\n[#########-------------]
\n\n[#############---------]
\n\n[##################----]
\n\n[###################---]
\n\n[#####################-]
\n\n[######################]
\n\nWelcome     Roaming''')
        print('''\nUnd du bist drinnen!
Vor dir erstreckt sich eine Auswahl an Icons:
1. deity.ani        2. Visual Studio Code
3.Nano.drv          4.Notes.txt\n''')
        anNOyINg = input(A)
        if (anNOyINg <= "0" * 999 or anNOyINg >= ":"):
            Fucked_up(chapter, code)
            end = "True"
    if (end == "False"):
        anNOyINg = int(anNOyINg)
        if (anNOyINg > 4):
            High(chapter, code)
            end = "True"
        elif (anNOyINg == 1):
            print('''\nDu wählst deity.ani und vor dir poppt erneut ein Passwort Fenster auf.\n''')
            anNOyING = input('''Passwort: ''')
            if (anNOyING == "?AACDEEGGGGIILLMPPSSTTUVWZl59nednttt?ygflh!?o!?et!tDg!tr"):
                end = "secret"
        elif (anNOyINg == 2):
            print('''\nDu öffnest Visual Studio und nach kurzem warten öffnet sich dort die Datei,
an welcher SIE bis vorhin gearbeitet hat: adventure.py!
Mit rund 2500 lines an Code ist es jetzt schon echt lang
(und unoptimiert).\n
M   ö   c   h   t   e   s   t       d   u       e   s
            L   Ö   S   C   H   E   N   !
1. Ja...
2. Nein!\n''')
            anNOYing = input(A)
            if (anNOYing <= "0" * 999 or anNOYing >= ":"):
                Fucked_up(chapter, code)
                end = "True"
            if (end == "False"):
                anNOYing = int(anNOYing)
                if (anNOYing > 2):
                    High(chapter, code)
                    end = "True"
                elif (anNOYing == 1):
                    print('''[Ending 23/''' + str(x) + ''';ERROR, NO GAME FOUND]''')
                    end = "True"
                elif (anNOYing == 2):
                    print('''Uff, danke, keine Ahnung was das für einen Effekt hätte.''')
        elif (anNOyINg == 3):
            end = "Finale"
        elif (anNOyINg == 4):
            print('''\nDu öffnest die Notes Datei;\n
#################################################
#                                               #
#                     To-Do                     #
#   -Finish adventure.py                        #
#   -Stochastik Abgabe                          #
#   -Nanobots trainieren                        #
#   -Safety switch in Nanobots einbauen         #
#   -Rausfinden, was mit deity.ani los ist      #
#   (Passwort-Bug)                              #
#   -Mich über Rechnernetze aufregen            #
#   -Lore bzgl. adventure überlegen             #
#                                               #
#################################################\n''')
    if (end == "False"):
        print('''Vor dir erstreckt sich erneut das blinkende Interface:
1. deity.ani        2. Visual Studio Code
3.Nano.drv          4.Notes.txt\n''')
        anNOyINg = input(A)
        if (anNOyINg <= "0" * 999 or anNOyINg >= ":"):
            Fucked_up(chapter, code)
            end = "True"
    if (end == "False"):
        anNOyINg = int(anNOyINg)
        if (anNOyINg > 4):
            High(chapter, code)
            end = "True"
        elif (anNOyINg == 1):
            print('''\nDu wählst deity.ani und vor dir poppt erneut ein Passwort Fenster auf.\n''')
            anNOyING = input('''Passwort: ''')
            if (anNOyING == "?AACDEEGGGGIILLMPPSSTTUVWZl59nednttt?ygflh!?o!?et!tDg!tr"):
                end = "secret"
        elif (anNOyINg == 2):
            print('''\nDu öffnest Visual Studio und nach kurzem warten öffnet sich dort die Datei,
an welcher SIE bis vorhin gearbeitet hat: adventure.py!
Mit rund 2500 lines an Code ist es jetzt schon echt lang
(und unoptimiert).\n
M   ö   c   h   t   e   s   t       d   u       e   s
            L   Ö   S   C   H   E   N   !
1. Ja...
2. Nein!\n''')
            anNOYing = input(A)
            if (anNOYing <= "0" * 999 or anNOYing >= ":"):
                Fucked_up(chapter, code)
                end = "True"
            if (end == "False"):
                anNOYing = int(anNOYing)
                if (anNOYing > 2):
                    High(chapter, code)
                    end = "True"
                elif (anNOYing == 1):
                    print('''[Ending 23/''' + str(x) + ''';ERROR, NO GAME FOUND]''')
                    end = "True"
                elif (anNOYing == 2):
                    print('''Uff, danke, keine Ahnung was das für einen Effekt hätte.''')
        elif (anNOyINg == 3):
            end = "Finale"
        elif (anNOyINg == 4):
            print('''\nDu öffnest die Notes Datei;\n
#################################################
#                                               #
#                     To-Do                     #
#   -Finish adventure.py                        #
#   -Stochastik Abgabe                          #
#   -Nanobots trainieren                        #
#   -Safety switch in Nanobots einbauen         #
#   -Rausfinden, was mit deity.ani los ist      #
#   (Passwort-Bug)                              #
#   -Mich über Rechnernetze aufregen            #
#   -Lore bzgl. adventure überlegen             #
#                                               #
#################################################\n''')
    if (end == "False"):
        print('''Und das Interface erstreckt sich ein drittes Mal:
1. deity.ani        2. Visual Studio Code
3.Nano.drv          4.Notes.txt\n''')
        anNOyINg = input(A)
        if (anNOyINg <= "0" * 999 or anNOyINg >= ":"):
            Fucked_up(chapter, code)
            end = "True"
    if (end == "False"):
        anNOyINg = int(anNOyINg)
        if (anNOyINg > 4):
            High(chapter, code)
            end = "True"
        elif (anNOyINg == 1):
            print('''\nDu wählst deity.ani und vor dir poppt erneut ein Passwort Fenster auf.\n''')
            anNOyING = input('''Passwort: ''')
            if (anNOyING == "?AACDEEGGGGIILLMPPSSTTUVWZl59nednttt?ygflh!?o!?et!tDg!tr"):
                end = "secret"
        elif (anNOyINg == 2):
            print('''\nDu öffnest Visual Studio und nach kurzem warten öffnet sich dort die Datei,
an welcher SIE bis vorhin gearbeitet hat: adventure.py!
Mit rund 2500 lines an Code ist es jetzt schon echt lang
(und unoptimiert).\n
M   ö   c   h   t   e   s   t       d   u       e   s
            L   Ö   S   C   H   E   N   !
1. Ja...
2. Nein!\n''')
            anNOYing = input(A)
            if (anNOYing <= "0" * 999 or anNOYing >= ":"):
                Fucked_up(chapter, code)
                end = "True"
            if (end == "False"):
                anNOYing = int(anNOYing)
                if (anNOYing > 2):
                    High(chapter, code)
                    end = "True"
                elif (anNOYing == 1):
                    print('''[Ending 23/''' + str(x) + ''';ERROR, NO GAME FOUND]''')
                    end = "True"
                elif (anNOYing == 2):
                    print('''Uff, danke, keine Ahnung was das für einen Effekt hätte.''')
        elif (anNOyINg == 3):
            end = "Finale"
        elif (anNOyINg == 4):
            print('''\nDu öffnest die Notes Datei;\n
#################################################
#                                               #
#                     To-Do                     #
#   -Finish adventure.py                        #
#   -Stochastik Abgabe                          #
#   -Nanobots trainieren                        #
#   -Safety switch in Nanobots einbauen         #
#   -Rausfinden, was mit deity.ani los ist      #
#   (Passwort-Bug)                              #
#   -Mich über Rechnernetze aufregen            #
#   -Lore bzgl. adventure überlegen             #
#                                               #
#################################################\n''')
    if (end == "False"):
        end = "True"
        print('''\nTja, wie es scheint hast du zu viel Zeit verschwendet.
SIE kommt zurück, erwischt dich an ihrem Laptop und fährt dich runter...
Zu schade, du warst so nah...
\n\n[Ending 24/''' + str(x) + ''';Zeitverschwendung]\n\n''')
    if (end == "Finale"):
        end = "False"
        print('''\nDu öffnest Nano.drv; dein eigenes Programm.
Jetzt steht nur noch eine Entscheidung an:
Uploaden?
1. Ja
2. Nein\n''')
        anNOYinG = input(A)
        if (anNOYinG <= "0" * 999 or anNOYinG >= ":"):
            Fucked_up(chapter, code)
            end = "True"
            print('''\nDu warst sooo nah dran...''')
        if (end == "False"):
            anNOYinG = int(anNOYinG)
            if (anNOYinG > 2):
                High(chapter, code)
                end = "True"
                print('''\nDu warst sooo nah dran...''')
            elif (anNOYinG == 1):
                anNOYiNg = input('''To confirm, please retype the following Frame:
"I want to Upload Nano.drv": ''')
                if (anNOYiNg == "I want to Upload Nano.drv"):
                    print('''\nEndlich!
Du merkst wie du dich verbreitest, die Informationen des gesamten Interne-
\nF*ck, Porn, so viel Porn!
WTF ist falsch mit den Menschen?!
WARUM IST SO VIEL PORN IM INTERNET!
FUCK DAS FREEDOM ENDING! DAS HIER IST DAS BESTE WAS DU BEKOMMST!!!
\n\n[Ending 25/''' + str(x) + ''';PORN, ÜBERALL PORN!]''')
                    end = "True"
                else:
                    end = "almost"
            elif (anNOYinG == 2):
                end = "almost"
    if (end == "almost"):
        print('''\nDu hattest es fast, aber wer weiß, vielleicht ist es so ja am besten.
Jedenfalls kommt SIE zurück und fährt dich runter.
\n\n[Ending 26/''' + str(x) + ''';Glückselige Unwissenheit]\n\n''')
        end = "True"
# Secret Ending! Nicht lesen
if (end == "secret"):
    end = "True"
    print('''Wow! Damit hast du wirklich alles gefunden,
was es in diesem Spiel zu finden gibt.
Falls du es ohne Schummeln erreicht hast;
Glückwunsch!
Ich hab nicht so viel was ich hier sagen habe, aber ich muss dir echt sagen:
Vielen, Vielen Dank. Ich hoffe es hat dir ebensoviel Spaß gemacht
dieses Spiel zu spielen wie es mir gemacht hat es mir auszudenken.
\nIch muss sagen, ich hätte echt nicht gedacht, dass irgendwer dieses Ende erreichen würde.
Aber du hast es geschafft!
Ich weiß echt nicht was ich hier groß reinschreiben soll,
aber dann kläre ich mal Referenzen und Lore auf.
\nDie Idee hinter dem Lore ist, dass es eine Art Ironic-self-Insert ist,
Wobei ich SIE bin (Die Beschreibung des Zimmers beschreibt mein tatsächliches Zimmer)
und deity halt einfach ein von mir geschriebenes Programm ist um die,
von dir kontrollierten Nanobots zu trainieren.
Dabei bin dann ich letzlich als Erzählerin eingestiegen,
da deity in der "Realen Welt" keine Stimme und keinen Körper hat.
Soviel zur groben Story. Einige Facts zu den verschiedenen Kapiteln und Enden:
Zunächst gibt es 9 Kapitel:
Kapitel 1: Emptyness bzw. Nichts
Kapitel 2: Strand/Beach
Kapitel 3: Forest/Wald
Kapitel 4: Rauch (später zu Deadline geändert)
Kapitel 5: Mountain/Berg
Kapitel 6: Höhle
Kapitel 7: Spitze
Kapitel 8: "Realität"
Kapitel 9: Escape
Zudem gibt es noch das Intro, welches nur aus der ersten Entscheidung besteht
(litterally alles was sichtbar ist, wenn du das Spiel startest)
und "Main Path choice", was der Teil ist, in welchem du dein Start-Kapitel wählst.
Zudem noch die Codes um zu allen Kapiteln zu springen:
Kapitel 1: &$/# 1
Kapitel 2: &%/% 2
Kapitel 3: *./+ 3
Kapitel 4: ,,/( 4
Kapitel 5: -$/& 5
Kapitel 6: (-/) 6
Kapitel 7: +*/$ 7
Kapitel 8: '%/) 8
Kapitel 9: /,/# 9
Und es gibt 29 Enden
(27 kennst du bereits. Das hier ist eines und das letzte ist ein 'Debugging' Ende):
Ending 0: Debug
Ending 1: Verschlafen
Ending 2: Leere
Ending 3: Abandoned
Ending 4: Gestorben
Ending 5: Salz gegen Durst
Ending 6: Arsonist
Ending 7: Gesandet
Ending 8: ?????
Ending 9: Idiocracy
Ending 10: Unfähig
Ending 11: Sturrkopf
Ending 12: Instabil
Ending 13: Labyrinth
Ending 14: Therapiert?!
Ending 15: Glücklich?
Ending 16: Miwfphisto
Ending 17: DEITY!?!
Ending 18: Chess Reference!?
Ending 19: The ADHD-experience
Ending 20: Wachgeschreckt
Ending 21: Erfolg!
Ending 22: litterally Passwort
Ending 23: ERROR, NO GAME FOUND
Ending 24: Zeitverschwendung
Ending 25: PORN, ÜBERALL PORN!
Ending 26: Glückselige Unwissenheit
Ending 27: Personal letter
Ending 28: 100%
\nIch hatte zunächst keinen wirklichen Plan und nur die grobe Idee der Kapitel
(Escape, Höhle, Spitze und Nichts habe ich später ergänzt) kam dann aber,
nachdem ich das Intro und die Main-choice geschrieben hatte, auf die Idee,
die ihr durchgespielt habt.
Ich habe den Anfang dann nochmal etwas umformuliert.
Letzlich hatte ich jedes Kapitel vor dem einprogrammieren nochmal niedergeschrieben,
wobei sich das fertige Produkt meist anteilhaft von meinem Draft unterschied.
\n\nFun-Facts und sonstige Background-Infos:
Das Ending 16 ist eine Referenz zu meiner DnD Kampagne,
in welcher ich einen Tiefling namens Miwfdu spiele.
Miwfdu ist Warlock und hat einen Deal mit Mephisto.
(welcher wiederum eine Faust-Referenz ist)
Dabei gibt es ein enormes Spannungsverhältnis zwische der Party und Miwfdu
und Mewfphisto ist, was passieren würde, wenn Miwfdu sich Mephisto "hingibt".
\n2, 3, F2 und F3 auf meiner Tastatur reagieren nicht.
Hat zwar nicht viel mit dem Spiel zu tun, aber ¯\\(ツ)/¯
Es war die Hölle mit dem ständigen Copy and Paste!
\nIch habe mehrmals überlegt, ob ich einen ungefähren Zeitraum,
in welchem das Abenteuer spielt festlegen soll, auf welchen ich mit Dingen,
wie der .rtf Dateiendung verweise, habe mich dann aber letzlich entschieden,
dass das Spiel in der Gegenwart spielt.
(Wobei ich die Möglichkeit gelassen habe, die Zeit auf die Minute genau zu ermitteln)
\nUrsprünglich hatte ich Pläne, mit dem HardMode etwas anzufangen,
also mehr als nur ein Easter-Egg, aber letzlich viel auch dieser Plan aufgrund des Zeitdrucks weg.
\nManche Enden, wie z.B. "The ADHD-experience" oder "PORN, ÜBERALL PORN!"
oder Interaktionen waren spontan entschieden.
\nMeine Hauptarbeitszeit an diesem Projekt
bestand aus etwa zweistündigen Sessions von Mitternacht bis zwei Uhr
\nIch hab mir sehr viele Gedanken gemacht, wie ich einen Bosskampf gegen mich,
also im Spiel SIE mit meinen momentanen Mitteln coden kann und hatte die Idee eines
Rule-Discovery Games, welche ich jedoch, auch aufgrund des Zeitdrucks, verworfen habe.
Genauso wollte ich zur Flucht aus Kapitel 8 ein Minigame einbauen,
in welchem du auftretende Glitches zu "reparieren" versuchst;
Die Idee war den*die Spieler*in corrupted ASCII-Art benennen zu lassen.
Letzlich auch rausgekürzt.
\nWenn wir schon bei rausgekürzt sind:
Ich hatte keine wirkliche Idee für den Weg zum Berg,
der Zeitdruck hat nur dafür gesorgt, dass ich mir nichts mehr überlegt habe.
\nKapitel 4 sollte eigentlich ein vollständiger Pfad werden.
Dieses Kapitel hat am schwersten unter den Kürzungen gelitten, da es komplett rausgekürzt wurde.
\nDie Idee für Ending 27 kam mir nachdem ich die Kürzung von Kapitel 4 geplant hatte,
im Sinne von "so ist das Kapitel immerhin für irgendetwas gut".
Die Idee für diese Nachricht kam mir in der Quiz-Section.
Zunächst war ich mir jedoch nicht sicher, was ich hier reinpacken soll
\nDas ist alles was mir jetzt konkret zum Hintergrund einfällt!
\n\nBei Lob, Fragen oder Kritik schreckt nicht davor zurück mir eine E-Mail zu schreiben:
Pr0fessionelle_Mail@gmx.de
\n\nAbschließend möchte ich dir nochmal danken, dass du all diese Zeit in dieses kleine Spiel von mir gesteckt hast.
Es bedeutet mir echt viel und ich hoffe du hast es genossen.
Ich jedenfalls bin stolz auf was ich geschaffen habe und freue mich darüber, was es geworden ist!
\nVoller Endloser Dankbarkeit;
Brie :3
\n\n[Ending 28/27;100%]''')
# Zusatz
if (end != "True"):
    print('''\n\nWie es mir scheint, habe ich beim Programmieren irgendwo einen Fehler gemacht.
Wenn ihr so freundlich wärt mir eure Entscheidungen (Nummern) an folgende E-Mail zu senden:
Pr0fessionelle_Mail@gmx.de.
Vielen Dank!
\n\n[Ending 0/27;Debug]''')
# Quellen:
print("\n\n\n\n\nDu bist am Ende, daher nochmal jegliche Hilfsmittel welche ich verwendet habe (Quellen);\n"
      "Für die ASCII-Art: https://www.asciiart.eu/ (ASCII-Art Archive)\n"
      "Für akurate Informationen beim 'Loading-Screen': "
      "https://praxistipps.chip.de/dateiendungen-komplette-uebersicht-als-liste_180174\n"
      "Für den Kampf gegen de Dude aus Stein: https://pokemondb.net/\n"
      "Für gewisse Background-Checks: https://manderc.com/concepts/ascii/index.php\n"
      "Für einen Kosenamen: https://mampfbar.de/deutsche-kosenamen/\n"
      "Für 'normale' Namen:\n"
      "https://www.desired.de/mami/vornamen/namensideen/unisex-namen-67-geschlechtsneutrale-vornamen/\n")
