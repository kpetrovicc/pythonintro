#List Intro

friends = ['Sarah', 'John', 'Hannah','Hannah', 'Oscar', 'Toby'] # always use square brackets for lists
#friends[1] = 'Mike' # change the value of an element in a list
#print("Index of Hannah is:" + str(friends.index('Hannah'))) # get the index of an element in a list
#print(friends[1:3]) # use colon to get a range of elements from a list, last element is not included

#List Functions

lucky_numbers = [4, 8, 15, 16, 23, 42]
#friends.extend(lucky_numbers) # add two lists together append at the end of friends
#friends.append('Creed') # add an element to the end of a list
#friends.insert(1, 'Kelly') # insert an element at a specific index
#friends.remove('John') # remove an element from a list
#friends.clear() # remove all elements from a list
#friends.pop() # remove the last element from a list
#print(friends.index('Mike')) # get the index of an element in a list
print(friends.count('Hannah')) # count the number of times an element appears in a list
friends.sort() # sort a list in alphabetical order
print(friends)
lucky_numbers.sort() # sort a list in ascending order
lucky_numbers.reverse() # reverse the order of elements in a list
print(lucky_numbers)

friends2 = friends.copy() # copy a list
print(friends2)