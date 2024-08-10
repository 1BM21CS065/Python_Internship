def word_count(string):
    words = string.split() #This function is used to split the sentences into words 
    return len(words) #This functions gives the length of the string/sentence

def main():
    while True:
        user_input = input("Enter the sentence (or press 0 to exit): ")
        if user_input == '0':
            break
        elif not user_input:
            print("Error-Empty input!!.")
            continue
        result = word_count(user_input)
        print(f"The word count is: {result}")

if __name__ == "__main__":
    main()