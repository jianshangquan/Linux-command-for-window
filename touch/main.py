import sys;
import os;

argumentLength = len(sys.argv);
if argumentLength >= 2:
    if not os.path.exists(sys.argv[1]):
        open(sys.argv[1], "w").close();
        print("File successfully created");
    else:
        print('The file already exists.');
else:
    print("Please provide a file name to create")