import time

def get_user_input(prompt, valid_responses):
    response = input(prompt).strip().lower()
    while response not in valid_responses:
        print("Invalid input. Please try again.")
        response = input(prompt).strip().lower()
    return response

def provide_guidelines(case):
    guidelines = {
        "1": "You should wear a mask when going out, keep a distance with people, and wash your hands well after touching surfaces. Do not touch your face until you wash your hands.",
        "2": "Adhere to the health conditions to avoid infection and avoid the spread of the epidemic on a larger scale. Try not to go out unless absolutely necessary.",
        "3": "Try to stay away from the elderly. Take necessary precautions and treat everyone around you as potentially infected to resist this pandemic.",
        "4": "Stay at home, and if any symptoms appear, get a check-up as soon as possible."
    }
    print(guidelines.get(case, "Wrong Input"))

def assess_symptoms():
    symptoms = {
        "Do you suffer from a headache? ": 10,
        "Are you having a fever? ": 20,
        "Do you have a dry cough / sneeze? ": 40,
        "Do you have a sore throat? ": 30
    }

    total_risk = 0
    for question, risk in symptoms.items():
        response = get_user_input(question, ['yes', 'no', '1', '2'])
        if response in ['yes', '1']:
            print(f"Q: Result / Risk: {risk}%")
            total_risk += risk
        else:
            print("Q: No Risk")
        time.sleep(0.5)

    print(f"\nTotal risk based on your symptoms: {total_risk}%")
    if total_risk >= 30:
        print("Take a Covid-19 test as soon as possible.")

def main():
    print("********GIVE STAR ONLY IF YOU LIKE********")
    print()
    while True:
        print("~" * 45)
        name = input("Enter Your Name: ")
        print("~" * 45)
        print(f"Welcome {name}\n")
        time.sleep(0.5)
        print("I'm an Advanced Coronavirus Program built with Python\n")
        time.sleep(0.5)
        location = input("Where are you living? ")
        time.sleep(0.5)
        print(f"\nWhat is the number of infected people in {location}?")
        print("\n1 = Less than 1000\n2 = Above 1000\n3 = Higher than 10,000\n4 = Widespread")
        case = get_user_input("Select Number: ", ['1', '2', '3', '4'])
        provide_guidelines(case)

        print("\nNow, I will ask you some questions to know your condition")
        print("Please answer with 'yes' or 'no'\n")
        time.sleep(1)
        assess_symptoms()

        response = get_user_input("\nFinally, do you have all the symptoms I mentioned earlier? (yes or no) ", ['yes', 'no', '1', '2'])
        if response in ['yes', '1']:
            print("Go to the hospital as soon as possible for a Covid-19 test as per your entries.")
        else:
            print("Q5: Good")

        re = get_user_input("Enter 1 to restart the program or 0 to stop it: ", ['1', '0'])
        if re == '0':
            break

    print("\nThank you for using this program.")
    print("If you like it, please leave a star (:")
    
if __name__ == "__main__":
    main()
