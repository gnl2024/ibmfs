'''
Flask application for Emotion Detection.

This script sets up a Flask web server that provides an interface
for analyzing text input and displaying the detected emotions using
a custom emotion detection module.
'''

# Import necessary modules from Flask and the custom package
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initialize the Flask application
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emot_detector():
    '''
    Endpoint to handle emotion detection requests.

    Retrieves the text to analyze from the query parameters ('textToAnalyze'),
    passes it to the emotion_detector function, and formats the response.
    Returns an error message if the input is invalid.

    Returns:
        str: Formatted string with emotion results or an error message.
    '''
    # Get the text from the 'textToAnalyze' query parameter
    text_to_analyze = request.args.get('textToAnalyze')

    # Call the emotion detector function from the package
    response = emotion_detector(text_to_analyze)

    # Check if the dominant emotion is None, which indicates an error
    # (e.g., blank input, API error handled in the function)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # If analysis is successful, extract the emotion scores and dominant emotion
    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Format the response string as required by the project description
    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {anger_score}, 'disgust': {disgust_score}, "
        f"'fear': {fear_score}, 'joy': {joy_score} and "
        f"'sadness': {sadness_score}. The dominant emotion is "
        f"{dominant_emotion}."
    )

    # Return the formatted successful response
    return formatted_response

@app.route("/")
def render_index_page():
    '''
    Endpoint for the root URL.

    Renders the main HTML interface (index.html) for the application.

    Returns:
        Rendered template: The content of templates/index.html.
    '''
    # Serve the index.html file located in the 'templates' folder
    return render_template('index.html')

# Standard Python entry point check
if __name__ == "__main__":
    # Run the Flask application
    # host='0.0.0.0' makes the server accessible from any network interface
    # port=5000 specifies the port number to listen on
    app.run(host="0.0.0.0", port=5000)
    