import socket
import random



def waitPlayerConnect(numOfPlayer: int, players: list):
    print("Waiting for connections...")

    while len(players) < numOfPlayer:
        connection, client_address = s.accept()
        players.append(connection)
        print(f"New connection from {client_address}. Players connected: {len(players)}/{numOfPlayer}")
        connection.sendall(f"Welcome! You are player [{len(players)}]\n".encode())
    


def randomNumber():
    numList = []
    while len(numList) < 6:
        x = random.randint(0, 9)
        if not x in numList:
            numList.append(x)

    return numList


def sendAllplayers(data: str, players: list):
    data = data.encode()
    for p in players:
        p.sendall(data)
    


def checkPattern(data: str, answer: list):
    numOfTruePosition = 0
    numOfWrongPosition = 0
    data = data.split()

    for i in range(0, len(data)):
        if int(data[i]) == answer[i]:
            numOfTruePosition += 1
            data[i] = None

    for j in range(0, len(data)):
        if data[j] != None:
            if (int(data[j]) in answer):
                numOfWrongPosition += 1

    return numOfTruePosition, numOfWrongPosition


if __name__ == '__main__':
    server_ip = "192.168.20.192"
    server_port = 4321

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((server_ip, server_port))
    s.listen(5)

    numOfPlayer = int(input("Enter the number of players in the room: "))
    players = []

    waitPlayerConnect(numOfPlayer, players)
    sendAllplayers(f"The game has started with {numOfPlayer} players!\n", players)

    maxRound = 12
    currentRound = 1
    player_counter = 0

    answer = randomNumber()
    print(answer)
    while currentRound <= maxRound:
        sendAllplayers(f"Round {currentRound}, Player {player_counter + 1}", players)

        try:
            playerData = players[player_counter].recv(1024).decode()
        except Exception as e:
            print(e)
            break

        numberOfTrue, numberOfWrong = checkPattern(playerData, answer)

        if (numberOfTrue == 6):
            sendAllplayers(f"Player: {player_counter + 1} is Winner. Answer is {answer}\n", players)
            break
        else:
            sendAllplayers(f"{numberOfTrue} {numberOfWrong} ({playerData})\n", players)

        player_counter += 1
        currentRound += 1

        if (player_counter >= len(players)):
            player_counter = 0

    sendAllplayers(f"Game over. Answer is {answer}\n", players)

    s.close()