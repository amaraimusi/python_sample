print ('pydubでmp3の音量を変更する')

# pydubを使うにはffmpegが必要-
from pydub import AudioSegment

# mp3ファイルの読み込み
audio1 = AudioSegment.from_file("./test_data/test1.mp3", "mp3")

#audio = audio1 +10; #音量を大きくする
audio = audio1 - 7; #音量を小さくする

# エクスポートする
audio.export("./test_data/output06.mp3", format="mp3")

print('Success!')

