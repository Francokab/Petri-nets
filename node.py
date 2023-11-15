class node:

    def __init__(self, marquage, transitions):
        self.marquage = marquage
        self.transitions = transitions
    
    def afficher(self):
        print("Les transitions sont :")
        print(self.transitions)
        print("Le marquage est :")
        print(self.marquage)