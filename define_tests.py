
# Designate the Domains and Score types

domains = {
    1: "Language",
    2: "Spatial",
    3: "Memory",
    4: "Attention",
    5: "Executive Function"
}

score_types = {
    1: "Standard Score",
    2: "Scaled Score",
    3: "T-Score",
    4: "Z-Score"
}

# Building Dictionaries
# This was originally intended to be a loop. 

x = 1

# Language Domain 

language_tests = {}

domain = domains[x]

print("Press 1 to enter a new", domain, "test.") 
print("When you have added all the", domain, "tests administered, press 0.")

response1 = int(input("Enter: "))
print()

# Error if user inputs a number other than 1 or 0

if (response1 > 1):
    print("ERROR!")
    response1 = int(input("Enter: "))
    print(response1)
    print()    
    
while (response1 == 1):
    test = str(input("Enter Test Name: "))
    print(test)
    print()

# For consistent responses, users enter the number assigned to the score type.
# Prints the score_types dictionary 
    print("Find the number associated with the type of score you will be entering for this test.")
    print("You will enter the NUMBER below. Not the name.")
    print()
    print(score_types)
    print()

    scoretype = int(input("Enter Score Type: "))
    print(score_types[scoretype])
    print()

    language_tests[test] = scoretype

    response1 = int(input("Press 1 to enter another test. Press 0 to proceed to the next domain."))
    print()

    if (response1 > 1):
        print("ERROR!")
        response1 = int(input("Enter: "))
        print()  
     
print()
print(domain)
print(language_tests)
print()
print()

x += 1


# Spatial

spatial_tests = {}


domain = domains[x]

print("Press 1 to enter a new", domain, "test.") 
print("When you have added all the", domain, "tests administered, press 0.")

response2 = int(input("Enter: "))
print()

# Error if user inputs a number other than 1 or 0
if (response2 > 1):
    print("ERROR!")
    response2 = int(input("Enter: "))
    print()
    
while (response2 == 1):
    test = str(input("Enter Test Name: "))
    print(test)
    print()

# For consistent responses, users enter the number assigned to the score type.
# Prints the score_types dictionary
    print("Find the number associated with the type of score you will be entering for this test.")
    print("You will enter the NUMBER below. Not the name.")
    print()
    print(score_types)
    print()

    scoretype = int(input("Enter Score Type: "))
    print(score_types[scoretype])
    print()
    
    spatial_tests[test] = scoretype

    response2 = int(input("Press 1 to enter another test. Press 0 to proceed to the next domain."))
    print()

    if (response2 > 1):
        print("ERROR!")
        response2 = int(input("Enter: "))
        print()
     
print()
print(domain)
print(spatial_tests)
print()
print()

x += 1

# Memory 

memory_tests = {}

domain = domains[x]

print("Press 1 to enter a new", domain, "test.") 
print("When you have added all the", domain, "tests administered, press 0.")

response3 = int(input("Enter: "))
print()

# Error if user inputs a number other than 1 or 0
if (response3 > 1):
    print("ERROR!")
    response3 = int(input("Enter: "))    
    print()
    
while (response3 == 1):
    test = str(input("Enter Test Name: "))
    print(test)
    print()

# For consistent responses, users enter the number assigned to the score type.
# Prints the score_types dictionary
    print("Find the number associated with the type of score you will be entering for this test.")
    print("You will enter the NUMBER below. Not the name.")
    print()
    print(score_types)
    print()

    scoretype = int(input("Enter Score Type: "))
    print(scoretype)
    print()

    memory_tests[test] = scoretype
    print(score_types[scoretype])
    print()    

    response3 = int(input("Press 1 to enter another test. Press 0 to proceed to the next domain."))
    print()

    if (response3 > 1):
        print("ERROR!")
        response3 = int(input("Enter: "))        
        print()
     
print()
print(domain)
print(memory_tests)
print()
print()

x += 1


# Attention

attention_tests = {}


domain = domains[x]

print("Press 1 to enter a new", domain, "test.") 
print("When you have added all the", domain, "tests administered, press 0.")

response4 = int(input("Enter: "))
print()

# Error if user inputs a number other than 1 or 0
if (response4 > 1):
    print("ERROR!")
    response4 = int(input("Enter: "))
    print()
    
while (response4 == 1):
    test = str(input("Enter Test Name: "))
    print(test)
    print()

