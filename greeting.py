name=input('What is your name?')
name=name.capitalize()
n_length=len(name)
S_N_L=str(n_length)
FL=name[0]
FL=FL.capitalize()
LL=name[-1]
LL=LL.capitalize()
NFAL=name[1:-1]

print('Hello there, '+name)
print('your name is '+S_N_L+' letters long')
print('Your first letter of your name is '+FL)
print('Your last letter of your name is '+LL)
print('Missing FAL letters: '+NFAL)
