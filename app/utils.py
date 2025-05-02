from google.cloud import texttospeech
import wave
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/gautam/Downloads/pelagic-cat-427508-v1-6f451366a269.json"
client = texttospeech.TextToSpeechClient()

#def generate_tts(text, output_path, voice_name="ar-XA-Standard-A"):
def generate_tts(text, output_path, voice_name="ar-XA-Standard-A", is_ssml=True):
    #synthesis_input = texttospeech.SynthesisInput(text=text)
    synthesis_input = (
        texttospeech.SynthesisInput(ssml=text) if is_ssml else texttospeech.SynthesisInput(text=text)
    )
    voice = texttospeech.VoiceSelectionParams(
        language_code="ar-XA",
        name=voice_name,
        ssml_gender=texttospeech.SsmlVoiceGender.FEMALE,
    )
    audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.LINEAR16)

    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    with open(output_path, "wb") as out:
        out.write(response.audio_content)
    print(f"✅ Generated: {output_path}")

def wrap_ssml(text, pause_before="500ms", pause_after="500ms", pitch="+2%", rate="85%"):
    return f"""
    <speak>
        <break time="{pause_before}"/>
        <prosody pitch="{pitch}" rate="{rate}">
            <emphasis level="moderate">{text}</emphasis>
        </prosody>
        <break time="{pause_after}"/>
    </speak>
    """