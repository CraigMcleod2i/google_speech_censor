from google.cloud import vision, speech
import os

# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.path.abspath('./mounted/env.json')

def transcribe_file_censored(speech_file, censored_words):
    """Transcribe the given audio file."""
    
    import io

    client = speech.SpeechClient()

    with io.open(speech_file, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        # sample_rate_hertz=16000,
        language_code="en-US",
    )

    response = client.recognize(config=config, audio=audio)
    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.

    for result in response.results:   
        response = u"{}".format(result.alternatives[0].transcript).split()
        string = ' '

        for i, word in enumerate(response):
            for j, bleep in enumerate(censored_words):
                bleep
                if response[i].lower() == censored_words[j].lower():
                    response[i] = '*' * len(word)
        print(string.join(response))

transcribe_file_censored('dizzee.wav', ['it', 'as', 'he', 'she', 'paper', 'round', 'plan', 'act'])