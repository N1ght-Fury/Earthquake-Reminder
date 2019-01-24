import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime

import User_Database
import Inform_User
import Message
import Eq_Database

Mail = User_Database.Database_User()
User = User_Database.Database_User()
Earthquake = Eq_Database.Database_Eq()

print("""
Enter '1' to organize user database.
Enter '2' to start the program.
Enter 'q' to exit program.
""")

while True:

    number = input("Command: ")

    if (number == "1"):

        print("""
        Enter '1' to see all users.
        Enter '2' to add a new user.
        Enter '3' to delete a user.
        Enter '4' to update a user.
        Enter '5' to see total number of users.
        Enter '6' to go back to main menu.
        Enter 'q' to exit the program.
        """)

        while True:

            command = input("\nCommand for mail: ")

            # Shows every user
            if (command == "1"):
                Mail.show_mails()

            # Add new user
            elif (command == "2"):
                print("Enter a new mail address:")
                new_mail = input().lower()

                if (Mail.check_if_mail_exists(new_mail)):
                    print("\n" + new_mail, "already exists on database. Please try again.\n")
                    continue

                user_city = input("Enter the name of city you live in: ").upper().replace("İ", "I").replace("Ü","U").replace("Ö","O").replace("Ş", "S").replace("Ç","C")

                print("Would you want to receive mails? (Y/N):")
                user_stat = input().upper()

                if (user_stat == "Y"):
                    user_stat = True
                    text = new_mail + " successfully added to database."

                elif (user_stat == "N"):
                    user_stat = False
                    text = new_mail + " successfully added to database. Be aware that you wont receive any mails."

                else:
                    print("\nInvalid command. Try again.\n")
                    continue

                new_user = User_Database.User(new_mail, user_stat, user_city)
                Mail.add_mail(new_user)

                print(text)


            # Delete user
            elif (command == "3"):

                if (Mail.total_user() == 0):
                    print("\nNo user found on database.\n")
                    continue

                print("Enter the mail address you want to delete:")
                del_mail = input("Mail: ")

                if (Mail.check_if_mail_exists(del_mail) == 0):
                    print("There is no such mail address as " + del_mail + ". Please try again")
                    continue

                print("Are you sure you want to delete " + del_mail + "? (Y/N):")
                yes_no = input().upper()

                if (yes_no == "Y"):
                    Mail.delete_mail(del_mail)
                    print(del_mail, " successfully deleted from database.")

                elif (yes_no == "N"):
                    print("Process canceled.")
                    continue
                else:
                    print("\nInvalid command. Please try again.")


            # Update user
            elif (command == "4"):

                if (Mail.total_user() == 0):
                    print("\nNo user found on database.\n")
                    continue

                print("Enter the mail address you want to update: ")
                update_mail = input()

                if (Mail.check_if_mail_exists(update_mail) == 0):
                    print("There is not such mail address as " + update_mail + ". Please try again")
                    continue

                print("What would you want to change? "
                      "To go back enter 'q' , to change mail "
                      "enter M, to change status enter S, to change city enter 'C':")

                change_what = input().upper()

                # Updating User Mail
                if (change_what == "M"):
                    new_mail = input("Enter a new mail address: ")
                    Mail.update_mail(update_mail, new_mail)
                    print(update_mail, "changed to", new_mail + ".")

                # Updating Status (if 0, wont receive mails, else will)
                elif (change_what == "S"):
                    print("Would you want to get mails or not? (Y/N)")
                    yes_no = input().upper()
                    if (yes_no == "Y"):
                        Mail.update_stat(update_mail, True)
                        print(update_mail, "will now receive mails.")
                    elif (yes_no == "N"):
                        Mail.update_stat(update_mail, False)
                        print(update_mail, "will not receive mails anymore.")
                    else:
                        print("Wrong command. Please try again.")
                        continue

                # Updating the city
                elif (change_what == "C"):
                    print("Enter the new city name: ")
                    new_city = input().upper().replace("İ", "I").replace("Ü","U").replace("Ö","O").replace("Ş", "S").replace("Ç","C")
                    Mail.update_city(update_mail,new_city)
                    print("Your city has changed to " + new_city + ".")

                elif (change_what == "Q"):
                    print("You are back to menu.")

                else:
                    print("\nInvalid comamnd. Try again.\n")


            # Printing total user number
            elif (command == "5"):

                total = Mail.total_user()

                if (total != 0):
                    print("Total number of users: ", total)
                else:
                    print("No user found on database.")

            # Going Back to Main Menu
            elif (command == "6"):
                print("\nYou are on main menu right now.\n")
                break

            elif (command == "q"):
                exit()

            else:
                print("Invalid command. Try again.")


    elif (number == "2"):

        # To see how many times program works
        run = 0

        while True:

            new_earthquake = 0

            # Checking if there are any users on database
            if (Mail.total_user() == 0):

                print("No user found on database. You have to add at least one user to continue.")
                user_mail = input("Mail: ").lower()
                print("Would you want to receive mails?")
                stat = input("Y/N: ").upper()
                city = input("Enter the name of city you live: ").upper().replace("İ","I").replace("Ü","U").replace("Ö","O").replace("Ş","S")

                # Checking Stat
                if (stat == "Y"):
                    stat = True
                elif (stat == "N"):
                    stat = False
                else:
                    print("\nWrong command. Try again.\n")
                    continue

                user_info = User_Database.User(user_mail, stat, city)

                # Adding user to database
                Mail.add_mail(user_info)

                print(user_mail, "successfully added to database.")


            # Getting html content
            try:
                url = "http://www.koeri.boun.edu.tr/scripts/lst9.asp"
                response = requests.get(url)
                html_content = response.content
                soup = BeautifulSoup(html_content, "html.parser")
            except Exception as e:
                print('An error occurred. Time: ' + str(datetime.strftime(datetime.now(), "%X")))
                time.sleep(60)
                continue

            full_text_html = soup.find_all("pre")


            # Splitting full text
            full_text = str(full_text_html[0].text)
            full_text = full_text.split("\n",7)[7]
            list_info = full_text.split("\n")

            main_list = list()

            # Adding every row info to a list
            for info in list_info:
                i = info.split(" ")
                clear_list = [x for x in i if x != ""]
                clear_list =  clear_list[:-1]
                main_list.append(clear_list)

            # Run this code to see what our list looks like
            #for i in main_list:
                #print(i)

            # Running program for 10 times. To check only 5 rows, not every row.
            for item,run_time in zip(main_list,range(0,4)):

                try:

                    # Getting values from list
                    date = str(item[0])
                    action_time = str(item[1])
                    latit = item[2]
                    long = item[3]
                    depth = item[4]
                    strength = item[6]
                    city = str(item[8])

                    try:
                        if (str(item[9]).startswith("(") and str(item[9]).endswith(")")):
                            city = str(item[9]).replace("(","").replace(")","")
                    except:
                        pass
                    try:
                        if (str(item[10]).startswith("(") and str(item[10]).endswith(")")):
                            city = str(item[10]).replace("(","").replace(")","")
                    except:
                        pass
                    try:
                        if (str(item[11]).startswith("(") and str(item[11]).endswith(")")):
                            city = str(item[11]).replace("(","").replace(")","")
                    except:
                        pass
                    try:
                        if (str(item[12]).startswith("(") and str(item[12]).endswith(")")):
                            city = str(item[12]).replace("(","").replace(")","")
                    except:
                        pass
                    try:
                        if (str(item[13]).startswith("(") and str(item[13]).endswith(")")):
                            city = str(item[13]).replace("(","").replace(")","")
                    except:
                        pass

                    earthquake = Eq_Database.Eq(date,action_time,latit,long,depth,strength,city)

                    try:
                        if (not Earthquake.check_if_eq_exists(date, action_time) and float(strength) >= 4.0):

                            Earthquake.add_eq(earthquake)
                            print(earthquake)
                            new_earthquake += 1

                            user_list = User.get_mails(city)

                            text_of_mail = Message.Mail_Message(date, action_time, latit, long, depth, strength, city)
                            for user in user_list:
                                Inform_User.send_mail(user[0], text_of_mail)

                            user_list = User.get_mails("ALL")
                            for user in user_list:
                                Inform_User.send_mail(user[0], text_of_mail)



                    except:
                        print("Something unexpected happened.")


                    # Getting the time value
                    #now = datetime.now()
                    # Parsing time of earthquake to datetime so we can find the difference between these two values in seconds
                    #previous = datetime.strptime(action_time, '%H:%M:%S')
                    #in_secs = (now - previous).seconds

                    # If date is same as today's date
                    # If max 90 seconds has passed since earthquake
                    # And if strength of earthquake is more then 4.0
                    # Which means an earthquake just happened, and might me serious. Since the power of earthquake is more than 4.0
                    # So we will inform user

                    #Change the time check. The site doesnt upload the info immdietaly after eartquake happens
                    #So you probably need to save the info into database and check if earhquake exists

                    #if (date == str(time.strftime("%Y.%m.%d")) and in_secs <= 90 and float(strength) >= 4.0):

                        # To see how many earthquakes happened
                        #new_earthquake += 1

                        # Creating a list of users who lives in the city where earthquake happened so we can inform them
                        # user_list = User.get_mails(city)
                        #text_of_mail = Message.Mail_Message(date,action_time,latit,long,depth,strength,region,city)

                        # Sending mail
                        #for user in user_list:
                            #Inform_User.send_mail(user[0],text_of_mail)

                except:
                    print("List item out of range.")


            run += 1

            if (len(str(run)) == 1):
                run = "0" + str(run)

            if (new_earthquake == 0):
                text = "No earthquake happened. Time: "
            else:
                text = str(new_earthquake) + " new earthquake/s happened. Time: "

            print(str(run) + ". run - " + "Process finished. "
                  + text + str(datetime.strftime(datetime.now(), "%X")))

            run = int(run)

            time.sleep(60)


    elif (number.lower() == "q"):
        exit()

    else:
        print("Invalid command. Try again.")

