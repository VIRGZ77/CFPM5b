import time
class Valve():
    
    def __init__(self):
        self.OpenIndication = False
        self.CloseIndication = True
        self.Status = ''
    
    def OpenCmd(self):
        self.CloseIndication = False
        self.status = 'Opening'
        print('Status:', self.status)
        time.sleep(5)
        self.status = 'Opened'
        print('Status:', self.status)
        self.OpenIndication = True
        print('SCADA Valve Open Indication:',self.OpenIndication)
        print('SCADA Valve Closed Indication:',self.CloseIndication)
            
    def CloseCmd(self):
        self.OpenIndication = False
        self.status = 'Closing'
        print('Status:', self.status)
        time.sleep(5)
        self.status = 'Closed'
        print('Status:', self.status)
        self.CloseIndication = True  
        print('SCADA Valve Open Indication:',self.OpenIndication)
        print('SCADA Valve Closed Indication:',self.CloseIndication)
        
Inletvalve = Valve()
Outletvalve = Valve()

print('\n--- Inlet Valve Open Command ---')
Inletvalve.OpenCmd()

print('\n--- Outlet Valve Open Command ---')
Outletvalve.OpenCmd()

print('\n--- Inlet Valve Close Command---')
Inletvalve.CloseCmd()

print('\n--- Outlet Valve Close Command---')
Outletvalve.CloseCmd()