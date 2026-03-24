print("Let's play Mad Libs Game!")
noun = input("Enter a noun: ")   
verb = input("Enter a verb: ")    
adj = input("Enter an adjective: ")
place = input("Enter a place: ")      
num = input("Enter a number: ")

story = "Oneday," + noun + " went to the " + place + " to " + verb + ". It was a very " + adj + " day. Suddenly, it started raining and " + num + " drops of water fall on " + noun + "'s head. "

print("Here's your Mad Libs story:"+"\n" + story)
