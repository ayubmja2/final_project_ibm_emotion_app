"""
Emotion Detection Server

This python script runs the flask server and evaluates the user input and returns the approx
sentiment analysis done by the IBM AI.

Author(Leaner): [ayubmja2]
"""
from flask import Flask,request,render_template
from EmotionDetection.emotion_detection import emotion_detector
from EmotionDetection.emotion_detection import emotion_predictor

app = Flask("Emotion Detection")

def run_server():
    """
    This the server port. This function get called on the bottom of the page.
    """
    app.run(host="0.0.0.0", port=5000)

#emotion detector decorator
@app.route("/emotionDetector")

def send_to_detector():
    """
    This function sends the user provided input tot he detector function and return the results
    """
    text_to_detect = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_detect)
    formated_response = emotion_predictor(response)

    if formated_response['dominant_emotion'] is None:
        return "Invalid text! Please try again."
    return (
        f"For the given statement, the system response is 'anger': {formated_response['anger']} "
        f"'disgust': {formated_response['disgust']}, 'fear': {formated_response['fear']}, "
        f"'joy': {formated_response['joy']} and 'sadness': {formated_response['sadness']}. "
        f"The dominant emotion is {formated_response['dominant_emotion']}."
    )

@app.route("/")
def index_page():
    """
    This function renders the template page index.html on the "/" route
    """
    return render_template('index.html')

if __name__ == "__main__":
    run_server()
