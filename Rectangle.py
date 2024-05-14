import random

def roll():
    min_value = 3
    max_value = 20
    roll = random.randint(min_value, max_value)
    return roll

def play_game():
    play_again = input("Continue? (y/n): ").lower()
    print()
    return play_again 

def calculate_rectangle_properties(height, width): #Algebra in my programming class
    perimeter = 2 * (height + width)
    area = height * width
    return perimeter, area

def main():
    while True:
        try:
            print("Rectangle Calculator \n")
            height = roll()
            width = roll()
            print("Height:", height)
            print("Width:", width)
            #Use the algebra
            perimeter, area = calculate_rectangle_properties(height, width)
            print("Perimeter:", perimeter)
            print("Area:", area)
            
            #Janky spaces added to make it look like screenshot
            print("* " * width)     
            for i in range(height - 2):
                print("* " + "  " * (width - 2) + "*")
            print("* " * width + "\n") 
            choice = play_game()
            if choice == "n":
                break
        except ValueError:
            print("Error")
            continue
if __name__ == "__main__":
    main()