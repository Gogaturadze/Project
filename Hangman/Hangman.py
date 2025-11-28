import json
import random

"""
Hangman არის სიტყვების გამოცნობის თამაში. პროგრამა ირჩევს შემთხვევით სიტყვას წინასწარ განსაზღვრული სიიდან
და აჩვენებს მას ქვედა ტირეების გამოყენებით (რამდენი ასოცაა სიტყვაში, იმდენი ქვედა ტირე), რომელიც წარმოადგენს
ფარულ ასოებს. მომხმარებლებს სთხოვენ გამოიცნონ ასო და პროგრამა ამოწმებს არის თუ არა ასო სიტყვაში. ვლინდება სწორად 
გამოცნობილი ასოები და თამაში გრძელდება მანამ, სანამ მომხმარებელი არ გამოიცნობს სიტყვას ან არ ამოიწურება
მცდელობები.
"""


class HangmanService:
    def __init__(self, life=int):

        # სიტყვების ჩატვირთვა ფაილიდან
        with open("words.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            self.word_list = data["words"]

        self.life = life

    # შემთხვევითი სიტყვის არჩევა
    def get_random_word(self):
        return random.choice(self.word_list)


class HangmanGame(HangmanService):
    def __init__(self, life=int):
        super().__init__(life)

    # თამაშის ლოგიკა
    def play(self):
        chosen_word = self.get_random_word()
        separated_word = list(chosen_word)
        hidden_word = ["_"] * len(chosen_word)

        while self.life > 0:
            print(" ".join(hidden_word))
            user_input = input("შეიყვანეთ ასო: ").lower()

            # ვალიდაცია
            if len(user_input) != 1:
                print("გთხოვთ შეიყვანოთ მხოლოდ ასო")
                continue
            elif not ("\u10d0" <= user_input <= "\u10f0"):
                print("გთხოვთ შეიყვანოთ ქართული ასო")
                continue
            elif not user_input.isalpha():
                print("გთხოვთ შეიყვანოთ მხოლოდ ასოები")
                continue

            # ასოების შემოწმება
            if user_input in separated_word:
                for i, letter in enumerate(separated_word):
                    if letter == user_input:
                        hidden_word[i] = user_input
                print(f"თქვენ გამოიცანით ასო: {user_input}, {hidden_word}")
            else:
                self.life -= 1
                print(f"ასო {user_input} ვერ მოიძებნა. დაგრჩათ {self.life} სიცოცხლე.")

            if "_" not in hidden_word:
                print("გილოცავ! გამოცნობილი სიტყვაა:", chosen_word)
                return

        print("სამწუხაროდ თქვენ წააგეთ, სწორი სიტყვა იყო:", chosen_word)


game = HangmanGame(3)
game.play()
