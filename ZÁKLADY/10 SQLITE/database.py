import sqlite3
#vytvoř spojení s databází


#vytvor spojeni s databazi
connection = sqlite3.connect("game.db")

#vytvoreni kurzoru, ktery nam umoznuje navigaco po databazi
cursor = connection.cursor

#zapis do db

user_input = input("přidej postavičku do databáze:")

cursor.execute("INSERT INTO characters (name) VALUES (?)",((user_input,))

#potvrzeni vlozeni dat do db
connection.commit()

connection.close()