from flask import Flask, render_template, request, redirect, session # added request
import random
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

# our index route will handle rendering our form
@app.route('/')
def visits():
    if 'visits' in session:
        session['visits'] = session.get('visits') + 1  # reading and updating session data
    else:
        session['visits'] = 1 # setting session data
    # return "Total visits: {}".format(session.get('visits'))

    if session['visits'] == 1:
        print ('first visit')
        session['total_gold'] = 0

        # print ('not first visit')
        session['activities'] = []

    return render_template("index.html")

@app.route('/process_money', methods=['POST'])
def process_money():

# EVERY TIME YOU HIT SUMBMIT, YOU NEED TO CREATE A RANDOM INT TO SPECIFY
# IF YOU WIN OR LOSE
# EVERY TIME YOU HIT SUMBMIT, NEED TO CREATE RANDOM INT TO GENERATE POINTS EARNED


    session['win_lose'] = random.randint(0,1)
    session['random_points'] = random.randint(10,20)

    if request.form['places'] == 'farm':
        # print('activities: ' + session['activities'])
        # win_lose = random.randint(0,1)
        # random_points = random.randint(10,20)
        if session['win_lose']  == 0:
            session['total_gold'] -= session['random_points']
            activity = ('Entered a farm and lost ' + str(session['random_points']) + ' golds! Ouch!')
            # activity = '<p>Steven</p>'
            session['activities'].append(activity)
        else:
            session['total_gold'] += session['random_points']
            activity = ('Earned ' + str(session['random_points']) + ' golds from the farm!')
            # activity = '<p>Steven</p>'
            session['activities'].append(activity)

    elif request.form['places'] == 'cave':
        # win_lose = random.randint(0,1)
        # random_points = random.randint(5,10)
        if session['win_lose']  == 0:
            session['total_gold'] -= session['random_points']
            activity = ('Entered a cave and lost ' + str(session['random_points']) + ' golds! Ouch!')
            session['activities'].append(activity)
        else:
            session['total_gold'] += session['random_points']
            activity = ('Earned ' + str(session['random_points']) + ' golds from the cave!')
            session['activities'].append(activity)

    elif request.form['places'] == 'house':
        # win_lose = random.randint(0,1)
        # random_points = random.randint(2,5)
        if session['win_lose']  == 0:
            session['total_gold'] -= session['random_points']
            activity = ('Entered a house and lost ' + str(session['random_points']) + ' golds! Ouch!')
            session['activities'].append(activity)
        else:
            session['total_gold'] += session['random_points']
            activity = ('Earned ' + str(session['random_points']) + ' golds from the house!')
            session['activities'].append(activity)

    elif request.form['places'] == 'casino':
        # win_lose = random.randint(0,1)
        # random_points = random.randint(0,50)
        if session['win_lose']  == 0:
            session['total_gold'] -= session['random_points']
            activity = ('Entered a casino and lost ' + str(session['random_points']) + ' golds! Ouch!')
            session['activities'].append(activity)
        else:
            print ('won')
            session['total_gold'] += session['random_points']
            print('new total = ', session['total_gold'])
            activity = ('Earned ' + str(session['random_points']) + ' golds from the casino!')
            session['activities'].append(activity)
            print (session['activities'])

    return redirect('/')


# IF YOU HAVE A BUTTON POINTING TO THIS METHOD, YOU NEED TO POST, OTHERWISE
# USE SECOND APP.ROUTE WITHOUT POST
@app.route('/destroy_session', methods=['POST'])
# @app.route('/destroy_session')
def delete_session():
    session.clear()
    # session.pop('visits') # delete visits
    return redirect('/')
    # return 'Sessions deleted'


if __name__ == "__main__":
    app.run(debug=True)
