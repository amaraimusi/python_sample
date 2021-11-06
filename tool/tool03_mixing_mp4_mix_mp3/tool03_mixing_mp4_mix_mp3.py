print ('mp4にmp3をミキシング')

# 文字列を右側から印文字を検索し、右側の文字を切り出す
# @param string s 対象文字列
# @param $mark 印文字
# @return 印文字から右側の文字列
def stringRightRev(s, mark):
    a =s.rfind(mark)
    res = s[a+len(mark):]
    return res

# 文字列を右側から印文字を検索し、左側の文字を切り出す
# @param string s 対象文字列
# @param $mark 印文字
# @return 印文字から左側の文字列
def stringLeftRev(s, mark):
    a =s.rfind(mark)
    res = s[0:a]
    return res

import os
import datetime
import ffmpeg
from pydub import AudioSegment
from ConfigX import ConfigX

dt = datetime.datetime.now()
u = dt.strftime("%Y%m%d%H%M%S")

configX = ConfigX();
configs = configX.getConfigs('./config.txt');

input_mp4_fp = configs['input_mp4_fp'];
input_mp3_fp = configs['input_mp3_fp'];

print('入力ファイルパスmp4→' +  input_mp4_fp)
print('合成オーディオパスmp3→' +  input_mp3_fp)
position = configs['position']
volume = configs['volume']
print('position=' + position)
print('volume=' + volume)
position = int(position);
volume = int(volume);
ext = stringRightRev(input_mp4_fp, '.')
ext = ext.lower()
if ext != 'mp4':
    print('mp4ファイルでありません。処理を中断します。')
    exit()
    
ext = stringRightRev(input_mp3_fp, '.')
ext = ext.lower()
if ext != 'mp3':
    print('合成オーディオファイルはmp3ファイルでありません。処理を中断します。')
    exit()
    
tmp_fn = 'tmp' + u +  ' .mp3'
    
left_path = stringLeftRev(input_mp4_fp, '.')
output_mp4_fp = left_path + '_' + u + '.mp4'
print('出力ファイルパスmp4→' +  output_mp4_fp)




print('mp4読み込み中')
audio1 = AudioSegment.from_file(input_mp4_fp, "mp4")

print('mp3読み込み中')
audio2 = AudioSegment.from_file(input_mp3_fp, "mp3")

print('mp3の音量調整')
audio2 = audio2 - 10 #音量を変更
    
print('音声のミキシング中')
audio3 = audio1.overlay(audio2, position=position)
print('ミキシングした音声を仮出力')
audio3.export(tmp_fn,  format="mp3")

# 既存があれば除去する
print('既存ファイルを除去')
if os.path.exists(output_mp4_fp):
    os.remove(output_mp4_fp)

# 映像を読みこむ
print('映像と音声の再結合処理中...')
stream_video = ffmpeg.input(input_mp4_fp)
stream_audio = ffmpeg.input(tmp_fn)
stream = ffmpeg.output(stream_video, stream_audio, output_mp4_fp, vcodec="copy", acodec="copy")
print('最終出力中...')
ffmpeg.run(stream)

os.remove(tmp_fn)

# print('mp4読み込み中')
# audio1 = AudioSegment.from_file(input_mp4_fp, "mp4")
#
# print('mp3読み込み中')
# audio2 = AudioSegment.from_file(input_mp3_fp, "mp3")
#
# print('音声のミキシング中')
# audio3 = audio1.overlay(audio2, position=position)
#
#
# print('出力中...')
# audio3.export(output_mp4_fp,  format="mp4")





# # mp4ファイルの読み込み
# audio = AudioSegment.from_file(input_mp4_fp, "mp4")
#
# # mp3としてエクスポートする
# audio.export("tmp.mp3", format="mp3")
#
# audio1 = AudioSegment.from_file(input_mp3_fp, "mp3")
# audio2 = AudioSegment.from_file('tmp.mp3', "mp3")
#
# audio3 = audio2.overlay(audio1, position=position)
#
# audio3.export(output_mp3_fp,  format="mp3")





#stream = ffmpeg.output(stream_video, stream_audio, "./test_data/output07.mp4", vcodec="copy", acodec="copy")

#
# left_path = stringLeftRev(input_mp3_fp, '.')
# output_mp3_fp = left_path + '_fadeout.mp3'
#
# print('出力ファイルパス→' +  output_mp3_fp)
# print('しばらくお待ちください...')
#
# audio = AudioSegment.from_file(input_mp3_fp, "mp3")
#
# # フェードイン,フェードアウト変換
# audio2 = audio.fade_in(fadein_time).fade_out(fadeout_time)
#
# # 変換したオーディオオブジェクトを出力
# audio2.export(output_mp3_fp,  format="mp3")

print('Success!')

