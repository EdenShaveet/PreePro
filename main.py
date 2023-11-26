import art
import random
import re
import sys
import time
from datetime import datetime
from getpass import getpass
from prettytable import PrettyTable

def get_points_age(age):
    if age < 20:
        return 3
    elif 20 <= age <= 34:
        return 0
    elif 35 <= age <= 39:
        return 2
    else:
        return 4

def get_points_height(height):
    if height < 150:
        return 2
    else:
        return 0

def calculate_bmi(height, weight):
    height_in_meters = height / 100
    bmi = weight / (height_in_meters ** 2)
    if bmi < 24.9:
        return 0
    elif bmi < 29.9:
        return 1
    else:
        return 3

def get_points_preg_type(preg_type):
    if preg_type == 1:
        return 0
    elif preg_type == 2:
        return 4
    else:
        return 0

def get_points_gest(gest):
    if gest < 28:
        return 5
    elif gest <= 34:
        return 4
    elif gest <= 37:
        return 3
    elif gest > 37:
        return 0
    else:
        return 0

def get_points_smoke(smoke):
    if smoke == 1:
        return 3
    elif smoke == 2:
        return 0
    else:
        return 0

def get_points_concept(concept):
    if concept == 1:
        return 0
    elif concept == 2:
        return 3
    else:
        return 0

def get_points_hyper(hyper):
    if hyper == 1:
        return 5
    elif hyper == 2:
        return 0
    else:
        return 0

def get_points_diabetes(diabetes):
    if diabetes == 1:
        return 3
    else:
        return 0

def get_points_autoimmune(autoimmune):
    if autoimmune == 1:
        return 5
    else:
        return 0

def get_points_parity(parity):
    points_dict = {1: 0, 2: 1, 3: 3}
    return points_dict.get(parity, 0)

def get_points_ab_pain(ab_pain):
    if ab_pain == 1:
        return 1
    else:
        return 0

def get_points_headache(headache):
    if headache == 1:
        return 1
    else:
        return 0

def get_points_vis(vis):
    if vis == 1:
        return 1
    else:
        return 0

def get_points_hyper_ref(hyper_ref):
    if hyper_ref == 1:
        return 1
    else:
        return 0

def get_points_dist_cons(dist_cons):
    if dist_cons == 1:
        return 1
    else:
        return 0

def get_points_dyspnea(dyspnea):
    if dyspnea == 1:
        return 1
    else:
        return 0

def get_points_bleed(bleed):
    if bleed == 1:
        return 1
    else:
        return 0

def calculate_total_risk_score(points):
    ab_pain = None
    while ab_pain not in [1, 2]:
      try:
        ab_pain = int(input("Abdominal pain? (Enter 1 for yes, 2 for no): ").strip())
        if ab_pain not in [1, 2]:
          print("Invalid input. Please enter 1 or 2.")
      except ValueError:
        print("Invalid input. Please enter a valid integer.")
        ab_pain = None
    points += get_points_ab_pain(ab_pain)


    headache = None
    while headache not in [1, 2]:
      try:
        headache = int(input("Headaches? (Enter 1 for yes, 2 for no): ").strip())
        if headache not in [1, 2]:
          print("Invalid input. Please enter 1 or 2.")
      except ValueError:
          print("Invalid input. Please enter a valid integer.")
          headache = None
    points += get_points_headache(headache)

    vis = None
    while vis not in [1, 2]:
      try:
        vis = int(input("Visual disturbances? (Enter 1 for yes, 2 for no): ").strip())
        if vis not in [1, 2]:
          print("Invalid input. Please enter 1 or 2.")
      except ValueError:
        print("Invalid input. Please enter a valid integer.")
        vis = None
    points += get_points_vis(vis)

    hyper_ref = None
    while hyper_ref not in [1, 2]:
      try:
        hyper_ref = int(input("Hyper-reflexia? (Enter 1 for yes, 2 for no): ").strip())
        if hyper_ref not in [1, 2]:
          print("Invalid input. Please enter 1 or 2.")
      except ValueError:
        print("Invalid input. Please enter a valid integer.")
        hyper_ref = None
    points += get_points_hyper_ref(hyper_ref)

    dist_cons = None
    while dist_cons not in [1, 2]:
      try:
        dist_cons = int(input("Disturbances of consciousness? (Enter 1 for yes, 2 for no): ").strip())
        if dist_cons not in [1, 2]:
          print("Invalid input. Please enter 1 or 2.")
      except ValueError:
        print("Invalid input. Please enter a valid integer.")
        dist_cons = None
    points += get_points_dist_cons(dist_cons)

    dyspnea = None
    while dyspnea not in [1, 2]:
      try:
        dyspnea = int(input("Dyspnea? (Enter 1 for yes, 2 for no): ").strip())
        if dyspnea not in [1, 2]:
          print("Invalid input. Please enter 1 or 2.")
      except ValueError:
        print("Invalid input. Please enter a valid integer.")
        dyspnea = None
    points += get_points_dyspnea(dyspnea)

    bleed = None
    while bleed not in [1, 2]:
      try:
        bleed = int(input("Bleeding tendency? (Enter 1 for yes, 2 for no): ").strip())
        if bleed not in [1, 2]:
          print("Invalid input. Please enter 1 or 2.")
      except ValueError:
        print("Invalid input. Please enter a valid integer.")
        bleed = None
    points += get_points_bleed(bleed)

    print("Extracting blood pressure reading from device...")
    loading_bar(10)
    print("")
    sys = random.randint(90, 130)
    dia = random.randint(60, 90)
    print(f"{sys}/{dia}")

    if sys >= 140 or dia >= 90:
        #Hypertensive range
        points += 4
    elif sys >= 120 or dia >= 80:
        #Elevated range
        points += 2
    else:
        #Normal range
        points += 0

    word_list = ["Negative", "1", "2", "3"]
    print("Extracting proteinuria reading from device...")
    loading_bar(10)
    print("")
    proteinuria = random.choice(word_list)
    print(proteinuria)
    if proteinuria == "Negative":
        points += 0
    elif proteinuria == "1":
        points += 2
    elif proteinuria == "2" or proteinuria == "3":
        points += 4

    return points

