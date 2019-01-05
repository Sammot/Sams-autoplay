from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time
import os
import random

proval = True
titleval = True
dev = False

def mutetoggle():
        try:
            mute = driver.find_element_by_xpath("""//*[@id="movie_player"]/div[20]/div[2]/div[1]/span/button""")
            mute.click()
            time.sleep(0.1)
        except Exception as e:
            print("Runtime Log: " + str(e))
            trymute()
            

print("In order to get the full experience, you must sign into your google account.")
print("")

if dev == True:
        firstnode = "https://www.youtube.com/watch?v=xrTT-fZTyiE"
        passwordget = "silva2904"
        usernameget = "ddspaws4life@gmail.com"
else:
        usernameget = input("Your google account email address: ")
        passwordget = input("Your google account password: ")
        firstnode = input("First youtube video link: ")



driver = webdriver.Chrome()
driver.get("https://accounts.google.com/signin/v2/identifier?passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den-GB%26next%3D%252F&uilel=3&service=youtube&hl=en-GB&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
emailinput = driver.find_element_by_xpath("""//*[@id="identifierId"]""")
emailinput.send_keys(usernameget)
emailinput.send_keys(Keys.ENTER)
time.sleep(1)

passwordinput = driver.find_element_by_xpath("""//*[@id="password"]/div[1]/div/div[1]/input""")
passwordinput.send_keys(passwordget)
passwordinput.send_keys(Keys.ENTER)
time.sleep(0.9)

if dev == True:
    try:
        sidepanel = driver.find_element_by_xpath("""//*[@id="guide-icon"]""")
        sidepanel.click()
        for i in range(4):
            try:
                subget = sidepanel.find_element_by_xpath("""//*[@id="items"]/ytd-guide-entry-renderer[""" + str(i) + """]""")
                subname = subget.find_element_by_xpath("""//*[@id="items"]/ytd-guide-entry-renderer[""" + str(i) + """]""")
                subfloat = subname.text
                print(subfloat)
            except:
                print("Runtime log: Subscription obtainment error.")
    except:
        print("Runtime log: Failed to fetch subscriptions")
    
driver.get(firstnode)

while proval == True:
    
    videoplay = True
    autoplaylist = []
    
    print("")
    if titleval == True:
        print("-----------------------Starting First Video-----------------------")
        titleval = False
    else:
        print("-----------------------Next Video-----------------------")

    #vid = driver.find_element_by_xpath("""//*[@id="items"]/ytd-compact-video-renderer[3]""")
    #vid.click()
    time.sleep(20)

    try:
        mutehover = driver.find_element_by_xpath("""//*[@id="container"]/h1/yt-formatted-string""")
        hover = ActionChains(driver).move_to_element(mutehover)
        hover.perform()
        time.sleep(0.9)
    except:
        print("Runtime log: Failed to mouseover the timeline.")

    for i in range(10):
        try:
            currenttimeget = driver.find_element_by_xpath("""//*[@id="movie_player"]/div[27]/div[2]/div[1]/div/span[1]""")
            durationget = driver.find_element_by_xpath("""//*[@id="movie_player"]/div[27]/div[2]/div[1]/div/span[3]""")
        except:
            print("Runtime log: Video time error, try leaving you mouse hovering over the time bar to keep it present")
            print("")
            currenttimeget = driver.find_element_by_xpath("""//*[@id="movie_player"]/div[27]/div[2]/div[1]/div/span[1]""")
            durationget = driver.find_element_by_xpath("""//*[@id="movie_player"]/div[27]/div[2]/div[1]/div/span[3]""")

    videonameget = driver.find_element_by_xpath("""//*[@id="container"]/h1/yt-formatted-string""")
    videoname = videonameget.text
    print("Video name: " + videoname)
    print("")
    
    channelnameget = driver.find_element_by_xpath("""//*[@id="owner-name"]/a""")
    channelname = channelnameget.text
    print("Channel name: " + channelname)
    print("")
    currenttime = currenttimeget.text
    duration = durationget.text
    print("Current video time: " + currenttime)
    print("Duration of video: " + duration)

    print("")
    durationminute, durationseconds = duration.split(":")
    #print("Duration in minutes: " + durationminute)
    #print("Duration in seconds: " + durationseconds)
    floatduration = durationminute + "." + durationseconds
    #print(floatduration)
    #print("")
        
    playbackminute, playbackseconds = currenttime.split(":")
    #print("playback point in minutes: " + playbackminute)
    #print("playback point in seconds: " + playbackseconds)
    floatplayback = playbackminute + "." + playbackseconds
    #print(floatplayback)

    minuteminus = int(durationminute) - 1
    endpoint = str(minuteminus) + ":" + str(durationseconds)
    print("Play next video at: " + str(endpoint))

    while videoplay == True:
        try:
            currenttimeget = driver.find_element_by_xpath("""//*[@id="movie_player"]/div[27]/div[2]/div[1]/div/span[1]""")
            currenttime = currenttimeget.text
        except:
            print("Runtime log: Something has blocked the script from reading the time of the video, possibly an advertisement.")
            
        if str(endpoint) == currenttime:
            print("")
            print("Video Candidates: ")
            print("")
            for i in range(21):
                try:
                    floatvid = driver.find_element_by_xpath("""//*[@id="items"]/ytd-compact-video-renderer[""" + str(i) + """]""")
                    viduploader = floatvid.find_element_by_id("byline")
                    uploader = viduploader.text
                    print(uploader)
                    if uploader == channelname:
                        autoplaylist.append("""//*[@id="items"]/ytd-compact-video-renderer[""" + str(i) + """]""")
                except:
                    print("Runtime log: channel name obtainment error.")

            print("Possible next video xpaths: \n\n" + str(autoplaylist))
            videoplay = False
    nextvideoget = random.choice(autoplaylist)
    nextvideo = driver.find_element_by_xpath(nextvideoget)
    print("Chosen next video xpath: " + nextvideoget)
    nextvideo.click()
    #driver.quit()
