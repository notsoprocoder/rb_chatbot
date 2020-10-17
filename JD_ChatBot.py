# Importing modules
import re
from nltk.corpus import wordnet

# Building a list of Keywords
list_words = ['hello', 'timings','eat','drink','meal','dinner','food','fun','activity','exciting','enjoy','buy','shopping','good','great','happy','bad','unhappy','sad','upset']
list_syn = {}
for word in list_words:
    synonyms = []
    for syn in wordnet.synsets(word):
        for lem in syn.lemmas():
            # Remove any special characters from synonym strings
            lem_name = re.sub('[^a-zA-Z0-9 \n\.]', ' ', lem.name())
            synonyms.append(lem_name)

    list_syn[word] = set(synonyms)

#print(list_syn)

# Building dictionary of Intents & Keywords
keywords = {}
keywords_dict = {}

# Defining a new key in the keywords dictionary
keywords['greet'] = []

# Populating the values in the keywords dictionary with synonyms of keywords formatted with RegEx metacharacters
for synonym in list(list_syn['hello']):
    keywords['greet'].append('.*\\b' + synonym + '\\b.*')

    # Defining a new key in the keywords dictionary
keywords['how'] = ['.*\\bhow are\\b.*|.*\\bare you\\b.*|.*\\bfeeling\\b.*|.*\\bfeel\\b.*']

keywords['good'] = []

# Populating the values in the keywords dictionary with synonyms of keywords formatted with RegEx metacharacters
for synonym in list(list_syn['good']):
    keywords['good'].append('.*\\b' + synonym + '\\b.*')

for synonym in list(list_syn['great']):
    keywords['good'].append('.*\\b' + synonym + '\\b.*')

for synonym in list(list_syn['happy']):
    keywords['good'].append('.*\\b' + synonym + '\\b.*')

keywords['bad'] = []

# Populating the values in the keywords dictionary with synonyms of keywords formatted with RegEx metacharacters
for synonym in list(list_syn['bad']):
    keywords['bad'].append('.*\\b' + synonym + '\\b.*')

for synonym in list(list_syn['unhappy']):
    keywords['bad'].append('.*\\b' + synonym + '\\b.*')

for synonym in list(list_syn['sad']):
    keywords['bad'].append('.*\\b' + synonym + '\\b.*')

for synonym in list(list_syn['upset']):
    keywords['bad'].append('.*\\b' + synonym + '\\b.*')

# Defining a new key in the keywords dictionary
keywords['timings'] = []

# Populating the values in the keywords dictionary with synonyms of keywords formatted with RegEx metacharacters
for synonym in list(list_syn['timings']):
    keywords['timings'].append('.*\\b' + synonym + '\\b.*')

# Defining a new key in the keywords dictionary
keywords['food'] = ['.*\\beat\\b.*']

# Populating the values in the keywords dictionary with synonyms of keywords formatted with RegEx metacharacters
for synonym in list(list_syn['eat']):
    keywords['food'].append('.*\\b' + synonym + '\\b.*')

for synonym in list(list_syn['meal']):
    keywords['food'].append('.*\\b' + synonym + '\\b.*')

for synonym in list(list_syn['dinner']):
    keywords['food'].append('.*\\b' + synonym + '\\b.*')

for synonym in list(list_syn['food']):
    keywords['food'].append('.*\\b' + synonym + '\\b.*')


# Defining a new key in the keywords dictionary
keywords['drink'] = ['.*\\bdrink\\b.*']

# Populating the values in the keywords dictionary with synonyms of keywords formatted with RegEx metacharacters
for synonym in list(list_syn['drink']):
    keywords['drink'].append('.*\\b' + synonym + '\\b.*')

keywords['pub'] = ['.*\\bpub\\b.*']
keywords['coffee'] = ['.*\\bcoffee\\b.*']

keywords['pennybank'] = ['.*\\bpenny\\b.*|.*\\bbank\\b.*']
keywords['waterwitch'] = ['.*\\bwater\\b.*|.*\\bwitch\\b.*']
keywords['sunhotel'] = ['.*\\bsun\\b.*|.*\\bhotel\\b.*']

