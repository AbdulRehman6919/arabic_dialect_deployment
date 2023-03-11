
#Falsk Libs
from flask import Flask,request, jsonify, render_template

#Loading the audio file class for prediction
from klaam import SpeechClassification
model = SpeechClassification()


app=Flask(__name__)

def predict_wav_file(wav_file_path):
    predicted_label = model.classify(wav_file_path)
    return predicted_label

    
@app.route('/')
def home():
    return "hello pakistan"

@app.route('/predict',methods=['POST'])
def predict():
    file = request.files['']
    filename = "testing_wav_file.wav"
    file.save(filename)
    response = predict_wav_file(filename)
    return response

if __name__=="__main__":
    app.run(debug=True)



