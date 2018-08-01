def main():
    ClientSystem()

def ClientSystem():
    infile = open("G:/python/program/clientsystem.txt", "r")
    clientinformation = [line.rstrip().split(",") for line in infile]
    clientdict = dict(clientinformation)
    infile.close()
    name = input("Enter client's name:")
    name = name.upper()
    if name not in clientdict.keys():
        client = AccountSystem(name)
        clientdict = DealSystem(client, clientdict)
    else:
        client = AccountSystem(name, float(clientdict[name]))
        clientdict = DealSystem(client, clientdict)
    OutputSystem(clientdict)

def DealSystem(client, clientdict):
    DWQB = input("Enter D, W, Q or B:")
    DWQB = DWQB.upper()
    while not DWQB == "Q":
        while DWQB == "D":
            deposit = float(input("Enter amount to deposit:"))
            client.Deposit(deposit)
            print("Balance: {0:,.2f}".format(client.GetBalance()))
            clientdict[client.GetName()] = client.GetBalance()
            break
        while DWQB == "W":
            withdrawal = float(input("Enter amount to withdrawal:"))
            if withdrawal > client.GetBalance():
                print("Insufficient funds, transaction denied.")
                print("Balance: {0:,.2f}".format(client.GetBalance()))
                break
            else:
                client.Withdraw(withdrawal)
                print("Balance: {0:,.2f}".format(client.GetBalance()))
                clientdict[client.GetName()] = client.GetBalance()
                break
        while DWQB == "B":
            print("Balance: {0:,.2f}".format(client.GetBalance()))
            break
        while not (DWQB == "D" or DWQB == "W" or DWQB == "B"):
            print("Enter error. Try again.")
            break
        DWQB = input("Enter D, W, Q or B:")
        DWQB = DWQB.upper()
    print("End of transactions. Have a good day", client.GetName())
    return clientdict

def OutputSystem(clientdict):
    outfile = open("G:/python/program/clientsystem.txt", "w")
    clientinformation = []
    for k, v in clientdict.items():
        clientinformation.append([k, str(v)])
    print(clientinformation)
    clientinformation.sort(key = lambda x: x[0])
    for m, n in clientinformation:
        outfile.write(m + ',' + n + '\n')
    outfile.close()

class AccountSystem():
    def __init__(self, name, balance = 0):
        self._name = name
        self._balance = balance

    def GetName(self):
        return self._name

    def GetBalance(self):
        return self._balance

    def Deposit(self, deposit):
        self._balance += deposit

    def Withdraw(self, withdraw):
        self._balance -= withdraw

    def __str__(self):
        return self._name + "," + str(self._balance)

main()