# For consistent responses, users enter the number assigned to the score type.
# Prints the score_types dictionary
    print("Find the number associated with the type of score you will be entering for this test.")
    print("You will enter the NUMBER below. Not the name.")
    print()
    print(score_types)
    print()

    scoretype = int(input("Enter Score Type: "))
    print(score_types[scoretype])
    print()

    attention_tests[test] = scoretype

    response4 = int(input("Press 1 to enter another test. Press 0 to proceed to the next domain."))
    print()

    if (response4 > 1):
        print("ERROR!")
        response4 = int(input("Enter: "))
        print()
     
print()
print(domain)
print(attention_tests)
print()
print()

x += 1

# Executive Function

executive_tests = {}


domain = domains[x]

print("Press 1 to enter a new", domain, "test.") 
print("When you have added all the", domain, "tests administered, press 0.")

response5 = int(input("Enter: "))
print()

# Error if user inputs a number other than 1 or 0
if (response5 > 1):
    print("ERROR!")
    response5 = int(input("Enter: "))
    print()
    
while (response5 == 1):
    test = str(input("Enter Test Name: "))
    print(test)
    print()

# For consistent responses, users enter the number assigned to the score type.
# Prints the score_types dictionary
    print("Find the number associated with the type of score you will be entering for this test.")
    print("You will enter the NUMBER below. Not the name.")
    print()
    print(score_types)
    print()

    scoretype = int(input("Enter Score Type: "))

    executive_tests[test] = scoretype
    print(score_types[scoretype])
    print()

    response5 = int(input("Press 1 to enter another test. Press 0 to proceed to the next domain."))
    print()

    if (response5 > 1):
        print("ERROR!")
        response5 = int(input("Enter: "))
        print()
     
print()
print(domain)
print(executive_tests)
print()
print()

# Allow for more tests to be added

print("Do you need to add any additional tests?")
edits = int(input("Press 1 for yes. Press 0 for no."))
print()

if (edits > 1):
    print("ERROR!")
    edits = int(input("Enter: "))
    print()

