#Lesson 1 py

from datetime import datetime 
 
def function_name(username, year_of_birth): 
    age_in_years = datetime.now().year - year_of_birth 
    print(username,"let's celebrate your",age_in_years, "years of awesomeness!")
    print("Wishing you a day filled with joy and laughter as you turn,",age_in_years,)
    print(message)
    print("With love and best wishes,")
    print(sender)
username = input("Who's the recipient?\n") 
year_of_birth = int(input("Year of birth\n"))
message = input("Whats your message\n")
sender = input("Who's the sender\n")
 
function_name(username, year_of_birth) 
