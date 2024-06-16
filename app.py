#Use docker run -p 5001:5000 flask-joke-api to run the program
#use http://localhost:5001/jokes to run it on web browser

from flask import Flask, jsonify
import random

app = Flask(__name__)

jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Why don't programmers like nature? It has too many bugs.",
    "Why do cows have hooves instead of feet? Because they lactose.",
    "Why was the math book sad? It had too many problems.",
    "Why did the coffee file a police report? It got mugged.",
    "Why are elevator jokes so good? They work on many levels.",
    "Why did the bicycle fall over? Because it was two-tired.",
    "Why don't skeletons fight each other? They don't have the guts.",
    "Why did the tomato turn red? Because it saw the salad dressing."
]

@app.route('/jokes', methods=['GET'])
def get_jokes():
    # Choose 10 random jokes from the list
    selected_jokes = random.sample(jokes, 10)
    
    # Join the jokes with new lines
    jokes_with_newlines = "  ".join(selected_jokes)
    
    # Return the jokes as a single string with new lines
    return jsonify({'jokes': jokes_with_newlines})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
