from gtts import gTTS as g
import json as j

def AudioMake(text, fname):
    tts = g(text, lang='en')
    tts.save(fname)

def Audiotor():
    with open('reddit_content.json', 'r') as file:
        data = j.loads(file.read())
        i=0
        for post in data:
            AudioMake(post["title"] + post["description"] + post["com1"] + post["com2"] + post["com3"], "lssets/" + "ludio{}.mp3".format(str(i)))
            i+=1
Audiotor()


