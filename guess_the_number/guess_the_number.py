from random import randint

"""ამ თამაშში პროგრამა აგენერირებს შემთხვევით რიცხვს მითითებული დიაპაზონიდან.
მომხმარებლებს სთხოვენ გამოიცნონ რიცხვი. არასწორი რიცხვის შემთხვევაში პროგრამა
მომხმარებელს აძლევს მინიშნებას (უფრო მაღალი/უფრო დაბალი). თამაში აკონტროლებს
მცდელობების რაოდენობას და აჩვენებს შედეგს, როდესაც მომხმარებელი გამოიცნობს სწორ რიცხვს.
"""
class GuessNumb:

    def __init__(self, start:int, end:int):
        self.start = start
        self.end = end

    def get_number(self):
        random_number = randint(self.start,self.end)
        return random_number

    def runner(self):
        random_number = self.get_number()
        life = 3

        print(f"გამოიცანით რიცხვი დიაპაზონიდან {self.start} {self.end} ")

        while life > 0:
            try:
                user_input = int(input("გთხოვთ შეიყვანოთ რიცხვი: "))
            except:
                print("გთხოვთ შეიყვანოთ რიცხვი")
                continue

            if user_input == random_number:
                print(f'გილოცავთ თქვენ გამოიცანით რიცხვი {random_number}')
                break
            elif user_input > random_number:
                print("რიცხვი მეტია ")
                life -= 1
            else:
                print("რიცხვი ნაკლებია")
                life -= 1
        else:
            print(f"სამწუხაროდ თქვენ ვერ მოიგეთ, გამოსაცნობი რიცხვი იყო {random_number}")

guess = GuessNumb(1,5)
guess.runner()











