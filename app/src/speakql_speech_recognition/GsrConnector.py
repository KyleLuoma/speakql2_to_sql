
from google.cloud import speech

class GsrConnector:

    def __init__(self, sample_rate=44100, channels=2):
        self.client = speech.SpeechClient()
        self.config = speech.RecognitionConfig(
            encoding = speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz = sample_rate,
            language_code="en-US",
            audio_channel_count = channels
        )

        self.adaptation = speech.AdaptationClient()

        pass

    def sendAudioToGsr(self, audio_file, sample_rate=44100, channels=2):
        # content = audio_file.read()

        self.config = speech.RecognitionConfig(
            encoding = speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz = sample_rate,
            language_code="en-US",
            audio_channel_count = channels
        )

        audio = speech.RecognitionAudio(content = audio_file)
        response = self.client.recognize(
            config = self.config,
            audio = audio
        )
        print(response.results[0].alternatives[0].transcript)
        return response.results[0].alternatives[0].transcript



