lexer_kws = []
file = open('./app/src/speakql_speech_recognition/speakql-keywords.txt', 'r')
for line in file:
    lexer_kws.append(line.replace('\n', ''))

print(lexer_kws)