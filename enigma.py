
#   TODO:
#   implement % to check str ranges inside of 26
#   implement rotor clicks with +/- to str index   
# 
# {"A": "", "B": "", "C": "", "D": "", "E": "", "F": "", "G": "", "H": "", "I": "", "J": "", "K": "", "L": "", "M": "", "N": "", "O":"", "P":"", "Q":"", "R":"", "S": "", "T": "", "U":"", "V":"", "W": "", "X": "", "Y": "", "Z": ""}

def rotors():
    wiresa =  [{"A": "Z"}, {"B": "X"}, {"C": "Y"}, {"D": "W"}, {"E": "V"}, {"F": "U"}, {"G": "T"}, {"H": "S"}, {"I": "R"}, {"J": "Q"}, {"K": "P"}, {"L": "O"}, {"M": "N"}, {"N": "M"}, {"O":"L"}, {"P":"K"}, {"Q":"J"}, {"R":"I"}, {"S": "H"}, {"T": "G"}, {"U":"F"}, {"V":"E"}, {"W": "D"}, {"X": "C"}, {"Y": "B"}, {"Z": "A"}]
    wiresB = [{"A": "N"}, {"B": "T"}, {"C": "Z"},{"D": "P"}, {"E": "S"}, {"F": "F"}, {"G": "B"}, {"H": "O"}, {"I": "K"}, {"J": "M"}, {"K": "W"}, {"L": "R"}, {"M": "C"}, {"N": "J"}, {"O":"D"}, {"P":"I"}, {"Q":"V"}, {"R":"L"}, {"S": "A"}, {"T": "E"}, {"U":"Y"}, {"V":"U"}, {"W": "X"}, {"X": "H"}, {"Y": "G"}, {"Z": "Q"}]
    wiresC = [{"A": "P"}, {"B": "E"}, {"C": "Z"}, {"D": "U"}, {"E": "O"}, {"F": "H"}, {"G": "X"}, {"H": "S"}, {"I": "C"}, {"J": "V"}, {"K": "F"}, {"L": "M"}, {"M": "T"}, {"N": "B"}, {"O":"G"}, {"P":"L"}, {"Q":"R"}, {"R":"I"}, {"S": "N"}, {"T": "Q"}, {"U":"J"}, {"V":"W"}, {"W": "A"}, {"X": "Y"}, {"Y": "D"}, {"Z": "K"}]
    reflector = {"A": "E", "B": "J", "C": "M", "D": "Z", "E": "A", "F": "L", "G": "Y", "H": "X", "I": "V", "J": "B", "K": "W", "L": "F", "M": "C", "N": "R", "O":"Q", "P":"U", "Q":"O", "R":"N", "S": "T", "T": "S", "U":"P", "V":"I", "W": "K", "X": "H", "Y": "G", "Z": "D"}

    reflector = 'YRUHQSLDPXNGOKMIEBFZCWVJAT' #Reflector (B)
    rotorI=     'EKMFLGDQVZNTOWYHXUSPAIBRCJ' #RotorC / 1
    rotorII=    'AJDKSIRUXBLHWTMCQGZNPYFVOE' #RotorB / 2
    rotorIII=   'BDFHJLCPRTXVZNYEIWGAKMUSQO' #RotorA / 3
    alpha =     'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#

class RotorA:
    def __init__(self, position):
        self.wires = 'BDFHJLCPRTXVZNYEIWGAKMUSQO'
        self.position = position
        self.alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def getOutput(self, position):
        positionWithOffset = (position + self.position) % 26
        wireOutput = self.wires[positionWithOffset]
        rtv = self.alpha.find(wireOutput)
        return rtv

    def inverseGetOutput(self, input):
        #inputWithOffset = (input - self.position) % 26
        letterOfInput = self.alpha[input]
        rtv = self.wires.find(letterOfInput)
        return rtv

    def rotateRotor(self):
        self.position += 1
    
    def getPosition(self):
        return self.position

    def resetPosition(self):
        self.position = 1

class RotorB:
    def __init__(self, position):
        self.wires = 'AJDKSIRUXBLHWTMCQGZNPYFVOE'
        self.position = position
        self.alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def getOutput(self, position):
        positionWithOffset = (position + self.position) % 26
        wireOutput = self.wires[positionWithOffset]
        rtv = self.alpha.find(wireOutput)
        return rtv

    def inverseGetOutput(self, input):
        #inputWithOffset = (input - self.position) % 26
        letterOfInput = self.alpha[input]
        rtv = self.wires.find(letterOfInput)
        return rtv

    def rotateRotor(self):
        self.position += 1

    def getPosition(self):
        return self.position

    def resetPosition(self):
        self.position = 1

