import urllib.request
import re
import time
from crawlGraphics import CrawlGraphic


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
def updateCrawlSpace(start, des=None):

    global links

    if start not in links:
        links[start] = []

    if des is not None:
        aList = links[start]
        if des not in aList:
            aList.append(des)


# Parses a HTML web page given the link, adds links found to a queue
def parseHTML(link, theQueue):

    global links

    try:
        page = urllib.request.urlopen(link)
        pageText = page.read()
        linksFound = re.findall('a href[=\s][=\s]?\\"(http[s]?://.*?)\\"', str(pageText))
        for i in linksFound:
            updateCrawlSpace(link, des=i)
            if i not in links:
                theQueue.append(i)
    except (urllib.error.HTTPError, urllib.error.URLError) as e:
        print("Can't access link " + link)


# Crawls the web by first reading a file line by line and starts crawling on those links
def crawlWeb(fileName, theQueue, crawlSpace):

    global pages

    # Get the initial links first
    with open(fileName, 'r') as f:
        link = f.readline().rstrip('\n')
        while link:
            theQueue.append(link)
            link = f.readline().rstrip('\n')

    # Start from queue
    while len(theQueue) != 0 and len(crawlSpace) < pages:
        print(len(crawlSpace))
        link = theQueue.pop(0)
        # print(link)
        updateCrawlSpace(link)
        parseHTML(link, theQueue)


# Amount of pages to process
pages = 75

# Global dictionary  to track visited links
links = {}

# Global queue to start reading from
queue = []

# Start Program here
if __name__ == '__main__':
    createSpider()
    #fileName = input("Enter full file name to be read: ")
    start = time.clock()
    print("Start: ", start)
    crawlWeb("urls.txt", queue, links)
    end = time.clock()
    print("End: ", end)
    delta = end - start
    print("Delta: ", delta)
    createCSV(links)
    graphics = CrawlGraphic(links)

