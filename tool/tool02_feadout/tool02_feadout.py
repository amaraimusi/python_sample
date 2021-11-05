print ('mp3をフェードアウト変換')

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

from pydub import AudioSegment
from ConfigX import ConfigX

configX = ConfigX();
configs = configX.getConfigs('./config.txt');

input_mp3_fp = configs['input_mp3_fp'];
fadeout_time = configs['fadeout_time'];
fadein_time = configs['fadein_time'];
fadeout_time = int(fadeout_time);
fadein_time = int(fadein_time);
print(fadeout_time)
print(fadein_time)

print('入力ファイルパス→' +  input_mp3_fp)
ext = stringRightRev(input_mp3_fp, '.')
ext = ext.lower()
if ext != 'mp3':
    print('mp3ファイルでありません。処理を中断します。')
    exit()

left_path = stringLeftRev(input_mp3_fp, '.')
output_mp3_fp = left_path + '_fadeout.mp3'

print('出力ファイルパス→' +  output_mp3_fp)
print('しばらくお待ちください...')

audio = AudioSegment.from_file(input_mp3_fp, "mp3")

# フェードイン,フェードアウト変換
audio2 = audio.fade_in(fadein_time).fade_out(fadeout_time)

# 変換したオーディオオブジェクトを出力
audio2.export(output_mp3_fp,  format="mp3")

print('Success!')

