# ytpy

**Sekarang support cmd**

## Fitur
* Unduh musik youtube
* unduh video youtube
* Menlanjutkan unduhan sebelumnya

## How to install
- [download](https://github.com/r3duc3/ytpy/archive/master.zip)
atau 
- clone: 
`git clone https://github.com/r3duc3/ytpy`

buka folder ytpy lalu jalankan install.sh
```
cd ytpy
[sudo] bash install.sh
```

## Install on windows
- [Download](https://www.python.org/downloads/) Python versi 3 ke atas
- Install python, centang add python to PATH

![Install python](https://i.ibb.co/3McpJrw/IMG-20200320-145220.jpg)
- [Download](https://ffmpeg.zeranoe.com/builds/win64/static/ffmpeg-4.2.2-win64-static.zip) ffmpeg
- buka file zip
- pilih folder bin
- "extract to" C:\ffmpeg

![Install ffmpeg](https://i.ibb.co/XJ3Gcr5/IMG-20200320-145008.jpg)
- buka control panel > System and Security > System > Advanced system settings
- klik Environment Variables
- Pada user variable klik Path > New
- Ketik C:\ffmpeg

![Add ffmpeg to path](https://i.ibb.co/2ydd72H/Screenshot-33.png)
- [Download](https://github.com/r3duc3/ytpy/archive/master.zip) ytpy
- extract

## requirements
- python versi 3 ke atas
- module pip, youtube-dl
- ffmpeg

## Note
Untuk menjalankan pada terminal linux. diharusnya menggunakan root user
  * contoh: sudo ytpy

## Tested on
- terminal, kali linux 2020.1
- termux, Android
- cmd, Windows 10
