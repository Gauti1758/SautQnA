import os
from app.pdf_reader import extract_qa_pairs_from_pdf
from app.tts_engine import auto_play_qa_pairs
from app.utils import generate_tts, wrap_ssml
import time


# export GOOGLE_APPLICATION_CREDENTIALS="/home/gautam/Downloads/pelagic-cat-427508-v1-6f451366a269.json"

pdf_path = "assets/sample_qna.pdf"
output_dir = "outputs"
os.makedirs(output_dir, exist_ok=True)

qa_pairs = extract_qa_pairs_from_pdf(pdf_path)
if not qa_pairs:
    print("❌ No Q&A pairs found.")
    exit()

all_wav_paths = []

# for idx, (question, answer) in enumerate(qa_pairs):
#     q_file = os.path.join(output_dir, f"q{idx+1}.wav")
#     a_file = os.path.join(output_dir, f"a{idx+1}.wav")

#     generate_tts(question, q_file, voice_name="ar-XA-Wavenet-B")
#     generate_tts(answer, a_file, voice_name="ar-XA-Standard-A")

#     all_wav_paths.extend([q_file, a_file])

for idx, (question, answer) in enumerate(qa_pairs):
    q_file = os.path.join(output_dir, f"q{idx+1}.wav")
    a_file = os.path.join(output_dir, f"a{idx+1}.wav")

    # ssml_q = wrap_ssml(question, pause_before="300ms", pause_after="400ms", pitch="+3%", rate="90%")
    # ssml_a = wrap_ssml(answer, pause_before="400ms", pause_after="700ms", pitch="1%", rate="85%")

    # generate_tts(ssml_q, q_file, voice_name="ar-XA-Wavenet-B", is_ssml=True)
    # generate_tts(ssml_a, a_file, voice_name="ar-XA-Standard-A", is_ssml=True)
    ssml_q = f"""<speak><prosody pitch="+2%" rate="92%"><break time="300ms"/>{question}<break time="400ms"/></prosody></speak>"""
    generate_tts(ssml_q, q_file, voice_name="ar-XA-Wavenet-B", is_ssml=True)

    ssml_a = f"""<speak><prosody pitch="+1%" rate="89%"><break time="250ms"/>{answer}</prosody></speak>"""
    generate_tts(ssml_a, a_file, voice_name="ar-XA-Standard-A", is_ssml=True)

time.sleep(2)

auto_play_qa_pairs(len(qa_pairs))
