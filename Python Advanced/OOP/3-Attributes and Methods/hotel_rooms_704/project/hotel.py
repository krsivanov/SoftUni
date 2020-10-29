class Hotel:
    def __init__(self, name):
        self.name = name
        self.guests = 0
        self.rooms = []

    @classmethod
    def from_stars(cls, stars_count):
        name = f"{stars_count} stars Hotel"
        return Hotel(name)
    
    def get_room_by_number(self, room_number):
        return [room for room in self.rooms if room.number == room_number][0]


    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        room =  self.get_room_by_number(room_number)
        result = room.take_room(people)
        if result:
            return result
        self.guests += people
        
    
    def free_room(self, room_number):
        room = self.get_room_by_number(room_number)
        guests_to_remove = room.guests
        result = room.free_room()
        if result:
            return result
        self.guests -= guests_to_remove

    def print_status(self):
        rooms_free = [room for room in self.rooms if not room.is_taken]
        rooms_taken = [room for room in self.rooms if room.is_taken]
        
        message = f''' Hotel {self.name} has {self.guests} total guests
Free rooms: {len(rooms_free)}
Taken rooms: {len(rooms_taken)}'''
        print(message)