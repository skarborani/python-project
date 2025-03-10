class MneuItem:
    
    def __init__(self,name, cost=0.0):
        self.name=name
        self.cost=cost
        self.ingredients={}
    def __repr__ (self):
      return self.name()+" "+self.cost()+" "+self.ingredients



    def get_name(self):
        return self.name
    def get_cost(self):
        return self.cost
    def get_ingredients(self):
        return self.ingredients
    def set_ingredients(self,water,coffee,suger,milk):
        self.ingredients={"water":water,"coffee":coffee,"suger":suger,"milk":milk}


class Menu:
    def __init__(self):
        
        self.sada=MneuItem("sada",0.5)
        self.sada.set_ingredients(5,5,0,0)
        self.late=MneuItem ("late",1.5)
        self.late.set_ingredients(7,5,2,5)
        self.wasat=MneuItem ("wasat",0.5)
        self.wasat.set_ingredients(5,3,2,0)
        self.foq_alwasat=MneuItem("foq_alwasat",0.5)
        self.foq_alwasat.set_ingredients(5,3,3,0)
        self.heloa=MneuItem  ("heloa",0.5)
        self.heloa.set_ingredients(5,3,5,0)

        self.mylist=[self.sada,self.late, self.wasat,self.foq_alwasat,self.heloa]

    def get_items(self):
        mymenu=""
        for i in range(5):
            mymenu=mymenu  + self.mylist[i].name+" | "
        
        return mymenu
        

    def find_drink(self,name):
        l=""
        for i in range(5):
            if name==self.mylist[i].name:
                l= name
        return l
    def getDrink(self,name): 
        l=1
        for i in range(5):
            o=self.mylist[i].name
            if (name==o):
                l=i
        return self.mylist[l]


        
    

class CoffeeMaker :
    def __init__(self,Water=50,Milk=40,Coffee=50,Suger=100):
        self.water =Water
        self.milk=Milk
        self.coffee=Coffee
        self.suger=Suger
    
    def addRescources(self,Water,Milk,Coffee,Suger):
        
        self.water +=Water
        self.milk +=Milk
        self.coffee +=Coffee
        self.suger +=Suger

    def report(self):
        print("water: ", self.water,"\nmilk : " ,self.milk,"\nsuger: " ,self.suger,"\ncoffee : ",self.coffee,"\n")
    def is_resource_sufficient(self,drink):
        if self.water - drink.ingredients['water'] >=0 and self.milk - drink.ingredients["milk"]>=0 and self.coffee - drink.ingredients["coffee"] >=0 and self.suger - drink.ingredients["suger"]>=0:
            return True
        else:
            return False
    
    def make_coffee(self,order):
        if self.is_resource_sufficient(order):
            self.water=self.water - order.ingredients["water"] 
            self.milk-=order.ingredients["milk"]
            self.coffee-=order.ingredients["coffee"] 
            self.suger-=order.ingredients["suger"]
            return True
        else:
            return False

class MoneyMachine:
    def __init__(self):
       self.profit=0
    def report(self):
        print("current profit: $",self.profit)
    def make_payment(self,cost,drink):
        if cost>=drink.cost:
            self.profit+=cost - drink.cost
            return "payment is accept"
        else:
            return "payment is not accept"


class coffeeMachin:
    def __init__(self):
        self.myMoney=MoneyMachine() 
        self.myMaker=CoffeeMaker()
        self.myMenu=Menu() 



myMachine=coffeeMachin()
i="1"
while i!="":
    
    print("for resource report enter 1 \nfor profit report 2\nfor menu 3 \nfor drink order 4" )
    i=input()
    
    if i=="1":
        myMachine.myMaker.report()
    
    elif i=="2":
        myMachine.myMoney.report()
    
    elif i=="3":
      print(myMachine.myMenu.get_items())
    elif i=="4":
        print("pleas enter drink name")
        name=input()
        
        if name==myMachine.myMenu.find_drink(name):
            if myMachine.myMaker.make_coffee(myMachine.myMenu.getDrink(name)): 
                print("pleas pay")
                cost=float(input())
                if myMachine.myMoney.make_payment(cost,myMachine.myMenu.getDrink(name))=="payment is accept":
                    print("payment is accept\nthe rest of the money is:",cost - myMachine.myMenu.getDrink(name).cost,"\nthe drink is ready\nthank you")
                else:
                    print("payment is not accept")
            else:
                print("sorry the resources are not enough")
        else:
            print("the drink is not exist")

    print("==============================")





