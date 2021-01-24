from pafy import new
print('''
[1] downlod video
[2] downlod audio
''')
aa = int(input('enter number : '))
if aa == 1 :
    url = input('enter url video : ')
    v = new(url)
    dl = v.getbest()
    dl.download()

elif aa ==2 :
    
    url2 = input('enter url audio: ')
    f = new(url2)
    audio = f.audiostreams
    audio[0].download()
