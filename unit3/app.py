from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def start():
    title = "The Haunted House"
    
    text = """It is a dark and cold night and the moon is full. You walk up to the haunted house.  
    As you approach the door, it creaks open and a chill runs down your spine!"""

    choices = [
        ('enter_house',"Go inside"),
        ('run_away',"Run away as fast as you can!!!")
    ]

    return render_template('adventure.html', title=title, text=text, choices=choices)



@app.route("/inside")
def enter_house():
    title = "You go inside..."
    
    text = """... and the door slams shut behind you!  And then -- absolute silence.  It is so quiet you can hear the 
    sound of your own heart beating.  A dusty wooden staircase leads up to the second floor.  Through a tangle of cobwebs
    you can see the faint, flickering light of a small candle."""

    choices = [
        ('up_stairs',"Go up the stairs"),
        ('run_away',"Try to escape out the front door")
    ]

    return render_template('adventure.html', title=title, text=text, choices=choices)

@app.route("/escape")
def run_away():
    title = "You run away!"
    
    text = """You bolt away from the house to safety.  You hear the sound of a sinister voice cackling madly behind you."""

    choices = []

    return render_template('adventure.html', title=title, text=text, choices=choices)

@app.route("/stairs")
def up_stairs():
    title = "Doors!"
    
    text = """As you climb up the stairs, you hear noises coming from downstairs.
    As you reach the top of stairs, you see two closed doors with smoke coming from one door."""

    choices = [
        ('open_door1',"Go inside the first door"),
        ('run_away',"Try to escape out the front door")
    ]

    return render_template('adventure.html', title=title, text=text, choices=choices)



@app.route("/door1")
def open_door1():
    title = "hell's kitchen!"
    
    text = """As you enter door one, you see flies taped to the walls and the back of the door, dead animals or coarpse floating in pools of water.
    two rats come out of the pool with screaching voices which gives you a scare. You run outside the first room and enter the second room by a mistake."""

    choices = [
        ('open_door2',"run outside and enter the second door"),
        ('run_away',"Try to escape out the front door")
    ]

    return render_template('adventure.html', title=title, text=text, choices=choices)

@app.route("/door2")
def open_door2():
    title = "Look out!"
    
    text = """As you enter the second door, you hear loud noises. You see a faceless doll and a clown doll holding a knife near the stairs laughing.
    Once inside the second door, spiders start dropping from everywhere. Spiders on the ground start coming toward you. you scream because of terror and that intimidates the spiders
    which eventually bite you."""

    choices = [
    ]

    return render_template('adventure.html', title=title, text=text, choices=choices)
