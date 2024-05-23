# Advanced Coronavirus Assessment Program

Welcome to the **Advanced Coronavirus Assessment Program**! This program is designed to help you assess your risk of having contracted COVID-19 based on your symptoms and the number of infected people in your area. Please note that this program is not a substitute for professional medical advice. If you believe you may have COVID-19, please consult a healthcare provider.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
- [Acknowledgements](#acknowledgements)

## Features

- User-friendly interaction with prompts and guidelines.
- Risk assessment based on user-inputted symptoms.
- Health guidelines based on the number of infected cases in the user's area.
- Option to restart the assessment after each run.

## Requirements

- Python 3.7.1 or later

## Usage

1. **Clone the repository** or **download the script** to your local machine.
2. **Open a terminal or command prompt** and navigate to the directory containing the script.
3. **Run the script** using the following command:
   ```sh
   python corona_assessment.py
   ```

### Example

```sh
~$ python corona_assessment.py
*********************************************
Enter Your Name: John Doe
*********************************************
Welcome John Doe

I'm an Advanced Coronavirus Program built with Python.

Where are you living? New York

What is the number of infected people in New York?
1 = Less than 1000
2 = Above 1000
3 = Higher than 10,000
4 = Widespread
Select Number: 3
Try to stay away from the elderly. Take necessary precautions and treat everyone around you as potentially infected to resist this pandemic.

Now, I will ask you some questions to know your condition
Please answer with 'yes' or 'no'

Do you suffer from a headache? yes
Q: Result / Risk: 10%

Are you having a fever? no
Q: No Risk

Do you have a dry cough / sneeze? yes
Q: Result / Risk: 40%

Do you have a sore throat? yes
Q: Result / Risk: 30%

Total risk based on your symptoms: 80%
Take a Covid-19 test as soon as possible.

Finally, do you have all the symptoms I mentioned earlier? yes
Go to the hospital as soon as possible for a Covid-19 test as per your entries.

Enter 1 to restart the program or 0 to stop it: 0

Thank you for using this program.
If you like it, please leave a star (:
```

## Code Explanation

### Main Functions

- **`get_user_input(prompt, valid_responses)`**: Prompts the user for input and validates it against a list of valid responses.
- **`provide_guidelines(case)`**: Provides health guidelines based on the number of infected cases.
- **`assess_symptoms()`**: Asks the user a series of questions about their symptoms and calculates the total risk percentage.
- **`main()`**: The main function that runs the program, displaying welcome messages, collecting user inputs, providing guidelines, assessing symptoms, and determining the next steps.

### Code Flow

1. **Welcome Message and Initial Inputs**: The program starts by greeting the user and asking for their name and location. It then asks for the number of infected people in their area and provides relevant health guidelines.
2. **Symptom Assessment**: The program asks the user a series of questions about common COVID-19 symptoms, calculates the risk percentage, and advises if they should get tested.
3. **Restart Option**: After the assessment, the user is given the option to restart the program or exit.

## Acknowledgements

This program is inspired by the need to provide a simple and interactive tool for self-assessment during the COVID-19 pandemic. While it is a helpful tool, it is important to consult a healthcare professional for medical advice and testing.

Thank you for using the Advanced Coronavirus Assessment Program. If you find this tool useful, please give it a star on the repository. Stay safe!
