import wikipedia, os
from colorama import Fore, Back, Style

def emptyLine():
    """Just for empty line."""
    print()

def error(message):
    print(Fore.WHITE + Back.RED + message + Style.RESET_ALL)

def exportPage( page):
    exportFile = open(page.title + ".txt", "w")
    pageArray = page.content.split("\n")
    for i in pageArray:
        exportFile.writelines(i)
    
    exportFile.close()
    error("Article exported")

def fullPage(page):
    pageArray = page.content.split("\n")
    for i in pageArray: 
        if i[0:3] == "== " or i[0:3] == "===": 
            if i[0:3] == "==":
                print(Fore.RED + i.upper() + Style.RESET_ALL)
            else:
                print(Fore.RED + i + Style.RESET_ALL) 
        else:
            print(i)
    seeAlso(page)
    # Export option has disabled because it has problems.
    # This option will replace again with updated version.
    # textQuestion = input("Do you want to export this article? (y / n): " + Fore.YELLOW + Style.RESET_ALL)
    # if textQuestion == "y":
    #     exportPage(page)
    
    # else:
    #     exit
        
    
                   
def resultRender(page):
    os.system("clear")
    try:
        print(Fore.WHITE + Back.RED + page.title + Style.RESET_ALL)
        exit
    except AttributeError:
        error("A problem occured")
    
    try:
        if page.coordinates != None:
            lat = str(round(page.coordinates[0], 2))
            lon = str(round(page.coordinates[1], 2))
            print(Fore.RED + "Coordinates: " + Style.RESET_ALL + lat + ", " + lon)
        else:
            pass
    except KeyError:
        pass

    print(page.summary)
    emptyLine()
    print(Fore.YELLOW + "For more information: " + Style.RESET_ALL + page.url)
    fullQuestion = input("Do you want to see full page? (y/n): ")
    if fullQuestion == "y":
        os.system("clear")
        fullPage(page)
    else:
        exit


def pageSelect(searchQuery, selectedPage):
    try:
        if selectedPage != "":
            return wikipedia.page(searchQuery[int(selectedPage)-1])
        else:
            return wikipedia.page(searchQuery[0])
    except ValueError:
        print(Fore.WHITE + Back.RED + "Your value is undefined. You must choose a value between 1 and " + str(len(searchQuery)) + Style.RESET_ALL)
    except wikipedia.DisambiguationError:
        print(Fore.WHITE + Back.RED + "This query has disambugation" + Style.RESET_ALL)
    
def listSearch(searchQuery):
    os.system("clear")
    counter = 0
    for i in searchQuery:
        counter = counter + 1
        print(Fore.RED + str(counter) + ". " + Style.RESET_ALL + i)

def mahmut():
    resultRender(wikipedia.page("Mahmud"))
    exit


def seeAlso(page):
    seeAlsoQuestion = input(Fore.BLUE + "Do you want to see also section? (y / n): " + Fore.YELLOW + Style.RESET_ALL)
    if seeAlsoQuestion == "y":
        readControl = 0
        seeAlsoArray = []
        pageArray = page.content.split("\n")

        for i in pageArray:
            if i == "== See also ==":
                readControl = 1

            if readControl == 1:
                seeAlsoArray += str(i).split("-")

            if i == "":
                readControl = 0
        
        del seeAlsoArray[0]
        del seeAlsoArray[-1]
        for i in seeAlsoArray:
            print(i)
        if len(seeAlsoArray) != 0:
            listSearch(seeAlsoArray)
            selectedPage = input("Please choose one of the following options (Press enter for first option)=> " + Fore.YELLOW)
            page = pageSelect(seeAlsoArray, selectedPage)
            emptyLine()
            resultRender(page)
        else:
            error("This page hasn't \'See Also\' section")


def seeSections(page):
    sectionArray = []
    trimmedSectionArray = []
    pageArray = page.content.split("\n")
    for i in pageArray:
        if i[0:3] == "===" or i[0:3] == "== ":
            if i[0:3] == "== ":
                i = str(i) + "2"
                sectionArray.append(str(i).replace("=",""))
                
            elif i[0:3] == "===":
                i = str(i) + "3"
                sectionArray.append(str(i).replace("=",""))
                

    for i in sectionArray:
        i = i.strip()
        trimmedSectionArray.append(i)
    
    return trimmedSectionArray