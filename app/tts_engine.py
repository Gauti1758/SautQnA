from google.cloud import texttospeech
import os
import subprocess
import time

# Initialize the Google TTS client
client = texttospeech.TextToSpeechClient()

def synthesize_arabic_speech(text, filename="arabic_google_tts.wav"):
    # Define synthesis input
    synthesis_input = texttospeech.SynthesisInput(text=text)

    # Set up voice params (female voice, Arabic)
    voice = texttospeech.VoiceSelectionParams(
        language_code="ar-XA",
        name="ar-XA-Standard-A",
        ssml_gender=texttospeech.SsmlVoiceGender.FEMALE
    )

    # Define output config
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.LINEAR16  # WAV
    )

    # Synthesize
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    # Save to outputs/
    output_path = os.path.join("outputs", filename)
    with open(output_path, "wb") as out:
        out.write(response.audio_content)
        print(f"✅ Audio saved at: {output_path}")


def synthesize_speech(text, voice_name, gender, output_path):
    synthesis_input = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(
        language_code="ar-XA", name=voice_name, ssml_gender=gender
    )
    audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.LINEAR16)

    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    with open(output_path, "wb") as out:
        out.write(response.audio_content)

def auto_play_qa_pairs(num_pairs, output_dir='outputs'):
    for i in range(1, num_pairs + 1):
        q_file = os.path.join(output_dir, f"q{i}.wav")
        a_file = os.path.join(output_dir, f"a{i}.wav")

        if os.path.exists(q_file):
            print(f"\n▶️ Playing Q{i}")
            subprocess.run(["aplay", q_file])
            time.sleep(1.2)

        if os.path.exists(a_file):
            print(f"🎤 Playing A{i}")
            subprocess.run(["aplay", a_file])
            time.sleep(1.8)