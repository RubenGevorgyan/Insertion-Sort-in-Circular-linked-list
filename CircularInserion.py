class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class CircularList:
    def __init__(self):
        self.headval = None

    def addnode(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        last = self.headval
        while(last.nextval and last.nextval!=self.headval):
            last = last.nextval
        last.nextval=NewNode
        last.nextval.nextval=self.headval
        
        
        
    def printlist(self):
        printval = self.headval.nextval
        print(self.headval.dataval)
        while (printval and printval!=self.headval):
            print (printval.dataval)
            printval = printval.nextval
    
    def get_values(self):
        vals=[]
        vals.append(self.headval.dataval)
        val=self.headval.nextval
        while (val and val!=self.headval):
            vals.append(val.dataval)
            val=val.nextval
        return vals

class Sort:
        
    def sort(self,vals):
        for i in range(1, len(vals)): 
            temp = vals[i] 
            j = i-1
            while (j >=0 and temp < vals[j])   : 
                    vals[j+1] = vals[j] 
                    j -= 1
            vals[j+1] = temp 
        return vals
        
        
        
def main():
    clist=CircularList()
    for i in range (0,int(input("How many imputs do you want to input?"))):
        clist.addnode(input("Input your input"))
    insertion=Sort()
    numbers=insertion.sort(clist.get_values())
    for i in range(0,len(numbers)): 
        print (numbers[i]) 

main()
