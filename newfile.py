print('Welcome Champion')

response = input('Are you an I.T guru? ')

if response.lower() == 'yes':
    print('let\'s start!, hope you win 🤞 ')
else:
    over = input('Are you sure you want to quit❓ ')
    if over == 'yes':
        quit()

score = 0
        
answer = input('Full meaning of CPU? ')
if answer.lower() == 'central processing unit':
    print('correct ✔')
    score += 1
else:
    print('incorrect ❌')

answer = input('what is the abbreviation for Integrated Development Environment? ')
if answer == 'IDE':
    print('correct ✔')
    score += 1    
else:
    print('incorrect ❌')
    
answer = input('What does VDU stand for? ')
if answer.lower() == 'visual display unit':
    print('correct ✔')
    print('keep going 🔥')
    score += 1
else:
    print('incorrect 😒')
    
answer = input('Name the developer of the quiz ')
if answer.lower() == 'edem':
    print('correct 👍')
    score += 1
elif answer.lower() == 'ishmael':
    print('correct 👍')
    score += 1
elif answer.lower() == 'edem ishmael':
    print('correct 👍')
    score += 1
elif answer.lower() == 'ishmael edem':
    print('correct 👍')    
else:
    print('incorrect 😒')
    
print('Well done on taking this challenge like a champ')
print('you got ' + str(score/4 * 100) + '%' )
print('Care to try again 😊❓ ')

