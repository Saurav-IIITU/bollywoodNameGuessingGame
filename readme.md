# Bollywood Movie Name Guessing Game

This is a fun Bollywood movie name guessing game where players guess consonants to reveal the name of a Bollywood movie. The game is built using Python's Flask web framework, with a simple front-end interface for interaction.

## Game Concept

The player needs to guess the name of a Bollywood movie by inputting consonants (non-vowel letters) one at a time.

### How the Game Works:
1. A random Bollywood movie name is selected for the player to guess.
2. The movie name is displayed with all consonants hidden, while vowels are revealed.
3. The player inputs one consonant at a time to guess the name.
4. For each guess:
   - If the guessed consonant is in the movie name, it is revealed in all the correct positions.
   - If the guessed consonant is not in the movie name or has already been guessed, the player receives a warning or loses a chance.
5. The player starts with **8 chances** to guess the full name.
6. **Extra chance**: Every correct guess rewards the player with one extra chance.

### Game End:
- The game ends in one of two ways:
   - **Win**: The player correctly guesses all the consonants in the movie name.
   - **Lose**: The player runs out of chances without guessing the full name.

## Features
- **Consonant Guessing**: The game only allows guessing consonants (no vowels).
- **Warning for Repeated Guesses**: If a player guesses the same consonant more than once, a warning is shown without deducting a chance.
- **Chance System**: Players lose a chance for incorrect guesses but gain a chance for each correct guess.
- **Replay Option**: After finishing a game, players can start a new game.

## Game Interface
- The game provides a simple web interface where the partially guessed movie name is shown, and the player can input their next guess.
- Chances left are displayed, and a result (win/lose) is shown when the game ends.

## How to Run
To run the game locally:
1. Clone the repository.
2. Install the required dependencies (Flask and pandas).
3. Run the `app.py` file.
4. Access the game in your browser at `http://localhost:5000`.

```bash
# Install required packages
pip install flask pandas

# Run the game
python app.py
