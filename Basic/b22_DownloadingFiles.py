from urllib import request

mylink = "https://sourceforge.net/p/keepass/discussion/329221/thread/ab9b45d1/abcf/6223/attachment/pwmarkelt%20pw.kp.csv"

def DownloadIt(link):
    # open the url
    resp = request.urlopen(link)
    # read data from the opened url
    myFile = resp.read()
    # convert the data to a string
    myFile_str = str(myFile)
    # split the string to lines "the delimiter is the new line character"
    lines = myFile_str.split("\\n")
    # Create a file on my computer
    dest = r"C:\Users\Root\PycharmProjects\Beggining\FileManipulation\MyFile.csv"
    myFile_Obj = open(dest, "w")
    # store the retrieved data to it
    for line in lines:
        myFile_Obj.write(line)
    # close the file
    myFile_Obj.close()


DownloadIt(mylink)