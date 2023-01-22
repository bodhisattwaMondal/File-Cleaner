import os

def createFolder(folder):
    """This function will create a folder if not present."""
    if not os.path.exists(folder):
        os.makedirs(folder)


def move(folderName,files):
    """This function will move the files to corresponding folders."""
    global count
    for file in files:
        os.replace(file, f"{folderName}/{file}")
        count += 1

count = int(0) # It will count the no. of files been moved.

# Driver Code :
def main():

    # Getting the Script Name in order to exclude it :
    Script_dir = __file__.split("\\") # It will create a list of directory path
    Position = len(Script_dir)-1 

    # Listing all the files in the current directory :
    files = os.listdir()
    # Excluding the Script file(main.py) :
    files.remove(Script_dir[Position]) # It will take main.py from the list


    # Cheking file extension formats : 
    imgExt = [".jpg",".j.peg", ".png", ".gif", ".tiff"]
    images = [file for file in files if os.path.splitext(file)[1].lower() in imgExt]

    docExt = [".doc",".docx", ".pdf", ".xls", ".xlsx", ".ods", ".ppt", "pptx", ".txt", ".csv"]
    documents = [file for file in files if os.path.splitext(file)[1].lower() in docExt]

    mediaExt = [".mp4",".mp3", ".mkv", ".flv", ".wmv", ".m4p", ".m4v", ".svi", ".3gp", ".webm"]
    medias = [file for file in files if os.path.splitext(file)[1].lower() in mediaExt]

    jsExt = [".js"]
    jS = [file for file in files if os.path.splitext(file)[1].lower() in jsExt]

    htmlExt = [".html"]
    html = [file for file in files if os.path.splitext(file)[1].lower() in htmlExt]

    cssExt = [".css"]
    css = [file for file in files if os.path.splitext(file)[1].lower() in cssExt]

    javaExt = [".java", ".class"]
    java = [file for file in files if os.path.splitext(file)[1].lower() in javaExt]

    cExt = [".c"]
    c = [file for file in files if os.path.splitext(file)[1].lower() in cExt]

    pythonExt = [".py"]
    python = [file for file in files if os.path.splitext(file)[1].lower() in pythonExt]

    adobeExt = [".psd", ".ai", ".indd"]
    adobe= [file for file in files if os.path.splitext(file)[1].lower() in adobeExt]

    rawExt = [".cr2", ".crw", ".nef", ".pef"]
    raw= [file for file in files if os.path.splitext(file)[1].lower() in rawExt]

    softwareExt = [".exe"]
    software = [file for file in files if os.path.splitext(file)[1].lower() in softwareExt]

    appExt = [".apk"]
    app = [file for file in files if os.path.splitext(file)[1].lower() in appExt]

    others = []
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if (ext not in imgExt) and (ext not in mediaExt) and (ext not in docExt) and (ext not in pythonExt) \
        and (ext not in jsExt) and (ext not in cssExt) and (ext not in htmlExt) and (ext not in pythonExt) \
        and (ext not in javaExt) and (ext not in cExt) and (ext not in adobeExt) and (ext not in softwareExt) \
        and (ext not in appExt) and (ext not in rawExt) and (os.path.isfile(file)) :
            others.append(file)


    # Creating folders if not present and moving all the files to their corresponding folder :-
    if len(images) > 0:
        createFolder('Image')
        move("Image",images)
        
    if len(medias) > 0:
        createFolder('Media')
        move("Media",medias)

    if len(documents) > 0:
        createFolder('Document')
        move("Document",documents)

    if len(python) > 0:
        createFolder('Python')
        move("Python",python)

    if len(html) > 0:
        createFolder('HTML')
        move("HTML",html)

    if len(css) > 0:
        createFolder('CSS')
        move("CSS",css)

    if len(jS) > 0:
        createFolder('javaScript')
        move("javaScript",jS)

    if len(java) > 0:
        createFolder('JAVA')
        move("JAVA",java)

    if len(adobe) > 0:
        createFolder('Adobe')
        move("Adobe",adobe)

    if len(raw) > 0:
        createFolder('Raw')
        move("Raw",raw)

    if len(software) > 0:
        createFolder('Software')
        move("Software",software)

    if len(c) > 0:
        createFolder('C Program')
        move("C Program",c)

    if len(app) > 0:
        createFolder('App')
        move("App",app)

    if len(others) > 0:
        createFolder('Others')
        move("Others",others)

    # Displaying sussecfull message :-
    if count > 0:
        if count == 1: 
            print(f"{count} file has been succesfully moved !!")
        else:
            print(f"{count} files has been succesfully moved !!")
    else:
        print("Sorry! there is no file present in the current directory to organise.")

if __name__ == '__main__':
    main()


