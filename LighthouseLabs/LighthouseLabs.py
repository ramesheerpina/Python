letterHome=[
    # A title
    "A Letter Home",

    #proseString =
    """
    Hi Dear,

    Just writing to let you know that I have quit my job as a OCCUPATION and I am moving to 
    COUNTRY. The truth is, I have always been passionate about PLURAL_NOUN, and COUNTRY is the best place in the world to 
    build a career around them. I will need a start small-- At first, all i will be allow to do is VERB
    near them, but when people see how ADJECTIVE I can be, I am sure to rise to the top.
 
    Dont worry about me, and tell dad to take good care of my PERSONAL_ITEM. I will be sure to call every 
    HOLIDAY
 
    Love,
    NAME
    """,

#replacements
    [
        ["an occupation", "OCCUPATION"],
        ["a country", "COUNTRY"],
        ["A plural noun", "PLURAL_NOUN"],
        ["A verb like 'run', 'eat', or 'think'", "VERB"],
        ["An adjective like 'friendly', 'long', 'warm'", "ADJECTIVE"],
        ["A personal item", "PERSONAL ITEM"],
        ["A holiday", "HOLIDAY"],
        ["Your Name", "NAME"]
    ]
]

sale = [
    #Title
    "A Great Sale",
    
    # Prose String
    """
    SALE SALE SALE 
    Today only: Buy NUMBER PLURAL_NOUN and get a free NOUN:
    Sign up for our exclusive METAL card and receive 50% off your first purchase
    """,
    # Replacements
    [
        ["A number", "NUMBER"],
        ["A plural noun", "PLURAL_NOUN"],
        ["A noun", "NOUN"],
        ["A type of metal such as aluminium or gold", "METAL"]
    ]
]

showAndTell = [
    #Title
    "Show and Tell",

    """
    Have you seen my pet ANIMAL? It's the best-- No pet can VERB1 as ADVERB as it
    can. It's NUMBER years old, and its name is NAME. You ca VERB2 it if you want, 
    but be careful, because it might VERB.
    """,
    #Replacements
    [
        ["An Animal", "ANIMAL"],
        ["A verb, like 'run', 'jump', 'cry", "VERB1"],
        ["An adverb like 'quickly', 'elegantly', 'transparently'", "ADVERB"],
        ["A name", "NAME"],
        ["A transitive verb, like 'speak to', 'notice','touch'", "VERB2"],
        ["A verb, like 'run', 'jump', 'cry'", "VERB3"]
    ]
]

stories = [
    letterHome,
    sale,
    showAndTell
]
print("Select a story")
for index, story in enumerate(stories):
    title = story[0]
    print(str(index) + " - " + title)

selection = int(input("Choose a stroy"))
story = stories[selection]
proseString = story[1]
replacements = story[2]

for prompt, placeholder in replacements:
    userInput = input(prompt)
    proseString = proseString.replace(placeholder, userInput)
print(proseString)