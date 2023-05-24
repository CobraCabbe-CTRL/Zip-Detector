import webbrowser

print("Enter the path (link/filepath) you want to check bellow:")
link=input("")

unicode_string = '¤'.join([f"U+{ord(char):04X}" for char in link]) ##Convert the link into unicode characters

if "U+2215¤U+0040" in unicode_string:
    print("The path is probably a link and NOT a file download")
    print()
    yes=input("Do you want to open the URL in a new tab? (Y/N)\n")
    if yes.capitalize()=='Y':
        webbrowser.open_new_tab(link)
elif "U+2215" in unicode_string:
    print("The path might be a link instead of a file download")
    print()
    yes=input("Do you want to open the path in a new tab? (Y/N)\n")
    if yes.capitalize()=='Y':
        webbrowser.open_new_tab(link)
elif "\@":
    print("The path might be a link")
    print()   
    yes=input("Do you want to open the path in a new tab? (Y/N)\n")
    if yes.capitalize()=='Y':
        webbrowser.open_new_tab(link)
else:
    print("The path is probobly a file download")
    print()   
    yes=input("Do you want to open the path in a new tab? (Y/N)\n")
    if yes.capitalize()=='Y':
        webbrowser.open_new_tab(link)