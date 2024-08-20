import pandas as pd
print("Hello, world") 

df = pd.read_excel('C:/Users/james/OneDrive/Desktop/JobTracker.xlsx', sheet_name='Sheet2')

print(df)

def myFunction():
    names = ["James", "Emma", "Noah", "Faith", "Gatsby"]
    for name in names:
        print(name + " McConnell")

myFunction()
print()