from ByteStream.Writer import Writer
import random 

class Box(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24111
        self.player = player

    def encode(self):
    	self.writeVInt(203)
    	self.writeVInt(0)
    	self.writeVInt(1)
    	self.writeVInt(10)
    	
    	self.writeVInt(2)
    		
    	
    	self.writeVInt(random.randint(0, 100))
    	self.writeScId(16, 0)
    	self.writeVInt(7)
    	self.writeVInt(0) #29
    	self.writeVInt(0) #52
    	self.writeVInt(0) #23
    	self.writeVInt(0)
    	self.writeVInt(0)
    	
    	self.writeVInt(1)
    	self.writeScId(16, 0)
    	self.writeVInt(4)
    	self.writeVInt(0) #29
    	self.writeVInt(0) #52
    	self.writeScId(23, random.randint(234, 278)) #23
    	self.writeVInt(0)
    	self.writeVInt(0)
    	
    	
   	   	
    	self.writeBoolean(False)
    	self.writeVInt(0)
    	self.writeLogicLong(-1)
    	