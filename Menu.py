import os

# Menu error class
class ErrorMenu(Exception):


    def __init__(self, choice):
        """Saves your choice to say later that it is incorrect"""
        self.choice = choice
    

    def __str__(self):
        # Перегружаем вывод ошибки
        return f"Вы ввели команду {self.choice}, к сожалению данное меню ее не подразумавало,\n попробуйте еще раз"


    def reaction(self):
        """Error response function"""
        os.system("cls")
        print(self)
        os.system("pause")

# Menu class
class Menu:


    def __init__(self, comWords, display = None):
        """We save the commands and the auxiliary output function"""
        self.display = display
        self.comWords = comWords


    def cap(self):
        """Output of the menu header"""
        os.system("cls")
        if not self.display is None:
            self.display()
        for i, key in enumerate(self.comWords):
            print(f"{i + 1}. {key}")
        print("Введите команду: ", end = "\n---> ")


    def play(self):
        """Menu Execution"""
        while True:
            self.cap()
            try:
                choice = input()
                if choice in self.comWords:
                    self.comWords[choice]()
                    if choice == list(self.comWords.keys())[0]:
                        break
                elif choice.isdigit():
                    helpComWords = list(self.comWords.keys())
                    if 0 < int(choice) <= len(helpComWords):
                        self.comWords[helpComWords[int(choice) - 1]]()
                        if int(choice) == 1:
                            break
                    else:
                        raise ErrorMenu(choice)
                else:
                    raise ErrorMenu(choice)
            except ErrorMenu as e:
                e.reaction()
                    