def categorize_risk_initial(score):
    if score <= 13:
        return "Low"
    elif score <= 27:
        return "Moderate"
    else:
        return "High"

def categorize_risk_total(score):
    if score <= 18:
        return "Low"
    elif score <= 37:
        return "Moderate"
    elif score <= 50:
        return "High"
    elif score <= 55:
        return "Critical"
    else:
        return "High"

def loading_bar(total, length=20):
    for i in range(1, total + 1):
        percent = i / total
        bar_length = int(length * percent)
        bar = "█" * bar_length + "-" * (length - bar_length)
        sys.stdout.write(f"\r[{bar}] {int(percent * 100)}%")
        sys.stdout.flush()
        time.sleep(0.1)

def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email)

def is_valid_phone_number(phone_number):
    phone_number_regex = r'^\d{10}$'
    return re.match(phone_number_regex, phone_number)


def main():
    points = 0
    print(art.logo)
    print("=============================")
    print("Welcome to PreePro!")
    print("=============================")
    print("Create your free account")
    input("Choose a username: ")
    user_email = input("Email: ")
    while not is_valid_email(user_email):
      print("Invalid email address. Please enter a valid email.")
      user_email = input("Email: ")
    getpass("Password: ")
    user_phone_number = input("Phone number: ")
    while not is_valid_phone_number(user_phone_number):
      print("Invalid phone number. Please enter a valid phone number.")
      user_phone_number = input("Phone number: ")


    print("Let's get you set up.")
    name = input("What is your name? ").strip()
    print(f"Hi {name}!")
    print("Your PreePro ProBox should contain: \n")
    print("• An iHealth blood monitor")
    print("• A Healthy.io urine testing kit")
    print("• Detailed use intsructions")

    print("Let's sync up your iHealth blood pressure monitoring device.")
    print("1. Turn on your iHealth blood pressure monitor")
    print("2. Enable Bluetooth on your smartphone")

    sync = None
    while sync != 1:
        try:
            sync = int(input("Press 1 to sync your device: ").strip())
            if sync != 1:
                print("Invalid input. Please enter 1")

        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            sync = None

    loading_bar(10)
    print("\nSync complete!")

    print("Let's learn more about you!")
    print("The next section will ask you for relevant information related to your personal and medical history")
    print("Pregnancy Details:")

    preg_type = None
    while preg_type not in [1, 2]:
      try:
            preg_type = int(input("Are you having one or multiple babies? (Enter 1 for Singleton, 2 for Twins): ").strip())
            if preg_type not in [1, 2]:
              print("Invalid input. Please enter 1 or 2.")
      except ValueError:
            print("Invalid input. Please enter a valid integer.")
            preg_type = None
    points += get_points_preg_type(preg_type)

    while True:
      date_str = input("Due date (YYYY-MM-DD): ")
      try:
          date_obj = datetime.strptime(date_str, "%Y-%m-%d")
          print("You entered:", date_obj)
          break
      except ValueError:
        print("Invalid date format. Please enter the date in the format YYYY-MM-DD.")

    print("Maternal Characteristics:")
    while True:
      try:
          age = int(input("How old are you? ").strip())
          break
      except ValueError:
        print("Invalid input. Please enter a valid numeric value for age.")
    points += get_points_age(age)

    while True:
      try:
        height = int(input("How tall are you? (in cm): ").strip())
        break
      except ValueError:
        print("Invalid input. Please enter a valid numeric value for height.")
    points += get_points_height(height)

    while True:
      try:
        weight = int(input("How much do you weigh? (in lbs): ").strip())
        break
      except ValueError:
        print("Invalid input. Please enter a valid numeric value for weight.")
    points += calculate_bmi(height, weight)

    gest = None
    while gest is None or gest < 0 or gest > 45:
        try:
            gest = int(input("How many weeks along are you? ").strip())
            if gest < 0 or gest > 45:
                print("Invalid input. Please enter a value between 0 and 45.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    points += get_points_gest(gest)


    print("Please select all races/ethnicities that apply to you: \n")
    print("• American Indian or Alaska Native (enter 1)")
    print("• Asian (enter 2)")
    print("• Black or African American (enter 3)")
    print("• Hispanic or Latino (enter 4)")
    print("• Native Hawaiian or Other Pacific Islander (enter 5)")
    print("• White (enter 6)")

    valid_options = (['1', '2', '3', '4', '5', '6'])

    while True:
        user_input = input("Separate input by commas: ")
        input_values = user_input.split(',')
        if all(option.strip() in valid_options for option in input_values):
            break
        else:
            print("Invalid input. Please enter valid options separated by commas.")
    print("You selected:", input_values)

    smoke = None
    while smoke not in [1, 2]:
      try:
        smoke = int(input("Do you smoke while pregnant? (Enter 1 for yes, 2 for no):").strip())
        if smoke not in [1, 2]:
            print("Invalid input. Please enter 1 or 2.")
      except ValueError:
        print("Invalid input. Please enter a valid integer.")
        smoke = None
    points += get_points_smoke(smoke)

    concept = None
    while concept not in [1, 2]:
      try:
        concept = int(input("Conception method (Enter 1 for natural, 2 for assisted reproduction (IVF, etc.)):").strip())
        if concept not in [1, 2]:
            print("Invalid input. Please enter 1 or 2.")
      except ValueError:
        print("Invalid input. Please enter a valid integer.")
        concept = None
    points += get_points_concept(concept)

    print("Medical History")
    hyper = None
    while hyper not in [1, 2]:
      try:
        hyper = int(input("Do you have Chronic Hypertension? (Enter 1 for Yes, 2 for No): ").strip())
        if hyper not in [1, 2]:
            print("Invalid input. Please enter 1 or 2.")
      except ValueError:
        print("Invalid input. Please enter a valid integer.")
        hyper = None
    points += get_points_hyper(hyper)

    diabetes = None
    while diabetes not in [1, 2]:
      try:
        diabetes = int(input("Do you have Diabetes (Type I or Type II)? (Enter 1 for yes, 2 for no): ").strip())
        if diabetes not in [1, 2]:
            print("Invalid input. Please enter 1 or 2.")
      except ValueError:
        print("Invalid input. Please enter a valid integer.")
        diabetes = None
    points += get_points_diabetes(diabetes)

    autoimmune = None
    while autoimmune not in [1, 2, 3]:
      try:
        autoimmune = int(input("Do you have an Autoimmune Disorder, such as Lupus or Antiphospholipid Syndrome? (Enter 1 for yes, 2 for no): ").strip())
        if autoimmune not in [1, 2]:
            print("Invalid input. Please enter 1 or 2")
      except ValueError:
        print("Invalid input. Please enter a valid integer.")
        autoimmune = None
    points += get_points_autoimmune(autoimmune)

    print("Obstetric History")
    parity = None
    while parity not in [1, 2, 3]:
      try:
        parity = int(input("Have you ever given birth before? (Enter 1 for no (Nulliparous), 2 for yes (Parous) with no adverse outcomes, 3 for yes (Parous) with adverse outcomes): ").strip())
        if parity not in [1, 2, 3]:
            print("Invalid input. Please enter 1, 2, or 3.")
      except ValueError:
        print("Invalid input. Please enter a valid integer.")
        parity = None
    points += get_points_parity(parity)

    print(f"\nInitial Intake Risk Score: {points}")
    initial_risk_category = categorize_risk_initial(points)
    print(f"Initial Intake Risk Category: {initial_risk_category} Initial Risk\n")
    initial_table = PrettyTable()
    initial_table.field_names = ["Low Risk", "Moderate Risk", "High Risk"]
    initial_table.add_row(["0 - 15", "16 - 30", "31 - 45"])
    print(initial_table)

    print("Great! Your intake is complete.")
    print("Let's enter this week's screening information. Enter '1' for every symptom you've experienced this week.")

    points = calculate_total_risk_score(points)
    print(f"Total Risk Score: {points} / 60")
    total_risk_category = categorize_risk_total(points)

    print(f"Total Risk Category: {total_risk_category} Total Risk")

    total_table = PrettyTable()
    total_table.field_names = ["Low Risk", "Moderate Risk", "High Risk", "Critical Risk"]
    total_table.add_row(["0 - 20", "21 - 40", "41 - 55", "56 - 60"])
    print(total_table)
    
    if total_risk_category == "Critical":
        print("Seek Medical Attention Immediately!")

if __name__ == "__main__":
    main()
