
import msvcrt


def any_key():

    print("Press any key to continue...")
    msvcrt.getch()
    


def specif_key(key_var):   #Unfinished
    
    value2 = 'Bob'

    print(f"Press {key_var} to continue...")

    while value2 != key_var:

        command2 = msvcrt.getch()
        value2 = str(list(str(command2))[2])
        
        if value2 == key_var:
            break


specif_key

