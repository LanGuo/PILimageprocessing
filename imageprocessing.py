import sys
import piltest

if len(sys.argv) < 3:
  print 'Usage:'
  print '  python imageprocessing.py  <imaging data directory> (abbreviation for each channel)'
  exit()

inputdir = sys.argv[1]
channelnames = sys.argv[2]



