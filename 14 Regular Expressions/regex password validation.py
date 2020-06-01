import re
#create a new password
#at least 8 char long

pattern3 = re.compile(r"[A-Za-z0-9$%#@]{8,}\d")
password = 'an#%i$@a9'

#contains let, numbers $%#@

a = pattern3.search(password)
check = pattern3.fullmatch(password)
print(a)
#has to end with a number
print(check)