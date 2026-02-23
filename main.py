from ChatBot.consultant_bot import business_chat

def run_system():

    print("\n=== AI Digital Twin Business Simulator ===\n")

    marketing = int(input("Enter Marketing Spend: "))
    employees = int(input("Enter Number of Employees: "))
    time = int(input("Enter Days: "))

    result = business_chat(marketing, employees, time)

    print("\n--- Simulation Result ---\n")

    for key, value in result.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    run_system()