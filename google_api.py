def run_google_api(rec_file):
    """Transcribe the given audio file."""
    from google.cloud import speech
    from google.cloud.speech import enums
    from google.cloud.speech import types
    import io

    client = speech.SpeechClient()
    with io.open(rec_file, 'rb') as audio_file:
        content = audio_file.read()

    audio = types.RecognitionAudio(content=content)
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
        sample_rate_hertz=16000,
        language_code='en-US')

    response = client.recognize(config, audio)
    return response


if __name__ == '__main__':
    run_google_api()
