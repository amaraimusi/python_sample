print ('pydubでmp3のフェードインとフェードアウト')

# pydubを使うにはffmpegが必要-

from pydub import AudioSegment


audio = AudioSegment.from_file("./test_data/test3.mp3", "mp3")

# フェードイン4秒、フェードアウト3.5秒に変換したオーディオオブジェクトを作成
audio2 = audio.fade_in(4000).fade_out(3500)

# 変換したオーディオオブジェクトを出力
audio2.export("./test_data/output02.mp3",  format="mp3")