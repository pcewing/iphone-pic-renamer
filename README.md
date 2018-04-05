# IPhone Picture File Renamer

When taking pictures with the IPhone camera app, the image files saved have names that are annoying to work with for a couple reasons:
* They don't sort nicely by name
* They contain spaces

The file names look like:
```
Photo Mar 07, 6 50 03 PM.jpg
Photo Mar 13, 8 50 50 PM.jpg
Photo Mar 13, 8 50 50 PM (1).jpg
```

This repository contains a quick and dirty Python script for renaming these image files. The resulting file names look like:
```
# Month-Day_Hour-Minute-Second_Copy
03-07_18-50-03_00.jpg
03-13_20-50-50_00.jpg
03-13_20-50-50_01.jpg
```

These file names don't contain the year because the original filenames don't either. You will need to manually prepend that to the resulting files. 

## Running the script
```
$ ./main.py --directory $HOME/Pictures
Moving /home/paul/Pictures/Photo Apr 03, 8 33 25 PM.jpg to /home/paul/Pictures/04-03_20-33-25_00.jpg
Moving /home/paul/Pictures/Photo Mar 07, 6 50 03 PM.jpg to /home/paul/Pictures/03-07_18-50-03_00.jpg
Moving /home/paul/Pictures/Photo Mar 13, 8 50 50 PM.jpg to /home/paul/Pictures/03-13_20-50-50_00.jpg
Moving /home/paul/Pictures/Photo Mar 10, 9 21 47 AM.jpg to /home/paul/Pictures/03-10_09-21-47_00.jpg
```

The script will not actually move anything unless it is executed with the `--live` flag.

