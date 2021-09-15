
print('mp4ファイル、またはmp3ファイルの情報をダンプ')
import ffmpeg
import pprint

print('--------------mp4ファイルの情報--------------')
video_info = ffmpeg.probe('./test_data/MVI_0887.MP4')
pprint.pprint(video_info)

print('--------------mp3ファイルの情報--------------')
video_info = ffmpeg.probe('./test_data/MVI_0887.MP4')
pprint.pprint(video_info)

