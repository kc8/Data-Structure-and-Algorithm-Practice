class LogicGate: 

    def __init__(self, n):
        self.label = n
        self.output = None
    
    def get_label(self):
        return self.label

    def get_output(self):
        self.output = self.performGateLogic() #not implmented yet but all objects are initiliazed with this method
        return self.output

class BinaryGate(LogicGate):

    def __init__(self, n):
        LogicGate.__init__(self, n)

        self.pinA = None #output output or logical operation
        self.pinB = None #another output or logical operation
    
    def getPinA(self):
        if self.pinA == None:
            return int(input("Enter Pin A input for Gate " + self.get_label() + "--> "))
        else:
            return self.pinA.getFrom().get_output()
    
    def getPinB(self):
        if self.pinB == None:
            return int(input("Enter Pin B input for Gate " + self.get_label() + "--> "))
        else:
            return self.pinB.getFrom().get_output()
    
    def setNextPin(self, source):
        if self.pinA == None: 
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source 
            else: raise RuntimeError("No Available Pins")


class AndGate(BinaryGate):
   
    def __init__(self, n):
        super(AndGate, self).__init__(n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        if a == 1 and b == 1: 
            return 1
        else: 
            return 0

class OrGate(BinaryGate):
    
    def __init__(self, n):
        super(OrGate, self).__init__(n)
    
    def perfomeGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        if a == 1 or b == 1:
            return 1 
        else: 
            return 0

class UnaryGate(LogicGate):

    def __init__(self, n):
        LogicGate.__init__(self, n) #super is making reference to unaryGate

        self.pin = None
    
    def getPin(self):
        if self.pin == None:
            return int(input("Enter Pin input for Gate " + self.get_label() + "--> "))
        else:
            return self.pin.getFrom().get_output()
    
    def setNextPin(self, source):
        if self.pin == None: 
            self.pin = source
        else: raise RuntimeError("No Available Pins")


class NotGate(UnaryGate):

    def __init__(self, n):
        super(NotGate, self).__init__(n)
    
    def performGateLogic(self):
        if self.getPin(): 
            return 1
        else: 
            return 0 

class Connector:
    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextPin(self)
    
    def getFrom(self):
        return self.fromgate()
    
    def getTo(self):
        return self.togate()




g1 = AndGate("G1")
g2 = AndGate("G2")
g3 = OrGate("G3")
g4 = NotGate("G4")
c1 = Connector(g1,g3)
c2 = Connector(g2,g3)
c3 = Connector(g3,g4)
g1.get_output()
