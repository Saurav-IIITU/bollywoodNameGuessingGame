from flask import Flask, render_template, request, session, redirect, url_for
from game import choose_random_name, display_partial_name
import pandas as pd

app = Flask(__name__)
app.secret_key = "\x9c\xcaFHo\x9b\x10\xdelG\xb5\xe3'\xb2\x80\xe9&\x06\\T\xfa\xdf\x16m"  # Set a secret key for session management

# Read the CSV file
df = pd.read_csv('Data for repository.csv')

@app.route('/')
def index():
    session.clear()  # Clear session data
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    session.clear()  # Clear session data for a new game
    session['name_to_guess'] = choose_random_name()
    session['guessed_consonants'] = []
    session['chances'] = 8
    return redirect(url_for('game'))

@app.route('/game')
def game():
    if 'name_to_guess' not in session:  # Check if name_to_guess is not in session
        return redirect(url_for('index'))

    return render_template('play.html', name=session['name_to_guess'], partial_name=display_partial_name(session['name_to_guess'], session['guessed_consonants']), chances=session['chances'])

@app.route('/guess', methods=['POST'])
def guess():
    if 'name_to_guess' not in session:
        return redirect(url_for('index'))  # Redirect to index if session data is not initialized

    user_guess = request.form['guess'].lower()
    name_to_guess = session['name_to_guess']
    guessed_consonants = session['guessed_consonants']
    chances = session['chances']
    partial_name_display = ""

    if len(user_guess) == 1 and user_guess.isalpha() and user_guess not in "aeiou" and user_guess not in guessed_consonants:
        guessed_consonants.append(user_guess)
        session['guessed_consonants'] = guessed_consonants
        partial_name_display = display_partial_name(name_to_guess, guessed_consonants)

        if "_" not in partial_name_display:
            result = "Congratulations! You've guessed the name: " + name_to_guess
        else:
            result = None
    else:
        result = "Invalid guess. Please enter a single consonant that you haven't guessed before."

    if len(user_guess) == 1 and user_guess in name_to_guess.lower():
        session['chances'] += 1  # Reward: gain one chance on correct guess

    session['chances'] -= 1

    if session['chances'] == 0 and result is None:
        result = "Sorry, you've run out of chances. The correct name was: " + name_to_guess

    return render_template('play.html', name=name_to_guess, partial_name=partial_name_display, chances=session['chances'], result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000,debug=True)
