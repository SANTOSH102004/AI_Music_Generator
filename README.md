# AI Music Generator

A local AI-powered music generator using Bark by Suno. This application allows you to generate audio from text prompts entirely offline.

## Features

- Generate music or audio from text prompts (e.g., "Jazz with saxophone", "Lo-fi beat")
- Simple web interface built with Flask
- Runs entirely locally, no internet required after setup
- Saves generated audio as WAV files

## Requirements

- Python 3.8 or higher
- Sufficient RAM (at least 8GB recommended for Bark model)
- GPU recommended for faster generation (optional)

## Installation

1. Clone or download this repository.

2. Install Python dependencies:
   ```
   pip install -r requirements.txt
   ```

   Note: Installing Bark may take some time as it downloads the models.

3. Run the application:
   ```
   python app.py
   ```

4. Open your browser and go to `http://127.0.0.1:5000/`

## Usage

1. Enter a text prompt describing the music you want to generate (e.g., "Upbeat pop song with guitar").
2. Click "Generate Music".
3. Wait for the audio to be generated (this may take 10-30 seconds depending on your hardware).
4. Once generated, an audio player will appear allowing you to play the generated music.

## How it Works

- The backend uses Bark, an open-source text-to-audio model by Suno.
- Bark generates audio waveforms from text prompts.
- Generated audio is saved as WAV files in the `static/` directory.
- The web interface provides a simple way to input prompts and play results.

## Troubleshooting

- If generation fails, ensure you have enough RAM and disk space.
- Bark models are downloaded on first run, so initial startup may be slow.
- For GPU acceleration, ensure PyTorch is installed with CUDA support.

## License

This project uses Bark, which is licensed under the MIT License.
