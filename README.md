# HFE-L3Anatomy
converting the lectures into a mp3 for listening whilst running. 


Sourcelist: https://vimeo.com/269866346 , select more until you reach #1


```
NUM_PARALLEL=8
ext='.mp4'
outdir='mp3'
indir='downloads'
mkdir ${outdir}

speed="1.2"
faster="mp3-${speed}x"
mkdir ${faster}

(
for thing in ${indir}/*${ext}; do 
   ((i=i%NUM_PARALLEL)); ((i++==0)) && wait
   base=$(basename $thing $ext)
   # echo "- $thing $outdir/${base}.mp3" &  

   # to mp3
   ffmpeg -i ${thing} ${outdir}/${base}.mp3 && ffmpeg -i ${outdir}/${base}.mp3 -filter:a "atempo=${speed}" ${faster}/${base}.mp3 &
done
)


```


