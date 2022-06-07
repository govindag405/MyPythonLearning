#Define a class which has at least two methods: getString: to get a string from console input, printString: to print the string in upper case.
#Also please include simple test function to test the class methods.
class ConvertUppercase:
    def __init__(self):
        self.string_input = ''
        self.output_string = ''
    def getString(self):
        self.string_input = input("Please enter the string that needs to convert to uppercase: ")
    def printString(self):
        self.output_string = self.string_input.upper()
        print(self.output_string)

string1=ConvertUppercase()
string1.getString()
string1.printString()
