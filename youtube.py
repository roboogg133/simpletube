import pytubefix
import argparse                 
from pathlib import Path
from youtube_transcript_api import YouTubeTranscriptApi
import os
import requests  

print(

"""███████╗██╗███╗   ███╗██████╗ ██╗     ███████╗████████╗██╗   ██╗██████╗ ███████╗      
██╔════╝██║████╗ ████║██╔══██╗██║     ██╔════╝╚══██╔══╝██║   ██║██╔══██╗██╔════╝      
███████╗██║██╔████╔██║██████╔╝██║     █████╗     ██║   ██║   ██║██████╔╝█████╗        
╚════██║██║██║╚██╔╝██║██╔═══╝ ██║     ██╔══╝     ██║   ██║   ██║██╔══██╗██╔══╝        
███████║██║██║ ╚═╝ ██║██║     ███████╗███████╗   ██║   ╚██████╔╝██████╔╝███████╗      
╚══════╝╚═╝╚═╝     ╚═╝╚═╝     ╚══════╝╚══════╝   ╚═╝    ╚═════╝ ╚═════╝ ╚══════╝     """
)
print('by: roboogg133')             


parser = argparse.ArgumentParser()

parser.add_argument('link', type=str, help='Video link.')

parser.add_argument('-a', '--audio', action='store_true', help='Downloads only audio.')

parser.add_argument('-v', '--video', action='store_true', help='Download video.')

parser.add_argument('-t', '--thumbnail', action='store_true', help='Download the thumbnail.')

parser.add_argument('-o', '--output', type=str, help='Output path.', default=Path.home()/ 'Downloads')

parser.add_argument('-at', '--audiototext', action='store_true', help='Audio from youtube video to text.(Only works if the vide has captions, or automatic captions.)')

parser.add_argument('-s', '--save', action='store_true', help='save in a .txt.')


args = parser.parse_args()


link = args.link

audio = args.audio






video = pytubefix.YouTube(link)









def mwav(file):


    dst = "audio_file.wav"

    # convert mp4 to wav
    sound = AudioSegment.from_file(file,format="mp4")
    sound.export(dst, format="wav")
    return dst


def download_audio(): 
    print(f'Downloading: "{video.title}"...')   
    video.streams.filter(only_audio=True).first().download(args.output, mp3 =True)           
    print(f'{video.title} have been downloaded on: {args.output}')

def thumbnail():
    response = requests.get(video.thumbnail_url)

    if response.status_code == 200:

        image_name = str(video.title + ".jpg")
        complete_path = os.path.join(args.output, image_name)


        with open (complete_path, 'wb') as image_name:
            image_name.write(response.content)

        print(f'Saved as: {complete_path}')
    else: 
        print(f"ERROR, HTTP STATUS CODE:{response.status_code} ")

def transcript():
    video_id = video.video_id         
    

    try:                             
        otranscript = YouTubeTranscriptApi.get_transcript(video_id, languages=["pt", "en"])
        subtitle_text = " ".join([entry["text"] for entry in otranscript])


    except:
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        print("Error: availiabe languages:\n\n")

        for transcript in transcript_list:
            print(transcript.translation_languages)





    return subtitle_text
def download_video():
    print(f'Downloading: "{video.title}"...')
    video.streams.get_highest_resolution().download(args.output)


    titulo = video.title      

    print(f'{video.title} have been downloaded on: {args.output}') 





if args.thumbnail == True:
    thumbnail() 


if args.audio == True:
    download_audio()


if args.video == True:
    download_video()


if args.audiototext == True:
    otranscript = transcript()
    if args.save != True:
        print(otranscript)  


if args.save == True:
    if args.audiototext==True:

        archive_name = str(video.title + " captions.txt")

        full_path = os.path.join(args.output, str(video.title + " captions.txt"))


        with open(full_path, 'w') as archive_name:
            archive_name.write(otranscript)

        print(f'text filed saved as: {full_path}')
    else:
        print("This paramenter only works with -at")