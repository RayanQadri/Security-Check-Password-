
password=raw_input("Enter your new password (Must have at least one capital, must have at least one numeric character, must not contain anything"+"\n"+"but numbers, letters and underscores):")

upper_case="QWERTYUIOPASDFGHJKLZXCVBNM"
special_characters="~`!@#$%^&*()-=+[{]}\|;:',<.>/?"

special_count=0
capital_count=0
numbers_count=0

for x in range(0,10):
    if password.count(str(x)) > 0:
        numbers_count += 1
        
for x in upper_case:
    if x in password:
        capital_count += 1
        
for x in special_characters:
    if x in password:
        special_count += 1
        


                
if numbers_count > 0 and capital_count > 0 and special_count == 0:
    print "New password is valid"
else:
    print "New password is invalid"
