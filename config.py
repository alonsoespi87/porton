# Audio configuration
AUDIO_FILENAME = "input.wav"
AUDIO_DURATION = 4  # seconds
SAMPLE_RATE = 16000

# Voice settings
VOICE_LANGUAGE = "spanish"  # Try "spanish-latin" if needed
VOICE_RATE = 160  # Speech speed

# Whisper model settings
WHISPER_MODEL_SIZE = "base"
WHISPER_COMPUTE_TYPE = "int8"

# LLM model path
LLM_MODEL_PATH = "models/phi-2.gguf"
LLM_CONTEXT_SIZE = 2048

# Classifier model path
CLASSIFIER_MODEL_PATH = "model.pkl"

# Database path
MENU_DB_PATH = "data/menu.db"
