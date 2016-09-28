# This on is like your scripts with argv
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

#this just takes one arguement 
def print_one(arg1):
	print "arg1: %r " % arg1 

#this takes no arguements
def print_none():
	print "I go nothin'."

print_two("Myia", "Dickens")
print_two_again("Myia", "Dickens")
print_one("First!")
print_none()