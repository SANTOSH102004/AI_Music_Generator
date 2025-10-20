from flask import Flask, render_template, request, send_from_directory
import os
import uuid
import torch.serialization
import numpy
import numpy.core.multiarray
from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav

app = Flask(__name__)

# # Preload Bark models with safe globals for PyTorch 2.6
# with torch.serialization.safe_globals([numpy.core.multiarray.scalar]):
#     preload_models()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    prompt = request.form['prompt']
    if not prompt:
        return {'error': 'No prompt provided'}, 400

    try:
        # Generate audio with weights_only=False for compatibility
        import torch
        original_load = torch.load
        torch.load = lambda *args, **kwargs: original_load(*args, **kwargs, weights_only=False)
        audio_array = generate_audio(prompt, text_temp=0.7, waveform_temp=0.7)
        torch.load = original_load
    except Exception as e:
        return {'error': f'Failed to generate audio: {str(e)}'}, 500

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
