import json
import random

f = open("/Users/vanshbadjate/Documents/Vansh/Programs/Python Program/Projects/would-you-rather/questions.json", 'r')
situation = json.load(f)
f.close()

def game():
    
    
    while True:
        random.shuffle(situation)
        
        for s in situation:
            print("\nWould you rather:")
            print(f"1. {s['question1']}")
            print(f"2. {s['question2']}")
            
            choice = input("Enter your choice (1 or 2) or press 'q' to quit: \n").strip()

            if choice == '1':
                s['count'][0] += 1
            elif choice == '2':
                s['count'][1] += 1
            elif choice.lower() == 'q':
                
                fp = open("/Users/vanshbadjate/Documents/Vansh/Programs/Python Program/Projects/would-you-rather/questions.json", 'w')
                json.dump(situation, fp, indent=4)
                fp.close()
                print("\nThanks for playing!")
                return  
            else:
                print("Invalid choice! Please choose 1, 2, or press 'q' to exit.")
                continue

            total = sum(s['count'])
            per1 = (s['count'][0] / total) * 100
            per2 = (s['count'][1] / total) * 100
            
            print(f"{per1:.2f}% chose {s['question1']}")
            print(f"{per2:.2f}% chose {s['question2']}")

def main():
    print("\nWelcome to 'Would You Rather' Game")
    print("Developed by Vansh Badjate")
    start = int(input("Press 1 to begin:\n"))

    if start == 1:
        game()

if __name__ == '__main__':
    main()
