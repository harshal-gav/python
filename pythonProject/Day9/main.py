from mypack.voting import Voter, VotingNotAllowedException

try:
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))

        voter = Voter(name, age)
        print("Voter registration successful!")

except VotingNotAllowedException as e:
        print(f"Exception: {e}")


