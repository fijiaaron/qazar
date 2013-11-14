from cloudtestenvironment.models.customer import Customer

cust = Customer("Aaron", "aarone@one-shore.com")

assert cust.name == "Aaron"
assert cust.email == "aarone@one-shore.com"

print " " 
print "cust: " + cust.email