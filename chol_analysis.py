def HDL_analysis(HDL_level):
    if HDL_level >= 60:
        return "normal"
    elif 40 <= HDL_level < 60:
        return "borderline low"
    else:
        return "low"


def LDL_analysis(LDL_level):
    if LDL_level >= 190:
        return "very high"
    elif 160 <= LDL_level <= 189:
        return "high"
    elif 130 <= LDL_level <= 159:
        return "borderline high"
    else:
        return "normal"


def cholesterol_analysis():
    print("Cholesterol analysis")
    HDLinput = input("Enter test result: ")
    test_info = HDLinput.split("=")
    if test_info[0] == "HDL":
        answer = HDL_analysis(int(test_info[1]))
        print("The level is {}.".format(answer))
    if test_info[0] == "LDL":
        answer = LDL_analysis(int(test_info[1]))
        print("The level is {}.".format(answer))



def new_feature():
    pass

def name_function():
    first_name = input("First name")
    last_name = input("Last name")


def interface():
    choice = 0
    while True:
        print("Cholesterol Calculator")
        print("Options: ")
        print("   9 - Quit")
        choice = input("Enter your option: ")
        if choice == '9':
            return
        elif choice == "1":
            cholesterol_analysis()



if __name__ == "__main__":
    interface()
