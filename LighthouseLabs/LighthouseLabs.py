proseString = """
Hi Dear,

Just writing to let you know that I have quit my job as a OCCUPATION and I am moving to 
COUNTRY. The truth is, I have always been passionate about PLURAL_NOUN, and COUNTRY is the best place in the world to 
build a career around them. I will need a start small-- At first, all i will be allow to do is VERB
near them, but when people see how ADJECTIVE I can be, I am sure to rise to the top.
 
 Dont worry about me, and tell dad to take good care of my PERSONAL_ITEM. I will be sure to call every 
 HOLIDAY
 
 Love,
 NAME
 """

replacements = [
    ["an occupation", "OCCUPATION"],
    ["a country", "COUNTRY"],
    ["A plural noun", "PLURAL_NOUN"],
    ["A verb like 'run', 'eat', or 'think'", "VERB"],
    ["An adjective like 'friendly', 'long', 'warm'", "ADJECTIVE"],
    ["A personal item", "PERSONAL ITEM"],
    ["A holiday", "HOLIDAY"],
    ["Your Name", "NAME"]
]
for prompt, placeholder in replacements:
    userinput = input(prompt)
    proseString = proseString.replace(placeholder, userinput)

print(proseString)