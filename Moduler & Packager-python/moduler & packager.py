import date_time as dt
import Mathematical_Operations as mo
import Random_data_generation as rdg
import Generate_Unique_Identifiers as gui
import File_Operations as fo
import Explore_Module_Attributes as ema

print("=" * 30)
print("Welcome to Multi-Utility Toolkit")
while True:
    print("="*30)
    print("Choose your option:")
    print("1. Datetime and Time Operations")
    print("2. Mathematical Operations")
    print("3. Random Data Generation")
    print("4. Generate Unique Identifiers")
    print("5. File Operations")
    print("6. Explore Module Attributes")
    print("7. Exit")
    print("="*30)
    choice = int(input("Enter your choice: "))
    if choice == 1:
        dt.main()
    elif choice == 2:
        mo.main()
    elif choice == 3:
        rdg.main()
    elif choice == 4:
        gui.main()
    elif choice == 5:
        fo.main()
    elif choice == 6:
        ema.main()
    elif choice == 7:
        print("=" * 30)
        print("Thank youu for using the multi-utility toolkit!")
        break
    else:
        print("=" * 30)
        print("Invalid choice")
        print("=" * 30)