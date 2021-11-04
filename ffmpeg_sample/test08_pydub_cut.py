print ('pydubでmp3をカットする')

from pydub import AudioSegment


# mp3ファイルの読み込み
sound = AudioSegment.from_file("./test_data/test1.mp3", format="mp3")

# 5000ms～10000ms(5～10秒)を抽出
sound1 = sound[5000:10000]

# 最後の10000ms(10秒)を抽出
sound2 = sound[-10000:]

# 抽出した部分を出力
sound1.export("output1.mp3", format="mp3")
sound2.export("output2.mp3", format="mp3")