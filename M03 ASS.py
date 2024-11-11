#7.4 Make a list called things with these three strings as elements: "mozzarella", "cinderella", "salmonella".

things = ["mozzarella","cinderella","salmonella"]

#7.5 Capitalizing the element referring to a person, in this case is "cinderella", which is the second element in the list "things"

things[1] = things[1].capitalize()
print(things)

#7.6 Capilizing the cheesy element, in this case, it would be the 1st element

things[0] = things[0].capitalize()
print(things)

#7.7 Delete the element contain "disease" in the list, then print the list.
things.pop(2)
#.pop() is used here to target the specific index. If .remove() was to be used, you would need to know what the specific element/item is called. 
print(things)
#9.1 Define a function called good() that returns a list
def good(): 
    list = ["Harry","Ron","Hermione"]
    print(list)

good()
    

# 9.2 Define a generator function called get_odds() that returns the odd numbers from range(10). Use a for loop to find and print the third value returned.
def get_odds(): 
    for num in range(10): 
        if num % 2: 
            yield num

for n in get_odds(): 
    print(n)