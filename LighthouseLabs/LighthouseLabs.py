proseString = """
Hi Dear,

Just writing to let you know that I have quit my job as a OCCUPATION and I am moving to 
COUNTRY. The truth is, I have always been passionate about PLURAL_NOUN, and COUNTRY is the best place in the world to 
build a career around them. I will need a start small-- At first, all i will be allow to do is VERB
near them, but when people see how ADJECTIVE I can be, I am sure to rise to the top.
 
 Dont worry about me, and tell dad to take good care of my PERSONAL_ITEM. I will be sure to call every 
 HOLIDAY
 """

prompt = "Please provide a holiday"
placeholder = "HOLIDAY"
userinput = input(prompt)
newProseString = proseString.replace(placeholder, userinput)
print(newProseString)
