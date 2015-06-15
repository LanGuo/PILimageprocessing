'''
This is a python program using Python Imaging Library to manipulate image files. It should merge images taken on different channels of the same section. 
'''

import os
from os import listdir
from os.path import isfile, join

# Interact with user to get file path, channel names
def getImagingFiles(inputdir):
    """
    Get filenames of images in the input directory.
    """
    if not os.path.isdir(inputdir):
        raise RuntimeError, "The directory provided does not exist"
    # Get all the filenames from the input directory, right now ignoring subdirectories. May consider using os.walk to get files from subdirectories in the future.
    onlyfiles = [ f for f in listdir(inputdir) if isfile(join(inputdir,f)) ]
    onlyfilespull = join(inputdir, onlyfiles)
    return onlyfilesfull

# Make n lists of filenames (n=number of channels), should call it with onlyfilesfull and channelnames.  
def getChannels(filenames, channelnames):
    # num_channels = len(channelnames)
    for c in channelnames: 
        channelmap = {c : sorted(f for f in filenames if f.endswith(c))}
    return channelmap

# Use image.merge to iterate over the channel lists and merge the channels of the same section to get a composite image
def mergeAllChannels(channelmap):
    sectionstomerge = map(channelmap.values()) #this should return a list of tuples with the different channels from the same section
    for s in sectionstomerge:    
        mergedfile = Image.merge("RGB", s)

# Output and save image

# Rotate image using registration


  
