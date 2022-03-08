


# multiple statements in a line
print("1st statement"); print("2nd statement")   # not good thing to do but know that ; allows it

first_name = "Testing"
last_name = "World"
number = 1
print(first_name + " " + last_name)
print(first_name + str(number) + " " + last_name)

a, b, c = 10, 20, 30
print(a, b, c)

x = y = z = "testing"
print(x, y, z)

SCHOOL = "FSU"
SCHOOL = "UF"
print(SCHOOL)


def sip_outbound(api_key,country, productClass="sip", topic='event_sip_outbound_anonymized'):
    print(productClass)


sip_outbound(12, "US")       # requires the 2 positional args






