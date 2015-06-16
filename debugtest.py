import sys
import piltest
from PIL import Image
import os
from os import listdir
from os.path import isfile, join

if len(sys.argv) < 3:
  print 'Usage:'
  print '  python imageprocessing.py  <imaging data directory> (abbreviation for each channel)'
  sys.exit()

inputdir = sys.argv[1]
channelnames = tuple(sys.argv[2:])

filenames = piltest.getImagingFiles(inputdir)
print filenames

channelmap = piltest.getChannels(filenames, channelnames)
print channelmap

sectionstomerge = map(channelmap.values())
print sectionstomerge
