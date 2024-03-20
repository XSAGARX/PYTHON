# this method sorts the list in ascending order. The original list is updated

int = [1,9,6,8,45,96,4,567,94120,5,86,2287945646]
int.sort() # sort methods helps us in sorting of lists 
print(int)

num = [51,6,56,89,5,82,12,65,98,42,245,963,35,8,9,3,2,74]
num.sort() # sorting lists
print(num)

# what if we want to print list in the descending order 

colors=["violet", "indigo", "purple", "green", "orange"]
colors.sort(reverse=True) # here o/p will be in reverse order
print(colors)

num = [4,56,523,96,5,89,8635,12,39566,2,6]
num.sort(reverse=True)
print(num)

# Reverse()

colors = ["violet", "indigo", "blue", "green"]
colors.reverse()
print(colors)

num = [4,52,6,95,7,56,95,4765]
num.reverse()
print(num)


# Index() : this methods returns the index of the first occurrence of the list item.


colors = ["violet", "green", "indigo", "blue"]
print(colors.index("blue"))

num = [4,2,3,4,56,69,5,633,82]
print(num.index(633))

# count (): return the count of the number if items with the given value.

colors =["violet", "green", "indigo", "blue", "black"]
print(colors.count("indigo")) # yei yaha pe count krta hai ki woh strings kitni baar aaya hai


# Copy(): returns copy of the list. This can be done to perform opertaions 
# on the list without modifying the original list.

colors = ["violet", "green", "indigo", "blue"]
newlist = colors.copy()
print(colors)
print(newlist)

#append: this method appends items to the end of the existing list.

colors = ["violet", "indigo", "blue"]
colors.append("green")
print(colors)
colors.append("purple") # append aur extra cheezo ko add kr deta hai
print(colors)

#insert(): this method inserts an item at the given index. user has to specify index and the item
# to be inserted within the insert() method.

colors = ["violet", "indigo", "blue"]
#             [0]      [1]      [2] insert krta hai insert method jaha bhi insert krna ho jiske bich mei uSka index dedo ho jaata hai insert

colors.insert(1, "green") # inserts item at index 1 
print(colors)

# extend(): this method adds an entire list or any other collection datatype(set,tuple,dictionary)
# to the existing list.
# add a list to a list
colors = ["violet", "indigo", "blue"]
rainbow = ["green", "yellow", "orange", "red"] # extend karke print krta hai saara add kr deta hai ek hi list mei
colors.extend(rainbow)
print(colors)

# concatenating two lists: you can simply concatenate two lists to join two lists.
colors = ["violet", "indigo", "blue", "green"]
colors2 = ["yellow", "orange", "red"]
colors3 = ["black", "white", "narangi"]
print(colors + colors2 + colors3 )