keywords['diggles'] = ['.*\\bdiggles\\b.*']
keywords['costacoffee'] = ['.*\\bcosta\\b.*']
keywords['starbucks'] = ['.*\\bstarbucks\\b.*']

keywords['italian'] = ['.*\\bitalian\\b.*']
keywords['pizzamargherita'] = ['.*\\bpizza\\b.*|.*\\bmargherita\\b.*']
keywords['marcos'] = ['.*\\bmarcos\\b.*']
keywords['etna'] = ['.*\\betna\\b.*']

keywords['indian'] = ['.*\\bindian\\b.*']
keywords['bombaybalti'] = ['.*\\bbombay\\b.*|.*\\bbalti\\b.*']
keywords['masala'] = ['.*\\bmasala\\b.*']
keywords['babarelephant'] = ['.*\\bbabar\\b.*|.*\\belephant\\b.*']

keywords['chinese'] = ['.*\\bchinese\\b.*']
keywords['thehoneytree'] = ['.*\\bthe\\b.*|.*\\bhoney\\b.*|.*\\btree\\b.*']
keywords['fortunestar'] = ['.*\\bfortune\\b.*|.*\\bstar\\b.*']
keywords['goldendragon'] = ['.*\\bgolden\\b.*|.*\\bdragon\\b.*']

keywords['thai'] = ['.*\\bthai\\b.*']
keywords['blackstonegrill&thai'] = ['.*\\bblack\\b.*|.*\\bstone\\b.*|.*\\bgrill\\b.*']
keywords['arayathai'] = ['.*\\baraya\\b.*']

keywords['pubgrub'] = ['.*\\bpub grub\\b.*|.*\\bpub\\b.*|.*\\bgrub\\b.*']
keywords['wetherspoons'] = ['.*\\bwetherspoon\\b.*|.*\\bwetherspoons\\b.*|.*\\bspoons\\b.*']
keywords['thewhitecross'] = ['.*\\bwhite\\b.*|.*\\bcross\\b.*']

# Defining a new key in the keywords dictionary
keywords['fun'] = ['.*\\bday\\b.*']

# Populating the values in the keywords dictionary with synonyms of keywords formatted with RegEx metacharacters
for synonym in list(list_syn['fun']):
    keywords['fun'].append('.*\\b' + synonym + '\\b.*')

for synonym in list(list_syn['exciting']):
    keywords['fun'].append('.*\\b' + synonym + '\\b.*')

for synonym in list(list_syn['activity']):
    keywords['fun'].append('.*\\b' + synonym + '\\b.*')

for synonym in list(list_syn['enjoy']):
    keywords['fun'].append('.*\\b' + synonym + '\\b.*')

keywords['shop'] = []

# Populating the values in the keywords dictionary with synonyms of keywords formatted with RegEx metacharacters
for synonym in list(list_syn['buy']):
    keywords['shop'].append('.*\\b' + synonym + '\\b.*')

for synonym in list(list_syn['shopping']):
    keywords['shop'].append('.*\\b' + synonym + '\\b.*')

keywords['zoo'] = ['.*\\bzoo\\b.*']

keywords['aquarium'] = ['.*\\baquarium\\b.*']

keywords['themepark'] = ['.*\\btheme\\b.*|.*\\bpark\\b.*']

keywords['supermarket'] = ['.*\\bsupermarket\\b.*']

keywords['clothes'] = ['.*\\bclothes\\b.*|.*\\bclothing\\b.*|.*\\bdress\\b.*|.*\\bpants\\b.*|.*\\bshirt\\b.*|.*\\btrousers\\b.*|.*\\bsuit\\b.*|.*\\bshoe\\b.*']

keywords['electronics'] = ['.*\\btech\\b.*|.*\\belectronic\\b.*|.*\\bpc\\b.*|.*\\bcomputer\\b.*|.*\\bphone\\b.*|.*\\bplaystation\\b.*|.*\\bxbox\\b.*|.*\\bcamera\\b.*|.*\\btv\\b.*|.*\\bmonitor\\b.*']

