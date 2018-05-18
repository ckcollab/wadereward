import random

from flask import Flask, render_template
app = Flask(__name__)


WADE_REWARDS = (
    "Jackyl Donson the wolf guy",
    "A tooth whitening. You choose the tooth.",
    "5 CARTONS OF CIGARETTES!!!\n...that have been submerged in a lake",
    "A lifetime supply of sippy-cups filled with apple juice. Never go thirsty again.",
    "A kick in the nuts so hard, you'll never have kids. Cheaper than a vasectomy!",
    "A whole colony of bees on leashes. Take them on a walk, or tie them to a post!",
    "A horse with broken legs! It's still a horse!",
    "$1000 in pennies buried somewhere in Antarctica.",
    "A years-worth of clams. Must supply own refrigeration.",
    "A rubber band snap from 100 naked women. Combined average attractiveness:\n4.75 / 10",
    "A swimming-pool FULL of everyone's favorite schoolyard game: Jacks.",
    "A one-way ticket to... NORTH KOREA!!!",
    "An exotic, all expense paid getaway to Detroit! 3 weeks in a motel with your choice of a daily TV dinner!",
    "Free room! Spacious 6 x 6 with no locks, no doors, and no windows.",
    "A trailer full of flat Lego pieces!",
    "A free cage! You pick what goes inside!",
    "Never vacuum again when you take home this Rumba bot covered in rusty, needle-sharp spikes. Does not turn off.",
    "A remarkable, one of a kind freezer truck filled with dead flies! Just imagine the frogs you could catch!",
    "A Razer Scooter, lifetime warranty.",
    "A whole pallet of phonebooks.",
    "A printer the size of a car! The cartridge is out of production, so print wisely!",
    "100 Puppies! All inflicted with rabies.",
    "A kite.",
    "A DIY motherboard.",
    "A tour of Loch Ness, in a rowboat. Tour ends when you take the blindfold off.",
    "All of the damaged goods from Bounty paper towels; once a month for six years.",
    "An exceptionally rare and poisonous snake hidden somewhere in your house!",
    "A thumbtack on every chair you will sit on, for eternity!",
    "A 40ft tower of chocolate pudding in death valley. Must claim in 50 days or suffer the consequences.",
    "FREE silverfish infestation!",
    "A triceratops promise. 3 horns or your money back.",
    "You are now the proud owner of a house fire! Congratulations on your fresh start!",
    "A personal squatting Serbian in a tracksuit. He will smoke all of your cigarettes for you.",
    "A 2 x 4 board that will always fall down, and always find its way into your garage.",
    "A lifetime supply of disappointment.",
    "A wheelbarrow full of earwax.",
    "A pair of pants that cause you to scream expletives and racist comments while wearing them.",
    "5 cartons of cigarettes, that have been dropped in a lake.",
    "A jar of peanut butter. Get a blowjob from your dog!",
    "A core sample of someone's rectum. Complete with display case.",
    "A really hot date. She won't call you back.",
    "Jimmy Buffet's complete discography, on burned CDs!",
    "Free all access pass to Comic Con, under the conditions that you are to accompany a 32 year old Brony, and he calls the shots.",
)


@app.route("/")
def hello():
    return render_template('index.html', reward=random.choice(WADE_REWARDS))


if __name__ == "__main__":
    app.run()
