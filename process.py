from vimeo_downloader import Vimeo
from p_tqdm import p_map

# quality we want to download
quality = '360p'

data = eval(open('collection.txt').read())
data = [i[0] for i in data[::-1]]

def dvid(url):
    id = int(url.split('/')[-1])

    #  get video info
    v = Vimeo.from_video_id(video_id=str(id))
    for s in v.streams:
        if s.quality == quality:
            
            s.download(download_directory='downloads', filename=v.metadata.title)
            return None

# parallel process
p_map(dvid,data)