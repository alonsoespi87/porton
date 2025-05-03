import pyttsx3
from config import VOICE_LANGUAGE, VOICE_RATE


def speak(text):
    engine = pyttsx3.init()
    # Configurar una voz en español
    voices = engine.getProperty('voices')
    for voice in voices:
        if 'spanish' in voice.name.lower() or 'es-' in voice.id.lower():
            engine.setProperty('voice', voice.id)
            break
    else:
        print("No se encontró una voz en español. Usando la voz predeterminada.")
    engine.setProperty('rate', VOICE_RATE)
    engine.setProperty('voice', VOICE_LANGUAGE)  # Try "spanish-latin" if needed
    engine.say(text)
    engine.runAndWait()