while (edits == 1):
    # For consistent responses, users enter the number assigned to the score type.
    # Prints the domains dictionary
    print("Find the number associated with the domain you wish to edit.")
    print("You will enter the NUMBER below. Not the name.")
    print()
    print(domains)
    print()
    
    #Selects the domain to add more tests too.
    #If-Elif statements determine which dictionary to append
    edit_domain = int(input("Enter Domain: "))

    if (edit_domain == 1):
        domain = domains[1]

        print("Press 1 to enter a new", domain, "test.") 
        print("When you have added all the", domain, "tests administered, press 0.")

        response1 = int(input("Enter: "))        
        print()

        if (response1 > 1):
            print("ERROR!")
            response1 = int(input("Enter: "))            
            print()
    
        while (response1 == 1):
            test = str(input("Enter Test Name: "))
            print(test)
            print()

            print("Find the number associated with the type of score you will be entering for this test.")
            print("You will enter the NUMBER below. Not the name.")
            print()
            print(score_types)
            print()

            scoretype = int(input("Enter Score Type: "))
            print(score_types[scoretype])
            print()

            language_tests[test] = scoretype

            response1 = int(input("Press 1 to enter another test. Press 0 to proceed to the next domain."))
            print()

            if (response5 > 1):
                print("ERROR!")
                response5 = int(input("Enter: "))
                print()
     
        print()
        print(domain)
        print(language_tests)
        print()
        print()

        print("Do you need to add any additional tests?")
        edits = int(input("Press 1 for yes. Press 0 for no."))
        print(edits)
        print()
    elif (edit_domain == 2):
        domain = domains[2]

        print("Press 1 to enter a new", domain, "test.") 
        print("When you have added all the", domain, "tests administered, press 0.")

        response2 = int(input("Enter: "))        
        print()

        if (response2 > 1):
            print("ERROR!")
            response2 = int(input("Enter: "))            
            print()
    
        while (response2 == 1):
            test = str(input("Enter Test Name: "))
            print(test)
            print()

            print("Find the number associated with the type of score you will be entering for this test.")
            print("You will enter the NUMBER below. Not the name.")
            print()
            print(score_types)
            print()

            scoretype = int(input("Enter Score Type: "))
            print(score_types[scoretype])
            print()
    
            spatial_tests[test] = scoretype

            response2 = int(input("Press 1 to enter another test. Press 0 to proceed to the next domain."))
            print()

            if (response2 > 1):
                print("ERROR!")
                response2 = int(input("Enter: "))                
                print()
     
        print()
        print(domain)
        print(spatial_tests)
        print()
        print()

        print("Do you need to add any additional tests?")
        edits = int(input("Press 1 for yes. Press 0 for no."))
        print(edits)
        print()
    elif (edit_domain == 3):
        domain = domains[3]

        print("Press 1 to enter a new", domain, "test.") 
        print("When you have added all the", domain, "tests administered, press 0.")

        response3 = int(input("Enter: "))       
        print()

        if (response3 > 1):
            print("ERROR!")
            response3 = int(input("Enter: "))          
            print()
    
        while (response3 == 1):
            test = str(input("Enter Test Name: "))
            print(test)
            print()

            print("Find the number associated with the type of score you will be entering for this test.")
            print("You will enter the NUMBER below. Not the name.")
            print()
            print(score_types)
            print()

            scoretype = int(input("Enter Score Type: "))
            print(scoretype)
            print()

            memory_tests[test] = scoretype
            print(score_types[scoretype])
            print()    

            response3 = int(input("Press 1 to enter another test. Press 0 to proceed to the next domain."))
            print()

            if (response3 > 1):
                print("ERROR!")
                response3 = int(input("Enter: "))                
                print()
     
        print()
        print(domain)
        print(memory_tests)
        print()
        print()

        print("Do you need to add any additional tests?")
        edits = int(input("Press 1 for yes. Press 0 for no."))
        print(edits)
        print()
    elif (edit_domain == 4):
        domain = domains[4]

        print("Press 1 to enter a new", domain, "test.") 
        print("When you have added all the", domain, "tests administered, press 0.")

        response4 = int(input("Enter: "))
        print(response4)
        print()

        if (response4 > 1):
            print("ERROR!")
            response4 = int(input("Enter: "))
            print()
    
        while (response4 == 1):
            test = str(input("Enter Test Name: "))
            print(test)
            print()

            print("Find the number associated with the type of score you will be entering for this test.")
            print("You will enter the NUMBER below. Not the name.")
            print()
            print(score_types)
            print()

            scoretype = int(input("Enter Score Type: "))
            print(score_types[scoretype])
            print()

            spatial_tests[test] = scoretype

            response4 = int(input("Press 1 to enter another test. Press 0 to proceed to the next domain."))
            print()

            if (response4 > 1):
                print("ERROR!")
                response4 = int(input("Enter: "))
                print()
     
        print()
        print(domain)
        print(attention_tests)
        print()
        print()

        print("Do you need to add any additional tests?")
        edits = int(input("Press 1 for yes. Press 0 for no."))
        print(edits)
        print()
    elif (edit_domain == 5):    
        domain = domains[5]

        print("Press 1 to enter a new", domain, "test.") 
        print("When you have added all the", domain, "tests administered, press 0.")

        response5 = int(input("Enter: "))
        print(response5)
        print()

        if (response5 > 1):
            print("ERROR!")
            response5 = int(input("Enter: "))
            print(response5)
            print()
    
        while (response5 == 1):
            test = str(input("Enter Test Name: "))
            print(test)
            print()


            print("Find the number associated with the type of score you will be entering for this test.")
            print("You will enter the NUMBER below. Not the name.")
            print()
            print(score_types)
            print()

            scoretype = int(input("Enter Score Type: "))

            executive_tests[test] = scoretype
            print(score_types[scoretype])
            print()

            response5 = int(input("Press 1 to enter another test. Press 0 to proceed to the next domain."))
            print()

            if (response5 > 1):
                print("ERROR!")
                response5 = int(input("Enter: "))
                print()
     
        print()
        print(domain)
        print(executive_tests)
        print()
        print()

        print("Do you need to add any additional tests?")
        edits = int(input("Press 1 for yes. Press 0 for no."))
        print(edits)
        print()
    else:
       #Final Else is an error message in case users enter a number not associated with a domain
        print("ERROR!")
        print()
        print("Find the number associated with the domain you wish to edit.")
        print("You will enter the NUMBER below. Not the name.")
        print()
    
        print(domains)
        print()
        edit_domain = int(input("Enter Domain: "))

print("Test Entry Complete.")

# Make new nested dictionary of the tests and their score types

d = {
    1: language_tests,
    2: spatial_tests,
    3: memory_tests,
    4: attention_tests,
    5: executive_tests
}
print(d)

# save dict in pickle format as test_lists.p
import pickle

filename = "test_lists.p"

outfile = open(filename, "wb")

pickle.dump(d, outfile)

outfile.close()
    

        
