class VotingNotAllowedException(Exception):
    pass

class Voter:
    def __init__(self, name,age):
        self.name = name
        self.age = age
        if(age<18):
            raise VotingNotAllowedException("Voting is not allowed for minor age")
        else :
            print("Voting is allowed")
