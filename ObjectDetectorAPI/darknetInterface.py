import subprocess
import urllib.request
import os

def savePictureLocal(url):
    print("Fetching picture from " + url)
    urllib.request.urlretrieve(url, "current.png")

def cleanUp():
    os.remove("current.png") 
    os.remove("predictions.jpg") 

# Some very "pragmatic" conversion of Darknet output
def analyzeCurrentPicture():
    print("Analyzing picture...")
    result = subprocess.getstatusoutput("..\darknet\darknet.exe detector test obj.data yolov4-four-obj.cfg yolov4-obj_final.weights -thresh 0.25 current.png")[1]
    interestingPart = result[result.find("Predicted in"):]
    items = interestingPart.splitlines()

    if len(items) > 1:
        return (items[1].split()[0])[:-1]
    else:
        return ""
        
    # In case we want to return a dictionary with all concepts (see Task 3)
    # concepts = { 'concepts' : [] }
    # for item in items[1:]:
    #    itemConcept = (item.split()[0])[:-1]
    #    concepts.get('concepts').append(itemConcept)

def findObjects(url):
    savePictureLocal(url)
    results = analyzeCurrentPicture()
    cleanUp()
    return results