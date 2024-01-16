from time import *
import random as r 

def mistake(partest,usertest):
    error=0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error=error+1
        except:
            error = error+1
    return error

def speed_time(time_s,time_e,userinput):
    time_delay=time_e - time_s
    time_r = round(time_delay,2)
    speed = len(userinput) / time_r
    return round(speed)

test=[ "Welcome to our speed test platform designed to measure your internet connection's speed and quality.",
    "Experience lag-free browsing and smooth streaming by checking your download and upload speeds with our tool.",
    "Is your connection up to par? Run a quick speed test and find out how well your internet is performing.",
    "Get accurate insights into your internet speed at the click of a button using our user-friendly testing tool.",
    "Frustrated with slow downloads? Use our speed test to pinpoint if your connection is meeting your needs.",
    "Stay connected with confidence. Our speed test helps you identify any issues affecting your online experience.",
    "Optimize your gaming sessions by testing your ping and latency for a seamless online gameplay experience.",
    "Buffering interrupting your streaming? Check your internet speed to ensure a smooth entertainment experience.",
    "Empower yourself with information. Our speed test lets you compare your speeds against what you're paying for.",
    "Don't let a poor connection slow you down. Test your speed now to troubleshoot any performance bottlenecks.",
    "Elevate your remote work setup with a reliable internet connection. Test your speeds for a productive workday.",
    "Unlock the true potential of your internet. Our speed test assists you in identifying and fixing connectivity issues.",
    "Join thousands of satisfied users who have optimized their internet using our accurate and efficient speed testing.",
    "Whether you're a casual surfer or a heavy downloader, our speed test helps you gauge your connection's capabilities.",
    "Experience online content the way it's meant to be. Use our speed test to ensure top-notch video and audio quality.",
    "Make informed decisions about your ISP with concrete data. Our speed test provides transparent results.",
    "Is latency impacting your online activities? Test your ping and latency to improve your real-time experiences.",
    "Stay ahead of the digital curve by regularly assessing your connection's performance with our speed test.",
    "Your virtual classroom deserves the best connection. Test your speed for lag-free online learning.",
    "Turn frustration into satisfaction. Identify slow spots in your connection with our comprehensive speed test."
]
test1=r.choice(test)
print("******typing test *******")
print(test1)
print()
print()
time_1=time()
testinput=input("enter :")
time_2=time()

print('speed',speed_time(time_1,time_2,testinput),"w/sec")
print("error",mistake(test1,testinput))
