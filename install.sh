#!/usr/bin/bash
if [ -r /usr/bin ]; then
	PREFIX='/usr/bin'
	uler='python3'
	ulerpip='python3-pip'
else
	PREFIX='/data/data/com.termux/files/usr/bin'
	uler='python'
fi

apt install ffmpeg $uler $ulerpip
pip3 install youtube-dl
echo -e -n "cd $(pwd)\npython3 yt.py" > ytpy
chmod 777 ytpy
mv ytpy $PREFIX
clear
echo -e "Done!\nKetik 'ytpy' untuk menjalankannya"