keywords['toys'] = ['.*\\btoy\\b.*']

keywords['mens'] = ['.*\\bmen\\b.*']

keywords['womens'] = ['.*\\bwomen\\b.*']

keywords['childrens'] = ['.*\\bchildren\\b.*|.*\\bkid\\b.*|.*\\bboy\\b.*|.*\\bgirl\\b.*|.*\\bbaby\\b.*']



for intent, keys in keywords.items():
    # Joining the values in the keywords dictionary with the OR (|) operator updating them in keywords_dict dictionary
    keywords_dict[intent] =re.compile('|'.join(keys))
#print(keywords_dict)

# Building a dictionary of responses
responses={
    'greet':'\nHello! How can I help you?',
    'how':'\nI\'m very well thank you, how are you?',
    'good':'\nI\'m happy to hear that, how can I help you?',
    'bad':'\nI\'m sorry to hear that I hope you feel better soon, how can I help?',
    'timings':'\nWe are open from 9AM to 5PM, Monday to Friday. We are closed on weekends and public holidays.',
    'fallback':'\nI dont quite understand. Could you repeat that?',
    'food':'\nWe have a number of great local resaurants. what kind of food are you looking for? Italian, Indian, Chinese, Thai, Pub Grub',
    'drink':'\nWe have a number of great local pubs and coffee shops. which are you looking for? Pub or Coffee',
    'pub':'\nHere are a few recommendations which would you like to hear more about? \nPenny Bank\nThe Water Witch\nThe Sun Hotel',
    'coffee':'\nHere are a few recommendations which would you like to hear more about? \nDiggles\nCosta Coffee\nStarbucks',
    'italian':'\nHere are a few recommendations which would you like to hear more about? \nPizza Margherita\nMarcos\nEtna',
    'pizzamargherita':'\nPizza Margherita\n'
    '\nOur Story\n'
    '\nLANCASTER\'S FAVOURITE PIZZA\n'
    '\nWendy Allen , sister of Peter Boizot, founder of Pizza Express,\n'
    'restored the old lino warehouse in Moor Lane in 1979, and opened Pizza Margherita on 4th December that year.\n'
    'Forty years later we still have many people who have been coming on a regular basis since then.\n'
    'We are open from 10am to 10pm, 7 days a week.\n'
    '\nhttps://www.pizza-margherita.co.uk/ \n'
    '\n01524 36333\n'
    '\n2 MOOR LANE, LANCASTER, LA1 1QD\n',
    'marcos':'\nMarcos\n \nWelcome to Marco’s\n' 
    '\na modern Italian kitchen in the heart of Lancaster. The very best in freshly prepared Italian cuisine.\n'
    '\nWednesday – Sunday 5pm – 9pm\n'
    '\nhttps://www.marcosrestaurant.com/ \n'
    '\n01524 844445 \n'
    '\n27 North Rd, Lancaster LA1 1NS\n',
    'etna':'\nEtna\n'
    '\nOwned by an Italian family, authentic Italian dishes. A long time favourite for Lancaster residents.\n'
    '\nTuesday-Saturday 12-2pm & 5-9pm'
    '\nhttps://www.facebook.com/pages/Etna/150626014970606\n'
    '\n01524 69551\n'
    '\n22 New Street, Lancaster, LA1 1EG\n',
    'indian':'\nHere are a few recommendations which would you like to hear more about? \nBombay Balti\nMasala\nBabar Elephant',
    'bombaybalti':'\nBombay Balti\n'
    '\nA local favourite, great quality and value.\n'
    '\nOpen daily 5pm-11pm\n'
    '\nhttps://bombaybalti-lancaster.co.uk/\n'
    '\n01524 844550\n'
    '\n16 China Street, Lancaster, LA1 1EX\n',
    'masala':'\nMasala\n'
    '\n Masala Heysham has been selecting only the finest ingredients to create the most authentic Indian dishes served to you in truly warm surroundings.\n'
    '\nSunday - Thursday 5.00pm - 9.30pm Friday & Saturday 5.00pm - 10.00pm\n'
    '\nhttps://masalaheysham.co.uk/\n'
    '\n01524 850444\n'
    '\n 406 Heysham Road, Heysham, Lancashire LA3 2BJ\n',    
    'babarelephant':'\nBabar Elephant\n'
    '\nA warm welcome to the Babar Elephant Restaurant (exquisite Indian Cuisine with a Lancashire twist).\n' 
    'We have designed and developed our menu with you in mind - high quality cuisine is our aim.\n'
    'We have been serving delicious food across Lancashire for over two decades.\n' 
    'Our team of chefs are highly trained with a vast knowledge of authentic cooking.\n' 
    'We try to use locally sourced ingredients as much as possible.\n' 
    'We hope you enjoy your visit and we look forward to seeing you again and again.\n'
    '\nMon, Tue, Wed, Thu, Fri, 17:30 to 22:00 Sat, Sun, 15:30 to 22:00\n'
    '\nhttps://www.babarelephant.co.uk/contacts\n'
    '\n01524 388670\n'
    '\nMorecambe Road Lancaster LA1 5JB\n',
    'chinese':'\nHere are a few recommendations which would you like to hear more about? \nThe Honey Tree\nFortune Star\nGolden Dragon',
    'thehoneytree':'\nThe Honey Tree\n'
    '\nThe Honey Tree serves delicious Chinese cuisine overlooking the bay on the central promenade of Morecambe, just a few moments from the town centre.\n'
    'Our modern oriental menus offer tempting choices for all the family with a flair for wholesome and expertly prepared dishes.\n' 
    'We have an extensive menu of beef, pork, chicken and duck dishes, and if you are looking for something different, just ask and we will be happily make it for you.\n' 
    'Each dish is cooked fresh to order and served immediately as we want to ensure the freshness of your food.\n' 
    'Some dishes may arrive before others but the aim is we don’t want you to wait, just tuck in and share the Honey Tree experience.\n'
    'Bowls and chopsticks are also available for anyone feeling brave!\n'
    'Whether you are looking for a fun evening out with your loved ones, or a party to remember, we pride ourselves on catering for all your heart’s desires.\n' 
    'Not only does this mean you will get to enjoy our passion for great Chinese food but there is also our celebrated customer service.\n' 
    'We aim to offer you an experience that will keep you coming back time and time again. So why not come and experience our friendly atmosphere and some amazingly good food!\n'
    '\nOpen daily 5:00pm-11:00pm\n'
    '\nhttps://honeytreerestaurant.co.uk/\n'
    '\n01524 423860\n'
    '\n293 Marine Road Central, Morecambe, Lancashire LA4 5BY\n',
    'fortunestar':'\nFortune Star\n'
    '\nWe are a small family business near the heart of Lancaster City. Set up in April 1994, Fortune Star restaurant is the perfect place to eat out.\n' 
    'Whether it is for a birthday, an anniversary, or just as a treat, you\'re bound to find the ideal meal on our menu.\n'
    'We specialise in Cantonese and Oriental dishes, and also cater for vegetarians. Here you can see our restaurant and take-away meals by following the links above.\n' 
    'We hope to see you soon, and hope that you enjoy your meals with us.\n'   
    '\n Thursday            4:30 - 9:00\n'
        'Friday              4:30 - 9:00\n'
        'Saturday            4:30 - 9:00\n'
        'Sunday              4:30 - 9:00\n'
    '\nhttp://www.fortunestarrestaurant.co.uk/\n'
    '\n01524 842828\n'
    '\n16 Dalton Square, St Nicholas Arcades, Lancaster LA1 1PL\n', 
    'goldendragon':'\nGolden Dragon\n'
    '\nFantastic restaurant in the centre of Lancaster. Wide range of dishes available, great service. A real local favourite!\n'
    '\nOpen daily 5:00pm-12am\n'
    '\n01524 33100\n'
    '\n11 George St, Lancaster LA1 1XQ\n',
    'thai':'\nHere are a few recommendations which would you like to hear more about? \nBlack Stone Grill & Thai\nAraya Thai',
    'blackstonegrill&thai':'\nBlack Stone Grill & Thai\n'
    '\nWe have formally owned Bay Steakhouse and Thai Rose and we have now brought both of our unique restaurants together as one so you can enjoy the experience of both together.\n'
    'The Black Stone Grill and Thai is a new venture from Thai Rose and Bay Steakhouse offering a unique experience to Morecambe diners where they can have the choice of mouthwatering steaks or authentic Thai dishes.\n'
    'Choose from a selection of the finest quality meats, steak, seafood, which are brought to your table along with your personal Black Rock Grill, on which you cook the ingredients exactly to your own taste.\n' 
    'The meal is accompanied by a choice of potatoes, rice, dips and vegetables.\n'
    '\nSunday	5:30–9pm\n'
    'Monday	Closed\n'
    'Tuesday	5:30–9:30pm\n'
    'Wednesday	5:30–9:30pm\n'
    'Thursday	5:30–9:30pm\n'
    'Friday	    5:30–10pm\n'
    'Saturday	5:30–10pm\n'
    '\nhttp://www.blackandthai.co.uk/\n'
    '\n01524 409704\n'
    '\n271 Marine Road Central, Morecambe LA4 5BX\n',
    'arayathai':'\nAraya Thai\n'
    '\nFantastic local Thai restaurant with a real authentic feel. Great prices and also has an asian food store next door where you can buy all ingredients to make your own at home!\n'
    '\nSunday	12–3pm, 5–10pm\n'
    'Monday	Closed\n'
    'Tuesday	5–10pm\n'
    'Wednesday	5–10pm\n'
    'Thursday	5–10pm\n'
    'Friday	12–3pm, 5–10pm\n'
    'Saturday	12–3pm, 5–10pm\n'
    '\n01524 383889\n'
    '\n6 Chapel St, Lancaster LA1 1NZ\n',
    'pubgrub':'\nHere are a few recommendations which would you like to hear more about? \nWetherspoons\nThe White Cross\nThe Sun Hotel',
    'wetherspoons':'\nWetherspoons (The Sir Richard Owen)\n'
    '\nYour usual wetherspoons. Great prices and good quality one of the safe choices when eating out in a new area\n'
    '\nSunday	8am–11pm\n'
    'Monday	    8am–11pm\n'
    'Tuesday	8am–12am\n'
    'Wednesday	8am–12am\n'
    'Thursday	8am–12am\n'
    'Friday	    8am–1am\n'
    'Saturday	8am–1am\n'
    '\nhttps://www.jdwetherspoon.com/pubs/all-pubs/england/lancashire/the-sir-richard-owen-lancaster\n'
    '\n01524 541500\n'
    '\n4 Spring Garden St, Lancaster LA1 1RQ\n',
    'thewhitecross':'\nThe White Cross\n'
    '\nThe White Cross is situated in a refurbished cotton mill warehouse which was part of the old Storey’s Cotton Mill that was built next to Lancaster’s main canal.\n'
    '\nMon – Thurs – 11:30am to 23:00pm\n'
    'Fri & Sat – 11:30am to 00:30\n'
    'Sun/ Bank Holiday – 12:00pm to 23:00\n'
    '\nhttps://thewhitecross.co.uk/\n'
    '\n01524 33999\n'
    '\nQuarry Rd, Lancaster, Lancashire LA1 4XT\n',
    'sunhotel':'\nThe Sun Hotel\n' 
    '\nFor over 300 years, our beautiful Georgian building has offered fine drinks, food and rooms in the city centre.\n' 
    'It is one of the few hotels in Lancaster with such historic heritage.\n' 
    'The culture of the building needs to be seen in person.\n'
    'The Sun Hotel & Bar is a quirky boutique 4* hotel in Lancaster, unrivalled in its award-winning range of craft beers, spirits and wines.\n' 
    'Add our 16 luxury en-suite rooms and delicious food, and it’s the perfect combination.\n' 
    'If you’re looking for a central city-centre location, then our hotel and bar is the place for you!\n'
    '\nBreakfast\n' 
    'Monday – Friday 7.30am to 11am | Saturdays 8am to 11am | Sundays & Bank Holidays 8.30am to 11am\n'
    'Food\n'
    'Every day 12noon to 8pm\n'
    'Bar\n'
    'Every day 11am to 11pm\n'
    '\nhttps://www.thesunhotelandbar.co.uk/\n'
    '\n01524 66006\n'
    '\n63-65 Church Street, Lancaster, Lancs LA1 1ET\n',
    'pennybank':'\nPenny Bank\n' 
    '\nits a great local pub with good value draft ales\n'
    '\nMon: 11:00 - 22:00\n'
    'Tues: 11:00 - 22:00\n'
    'Wed: 11:00 - 22:00\n'
    'Thur: 11:00 - 22:00\n'
    'Fri: 11:00 - 22:00\n'
    'Sat: 11:00 - 22:00\n'
    'Sun: 12:00 - 22:00\n'
    '\nhttps://pennybank-lancaster.craftunionpubs.com/\n'
    '\n01524 847666\n'
    '\n53 Penny Street, Lancaster LA1 1UA England\n',  
    'waterwitch':'\nThe Water Witch\n'
    '\nThe multi-award-winning Water Witch is situated on the picturesque Lancaster canal, a five-minute stroll away from the hustle and bustle of the historic city centre.\n'
    'Whether you\'re visiting to sample our superb array of drinks, dine in our restaurant or combining a little of both - you\'re always guaranteed a warm welcome at The Water Witch.\n'
    '\nNew Opening Hours\n'
    '7 days a week: 11am - 9.30pm (last orders)\n'
    '\nFood Serving Hours\n'
    'Mon - Sat: 12-8.30pm\n'
    'Sun: 12-8pm\n'
    '\nhttps://www.waterwitchlancaster.co.uk/\n'
    '\n01524 63828\n'
    '\nWater Witch Lancaster LA1 1SU\n',
    'diggles':'\nDiggles\n'
    '\nFamily owned and independent, since 1963, we are here to give our customers delicious food and beverages at a fair price, in a friendly environment with excellent service.\n' 
    'DIGGLES delicious fresh bread and handmade cakes are loving made in our own bakery.\n'
    '\nSunday	10am–4pm\n'
    'Monday	    8am–6pm\n'
    'Tuesday	8am–6pm\n'
    'Wednesday	8am–6pm\n'
    'Thursday	8am–6pm\n'
    'Friday	    8am–6pm\n'
    'Saturday	8am–6pm\n'
    '\nhttps://diggles.co.uk/\n'
    '\n01524 841841\n'
    '\n51 Market St, St Nicholas Arcades, Lancaster LA1 1JG\n',
    'costacoffee':'\nCosta Coffee\n' 
    '\nGood range of Coffees and Teas at reasonable prices\n'
    '\nOpen daily 8am-5pm\n'
    '\nhttps://www.costa.co.uk/\n'
    '\n01524 845759\n'
    '\n2-6, Ashton Walk, St Nicolas Arcade, St Nicholas Arcades, Lancaster LA1 1ND\n',
    'starbucks':'\nStarbucks\n' 
    '\nA great range of Coffees and Teas, they are a little more expensive but worth it!\n'
    '\nOpen daily 8am-6:30pm\n'
    '\nhttps://www.starbucks.co.uk/\n'
    '\n01524 382261\n'
    '\n19 Market St, St Nicholas Arcades, Lancaster LA1 1HZ\n',
    'fun':'\nI can suggest a number of activities are you interested in any of the following?\n'
    '\nZoo\nAquarium\nPark\nTheme Park',    
    'zoo':'\nWhile Lancaster doesn\'t have a zoo there is one in Blackpool\n'
    '\nBlackpool Zoo\n'
    '\nThe Zoo has various animals including Tigers, Elephants, Lions, Gorillas and Giraffes\n'
    '\nTickets are £19.95 for adults and £15.50 for children 3-15\n'
    '\nOpen daily 10am-4.45pm\n'
    '\nhttps://www.blackpoolzoo.org.uk/\n'
    '\n01253 830830\n'
    '\nE Park Dr, Blackpool FY3 8PP\n',
    'aquarium':'\nWhile Lancaster doesn\'t have an Aquarium there is one in Blackpool\n'
    '\nSEA LIFE Blackpool\n'
    '\nSEA LIFE Centre has a wide variety of Fish, Turtles, Stingrays etc\n'
    '\nTickets are £19.50 for adults and £16.50 for children 3-14\n'
    '\nSaturday, 10am–6pm\n'
    'Sunday, 10am–5pm\n'
    'Monday, 10am–4pm\n'
    'Tuesday, 10am–4pm\n'
    'Wednesday, 10am–4pm\n'
    'Thursday, 10am–4pm\n'
    'Friday, 10am–4pm\n'
    '\nhttp://www.sealife.co.uk/blackpool\n'
    '\n01253 375187\n'
    '\nSEA LIFE Blackpool, Promenade, Blackpool, Lancashire, FY1 5AA\n',
    'themepark':'\nWhile Lancaster doesn\'t have a Theme Park but there is one in Blackpool\n'
    '\nBlackpool Pleasure Beach\n'
    '\nEnjoy a fun day out at the UK\'s most ride intensive theme park. Home to the legendary Big One & Valhalla. Iconic theme park rides for a fun family day out.\n'
    '\nTickets are £39 for adults and £33 for children under 12\n'
    '\nWeekdays 11am-5pm\n'
    'Weekends, 10am–6pm\n'    
    '\nhttps://www.blackpoolpleasurebeach.com/\n'
    '\n0871 222 1234\n'
    '\n525 Ocean Boulevard, Blackpool, Lancashire, FY4 1EZ\n',
    'shop':'\nWe have a number of shops in Lancaster what sort of shops are you looking for?\n'
    'supermarket\n'
    'clothes\n'
    'electronics\n'
    'toys\n',
    'supermarket':'\nThe are a few supermarkets in Lancaster City Centre\n'
    'Marks & Spencer\n'
    'Sainsburys\n'
    'Tesco\n',
    'clothes':'\nThe are a few clothing shops in Lancaster City Centre. What are you looking for?\n'
    'mens\n'
    'womens\n'
    'childrens\n',
    'mens':'\nTopman\nNew Look\nDr Kruger\nRiver Island\nLapel Menswear\nPrimark\nNext',
    'womens':'\nRiver Island\nNew Look\nTopshop\nPrimark\nRoom 12\nNext',
    'childrens':'\nPrimark\nNext\nNew Look',
    'electronics':'\nThe are a few electronic stores in Lancaster City Centre. My suggestions are?\n'
    'Currys PC World\n'
    'CeX\n'
    'Argos\n',
    'toys':'\nThe are a few toys stores in Lancaster City Centre. My suggestions are?\n'
    'The Entertainer\n'
    'The Works\n'
    'Argos\n'
    
    
}
print("Welcome to TourGuide. How may I help you?")

# While loop to run the chatbot indefinitely
while (True):

    # Takes the user input and converts all characters to lowercase
    user_input = input().lower()

    # Defining the Chatbot's exit condition
    if user_input == 'quit':
        print("Thank you for visiting.")
        break

    matched_intent = None

    for intent, pattern in keywords_dict.items():

        # Using the regular expression search function to look for keywords in user input
        if re.search(pattern, user_input):
            # if a keyword matches, select the corresponding intent from the keywords_dict dictionary
            matched_intent = intent

            # The fallback intent is selected by default
    key = 'fallback'
    if matched_intent in responses:
        # If a keyword matches, the fallback intent is replaced by the matched intent as the key for the responses dictionary
        key = matched_intent

        # The chatbot prints the response that matches the selected intent
    print(responses[key])