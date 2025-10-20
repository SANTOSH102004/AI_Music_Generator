from flask import Flask, render_template, request, send_from_directory
import os
import uuid
from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav

app = Flask(__name__)

# Preload Bark models
preload_models()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    prompt = request.form['prompt']
    if not prompt:
        return {'error': 'No prompt provided'}, 400

    # Generate audio
    audio_array = generate_audio(prompt)

    # Save audio to static folder with unique filename
    filename = f"{uuid.uuid4()}.wav"
    filepath = os.path.join('static', filename)
    write_wav(filepath, SAMPLE_RATE, audio_array)

    return {'audio_url': f'/static/{filename}'}

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

if __name__ == '__main__':
    if not os.path.exists('static'):
        os.makedirs('static')
    app.run(debug=True)
