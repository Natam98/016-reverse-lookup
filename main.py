def isInteger(numeric_string: str) -> bool:
    try:
        if not(float(numeric_string).is_integer()):
            return False
        return True
    except ValueError:
        return False

def create_dictionary() -> dict[str, str]:
    dictionary:dict[str, str]={}
    
    while not (isInteger(elements_number:=input("How many key-value pairs would you like to enter? ")) and int(elements_number)>=0):
        print("You have entered an invalid number of elements!")        
    for _ in range(int(elements_number)):
        key=input("Enter the key: ")
        value=input("Enter the value: ")
        dictionary[key]=value
    return dictionary
    
def reverseLookup(dictionary: dict[str, str], value_to_search: str) -> list[str]:
    return [key for key, value in dictionary.items() if value==value_to_search]


def main():
    dictionary=create_dictionary()
    value_to_search=input("Enter the value to search: ")

    result_list=reverseLookup(dictionary, value_to_search)
    print(f"List of keys = {result_list}")

if __name__=="__main__":
    main()