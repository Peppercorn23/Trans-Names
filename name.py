import os
from gtts import gTTS
language='en'
name=input("What name do you want to see and hear?  ")
for i in ["Hey " + name + ", come over here","How are you doing " + name + "?"] :
    aud = gTTS(text=i, lang=language, slow=False)
    aud.save("nametest.mp3")
    print(i)
    os.system("afplay nametest.mp3")
