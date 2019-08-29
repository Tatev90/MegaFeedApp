import json
import socket

HOST, PORT = "tcptestapi.megafeed.com", 3126

message1 = '{"Command": "auth","Params":{"UserName":"operator4","Password":"12345678"}}^'
message2 = u'{"Command":"subscribeGames","Params":{"games":[263924]}}^'

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:

    sock.connect((HOST, PORT))

    sock.send(bytes(message1, 'utf-8'))
    received = sock.recv(1024)

    sock.send(bytes(message2, 'utf-8'))
    received1 = sock.recv(10240000)
    rec = str(received1, 'utf-8')

finally:
    sock.close()

rec = rec.replace("^", "")
obj = json.loads(rec)
# print(obj)
objects = obj["Objects"]
# print(objects)

# adding following values into one list
code = [i['code'] for i in objects]
text = [i['text'] for i in objects]
team = [i['team'] for i in objects]
value = [i['value'] for i in objects]
additional = [i['additional'] for i in objects]
# print(text[0])

current_game = []
for n in range(0, len(objects)):
    current_game.append([code[n], text[n], team[n], value[n], additional[n]])
# print(current_game)

score = [i['score'] for i in objects]
score_list = []
for m in range(0, len(objects)):
    score_list.append(score[m])
# print(score_list)

current_game_with_score = []
for k in range(0, len(objects)):
    current_game_with_score.append([code[k], text[k], team[k], value[k], additional[k], score[k]])
# print(current_game_with_score)
