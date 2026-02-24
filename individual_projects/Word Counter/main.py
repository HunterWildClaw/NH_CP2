# NH 2nd main file for word counter
#Import all the functions from the other tab
from file_handling import*
from time_handling import*
#def main function
def main():
    """Main program loop."""
    ensure_docs_dir()
    
    while True:
        print("\n=== Document Manager ===")
        print("1. Create new doc")
        print("2. Write to doc")
        print("3. View doc")
        print("4. View timestamp of doc")
        print("5. Exit")
        
        choice = input("Choose an option (1-4): ").strip()
        
        if choice=="1":
            create_document()
        elif choice=="2":
            write_document()
        elif choice=="3":
            view_document()
        elif choice=="4":
            get_current_iso_time
        elif choice=="5":
            print("CYA (Your work will save)!")
            break
        else:
            print("Invalid option. Please try again.")
# Call main function
main()