print("Let's play Mad Libs Game!")
noun = input("Enter a noun: ")   
verb = input("Enter a verb: ")    
adj = input("Enter an adjective: ")
place = input("Enter a place: ")      
num = input("Enter a number: ")

print("Choose a story template:")
print("1. Adventure Story")
print("2. Science Story")
print("3. Food Story")

choice = int(input("Enter 1, 2 or 3: "))
if choice == 1:
    story = f"One day, a brave {noun} decided to {verb} through the dark forest of {place}. Armed with {num} weapons and a very {adj} heart, the {noun} faced every danger alone. Historians still talk about this {adj} journey to this day."
elif choice == 2:
    story = f"Scientists at the {place} Institute discovered a {adj} new species of {noun}. It could {verb} at {num} times the speed of light! The lead scientist said it was the most {adj} thing she had ever seen in {num} years of research."
elif choice == 3:
    story = f"A famous chef in {place} invented a {adj} new dish made entirely of {noun}. The secret was to {verb} it for exactly {num} minutes. Food critics called it the most {adj} meal in the last {num} years!"
else:
    story = "Invalid choice!"
print(story)