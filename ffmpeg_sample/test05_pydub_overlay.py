print ('pydubでオーディオのミキシング（２つの音声を合成）')

# pydubを使うにはffmpegが必要-
from pydub import AudioSegment

# mp3ファイルの読み込み
audio1 = AudioSegment.from_file("./test_data/test1.mp3", "mp3")
audio2 = AudioSegment.from_file("./test_data/effect_sound1.mp3", "mp3")

audio = audio2.overlay(audio1, position=0)

# エクスポートする
audio.export("./test_data/output05.mp3", format="mp3")

print('Success!')

