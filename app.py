import random

from flask import Flask, render_template
app = Flask(__name__)


WADE_REWARDS = (
    "A tooth whitening. You choose the tooth.",
    "5 CARTONS OF CIGARETTES!!!\nthat have been submerged in a lake",
    "A core sample of someone's rectum. complete with display case.",
    "Free tickets to comic con, but you have to be a 32 year old brony's chaperone, and he calls all the shots.",
    "A really hot date. She won't call back.",
    "The complete works of Jimmy Buffet on burnt CD!",
    "Post it notes made from tanned hide. No adhesive. Just a lot of tiny squares of leather.",
    "Pair of pants that say racist comments while wearing them."
)


@app.route("/")
def hello():
    return render_template('index.html', reward=random.choice(WADE_REWARDS))


if __name__ == "__main__":
    app.run()
