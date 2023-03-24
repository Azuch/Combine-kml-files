I am using wigle, when i upload to my account, there is multiple file call .kml.
I am using this script to combine and extract the duplicate Access Points
The code is easy, no need to comment
Use all you like
Put all file on the ./tmp/
copy on of those and rename to base.kml
The output is base2.kml
Use this base2 to upload to earth.
Ex: python3 readAndWriteKml.py ./tmp/*
