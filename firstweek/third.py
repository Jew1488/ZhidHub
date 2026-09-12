svoi = ['A', 'H', 'I', 'M', 'O', 'T', 'U', 'V', 'W', 'X', 'Y', '1', '8' ]
alien = ['E', 'J', 'S', 'Z']
alien2 = ['3', 'L', '2', '5']
sr = str(input())
mirror = bool(0)
napalenom = bool(0)
for i in range(int(len(sr)/2+1)):
    regular = bool(0)
    if(sr[i] in svoi):
        if(sr[i] != sr[len(sr)-i-1]):
            napalenom = 1
        else:
            regular = 1
    if(sr[i] in alien and mirror == 0):
        if(sr[len(sr)-i-1] != alien2[alien.index(sr[i])]):
            mirror = 1
        else:
            napalenom = 1
            regular = 1
    if(sr[i] in alien2 and mirror == 0):
        if(sr[len(sr)-i-1] != alien[alien2.index(sr[i])]):
            mirror = 1
        else:
            napalenom = 1
            regular = 1
    if(regular == 0):
        if(sr[i] != sr[len(sr) - 1 - i]):
            napalenom = 1
        mirror = 1
if(napalenom == 1):
    if(mirror == 1):
        print(sr+" is not a palindrome.")
    else:
        print(sr+" is a mirrored string.")
else:
    if(mirror == 1):
        print(sr+" is a regular palindrome.")
    else:
        print(sr+" is a mirrored palindrome.")
        
        
