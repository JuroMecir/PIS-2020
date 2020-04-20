from zeep import Client

class Web_service():
    def __init__(self):
        self.students = Client(wsdl='http://pis.predmety.fiit.stuba.sk/pis/ws/Students/Team093Student?WSDL')
        self.applications = Client(wsdl='http://pis.predmety.fiit.stuba.sk/pis/ws/Students/Team093Application?WSDL')
        self.rooms = Client(wsdl='http://pis.predmety.fiit.stuba.sk/pis/ws/Students/Team093Room?WSDL')
