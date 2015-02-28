#!/usr/bin/env python

import logging
import getopt
import sys
import time
import random

def main(argv):
    usageInfo = '\nUSAGE:\n\nlogGenerator.py --logFile <targetFile> [--minSleepMs <int>] [--maxSleepMs <int>] [--sourceDataFile <fileWithTextData>] [--iterations <long>]] [--minLines <int>] [--maxLines <int>]\n'

    interations = -1
    minSleep = 0.1
    maxSleep = 1
    minLines = 1
    maxLines = 1
    logFile = 'logGenerator.log'
    sourceDataFile = 'defaultDataFile.txt'
    sourceData = ''

    if len(argv) == 0:
        print usageInfo
        sys.exit(2)

    try:
        opts, args = getopt.getopt(argv,"h",["help","logFile=","minSleepMs=","maxSleepMs=","iterations=","dataFile=","minLines=","maxLines="])
    except:
        print usageInfo
        sys.exit(2)


    for opt, arg in opts:

        if opt in ('-h' , "--help"):
            print usageInfo
            sys.exit()

        elif opt in ("--logFile"):
            logFile = arg

        elif opt in ("--minSleepMs"):
            minSleep = (1000 / int(arg))

        elif opt in ("--maxSleepMs"):
            maxSleep = (1000 / int(arg))

        elif opt in ("--maxLines"):
            maxLines = int(arg)

        elif opt in ("--minLines"):
            minLines = int(arg)

        elif opt in ("--sourceDataFile"):
            sourceDataFile = arg

        elif opt in ("--iterations"):
            iterations = int(arg)


    # bring in source data
    with open (sourceDataFile, "r") as fh:
        sourceData=fh.read()
    sourceData = sourceData.splitlines(True)
    totalLines = len(sourceData)-1

    if (maxLines > totalLines):
        maxLines = totalLines

    print "sourceData lines: " + str(totalLines)
    print "minSleep: " + str(minSleep)
    print "maxSleep: " + str(maxSleep)
    print "minLines: " + str(minLines)
    print "maxLines: " + str(maxLines)

    mustIterate = True
    while (mustIterate):

        # sleep
        time.sleep(random.uniform(minSleep, maxSleep))

        # get random data
        lineToStart = random.randint(0,totalLines)
        linesToGet = -1
        while(linesToGet < lineToStart):
            linesToGet = random.randint(minLines, maxLines)

        print str(lineToStart)
        print str(linesToGet)

        lastLineToGet = (lineToStart + linesToGet)

        if (lastLineToGet > totalLines):
            lastLineToGet = totalLines

        toLog = ''.join(sourceData[lineToStart:lastLineToGet])

        logging.basicConfig(format='%(asctime)s %(message)s',filename=logFile,level=logging.DEBUG)
        logging.debug(toLog[:-1])

        if (iterations > 0):
            iterations = iterations - 1
            if (iterations == 0):
                mustIterate = False


if __name__ == "__main__":
   main(sys.argv[1:])
