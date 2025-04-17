
def IndoorVoice():
    lowercase = input("what words do you want to lower?").lower()
    print(lowercase)
#IndoorVoice()
def PlaybackSpeed():
    playbakspeed = input("what's words do you want to playback?").replace(" ","...")
    print(playbakspeed)
#PlaybackSpeed()
def face():
    emojiconvert = {
        ':)' : '🙂',
        ':(' : '🙁'
    }
    text = ''
    words = input("").split(" ")
    for i in  words:
        print(emojiconvert.get(i,i),end=" ")
        # text += emojiconvert.get(i,i) + " "
    # print(text)
# face()

def einstein():
    mass = int(input("m: "))
    print(f"E: {mass * pow(300000000,2):,}")
# einstein()

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    d = d.replace('$','')
    d = float(d)
    return round(d,1)

def percent_to_float(p):
    p = p.replace('%','')
    p = float(p) / 100
    return p
# main()