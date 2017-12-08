import os

header = ["textuilib"]
debug = [False]

class menu:
    def __init__(self, name, menuItems):
        self.menuItems = []
        
        if isinstance(name, str):
            self.name = name
            
        if isinstance(menuItems, list):
            for m in menuItems:
                if isinstance(m, menuItem):
                    self.menuItems.append(m)
                    
    def getName(self):
        return self.name
    
    def getOptions(self):
        return self.menuItems
    
    def displayOptions(self):
        for i, o in enumerate(self.menuItems):
            if isinstance(o, menuItem):
                print(str(i+1) + ". " + o.text)
    
    def displayName(self):
        print(self.name)
        
    def displayMenu(self):
        clear()
        displayHeader(self)
        self.displayOptions()
        if self.menuItems != []:
            return choice(self)
        
    def addMenuItem(self, item): #Takes a menuItem, not an int
        if isinstance(item, menuItem):
            self.menuItems.append(item)
            
    def removeMenuItem(self, item): #Takes a menuItem, not an int
        if isinstance(item, menuItem):
            for o in self.menuItems:
                if item == o:
                    self.menuItems.remove(o)
        
    def clearMenuItems(self):
        for o in self.menuItems:
            self.menuItems.remove(o)
            
class menuItem:
    def __init__(self, text, function):
        if isinstance(text, str) and isinstance(function, str):
            self.text = text
            self.function = function
            
class TypeMismatch(Exception):
    def __init__(self, mismatch):
        Exception.__init__(self, mismatch)
        
def setHeader(h):
    try:
        header.remove(header[0])
        if h[len(h)] != " ":
            h = h + " "
            header.append(h)
        else:
            header.append(h)
    except:
        if h[len(h) - 1] != " ":
            h = h + " "
            header.append(h)
        else:
            header.append(h)

def displayHeader(menu):
    print(header[0] + '- ' + menu.getName())
    print()

def clear():
    if os.name == 'nt':
        clr = 'cls'
    else:
        clr = 'clear'
    os.system(clr)

def choice(menu):
    print('')
    print('Choose an Option:')
    try:
        while True:
            option = int(input('Option: '))
            if option-1 < len(menu.menuItems):
                return menu.menuItems[option-1].function
            else:
                print("Invalid option!")

    except (KeyboardInterrupt, SystemExit):
        raise
