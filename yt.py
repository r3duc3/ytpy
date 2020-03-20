#!/usr/bin/python3

'''
coder: _reduce
Mau recode? setidaknya bagian ini jangan dihapus
cantumkan nama pemiliknya ea bujank
'''

from multiprocessing import Process as pro
import os, time

w = tuple([chr(27)+'[1;0m'] + list(chr(27)+'[1;3'+str(x)+'m' for x in range(1,7)))

if os.name == 'nt':
    clean = 'cls'
    apus = 'del'
    slash = '\\'
else:
    clean = 'clear'
    apus = 'rm'
    slash = '/'

def loading(x='', y=False):
    global a
    if os.name == 'nt':
        print(x, end='', flush=True) if x != '' else None
    else:
        if y:
            a = pro(target=lod, args=(x,))
            a.start()
        else:
            a.kill()

def lod(txt):
    print(w[4]+txt,end='')
    while True:
        for x in range(6):
            print('.',end='',flush=True)
            time.sleep(0.3)
        print('\b ',end='')
        for x in range(5):
            print('\b\b',end=' ',flush=True)
            time.sleep(0.1)
        print('\b',end='')

def cls():
    print('\n'*30)
    os.system(clean)
    print(f'''{w[1]} /$$     /$$ /$$     /$$$$$$$           
|  $$   /$$/| $$    | $$__  $$          
 \  $$ /$$//$$$$$$  | $$  \ $$ /$$   /$$
  \  $$$$/|_  $$_/  | $$$$$$$/| $$  | $$
   \  $$/   | $$    | $$____/ | $$  | $$
{w[0]}    | $$    | $$ /$$| $$      | $$  | $$
    | $$    |  $$$$/| $$      |  $$$$$$$
    |__/     \___/  |__/       \____  $$
                               /$$  | $$
                              |  $$$$$$/
                               \______/   v. 3.2''')

cls()
loading('Loading', True)
try:
    import youtube_dl, readline, json, re, sys
    from urllib.request import urlopen as req, Request

except Exception as ex:
    loading()
    exit(f"Module '{ex.name}' belum terinstall\nsilahkan install dengan command:\n\t[sudo] python3 -m pip install {ex.name}")

ytdl = youtube_dl.YoutubeDL

readline.set_history_length(1024)

cmd = (
        'q', 'exit',
        'set',
        'dl',
        'h', 'help',
        'cls'
        )

lsform = {
        144 : '160',
        240 : '133',
        360 : '134',
        480 : '135',
        720 : '136',
        1080 : '137'
        }

def size(num, suffix='B'):
    for unit in ['','K','M','G','T','P','E','Z']:
        if abs(num) < 1024.0:
            return "%04.2f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.2f%s%s" % (num, 'Y', suffix)

def q():
    exit()

def help():
    print('''Command yang tersedia:
    - q, exit
    - h, help
    - dl -> download audio | video dari url youtube
    - set -> setting tipe, bit, dir
    - cls -> clean screen''')

def h(): help()

def check(one, two):
    if one.isnumeric() and -1 < int(one)-1 < len(two):
        return True
    else:
        return False

def change(ada):
    global tipe,bit,dor
    if not ada:
        tipe,bit,dor = ('mp3',320,'Download')

    p = {
            'tipe' : tipe,
            'bit' : bit,
            'dir' : dor
            }
    open('.user.json','w').write(json.dumps(p));

def set():
    global tipe, bit, dor
    bits = {
            'mp3' : (64, 96, 128, 192, 256, 320),
            'mp4' : (144, 240, 360, 720, 1080)
        }
    cmd = ('tipe', 'bit', 'dir', 'default')
    for x in cmd:
        y = cmd.index(x)+1
        print(f'\t{y}. {x}')

    hah = input('pilih: ')
    if check(hah, cmd):
        hah = int(hah)-1
        if hah == 0:
            for x in bits.keys():
                y = tuple(bits.keys()).index(x)+1
                print(f'\t{y}. {x}')
            hah2 = input('pilih: ')
            if check(hah2, bits.keys()):
                tipe_old = tipe
                tipe = tuple(bits.keys())[int(hah2)-1]
                if tipe != tipe_old:
                    bit = 360 if tipe == 'mp4' else 320

        elif hah == 1:
            for x in bits[tipe]:
                y = bits[tipe].index(x)+1
                print(f'\t{y}. {x}')
            hah2 = input('pilih: ')
            if check(hah2, bits[tipe]):
                bit = bits[tipe][int(hah2)-1]

        elif hah == 2:
            hah2 = input('new location: ')
            if hah2 == '':
                return
            if not os.path.exists(hah2):
                os.mkdir(hah2)

            dor = hah2

        elif hah == 3:
            change(False)

        if hah in (0,1,2):
            change(True)

