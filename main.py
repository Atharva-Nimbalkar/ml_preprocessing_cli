from data_description import DataDescription
from data_input import dataInput
from imputation import Imputation
from download import Download

class Preprocessor:
    tasks = [
        '1. About Data',
        '2. Handling null Values',
        '3. Download the modified dataset'
    ]
    
    data = dataInput().Input()

    def __init__(self):
        print("\n\nWELCOME TO THE MACHINE LEARNING PREPROCESSOR CLI!!!\n\n")
    
    def removeTargetColumn(self):
        print("Columns:\n")
        for column in self.data.columns.values:
            print(column, end = "  ")

        while(1):
            column = input("\nWhich is the target variable:  ")
            choice = input("Are you sure?(y/n) ")
            if choice=="y" or choice=="Y":
                self.data.drop([column], axis = 1, inplace = True)
                print("Done.......")
                break
            else:
                print("Try again with the correct column name..")
        return
    def printData(self):
        # print(self.inputData())
        print(self.data)
    def preprocessorMain(self):
        self.removeTargetColumn()
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
            
            elif choice==3:
                Download(self.data).download()  
#if __name__ == "__main__ ":
obj = Preprocessor()
# print(obj.inputData())
#print(obj.printData())
obj.preprocessorMain()