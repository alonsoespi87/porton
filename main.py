from voice.listen import record_audio
from voice.speak import speak
from faster_whisper import WhisperModel
from nlp.intent_classifier import IntentClassifier
from nlp.fallback_llm import generate_response as llm_response
from utils.responses import generate_response as rule_response

whisper_model = WhisperModel("base", compute_type="int8")
classifier = IntentClassifier()
classifier.train("nlp/intent_dataset.csv")

while True:
    audio_path = record_audio()
    segments, _ = whisper_model.transcribe(audio_path)
    text = " ".join(seg.text for seg in segments)
    print("User said:", text)

    intent = classifier.predict(text)
    response = rule_response(intent)

    if not response:
        response = llm_response(text)

    print("Assistant:", response)
    speak(response)
