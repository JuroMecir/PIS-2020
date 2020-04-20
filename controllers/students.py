class Student ():
    def __init__(self, id, name, surname, email, password, date_of_birth, address, points, room_id):
        self.id = id
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password
        self.date_of_birth = date_of_birth
        self.address = address
        self.points = points
        self.room_id = room_id

    def get_id(self):
        return self.id
        #koment


