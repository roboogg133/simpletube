import pytubefix
import argparse
from pathlib import Path

print(

"""███████╗██╗███╗   ███╗██████╗ ██╗     ███████╗████████╗██╗   ██╗██████╗ ███████╗      
██╔════╝██║████╗ ████║██╔══██╗██║     ██╔════╝╚══██╔══╝██║   ██║██╔══██╗██╔════╝      
███████╗██║██╔████╔██║██████╔╝██║     █████╗     ██║   ██║   ██║██████╔╝█████╗        
╚════██║██║██║╚██╔╝██║██╔═══╝ ██║     ██╔══╝     ██║   ██║   ██║██╔══██╗██╔══╝        
███████║██║██║ ╚═╝ ██║██║     ███████╗███████╗   ██║   ╚██████╔╝██████╔╝███████╗      
╚══════╝╚═╝╚═╝     ╚═╝╚═╝     ╚══════╝╚══════╝   ╚═╝    ╚═════╝ ╚═════╝ ╚══════╝      
                                                                                      
██████╗  ██████╗ ██╗    ██╗███╗   ██╗██╗      ██████╗  █████╗ ██████╗ ███████╗██████╗ 
██╔══██╗██╔═══██╗██║    ██║████╗  ██║██║     ██╔═══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
██║  ██║██║   ██║██║ █╗ ██║██╔██╗ ██║██║     ██║   ██║███████║██║  ██║█████╗  ██████╔╝
██║  ██║██║   ██║██║███╗██║██║╚██╗██║██║     ██║   ██║██╔══██║██║  ██║██╔══╝  ██╔══██╗
██████╔╝╚██████╔╝╚███╔███╔╝██║ ╚████║███████╗╚██████╔╝██║  ██║██████╔╝███████╗██║  ██║
╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝"""
)
print('by: roboogg133')             


parser = argparse.ArgumentParser()

parser.add_argument('link', type=str, help='Video link.')

parser.add_argument('-a', '--audio', action='store_true', help='Downloads only audio.')

parser.add_argument('-t', '--thumbnail', action='store_true', help='Get the thumbnail link')

parser.add_argument('-o', '--output', type=str, help='Output path.', default=Path.home()/ 'Downloads')


args = parser.parse_args()


link = args.link

audio = args.audio

video = pytubefix.YouTube(link)




def download_audio():       
    video.streams.filter(only_audio=True).first().download(args.output)
    titulo = video.title            
    print(str(titulo) + ' have been downloaded on: ' + str(args.output))

def thumbnail():
    print(video.thumbnail_url)

if args.thumbnail == True:
    thumbnail()
if args.audio == True:
    download_audio()
else:
    video.streams.get_highest_resolution().download(args.output)
    titulo = video.title            
    print(str(titulo) + ' have been downloaded on: ' + str(args.output))
