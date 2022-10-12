from abc import ABC ,abstractmethod
from dis import get_instructions

class Band():
    instances=[]
    def __init__(self,name,members):
        self.name=name
        self.members=members
        Band.instances.append(self)
    
    def play_solos(self):
        member=[]
        for solo in self.members:
            member.append(solo.play_solos())

        return member
        
    @classmethod
    def to_list(cls): 
        return Band.instances

class Musician(ABC):

    def __init__(self,name):
        self.name=name

    def __str__(self):
        return f'My name is {self.name} and I play {self.get_instrument()}'

    def __repr__(self):
        return f"{self.__class__.__name__} instance. Name = {self.name}" 

    def get_instrument(self):
        pass

    def play_solo(self):
        return self.play_solos()
        


class Drummer(Musician):

    def __init__(self,name):
        self.name=name
    
    def play_solos(self):
        return "rattle boom crash"

    def get_instrument(self):
        return 'drums'

class Guitarist(Musician):

    def __init__(self,name):
        self.name=name
    
    def play_solos(self):
        return "face melting guitar solo"

    def get_instrument(self):
        return 'guitar'

class Bassist(Musician):

    def __init__(self,name):
        self.name=name

    def play_solos(self):
        return "bom bom buh bom"

    def get_instrument(self):
        return 'bass'



# members = [
#         Guitarist("Kurt Cobain"),
#         Bassist("Krist Novoselic"),
#         Drummer("Dave Grohl"),
#     ]

# some_band = Band("Nirvana", members)

# for member in some_band.members:
#     if member.get_instrument() == "guitar":
#         print(member.play_solo())  # == "face melting guitar solo"
#     elif member.get_instrument() == "bass":
#         print(member.play_solo())  # == "bom bom buh bom"
#     elif member.get_instrument() == "drums":
#         print(member.play_solo())  # == "rattle boom crash"

