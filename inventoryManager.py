from tkinter import *
class inventoryItem():
    def __init__(self,name,quantity):
        self.itemName=name
        self.itemQuantity=quantity
    def setName(self,name):
        self.itemName=name
    def getName(self):
        return self.itemName
    def setQuantity(self,quantity):
        self.itemQuantity=quantity
    def getQuantity(self):
        return self.itemQuantity
class inventory():
    def __init__(self):
        self.inventoryList=[]
    def addItemToList(self,name,quantity):
        self.inventoryList.append(inventoryItem(name,quantity))
    def removeItem(self,index):
        self.inventoryList.pop(index)
    def getInventoryList(self):
        return self.inventroyList
    def updateItem(index,name,quantity):
        self.inventoryList[index]=inventoryItem(name,quantity)
    def getItem(self,index):
        return self.inventoryList[index]
    def getInventory(self):
        return self.inventoryList
class inventoryManagerView():
    def __init__(self):
        
        self.inventory=inventory()
        self.window = Tk()
        
        self.window.title("Inventroy Management")
        Label(self.window, text="Item Name:").pack(side=LEFT)
        self.name=StringVar()
        self.entryName=Entry(self.window, textvariable=self.name).pack(expand=1, side=LEFT)
        Label(self.window, text="Quantity:").pack(side=LEFT)
        self.quantity=IntVar()
        self.buttonName=StringVar()
        self.buttonName.set("Add to inventory")
        self.entryQuantity=Entry(self.window, textvariable=self.quantity).pack(expand=1, side=LEFT)
        self.button1=Button(self.window,textvariable=self.buttonName,relief=RAISED,command=self.addToInventory).pack(expand=1, side=LEFT)
        self.listBox=Listbox(self.window,selectmode=SINGLE)
        self.listBox.bind("<Double-Button-1>",self.updateItemPrep)
        self.listBox.pack()
        self.displayItems()
        self.window.mainloop()
    def addToInventory(self):
        self.inventory.addItemToList(str(self.name.get()),str(self.quantity.get()))
        if(self.buttonName.get()=="Update"):
            self.buttonName.set("Add to inventory")
        self.name.set("")
        self.quantity.set("")
        self.displayItems()
        print("The item "+str(self.name)+" has been added ")
    def updateItemPrep(self,event):
        widget=event.widget
        index=int(widget.curselection()[0])
        item=self.inventory.getItem(index)
        self.inventory.removeItem(index)
        self.displayItems()
        self.quantity.set(item.getQuantity())
        self.name.set(item.getName())
        self.buttonName.set("Update")
    def displayItems(self):
        self.listBox.delete(0,END)
        for item in self.inventory.getInventory():
            self.listBox.insert(END,str(item.getName())+" "+str(item.getQuantity()))
            

inventoryManagerView()
