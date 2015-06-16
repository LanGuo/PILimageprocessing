'''
This is a python program using Python Imaging Library to manipulate image files. It should merge images taken on different channels of the same section. 
'''

import os
from os import listdir
from os.path import isfile, join
from PIL import Image


def getImagingFiles(inputdir):
    """
    Get filenames of images in the user specified input directory.
    """
    if not os.path.isdir(inputdir):
        raise RuntimeError, "The directory provided does not exist"
    # Get all the filenames from the input directory, right now ignoring subdirectories. May consider using os.walk to get files from subdirectories in the future.
    onlyfiles = [f for f in listdir(inputdir) if isfile(join(inputdir,f))]
    onlyfilesfull = [join(inputdir, f) for f in onlyfiles]
    return onlyfilesfull

  
def getChannels(filenames, channelnames):
    """
    Based on user specified channel names, generate separate lists of filenames for that channel, stored in a dictionary.
    """
    # num_channels = len(channelnames)
   
    channelmap = {}
    for c in channelnames: 
        for f in filenames: 
            if f.endswith(c):
                channelmap[c].extend(f) 
        channelmap[c] = sorted(channelmap[c])

    return channelmap


def mergeAllChannels(channelmap):
    """
    Use image.merge to iterate over the channel lists and merge the channels of the same section to get a composite image
    """
    # Mapping the lists of filenames in channelmap to generate a list of tuples with the different channels from the same section
    sectionstomerge = map(channelmap.values()) 
    for s in sectionstomerge:    
        mergedfile = Image.merge("RGB", s)
        mergedfile.save()



# Image rotation and registration


  
