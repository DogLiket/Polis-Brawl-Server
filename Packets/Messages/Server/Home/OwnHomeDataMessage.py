from Utils.Writer import Writer
from Database.DatabaseManager import DataBase
from Utils.Helpers import Helpers
from Logic.Shop import Shop


class OwnHomeDataMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24101
        self.player = player

    def encode(self):
        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(95)

        self.writeVint(999999)

        self.writeScId(28, 0)
        self.writeScId(43, 0)

        self.writeVint(0)  # array
        for x in range(0):
            pass

        # Selected Skins array
        self.writeVint(0)
        for x in range(0):
            pass

        # Unlocked Skins array
        self.writeVint(0)
        for x in range(0):
            pass

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeBoolean(False)
        self.writeVint(0)
        self.writeBoolean(False)

        self.writeVint(100)
        self.writeVint(99999)

        self.writeVint(1)

        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeBoolean(False)

        self.writeVint(0)
        self.writeVint(1)

        self.writeVint(0) # array
        for x in range(0):
            pass

        self.writeVint(0) # array
        for x in range(0):
            pass

        self.writeVint(200)
        self.writeVint(1000)

        self.writeVint(1)     # array
        self.writeVint(1)

        self.writeVint(99999)
        self.writeVint(0)

        self.writeScId(16, 0)

        self.writeString("RU")
        self.writeString()

        self.writeVint(0) # array
        for x in range(0):
            pass

        self.writeVint(1)

        self.writeVint(10)
        self.writeVint(0)

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(1)
        self.writeVint(1)
        self.writeVint(1)

        self.writeVint(0) # array
        for x in range(0):
            pass

        self.writeVint(0) # array
        for x in range(0):
            pass

        # Logic Events
        self.writeVint(1)
        self.writeVint(1)
        self.writeVint(1)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeScId(15, 0)

        self.writeVint(3)

        self.writeString()
        self.writeVint(0)
        self.writeVint(0) # array
        for x in range(0):
            pass
        self.writeVint(0)

        self.writeVint(0)


        self.writeVint(8)
        for i in [20, 35, 75, 140, 290, 480, 800, 1250]:
            self.writeVint(i)

        self.writeVint(8)
        for i in [1, 2, 3, 4, 5, 10, 15, 20]:
            self.writeVint(i)

        self.writeVint(3)
        for i in [10, 30, 80]:
            self.writeVint(i)

        self.writeVint(3)
        for i in [6, 20, 60]:
            self.writeVint(i)

        self.writeVint(len(Shop.gold))
        for item in Shop.gold:
            self.writeVint(item['Cost'])

        self.writeVint(len(Shop.gold))
        for item in Shop.gold:
            self.writeVint(item['Amount'])

        self.writeVint(0)
        self.writeVint(200)
        self.writeVint(20)
        self.writeVint(8640)
        self.writeVint(10)
        self.writeVint(5)
        self.writeVint(6)
        self.writeVint(50)
        self.writeVint(604800)
        self.writeBoolean(True)
        self.writeVint(0)

        self.writeVint(0) # array
        for x in range(0):
            pass

        self.writeInt(0)
        self.writeInt(1)

        self.writeVint(0) # array
        for x in range(0):
            pass

        self.writeBoolean(False)

        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(0)  # High Id
        self.writeVint(1)  # Low Id

        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(0)
        self.writeVint(0)

        if self.player.name == "Guest":
            self.writeString("Guest")  # Player Name
            self.writeVint(0)
            DataBase.createAccount(self)
        else:
            self.writeString(self.player.name)  # Player Name
            self.writeVint(1)

        self.writeString()

        self.writeVint(8)

        # Unlocked Brawlers & Resources array
        self.writeVint(4)

        self.writeVint(23)
        self.writeVint(0)
        self.writeVint(1)

        self.writeVint(5)
        self.writeVint(1)
        self.writeVint(100)

        self.writeVint(5)
        self.writeVint(8)
        self.writeVint(100)

        self.writeVint(5)
        self.writeVint(9)
        self.writeVint(100)

        # Brawlers Trophies array
        self.writeVint(1)
        self.writeScId(16, 0)
        self.writeVint(1)

        # Brawlers Trophies for Rank array
        self.writeVint(1)
        self.writeScId(16, 0)
        self.writeVint(1)

        self.writeVint(0) # array
        for x in range(0):
            pass

        # Brawlers Upgrade Points array
        self.writeVint(1)
        self.writeScId(16, 0)
        self.writeVint(1)

        # Brawlers Power Level array
        self.writeVint(1)
        self.writeScId(16, 0)
        self.writeVint(1)

        # Gadgets and Star Powers array
        self.writeVint(0)

        # "new" Brawler Tag array
        self.writeVint(0)

        self.writeVint(99999)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(2)
        self.writeVint(1585502369)