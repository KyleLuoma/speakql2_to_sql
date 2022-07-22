
from google.cloud import speech

class GsrConnector:

    def __init__(self, sample_rate=48000):
        self.client = speech.SpeechClient()
        self.config = speech.RecognitionConfig(
            encoding = speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz = sample_rate,
            language_code="en-US",
            audio_channel_count = 2
        )

        self.adaptation = speech.AdaptationClient()

        pass

    def sendAudioToGsr(self, audio_file):
        # content = audio_file.read()
        audio = speech.RecognitionAudio(content = audio_file)
        transcript = ""
        try:
            response = self.client.recognize(
                config = self.config,
                audio = audio
            )
            

            for result in response.results:
                transcript += (result.alternatives[0].transcript + " ")

            print(response.results)
        except:
            transcript = "GSR transcription timed out due to audio length. This is not a problem, your attempt is valid. Follow instructions from the facilitator to proceed."        

        return transcript



