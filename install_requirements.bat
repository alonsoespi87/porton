@echo off
python -m venv venv
call venv\Scripts\activate
pip install --upgrade pip
pip install faster-whisper pyttsx3 scikit-learn numpy sounddevice scipy llama-cpp-python
echo Installation completed. Press any key to continue...
pause