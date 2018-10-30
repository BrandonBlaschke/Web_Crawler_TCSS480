import urllib.request
import re
import time
from multiprocessing import Process, Manager
from crawlGraphics import CrawlGraphic


# Gets the current time in milliseconds
def currentTimeMili():
    return int(round(time.time() * 1000))


# Given a dictionary which contains lists, will create crawl space csv file
def createCSV(links):
    with open('crawl.csv', 'w') as f:
        f.write("Page,Links\n")
        for i in links.keys():
            row = i
            aList = links[i]
            for j in aList:
                row += (',' + j)
            row += '\n'
            f.write(row)

        popLinks = popularLinks(links)
        if len(popLinks) > 0:
            pops = ''
            for i in range(0, len(popLinks)):
                if i == 0:
                    pops += popLinks[i]
                else:
                    pops += ',' + popLinks[i] + ' '
            stat = "Most popular reference(s) were: " + pops
            f.write(stat)
        else:
            f.write("No Links, can't find most popular link")


# Given a dictionary which contains lists, returns a list of the referenced links in crawl space
def popularLinks(links):

    trackCounts = {}

    # Go through each links references and count number of times they appear
    for link in links.keys():
        for linkRef in links[link]:
            if linkRef in trackCounts:
                trackCounts[linkRef] += 1
            else:
                trackCounts[linkRef] = 0

    # Find the most popular link(s)
    mostPop = []
    for i in trackCounts.keys():
        if len(mostPop) == 0:
            mostPop.append(i)
        elif trackCounts[i] == trackCounts[mostPop[0]]:
            mostPop.append(i)
        elif trackCounts[i] > trackCounts[mostPop[0]]:
            mostPop = [i]
    return mostPop


# Prints a spider by Joan Stark :)
def createSpider():
    print("          _.._       ")
    print("        .'    '.     ")
    print("       /   __   \    ")
    print("    ,  |   ><   |  ,  ")
    print("   . \  \      /  / .                  ")
    print("    \_'--`(  )'--'_/                  ")
    print("      .--'/()\\\'--.               ")
    print("     /  /` '' `\  \                 ")
    print("       |        |              ")
    print("   WEB  \      /  CRAWLER")


# Updates the crawl space given the starting link and the ending link,
# if given just start it adds it to crawl space with a list.
def updateCrawlSpace(start, links, des=None):

    if start not in links:
        links[start] = []

    if des is not None:
        aList = links[start]
        if des not in aList:
            aList.append(des)
            links[start] = aList


# Parses a HTML web page given the link, adds links found to a queue
def parseHTML(links, link, theQueue):

    try:
        page = urllib.request.urlopen(link)
        pageText = page.read()
        linksFound = re.findall('a href[=\s][=\s]?\\"(http[s]?://.*?)\\"', str(pageText))
        for i in linksFound:
            updateCrawlSpace(link, links, des=i)
            if i not in links:
                theQueue.put(i)
    except (urllib.error.HTTPError, urllib.error.URLError) as e:
        print("Can't access link " + link)


# Crawls the web by first reading a file line by line and starts crawling on those links
def crawlWeb(fileName, theQueue, crawlSpace):

    global pages

    # Get the initial links first
    with open(fileName, 'r') as f:
        link = f.readline().rstrip('\n')
        while link:
            theQueue.put(link)
            link = f.readline().rstrip('\n')

    # Start from queue
    while not theQueue.empty() and len(crawlSpace) < pages:
        # print(len(crawlSpace))
        link = theQueue.get()
        # print(link)
        updateCrawlSpace(link, crawlSpace)
        parseHTML(crawlSpace, link, theQueue)


# Amount of pages to process
pages = 75

# Start Program here
if __name__ == '__main__':

    # Global dictionary  to track visited links
    manger = Manager()
    links = manger.dict()

    # Global queue to start reading from
    queue = manger.Queue()

    createSpider()
    #fileName = input("Enter full file name to be read: ")
    start = currentTimeMili()
    print("Start: ", start)

    # Create a list of processes and start them
    processes = []
    num = 3
    for i in range(num):
        p = Process(target=crawlWeb, args=("urls.txt", queue, links,))
        p.start()
        processes.append(p)

    for j in range(num):
        processes[j].join()

    end = currentTimeMili()
    print("End: ", end)
    delta = end - start
    print("Delta: ", delta)
    createCSV(links)
    graphics = CrawlGraphic(links)

