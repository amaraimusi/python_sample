print ('pydubでmp3のカット')

# pydubを使うにはffmpegが必要-

from pydub import AudioSegment


audio = AudioSegment.from_file("./test_data/test3.mp3", "mp3")


# 5000ms～10000ms(5～10秒)を抽出
audio2 = audio[0:14000]


# 変換したオーディオオブジェクトを出力
audio2.export("./test_data/output08.mp3",  format="mp3")

print('OK')