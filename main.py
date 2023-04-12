from gtts import gTTS
from io import BytesIO

# Assume `text` contains the extracted Arabic text
with open('do3a2.txt', 'r', encoding='utf-8') as file:

    # Read the contents of the file into a variable
    text = file.read()
# Create a gTTS object for the Arabic text
tts = gTTS(text=text, lang='ar')

# Use BytesIO to capture the audio content
audio_bytes = BytesIO()
tts.write_to_fp(audio_bytes)

# Save the audio to a file or play it directly
# Example of saving the audio to a file
with open("output.mp3", "wb") as f:
    f.write(audio_bytes.getbuffer())
