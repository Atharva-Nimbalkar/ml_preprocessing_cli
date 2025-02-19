from data_description import DataDescription
from data_input import dataInput
from imputation import Imputation
class Preprocessor:
    tasks = [
        '1. About Data',
        '2. Handling null Values',
        '3. Download the modified dataset'
    ]
    
    data = dataInput().Input()

    def __init__(self):
        print("Welcome!!!")
    
    def printData(self):
        # print(self.inputData())
        print(self.data)
    def whileLoop(self):
        while(1):
            print("\nWhat to do")
            for task in self.tasks:
                print(task)
            choice = int(input("\nEnter your Choice : (Press 0 to go exit)  "))
            if choice == 0:
                exit()
            elif choice==1:
                data_obj = DataDescription(self.data)
                data_obj.describe()
#               self.printData()
                DataDescription(self.data).describe()
            
            elif choice==2:
               # Imputation(self.inputData())
               Imputation(self.data).whileLoop()
#if __name__ == "__main__ ":
obj = Preprocessor()
# print(obj.inputData())
#print(obj.printData())