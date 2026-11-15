menus = [
    "Phone book | Search, Add name, Erase, Edit",
    "Messages | Write messages, Inbox, Outbox",
    "Chat | Start Chat",
    "Call register | Missed calls, Received calls, Dialled numbers",
    "Tones | Ringing tone, Ringing volume, Composer",
    "Settings | Call settings, Phone settings, Security settings",
    "Call divert | Divert all, Divert if busy, Cancel all diverts",
    "Music | Music player, Radio, Recorder",
    "Reminders | Add reminder, View reminders, Erase",
    "Games | Snake II, Space Impact, Bantumi",
    "Extras | Calendar, Clock, Stopwatch",
    "Calculator | Calculator, Currency converter",
    "Profiles | General, Silent, Meeting, Outdoor",
    "Services - WAP | Home, Bookmarks, Go to address",
    "SIM services | SIM services"
]

def show_main_menu():
    print("\n--- NOKIA 5510 ---")
    for i, line in enumerate(menus, 1):
        name = line.split("|")[0]
        print(i, "-", name.strip())
    print("0 - Exit")

def show_sub_menu(num):
    name, subs = menus[num-1].split("|")
    name = name.strip()
    sub_list = [s.strip() for s in subs.split(",")]
    print(f"\n>> {name} <<")
    for j, item in enumerate(sub_list, 1):
        print(j, "-", item)
    print("0 - Back")
    return name, sub_list

def do_calculator():
    print("\n--- CALCULATOR ---")
    a = float(input("First number: "))
    op = input(" + - * / : ")
    b = float(input("Second number: "))
    if op == "+":
        print("Answer =", a + b)
    elif op == "-":
        print("Answer =", a - b)
    elif op == "*":
        print("Answer =", a * b)
    elif op == "/":
        print("Answer =", a / b)
    else:
        print("Wrong operator")

def main():
    while True:
        show_main_menu()
        choice = input("Press Menu number: ")
        if choice == "0":
            print("Goodbye!")
            break

        num = int(choice)
        if 1 <= num <= 15:
            name, sub_list = show_sub_menu(num)
            sub_choice = input("Choose: ")
            if sub_choice == "0":
                continue

            picked = sub_list[int(sub_choice)-1]
            print(f"\nYou selected: {name} > {picked}")

            if name == "Calculator" and picked == "Calculator":
                do_calculator()
            else:
                print("...Doing it...")

            input("\nPress Enter to go back...")
        else:
            print("No such menu, try again")

main()
 

