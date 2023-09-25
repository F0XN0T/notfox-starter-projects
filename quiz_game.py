print("Welcome to the quz qiz quiz!")

playing = input("Are you sure you want to play? ")

if playing.lower() != "yes":
    quit()

print("Alrighty then! I hope you are ready! :)")
score = 0

answer = input("What day is Halloween? ")
if answer.lower() == "october 31":
    print('Correct!')
    score += 1
else:
    print("What are you DUMB?!")

answer = input("Did you get the last question correct? ")
if answer.lower() == "yes":
    print('Im glad to hear that you know when im at your house!')
    score += 1
else:
    print("I feel bad for you... to bad you don't know im your wall!")

answer = input("Do you worship God? ")
if answer.lower() == "yes":
    print('May god bless you AMEN')
    score += 1
else:
    print("You need to go to church you unholy being!")

answer = input("What does LGBTQ Stand For? ")
if answer.lower() == "lesbian gay bisexual transgender queer":
    print('You are wrong!')
    score += 1
else:
    print("I'm so proud of you for supporting lebron giving back to community!")

answer = input("Who's showing you this quiz? ")
if answer.lower() == "notfox":
    print('You are right! But did you subscribe to him? @notfoxs on youtube!')
    score += 1
else:
    print("Great this good to hear but! Its @notfoxs on youtube!")

answer = input("Did you pray today? ")
if answer.lower() == "yes":
    print('You are a good person!')
    score += 1
else:
    print("I'ts ok its never to late to pray! We all are sinners!")

answer = input("Do you like this quiz? ")
if answer.lower() == "yes":
    print('I like the quiz too!')
    score += 1
else:
    print("How dare you not like this quiz! You should feel bad!")

answer = input("Do you believe in santa? ")
if answer.lower() == "yes":
    print('Ho Ho Ho! Motha Fucka!')
    score += 1
else:
    print("Guess who else I need to add to the naughty list! YOU!")

answer = input("What does NNN stand for? ")
if answer.lower() == "no nut november":
    print('you get a free nut pass')
    score += 1
else:
    print("WOW! You must be really smart!")

answer = input("Are you Gay? ")
if answer.lower() == "yes":
    print('Congratulation Lesbo - Tico')
    score += 1
else:
    print("You GAY anyway! IDK smthing like that - Tico")

answer = input("Does it work? ")
if answer.lower() == "yes":
    print('You know what im talking about you pevert!')
    score += 1
else:
    print("I feel bad for you! Small PP Wide coochie!")

answer = input("Do you like girls? I mean Womens! ")
if answer.lower() == "no":
    print('Wow ME TOO! - Tico')
    score += 1
else:
    print("Ew that pussy stank! - Tico Friend")

answer = input("When is Happy New Year? ")
if answer.lower() == "december 31":
    print('I think so too!')
    score += 1
else:
    print("Maybe it is! I'm not so sure")

answer = input("When will you subcribe to notfox? (Today, Tomorrow, Next Week, or Never) ")
if answer.lower() == "today":
    print('thank you for subscribing!')
    score += 1
else:
    print("You know what! I think we might have a problem!")

answer = input('Say "I love you" ')
if answer.lower() == "i love you":
    print('male: You are gay!')
    print('female: i hope you are not ugly!')
    score += 1
else:
    print("i loved you but you didn't say it back!")

answer = input("Do it be squirtin and fartin? ")
if answer.lower() == "yes":
    print('IM DISGUSTED! - Tico clone')
    score += 1
else:
    print("Next time do it on my face! - Tico clone")

answer = input("Guess what Bapple Saus is! ")
if answer.lower() == "apple sauce":
    print('Yessir Bapple Saus is apple sauce!')
    score += 1
else:
    print("You are wrong! SMH")

answer = input("I finish the lyrics! This is my song and no one can take it away... ")
if answer.lower() == "its been so long but now you're here":
    print('And I wonder if you know what it means to find your dreams come true')
    score += 1
else:
    print("Come on Man its My Song by Labi Siffre")

answer = input("Did you know that this is notfox first successful coded quiz? ")
if answer.lower() == "no":
    print('Well now you know!')
    score += 1
else:
    print("Wow! Not even I knew that!")

answer = input("papa franku is now...? ")
if answer.lower() == "joji":
    print('how did you know that?')
    score += 1
else:
    print("well i guess you need to watch more filthy frank videos!")

answer = input("Why are you lonely? ")
if answer.lower() == "fat and gay":
    print('you are still fat and gay!')
    score += 1
else:
    print("Why don't girls look on the inside? There's no such thing as the friend zone!")

print("you have " + str(score) + " more extra years to live!")
print("don't worry i'll give you " + str((score / 21) * 100) + "%. of my stock to you")