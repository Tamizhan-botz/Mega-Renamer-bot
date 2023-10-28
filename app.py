#Thank you  for helping me in this journey !
#Must Subscribe On YouTube @Doremon_Botz 

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '@Doremon_Botz'


if __name__ == "__main__":
    app.run()
