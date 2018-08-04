from json import dumps,loads

class Scores:

    def __init__(self):
        self.scoreList = []

    def addScore(self,score,name=''):
        self.scoreList.append([score,name])

    def getScores(self,ordered=True):
        if ordered:
            return sorted(self.scoreList,key=lambda x: x[0])
        return self.scoreList

    def load(self,file):
        with open(file,'r') as f:
            self.scoreList = loads(f.read())

    def save(self,file):
        with open(file,'w') as f:
            f.write(dumps(self.scoreList))


if __name__=='__main__':
    Scores = Scores()