def dl():
    con = False
    idih = input('url: ')
    if idih == '': return
    cls()
    loading('Ngambil informasi', True)
    try:
        info = req(f'https://www.youtube.com/oembed?url={idih}')
    except Exception as exc:
        loading()
        print()
        if 'code' in dir(exc):
            print(f'{exc.code} {exc.msg}')
        else:
            print(exc)
        return

    opt = {'quiet' : True}
    quest = ytdl(opt).extract_info(f'{idih}', download=False)
    title = re.sub('/', '_',quest['title'])
    form = '251' if tipe == 'mp3' else lsform[bit]
    for x in quest['formats']:
        if x['format_id'] == form:
            url = x['url']
            break

    if os.path.exists(f'{dor}/{title}.{tipe}'):
        loading()
        ask = input(f'\n{title} sudah ada\nLanjut?[y/n] ')
        if ask not in ('Y','y'):
            return
        else:
            os.remove(f'{dor}/{title}.{tipe}')

    elif os.path.exists(f'.{title}.{tipe}.download'):
        loading()
        ask = input('\nMau melanjutkan unduhan yang sudah ada?[y/n] ')
        if ask in ('y','Y'):
            con = True

    width = os.get_terminal_size().columns
    open('.0.jpg','wb').write(req(f'https://i.ytimg.com/vi/{quest["id"]}/0.jpg').read())
    if con:
        hed = Request(url)
        pan = len(open(f'.{title}.{tipe}.download', 'rb').read())
        hed.add_header('Range', f'bytes={pan}-')
        resp = req(hed)
        bytesdone = pan
        total = pan
    else:
        resp = req(url)
        bytesdone = 0
        total = 0
    total += int(resp.info()['Content-Length'].strip())
    chunksize, t0 = 16384, time.time()
    outfh = open(f'.{title}.{tipe}.download', 'ab')
    loading(); cls()
    open(f'logs/{title}.txt','w', encoding='utf-8').write(f'''{"Information".center(width,"=")}
Uploader: {quest["uploader"]}
Title: {quest["title"]}
Thumbnail: https://i.ytimg.com/vi/{quest["id"]}/0.jpg
Description:
{quest["description"]}
{"="*width}''')
    print('\r'+open(f'logs/{title}.txt','rb').read().decode())
    print(f'{w[1]}Informasi tersimpan: logs{slash}{title}.txt\n{w[5]}Downloading: {title} ({size(total)})')
    while True:
        chunk = resp.read(chunksize)
        outfh.write(chunk)
        elapsed = time.time() - t0
        bytesdone += len(chunk)
        rate = 0
        if elapsed != 0:
            rate = (bytesdone / 1024) / elapsed
        if rate:
            eta = (total - bytesdone) / (rate * 1024)
        else:
            eta = 0
        if not chunk:
            outfh.close()
            break
        print(f'\r{" "*(width)}', end='')
        print('\r{2}[{0}{1}{2}] [{0}{3:.2%}{2}] [{0}{4:4.0f} kbps{2}] [{0}{5:.0f} secs{2}]'.format(w[0], size(bytesdone), w[2], bytesdone * 1.0 / total, rate, eta),end='', flush=True)
    print()
    loading('Tunggu dong', True)
    if tipe == 'mp3':
        os.system(f'ffmpeg -nostats -loglevel 0 -i "{outfh.name}" -vn -ab {bit}k -ar 48000 ".out.mp3" && ffmpeg -nostats -loglevel 0 -i ".out.mp3" -i .0.jpg -map 1:0 -map 0:0 -c:a copy -c:v copy -id3v2_version 3 "{dor}/{title}.mp3" && {apus} .0.jpg "{outfh.name}" ".out.mp3"')
    else:
        open(f'.{title}.audio','wb').write(req(quest['requested_formats'][1]['url']).read())
        os.system(f'ffmpeg -nostats -loglevel 0 -i "{outfh.name}" -i ".{title}.audio" -c:v copy -map 0:v:0 -map 1:a:0 -b:a 320k "{dor}/{title}.mp4" && {apus} .0.jpg ".{title}.audio" "{outfh.name}"')
    loading(); cls()
    print(f'Downloaded: {dor}{slash}{title}.{tipe}')

if not os.path.exists('logs'):
    os.mkdir('logs')

if not os.path.exists('.user.json'):
    change(False)

op = json.loads(open('.user.json').read())
tipe, bit, dor = op.values()
if not os.path.exists(dor):
    os.mkdir(dor)

cls(); loading()
while True:
    try:
        print(f'{w[1]}[{tipe}]{w[2]}[{bit}{"Kbps" if tipe == "mp3" else "p"}]{w[3]}[{dor}]')
        main = input(f'{w[6]}>>> {w[0]}')
        main = main.split() if main != '' else main
        if len(main) >= 1 and type(main) == list:
            if main[0] not in cmd:
                print(f'\x1b[7;31mtidak ada command "{main[0]}"{w[0]}')
            else:
                exec(f'{main[0]}()')
    except:
        exit()
