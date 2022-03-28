"""Request Syntax

response = client.synthesize_speech(
    Engine='standard'|'neural',
    LanguageCode='arb'|'cmn-CN'|'cy-GB'|'da-DK'|'de-DE'|'en-AU'|'en-GB'|'en-GB-WLS'|'en-IN'
    |'en-US'|'es-ES'|'es-MX'|'es-US'|'fr-CA'|'fr-FR'|'is-IS'|'it-IT'|'ja-JP'|'hi-IN'|'ko-KR'
    |'nb-NO'|'nl-NL'|'pl-PL'|'pt-BR'|'pt-PT'|'ro-RO'|'ru-RU'|'sv-SE'|'tr-TR'|'en-NZ'|'en-ZA',

    LexiconNames=[
        'string',
    ],
    OutputFormat='json'|'mp3'|'ogg_vorbis'|'pcm',
    SampleRate='string',
    SpeechMarkTypes=[
        'sentence'|'ssml'|'viseme'|'word',
    ],
    Text='string',
    TextType='ssml'|'text',
    VoiceId='Aditi'|'Amy'|'Astrid'|'Bianca'|'Brian'|'Camila'|'Carla'|'Carmen'|'Celine'
    |'Chantal'|'Conchita'|'Cristiano'|'Dora'|'Emma'|'Enrique'|'Ewa'|'Filiz'|'Gabrielle'
    |'Geraint'|'Giorgio'|'Gwyneth'|'Hans'|'Ines'|'Ivy'|'Jacek'|'Jan'|'Joanna'|'Joey'
    |'Justin'|'Karl'|'Kendra'|'Kevin'|'Kimberly'|'Lea'|'Liv'|'Lotte'|'Lucia'|'Lupe'
    |'Mads'|'Maja'|'Marlene'|'Mathieu'|'Matthew'|'Maxim'|'Mia'|'Miguel'|'Mizuki'|'Naja'
    |'Nicole'|'Olivia'|'Penelope'|'Raveena'|'Ricardo'|'Ruben'|'Russell'|'Salli'|'Seoyeon'
    |'Takumi'|'Tatyana'|'Vicki'|'Vitoria'|'Zeina'|'Zhiyu'|'Aria'|'Ayanda'
)"""



import boto3
from datetime import datetime
import json
import random

class PollyVoice:

    def __init__(self):
        self.polly_client = boto3.client('polly')
        
        self.sample_rate = '8000'
        self.engine = 'neural'

        self.neural_voices = ['Joanna', 'Salli', 'Kendra', 'Ivy', 'Kimberly', 
                              'Kevin', 'Matthew', 'Justin', 'Joey']


    def get_speech_audio(self, text, voice):
        response = self.polly_client.synthesize_speech(
            Engine=self.engine,
            OutputFormat='mp3',
            SampleRate=self.sample_rate,
            Text=text,
            TextType='text',
            VoiceId=voice,
        )
        print(response)
        return response["AudioStream"]

    
    def write_speech_to_file(self, audio_stream, filename):
        file = open('query_audio/' + filename, 'wb')
        file.write(audio_stream.read())
        file.close()


    def get_random_neural_voice(self):
        voice_index = random.randrange(0, len(self.neural_voices))
        return self.neural_voices[voice_index]


    def update_query_log_json(self, query_text, audio_file_name, voice, engine, sample_rate):
        with open("query_audio/query_log.json", "r") as jsonFile:
            data = json.load(jsonFile)

        data.append({
            "filename" : audio_file_name, 
            "query" : query_text, 
            "service" : "polly",
            "voice" : voice,
            "engine" : engine,
            "sample_rate" : sample_rate
            })

        with open("query_audio/query_log.json", "w") as jsonFile:
            json.dump(data, jsonFile, indent=4)


    def create_query_audio_and_log(self, query_text):
        timestamp = datetime.now().strftime("%m%d%Y%H%M%S")
        filename = 'polly_voicequery_' + timestamp + '.mp3'
        voice = self.get_random_neural_voice()
        audio = self.get_speech_audio(
            query_text,
            voice
        )
        self.write_speech_to_file(
            audio, 
            filename
        )
        self.update_query_log_json(
            query_text,
            filename,
            voice,
            self.engine,
            self.sample_rate
        )





    


polly = PollyVoice()

polly.create_query_audio_and_log(
    "DISPLAY nicer_but_slower_film_list dot FID and the average of ( length ) , average ( length ) , category IN nicer_but_slower_film_list as nt "
    )