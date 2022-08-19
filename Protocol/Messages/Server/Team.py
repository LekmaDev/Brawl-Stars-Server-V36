from ByteStream.Writer import Writer
import random


class Team(Writer):
    def __init__(self, client, player, invites=0):
        super().__init__(client)
        self.player = player
        self.id = 24124
        self.invites = invites

    def encode(self):
        #db = DBSQL()
        self.writeVInt(0)
        self.writeBoolean(False)
        self.writeVInt(1)
        
        self.writeInt(0)
        self.writeInt(1)
        
        self.writeVInt(0)
        
        self.writeBoolean(False)
        self.writeVInt(0)
        self.writeVInt(1)
        self.writeDataReference(15, self.player.map_id)
        self.writeBoolean(False)
        
        if self.invites >= 1:
        	self.writeVInt(2)
        else:
        	self.writeVInt(3)

        #PlayerEntry
        self.writeBoolean(True) #Owner
        self.writeLong2(0, self.player.ID) 
        self.writeDataReference(16, 0)
        self.writeDataReference(29, 0)
        
        self.writeVInt(0) #t
        self.writeVInt(0) #ht
        self.writeVInt(9)
        self.writeVInt(3) #State                               
        
        self.writeBoolean(False) # Is ready
        self.writeVInt(0) #Team
        self.writeVInt(52000000 + 69)
        self.writeVInt(52000000 + 69)
        self.writeVInt(0)
        self.writeVInt(0)
        
        self.writeString(self.player.name) #name
        self.writeVInt(100)
        self.writeVInt(28000000)  #  icon
        self.writeVInt(43000000)    # name color
        self.writeVInt(-1)
        self.writeScId(23, 76) #sp
        self.writeScId(23, 255)   #jaja 
        self.writeVInt(0)
        
        

        #PlayerEntry
        self.writeBoolean(True) #Owner
        self.writeLong2(0, 1) 
        self.writeDataReference(16, 49)
        self.writeDataReference(29, 343)
        
        self.writeVInt(0) #t
        self.writeVInt(0) #ht
        self.writeVInt(9)
        self.writeVInt(2) #State                               
        
        self.writeBoolean(False) # Is ready
        self.writeVInt(0) #Team
        self.writeVInt(52000000 + 69)
        self.writeVInt(52000000 + 69)
        self.writeVInt(0)
        self.writeVInt(0)
        
        self.writeString("v36") #name
        self.writeVInt(100)
        self.writeVInt(28000000)  #  icon
        self.writeVInt(43000000)    # name color
        self.writeVInt(-1)
        self.writeScId(23, 390) #sp
        self.writeScId(23, 392)   #jaja 
        self.writeVInt(0)
        
        #PlayerEntry
        self.writeBoolean(True) #Owner
        self.writeLong2(0, 1) 
        self.writeDataReference(16, 45)
        self.writeDataReference(29, 345)
        
        self.writeVInt(0) #t
        self.writeVInt(1250) #ht
        self.writeVInt(9)
        self.writeVInt(3) #State                               
        
        self.writeBoolean(False) # Is ready
        self.writeVInt(0) #Team
        self.writeVInt(52000000 + 69)
        self.writeVInt(52000000 + 69)
        self.writeVInt(0)
        self.writeVInt(0)
        
        self.writeString("github.com/viadev228") #name
        self.writeVInt(100)
        self.writeVInt(28000000)  #  icon
        self.writeVInt(43000006)    # name color
        self.writeVInt(-1)
        self.writeScId(23, 362) # sp
        self.writeScId(13, 364) # gadget
        self.writeVInt(0)
        

        if self.invites != 0:
        	self.writeVInt(1)
        	self.writeVInt(self.invites)
        	for i in range(self.invites):
        		self.writeLong2(0, i)
        		self.writeLong2(0, 1)
        		self.writeString("gene")
        		self.writeVInt(0)
        else:
        	self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)
        self.writeVInt(6)