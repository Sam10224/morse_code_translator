from flask import *
import webbrowser

app = Flask(__name__)

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    ' ': '/'
}

# Morse Code reverse dictionary
MORSE_CODE_REVERSED = {v: k for k, v in MORSE_CODE_DICT.items()}

"""
This function serves as the homepage of the website.
It returns the index.html file located in the templates folder.
"""

"""
This function serves as the homepage of the website.
It returns the index.html file located in the templates folder.
"""
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/text_to_morse', methods=['POST'])
def text_to_morse():
    """
    This function takes a POST request with a JSON payload containing a text string.
    It converts the text to Morse code and returns the result as a JSON response.

    Parameters:
    - request: The Flask request object containing the JSON payload.

    Returns:
    - jsonify({'morse_code': morse_code.strip()}): A JSON response containing the Morse code representation of the input text.

    Raises:
    - KeyError: If the input text contains a character not found in the MORSE_CODE_DICT dictionary.
    """
    text = request.json['text'].upper()
    morse_code = ''.join([MORSE_CODE_DICT[char] + ' ' if char in MORSE_CODE_DICT else char + ' ' for char in text])
    return jsonify({'morse_code': morse_code.strip()})

@app.route('/morse_to_text', methods=['POST'])
def morse_to_text():
    """
    This function takes a POST request with a JSON payload containing a Morse code string.
    It converts the Morse code back to text and returns the result as a JSON response.

    Parameters:
    - **kwargs: The Flask request object containing the JSON payload. The payload should have a key 'morse_code' with the Morse code string to be converted.

    Returns:
    - jsonify({'text': text}): A JSON response containing the text representation of the input Morse code.

    Raises:
    - KeyError: If the input Morse code does not match any code in the MORSE_CODE_DICT dictionary.
    """
    morse_code = request.json['morse_code']
    text = ''.join([MORSE_CODE_REVERSED[code] if code in MORSE_CODE_REVERSED else '' for code in morse_code.split()])
    return jsonify({'text': text})

if __name__ == '__main__':
    webbrowser.open('http://127.0.0.1:5000')
    app.run(debug=True)
