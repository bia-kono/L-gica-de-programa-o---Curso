def main():
    camelCase = input("camelCase: ")
    
    # create the variable to 
    snake_case = " "
    
    for char in camelCase:
        if char.isupper():
            snake_case += "_" + char.lower()
        else:
            snake_case += char
    print("Snake_case: ", snake_case.lstrip("_"))
    
if __name__ == "__main__":
    main()        

# Prompt the user for the name of a variable in camel case
# Read the input and store it in a variable (e.g., camelCaseName)

# Initialize an empty string for snake case (e.g., snake_case_name)

# For each character c in camelCaseName:
#     If c is uppercase:
#         Add "_" followed by lowercase(c) to snake_case_name
#     Else:
#         Add c to snake_case_name

# Output snake_case_name

    


