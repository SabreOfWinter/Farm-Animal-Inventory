import sqlite3

try:
    sqliteConnection = sqlite3.connect('inventory.db')
    print("Connected to database")

    def create_tables():
        cur = sqliteConnection.cursor()
    
        select_command = "SELECT name FROM sqlite_master WHERE type='table' AND name="

        tables_to_create = [
            str(select_command + "'all_details'"),
            str(select_command + "'all_medical'"),
            str(select_command + "'all_accounts'"),

            str(select_command + "'sheep_details'"),
            str(select_command + "'sheep_medical'"),
            str(select_command + "'sheep_accounts'"),

            str(select_command + "'pigs_details'"),
            str(select_command + "'pigs_medical'"),
            str(select_command + "'pigs_accounts'"),

            str(select_command + "'poultry_details'"),
            str(select_command + "'poultry_medical'"),
            str(select_command + "'poultry_accounts'"),

            str(select_command + "'goats_details'"),
            str(select_command + "'goats_medical'"),
            str(select_command + "'goats_accounts'"),

            str(select_command + "'dogs_and_cats_details'"),
            str(select_command + "'dogs_and_cats_medical'"),
            str(select_command + "'dogs_and_cats_accounts'"),

            str(select_command + "'alpacas_details'"),
            str(select_command + "'alpacas_medical'"),
            str(select_command + "'alpacas_accounts'"),
        ]

        for i in range(len(tables_to_create)):
            table = cur.execute(tables_to_create[i]).fetchall()

            if table == []:
                if i == 0: cur.execute("CREATE TABLE all_details(Id INT, Name TEXT)")
                elif i == 1: cur.execute("CREATE TABLE all_medical(Id INT, Name TEXT)")
                elif i == 2: cur.execute("CREATE TABLE all_accounts(Id INT, Name TEXT)")

                elif i == 3: cur.execute("CREATE TABLE sheep_details(Id INT, Name TEXT)")                    
                elif i == 4: cur.execute("CREATE TABLE sheep_medical(Id INT, Name TEXT)")
                elif i == 5: cur.execute("CREATE TABLE sheep_accounts(Id INT, Name TEXT)")
                
                elif i == 6: cur.execute("CREATE TABLE pigs_details(Id INT, Name TEXT)") 
                elif i == 7: cur.execute("CREATE TABLE pigs_medical(Id INT, Name TEXT)")
                elif i == 8: cur.execute("CREATE TABLE pigs_accounts(Id INT, Name TEXT)")

                elif i == 9: cur.execute("CREATE TABLE poultry_details(Id INT, Name TEXT)") 
                elif i == 10: cur.execute("CREATE TABLE poultry_medical(Id INT, Name TEXT)")
                elif i == 11: cur.execute("CREATE TABLE poultry_accounts(Id INT, Name TEXT)")

                elif i == 12: cur.execute("CREATE TABLE goats_details(Id INT, Name TEXT)") 
                elif i == 13: cur.execute("CREATE TABLE goats_medical(Id INT, Name TEXT)")
                elif i == 14: cur.execute("CREATE TABLE goats_accounts(Id INT, Name TEXT)")

                elif i == 15: cur.execute("CREATE TABLE dogs_and_cats_details(Id INT, Name TEXT)") 
                elif i == 16: cur.execute("CREATE TABLE dogs_and_cats_medical(Id INT, Name TEXT)")
                elif i == 17: cur.execute("CREATE TABLE dogs_and_cats_accounts(Id INT, Name TEXT)")

                elif i == 18: cur.execute("CREATE TABLE alpacas_details(Id INT, Name TEXT)") 
                elif i == 19: cur.execute("CREATE TABLE alpacas_medical(Id INT, Name TEXT)")
                elif i == 20: cur.execute("CREATE TABLE alpacas_accounts(Id INT, Name TEXT)")

            else:
                print("table")
            
            sqliteConnection.commit()
        
except sqlite3.Error as error:
    print("Failed to connect to database", error)
