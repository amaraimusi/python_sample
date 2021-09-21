print ('mp4にmp3を合成')


import ffmpeg

# 映像を読みこむ
stream_video = ffmpeg.input("./test_data/MVI_0887.MP4")

#オーディオを読み込む
stream_audio = ffmpeg.input("./test_data/test1.mp3")

#合成
stream = ffmpeg.output(stream_video, stream_audio, "./test_data/output07.mp4", vcodec="copy", acodec="copy")
ffmpeg.run(stream)

print('Success!')

