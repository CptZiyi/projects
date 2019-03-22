import urllib2
import hashlib
import getpass

#Input password
print("Check if your password has been found in the haveibeenpwned database of leaked passwords \n")

password = getpass.getpass("Password: \n")

#Import SHA-1 and parse the hash 
sha1 = hashlib.sha1()
sha1.update(password)
hexadecimal = sha1.hexdigest()
firstPart = hexadecimal[0:5]
secondPart = hexadecimal[5:40]

print("First 5 hexadecimal characters of your SHA-1 hash: ")
print(firstPart + "\n")

#Send API request with hash
baseUrl = "https://api.pwnedpasswords.com/range/"
url = baseUrl + firstPart
headers = {'User-Agent' : 'Personal Script'}
req = urllib2.Request(url, None, headers)

content = urllib2.urlopen(req).read()
content = content.splitlines()

found = False

#Compare hashes
for lines in content:
    if(secondPart == lines[0:35].lower()):
        found = True
        print("Hash match found! \n")
        print("Your password has been leaked: " + lines[36:] + " times")
        break

if(found == False):
    print("No hash match found. \n")
    print("Password has not been leaked, yet")