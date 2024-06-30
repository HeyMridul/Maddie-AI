import speech_recognition as sr
import os
import webbrowser
import openai
from config import apikey
import datetime
import random

chatstr = ""
def chat(query):
    global chatstr
    openai.api_key = apikey
    chatstr+=f"\nMridul: {query}\nMaddie: "
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=chatstr,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

# # todo: fix this.
# def ai(content):
#     openai.api_key = apikey
#     text=f"OpenAi response for Prompt{prompt} \n**************************************\n\n"
#
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo-1106",
#         messages=[
#             {
#                 "role": "user",
#                 "content": content
#             }
#         ],
#         temperature=1,
#         max_tokens=256,
#         top_p=1,
#         frequency_penalty=0,
#         presence_penalty=0
#     )
# todo: wrap this inside of a try catch block.

    say(response["choices"][0]["text"])
    chatstr += f"{response['choices'][0]['text']}\n"
    return responce["choices"][0]["text"]
    # if not os.path.exists("Openai"):
    #     os.mkdir("Openai")

    # with open(f"Openai/prompt- {random.randint(1,23223344322342)}","w") as f:
    with open(f"Openai/{''.join(promt.split('intelligence')[1:]).strip()}.txt", "w") as f:
        f.write(text)

def say(text):
    os.system(f"say {text}")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("recognizing...")
            query = r.recognize_google(audio)
            print(f"user said: {query}")
            return query
        except Exception as e:
            return "Some Error Occured. Sorry from Maddie."

if __name__ == '__main__' :
    print("Welcome to MaddieAi  ")
    say("hello i m maddie A.I")
    while True:
        print("Listening...")
        query = take_command()

# todo: add more sites.

        sites = [["YouTube","https://www.youtube.com"] , ["wikipedia","https://www.wikipedia.com"] , ["google","https://www.google.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} Sir...!")
                webbrowser.open(site[1])

# todo: add a feature to play your specific song.

            if "open music" in query:
                musicPath = "/Users/mridulbhardwaj/Downloads/music.mp3/theme-timeless-vlog-no-copyright-music-195165.mp3"
                # os.startfile(musicPath)          ##(for window system )
                # import subprocess, sys                        ##(for mac)
                # subprocess.call(['open', musicPath])
                os.system(f"open {musicPath}")

            elif "the time".lower() in query:
                # strfTime = datetime.datetime.now().strftime("%H:%M:%S")
                # say(f"Sir the time is {strfTime}")
                Hour = datetime.datetime.now().strftime("%H")
                min = datetime.datetime.now().strftime("%M")
                say(f"Sir the time is {Hour} baj karrr {min} minute")

# todo: add more apps.

            elif "open facetime".lower() in query.lower():
                 os.system(f"open /System/Applications/FaceTime.app")

            elif "using artificial intelligence".lower() in query.lower():
                ai(promt=query)

            elif "Maddie quit".lower() in query.lower():
                say("GoodBye Sir")
                exit()
            elif "reset chat".lowe() in query.lower():
                chatstr = ""

            else:
                print("chatting....)
                chat(query)

        # say(text)