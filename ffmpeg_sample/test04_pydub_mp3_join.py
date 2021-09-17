print ('pydubでmp3を連結する')

# pydubを使うにはffmpegが必要-
from pydub import AudioSegment

# mp3ファイルの読み込み
audio1 = AudioSegment.from_file("./test_data/test1.mp3", "mp3")
audio2 = AudioSegment.from_file("./test_data/test2.mp3", "mp3")
audio3 = AudioSegment.from_file("./test_data/test3.mp3", "mp3")

# オーディオを連結する
audio = audio1 + audio2 + audio3

# エクスポートする
audio.export("./test_data/output04.mp3", format="mp3")

print('Success!')

