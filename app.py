from flask import Flask, render_template, request, send_file
from gtts import gTTS
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/procesar', methods=['POST'])
def procesar():
    texto = request.form['texto']
    if texto:
        # Crear objeto de audio en memoria
        tts = gTTS(text=texto, lang='es')
        audio_bytes = io.BytesIO()
        tts.write_to_fp(audio_bytes)
        audio_bytes.seek(0)
        
        return send_file(
            audio_bytes,
            mimetype='audio/mp3',
            as_attachment=False,
            download_name='voz.mp3'
        )
    return 'No se recibió texto', 400

if __name__ == '__main__':
    app.run(debug=True)