print ('mp4からmp3を抽出する')

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

input_mp4_fp = configs['input_mp4_fp'];
print('入力ファイルパス→' +  input_mp4_fp)
ext = stringRightRev(input_mp4_fp, '.')
ext = ext.lower()
if ext != 'mp4':
    print('mp4ファイルでありません。処理を中断します。')
    exit()

left_path = stringLeftRev(input_mp4_fp, '.')
output_mp3_fp = left_path + '.mp3'

print('出力ファイルパス→' +  output_mp3_fp)
print('しばらくお待ちください...')

# # mp4ファイルの読み込み
audio = AudioSegment.from_file(input_mp4_fp)
# 
# mp3としてエクスポートする
audio.export(output_mp3_fp, format="mp3")

print('Success!')

