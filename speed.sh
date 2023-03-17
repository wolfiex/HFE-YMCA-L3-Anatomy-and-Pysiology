
cd "mp3";
speed="1.2"
mkdir "mp3-${speed}x"

for f in *.mp3
  do ffmpeg -i "$f" -filter:a "atempo=${speed}" "./speed-${speed}x/$f"
done
