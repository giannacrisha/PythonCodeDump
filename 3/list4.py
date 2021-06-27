guests = ["mama", "papa", "girby"]

print(len(guests))
print("Dear " + guests[0].title() + ", you are invited to dinner!")
print("Dear " + guests[1].title() + ", you are invited to dinner!")
print("Dear " + guests[2].title() + ", you are invited to dinner!\n")

print (guests[0].title() + " can't make it.")
print (guests[1].title() + " can't make it.\n")

guests[0] = "gwen"
guests[1] = "marco"

print(len(guests))
print("Dear " + guests[0].title() + ", you are invited to dinner!")
print("Dear " + guests[1].title() + ", you are invited to dinner!")
print("Dear " + guests[2].title() + ", you are invited to dinner!\n")

print("A bigger table was found.\n")

guests.append("mama")
guests.insert(2, "papa")
guests.insert(0, "kerby")

print(len(guests))
print("Dear " + guests[0].title() + ", you are invited to dinner!")
print("Dear " + guests[1].title() + ", you are invited to dinner!")
print("Dear " + guests[2].title() + ", you are invited to dinner!")
print("Dear " + guests[-3].title() + ", you are invited to dinner!")
print("Dear " + guests[-2].title() + ", you are invited to dinner!")
print("Dear " + guests[-1].title() + ", you are invited to dinner!\n")

print("The big table broke. Now, there are only two seats available.\n")

guests.pop(0)
guests.pop(0)
guests.pop(0)
guests.pop(1)

print(len(guests))
print("Dear " + guests[0].title() + ", you are still invited to dinner!")
print("Dear " + guests[1].title() + ", you are still invited to dinner!\n")

del guests[0]
del guests[0]

print(guests)
print(len(guests))
