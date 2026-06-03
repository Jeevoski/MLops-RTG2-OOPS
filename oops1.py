#initiate a class
class employee:
    #special method/magic method/dunder method-constructor
    def __init__(self):
         print("execution started data")
         self.id=123
         self.salary=50000
         self.designation="SDE"
         print("initiated data/attributes")
    def travel(self,destination):
         print("function is called manually")
         print(f"employee is travelling to {destination}") 
#Create obj / instance
sam=employee()
#sam.travel("kerala")
#print(sam.salary)
#print(sam.id)
print(type(sam))