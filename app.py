from flask import Flask, request
from umbrella import makeUmbrellaDecision
app = Flask(__name__)

# @app.route('/')
# def home():
#     return "HelloWorld"


# @app.route('/goodbye')
# def goodbye():
#     return "see ya"


# @app.route('/candy')
# def candy():
#     return "chocolates"


# @app.route('/')
# def home():
#     if makeUmbrellaDecision('new york', 'us'):
#         return 'Bring an umbrella'
#     else:
#         return 'No need for an umbrella'

# from flask import Flask, request
# from umbrella import makeUmbrellaDecision
# app = Flask(__name__)

@app.route('/')
def home():
    city = request.args.get('city')
    if city is None:
        city = 'new york'
    if makeUmbrellaDecision(city, 'us'):
        return 'Bring an umbrella in {city}'
    else:
        return 'No need for an umbrella in {city}'