import socket

def getId(data: str):
    index = data.index("[")
    return int(data[index + 1])

def checkMyTurn(msg: str, myID):
    codeNameId = f"Player {myID}"

    if (codeNameId in msg):
        return True
    else:
        return False

def getDataInput():
    while True:
        isRepeat = False

        data_user = input("ENTER THE NUMBER:")
        data = []

        for c in data_user:
            data.append(c)

        for i in range(10):
            if data.count(str(i)) >= 2:
                isRepeat = True
                break

        if len(data) == 6 and not isRepeat:
            userInput = []
            for i in range(0, len(data)):
                userInput.append(int(data[i]))
            return userInput
        else:
            print("Please enter the new numbers again.")

if __name__ == '__main__':
    server_ip = "192.168.4.192"
    server_port = 1234

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((server_ip, server_port))
    except:
        print("Can't connect to server.")
        exit()

    rawData = client.recv(1024).decode()
    ID = getId(rawData)

    start = client.recv(1024).decode()
    print(start)

    stopGameOver = "Game over"
    stopWinner = "Winner"

    while (True):
        try:
            message = client.recv(1024).decode()
        except:
            print("Connection failed...")
            break

        print(message)

        if (checkMyTurn(message, ID)):
            userData = getDataInput()
            userDataReformat1 = str(userData).replace("[", "")
            userDataReformat2 = userDataReformat1.replace("]", "")
            userDataReformat3 = userDataReformat2.replace(",", "")
            client.sendall(userDataReformat3.encode())
            print(userDataReformat3)

        if (stopGameOver in message or stopWinner in message):
            break

    client.close()