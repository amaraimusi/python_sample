print ('pydubでmp4からmp3を抽出: pydubでmp4を読み込み,mp3としてエクスポートする')

# pydubを使うにはffmpegが必要-
from pydub import AudioSegment

# mp4ファイルの読み込み
audio = AudioSegment.from_file("./test_data/MVI_0887.MP4", "mp4")

# mp3としてエクスポートする
audio.export("./test_data/output03.mp3", format="mp3")

print('Success!')

