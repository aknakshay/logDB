import datetime


class ADB:
    def __init__(self):
        self.logFile = "log_"
        self.threshold = 10  # (appends to the file name)
        self.thresholdNumber = 0
        self.logFileName = self.logFile + str(self.thresholdNumber)
        self.writeCounter = 0  # (counts when thresholdnumber needs to be incremented)

    def get(self, key):
        for i in range(self.thresholdNumber, -1, -1):
            print("Checking file: " + self.logFile + str(i))
            with open(self.logFile + str(i), 'r') as f:
                data = f.readlines()
                for lineNumber in range(len(data) - 1, -1, -1):
                    print("checking line number: " + str(lineNumber))
                    tmp = data[lineNumber].split(',')
                    if tmp[1] == key:
                        return tmp[2]

    def set(self, key, value):
        with open(self.logFileName, "a") as f:
            f.write(str(datetime.datetime.now()) + "," + str(key) + "," + str(value) + ",\n")
            self.writeCounter += 1
        if self.writeCounter == self.threshold:
            self.fileUpdate()

    def file_update(self):
        self.thresholdNumber += 1
        self.logFileName = self.logFile + str(self.thresholdNumber)
        with open(self.logFileName, 'w') as f:
            pass
        self.writeCounter = 0