class RotorC:
    def __init__(self, position):
        self.wires = 'EKMFLGDQVZNTOWYHXUSPAIBRCJ'
        self.position = position
        self.alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def getOutput(self, position):
        positionWithOffset = (position + self.position) % 26
        wireOutput = self.wires[positionWithOffset]
        rtv = self.alpha.find(wireOutput)
        return rtv

    def inverseGetOutput(self, input):
        #inputWithOffset = (input - self.position) % 26
        letterOfInput = self.alpha[input]
        rtv = self.wires.find(letterOfInput)
        return rtv

    def rotateRotor(self):
        self.position += 1

    def getPosition(self):
        return self.position

    def resetPosition(self):
        self.position = 1

class Reflector:
    def __init__(self):
        self.wires = 'YRUHQSLDPXNGOKMIEBFZCWVJAT'
        self.alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def getOutput(self, position):
        wireOutput = self.wires[position]
        rtv = self.alpha.find(wireOutput)
        return rtv




def get_rotor_choice():
    choice = int(input("Input: "))
    if choice == 1:
        rotorChoice = "A"
    if choice == 2:
        rotorChoice = "B"
    if choice == 3:
        rotorChoice = "C"
    if choice == 4:
        rotorChoice = "D"
    if choice == 5:
        rotorChoice = "E"
    return rotorChoice

def split(word):
    return list(word)


def rotor_selection_menu():
     print("Input 1 for Rotor A")
     print("Input 2 for Rotor B")
     print("Input 3 for Rotor C")
     print("Input 4 for Rotor D")
     print("Input 5 for Rotor E")

def main():

    outputString = ''
    rotC = RotorC(0)
    rotB = RotorB(0)
    rotA = RotorA(0)
    relf = Reflector()
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
     
    inputString = 'VIWY'
    
    for letter in inputString:


        rotA.rotateRotor()
        if rotA.getPosition() == 25:
            rotA.resetPosition()
            rotB.rotateRotor()
            if rotB.getPosition() == 25:
                rotB.resetPosition()
                rotC.rotateRotor()
                if rotC.getPosition == 25:
                    rotC.resetPosition()


        #-----------------------------------------------------------#

        inputLetterPositon = alpha.find(letter)
        outFromRotorA = rotA.getOutput(inputLetterPositon)
        outFromRotorB = rotB.getOutput(outFromRotorA)
        outFromRotorC = rotC.getOutput(outFromRotorB)

        #-----------------------------------------------------------#
        inverseStart = relf.getOutput(outFromRotorC) 
        #----------------------------------------------------------#

        afterRotorC = rotC.inverseGetOutput(inverseStart) 
        afterRotorB = rotB.inverseGetOutput(afterRotorC)
        afterRotorA = rotA.inverseGetOutput(afterRotorB)

        #-----------------------------------------------------------#
        encryptedLetter = alpha[afterRotorA]

        outputString += encryptedLetter
        print(f"Input was: {letter} Output is: {encryptedLetter}")

    print(outputString)
    return

    print("~~~~~Please select 3 out of 5 rotors to start with using seperate inputs~~~~~")
    rotor_selection_menu()
    rotorChoices = []
    rotorStartingSets = []
    while len(rotorChoices) < 3:
        rotor_choice = get_rotor_choice()
        rotorChoices.append(rotor_choice)
        print("Rotor Choices: ", *rotorChoices)

    for x in rotorChoices:
        print(f"What is the starting setting of rotor {x}?")
        nextRotorSetting = int(input("Pick a number from 1-26: "))
        rotorStartingSets.append(nextRotorSetting)

    rotorChoice1 = rotorChoices[0]
    rotorChoice2 = rotorChoices[1]
    rotorChoice3 = rotorChoices[2]

    rotorSetting1 = rotorStartingSets[0]
    rotorSetting2 = rotorStartingSets[1]
    rotorSetting3 = rotorStartingSets[2]

    #build all 3 rotors with classes
    if rotorChoice1 == 'A':
        rotor1 = RotorA(rotorSetting1)
    if rotorChoice1 == 'B':
        rotor1 = RotorB(rotorSetting1)
    if rotorChoice1 == 'C':
        rotor1 = RotorC(rotorSetting1)

    if rotorChoice2 == 'A':
        rotor2 = RotorA(rotorSetting2)
    if rotorChoice2 == 'B':
        rotor2 = RotorB(rotorSetting2)
    if rotorChoice2 == 'C':
        rotor2 = RotorC(rotorSetting2)

    if rotorChoice3 == 'A':
        rotor3 = RotorA(rotorSetting3)
    if rotorChoice3 == 'B':
        rotor3 = RotorB(rotorSetting3)
    if rotorChoice3 == 'C':
        rotor3 = RotorC(rotorSetting3)

    reflector = Reflector()

# Now we have all our rotors and their starting positions
# Next we get the input string and split it into chars to process

    inputString = input("Please enter the input string to be encrypted/decrypted: ")

    inputChars = split(inputString)
    #print(inputChars) => ['J', 'a', 'k', 'e']

    print("Done.")



#Call the main function to run the program.
main()