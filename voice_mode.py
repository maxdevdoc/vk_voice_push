import torch
import os
import numpy

def voice_push(list_post):
    language = 'ru'
    model_id = 'v3_1_ru'
    sample_rate = 48000
    speaker = 'xenia'
    device = torch.device('cpu')


    model, _ = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                        model='silero_tts',
                                        language=language,
                                        speaker=model_id)
    model.to(device)  # gpu or cpu
    for i in list_post:
            print(i)
            text = i
            audio = model.save_wav(text=text,
                                   speaker=speaker,
                                   sample_rate=sample_rate)
            os.rename('test.wav', f'{i[0:4]}.wav')