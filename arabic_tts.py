from google.cloud import texttospeech

# Create a client
client = texttospeech.TextToSpeechClient()

# Set the text input to be synthesized
synthesis_input = texttospeech.SynthesisInput(text="ما في مشكل، كيف حالك؟ نبدأ بالكتابة.")

# Build the voice request
voice = texttospeech.VoiceSelectionParams(
    language_code="ar-XA", 
    #name="ar-XA-Wavenet-B", #voice for male
    name="ar-XA-Standard-A",  #voice for female      ar-XA-Wavenet-C || ar-XA-Standard-A || ar-XA-Standard-C
    ssml_gender=texttospeech.SsmlVoiceGender.FEMALE
)

# Select the type of audio file to return
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.LINEAR16  # for WAV format
)

# Perform the text-to-speech request
response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config
)

# Save the audio to a file
with open("arabic_google_tts.wav", "wb") as out:
    out.write(response.audio_content)

print("Audio saved as arabic_google_tts.wav")
