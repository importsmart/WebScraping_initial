import webbrowser,sys, pyperclip

#sys.argv: seperates out spaces #list values

if(len(sys.argv)>1):  #checking it has data
    address = ' '.join(sys.argv[1:])  #combining everything after "mapit.py"
else:
    address = pyperclip.paste() #from clipboard

#link="https://www.google.com/maps/place/<address>

webbrowser.open('https://www.google.com/maps/place/' + address)
