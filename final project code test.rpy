define daylimit = 30
define floor = 4

label start():
    jump main4

label main4():
    menu:
        "it is now [day] on [floor]what will you do?"
        "search":
			call checkenergy()
            $ energy_point -= 10
            $ time = time + 5
            jump search4
        "camp":
            $ energy_point -= 15
            $ time = time + 10
            call checkenergy()
        "checkenergy":
            jump checkenergy
label search4():
            "you found a totem, a note, and a hat"
            menu:
                "totem"
                $ inventory.append("totem")
                jump puzzle4
                "note"
                $ inventory.append("a note")
                jump puzzle4
                "tophat"
                $ inventory.append("tophat")
                jump puzzle4
label puzzle4():
    menu:
        "insert item":
            $ actions = actions -1
            $ time = time +1
			call timechange():
            call inventory():
			   if totem jump puzzlecomplete
        "twist knob":
            $ actions = actions -1
            $ time = time +1
			call timechange()
        "press button":
            $ actions = actions -1
            $ time = time +1
			call timechange()
label main5():
    menu:
        "it is now [day] on [floor]what will you do?"
        "search":
            call checkenergy()
            $ energy_point -= 10
            $ time = time + 5
            jump search5
        "camp":
            call checkenergy()
            $ energy_point -= 15
            $ time = time + 10
        "checkenergy":
            jump checkenergy

label search5():
    "you found a totem, a note, and a hat"
    menu:
        ""
        $ inventory.append("")
        jump puzzle4
        "":
        $ inventory.append("")
        jump puzzle4
        "":
        $ inventory.append("")
        jump puzzle4
label puzzle5():
    menu:
        "turn wheel":
            $ actions = actions -1
            $ time = time +1
			call timechange()
        "press red button":
            $ actions = actions -1
            $ time = time +1
			call timechange()
			jump puzzlecomplete
        "press blue button":
            $ actions = actions -1
            $ time = time +1
			call timechange()
label inventory():
    items=["totem", "note", "tophat"]
    $ inventory.append()
	menu:
		"use totem" if ("totem" in inventory):
    
            $ inventory.remove ("totem")

label checkenergy():
    if actions <=0:
        "not enough energy to perform task."
        jump main
    else:
        return

label daychange():
    if day >= daylimit:
        jump fail
    $day++
    jump main
label timechange():
    if actions <= 0:
        jump checkenergy
    if time == 3:
        jump daychange
    else:
        jump main
label puzzlecomplete():
	"you have solved the puzzle you may proceed to the next floor!"
			$ time = time + 1
            $ floor = floor + 1
			call timechange()
            jump floorchange

label floorchange():
    if floor == 4:
        jump main4
    if floor == 5:
        jump main5
    if floor == 6:
        jump main6
