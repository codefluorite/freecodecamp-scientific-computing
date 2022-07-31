fh = open('mbox-short.txt')

for lx in fh:  # Loop to read through the file
    ly = lx.rstrip() # Throw away the non printing characters
    print(ly.upper()) #Converts strings where neccessary to upper case.