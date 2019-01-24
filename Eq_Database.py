import sqlite3

class Eq():

    def __init__(self,date,action_time,latit,long,depth,strength,city):

        self.date = date
        self.action_time = action_time
        self.latit = latit
        self.long = long
        self.depth = depth
        self.strength = strength
        self.city = city

    def __str__(self):
        return "New earthquake at {} with the strength of {}.".format(self.city,self.strength)


class Database_Eq():

    def __init__(self):

        self.connect_database()

    def connect_database(self):

        self.connection = sqlite3.connect("Earthquake.db")
        self.cursor = self.connection.cursor()

        query = "create table if not exists " \
                "Tbl_Earthquakes (" \
                "Date_of text," \
                "Action_Time text," \
                "Latit text," \
                "Long text," \
                "Depth text," \
                "Strength text," \
                "City text)"

        self.cursor.execute(query)
        self.connection.commit()


    def add_eq(self,Eq):

        query = "insert into Tbl_Earthquakes values (@p1,@p2,@p3,@p4,@p5,@p6,@p7)"
        self.cursor.execute(query,(Eq.date,Eq.action_time,Eq.latit,Eq.long,Eq.depth,Eq.strength,Eq.city))
        self.connection.commit()


    def check_if_eq_exists(self,date,action_time):

        query = "select * from Tbl_Earthquakes where Date_of = @p1 and Action_Time = @p2"
        self.cursor.execute(query,(date,action_time))
        list_items = self.cursor.fetchall()

        if (len(list_items) == 0):
            return False

        return True

