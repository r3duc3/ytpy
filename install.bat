@echo off
echo "add path ffmpeg and %CD%"
setx path "%path%;C:\ffmpeg;%CD%"
echo "install youtube-dl and pyreadline"
pip install youtube-dl pyreadline
echo "Done!"
