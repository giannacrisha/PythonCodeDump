guests = ["mama", "papa", "girby"]
print(sorted(reverse=True, guests))

print("Dear " + guests[0].title() + ", you are invited to dinner!")
print("Dear " + guests[1].title() + ", you are invited to dinner!")
print("Dear " + guests[2].title() + ", you are invited to dinner!")

print (guests[0].title() + " can't make it.")
print (guests[1].title() + " can't make it.")

guests[0] = "gwen"
guests[1] = "marco"

print("Dear " + guests[0].title() + ", you are invited to dinner!")
print("Dear " + guests[1].title() + ", you are invited to dinner!")
print("Dear " + guests[2].title() + ", you are invited to dinner!")

print("A bigger table was found.")

guests.append("mama")
guests.insert(2, "papa")
guests.insert(0, "kerby")

print("Dear " + guests[0].title() + ", you are invited to dinner!")
print("Dear " + guests[1].title() + ", you are invited to dinner!")
print("Dear " + guests[2].title() + ", you are invited to dinner!")
print("Dear " + guests[-3].title() + ", you are invited to dinner!")
print("Dear " + guests[-2].title() + ", you are invited to dinner!")
print("Dear " + guests[-1].title() + ", you are invited to dinner!")

print("The big table broke. Now, there are only two seats available.")

guests.pop(0)
guests.pop(0)
guests.pop(0)
guests.pop(1)

print("Dear " + guests[0].title() + ", you are still invited to dinner!")
print("Dear " + guests[1].title() + ", you are still invited to dinner!")

del guests[0]
del guests[0]

print(guests)
