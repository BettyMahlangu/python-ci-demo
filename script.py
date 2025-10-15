import datetime
import platform

def user_greet():
    user_name = "Betty"
    time_now = datetime.datetime.now().strftime("%Y-%M-%D %H:%M:%S")
    system = platform.system()

    print(f"Hello {user_name}!")
    print(f"The current time now is {time_now}")
    print(f"This script runs on {system}")
    print("Your first gitHub action is ready to role!!")

if __name__=="__main__":
    user_greet()