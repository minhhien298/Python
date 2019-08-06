def function(*args, bob, sally):
    print(args, bob, sally)


values = [1, 2, 3, 4]

function(bob="Hi bob", sally="Hello sally", *values)
function(*values, bob="Hi bob", sally="Hello sally")
function(bob="Hi bob", *values, sally="Hello sally")