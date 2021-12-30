print ('mp4を動画と音声に分割する')

import os
import datetime
import ffmpeg
from pydub import AudioSegment
from ConfigX import ConfigX


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


# mp4を音声なしmp4とmp3に分割する。
# @param string input_fp 入力動画ファイルパス
# @param string output_mp4_fp 出力動画ファイルパス（音声なしmp4)
# @param string output_mp3_fp 出力音声ファイルパス（mp3)
# 
def splitVideoAndSound(input_fp, output_mp4_fp, output_mp3_fp):
    
    sound = AudioSegment.from_file(input_fp, "mp4")
    sound_sec = sound.duration_seconds # 再生時間
    print(f'音声ファイルの長さ={str(sound_sec)}')
    
    movie = cv2.VideoCapture(input_fp)
    width = movie.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = movie.get(cv2.CAP_PROP_FRAME_HEIGHT)
    video_frame_count = movie.get(cv2.CAP_PROP_FRAME_COUNT) # フレーム数を取得する
    video_fps = movie.get(cv2.CAP_PROP_FPS) 
    print(f'入力動画ファイルのFPS={str(video_fps)}')
    #video_time = (video_fps * video_frame_count) / 1000
    print(f'入力動画ファイルのフレーム数={str(video_frame_count)}')
    
    output_video_fps = video_frame_count / sound_sec
    print(f'出力動画ファイルのfps={str(output_video_fps)}')
    
    # 出力動画ファイルの用意(mp4)
    fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
    output = cv2.VideoWriter(output_mp4_fp, int(fourcc), output_video_fps, (int(width), int(height)))
    print(f'{output_mp4_fp}の出力開始')
    
    while True:
        ret, frame = movie.read()
        output.write(frame)
        if not ret:
            break
    
    # 映像オブジェクトの解放
    movie.release()
    print(f'{output_mp4_fp}の出力完了')

    # 音声ファイルの出力
    sound.export(output_mp3_fp, format="mp3")
    print(f'{output_mp3_fp}の出力完了')



dt = datetime.datetime.now()
u = dt.strftime("%M%S")

configX = ConfigX();
configs = configX.getConfigs('./config.txt');

input_mp4_fp = configs['input_mp4_fp'];


print('入力ファイルパスmp4→' +  input_mp4_fp)


# position = configs['position']
# volume = configs['volume']
# print('position=' + position)
# print('volume=' + volume)
# position = int(position);
# volume = int(volume);
ext = stringRightRev(input_mp4_fp, '.')
ext = ext.lower()
if ext != 'mp4':
    print('mp4ファイルでありません。処理を中断します。')
    exit()
    
left_path = stringLeftRev(input_mp4_fp, '.')
output_mp4_fp = left_path + '_' + u + '.mp4'
output_mp3_fp = left_path + '_' + u + '.mp3'
print('出力ファイルパスmp4→' +  output_mp4_fp)
print('出力ファイルパスmp3→' +  output_mp3_fp)



# 動画の再生時間を取得する
probe = ffmpeg.probe(input_mp4_fp)
movInfo = probe['streams'][0];
mov_duration = float(movInfo['duration']); # 動画再生時間


#動画の元の音声を取得
print('mp4読み込み中')
audio1 = AudioSegment.from_file(input_mp4_fp, "mp4")

audio1_duration =audio1.duration_seconds ; # audio1の再生時間を取得
if mov_duration > audio1_duration + 2:
    print('動画の再生時間→' + str(mov_duration))
    print('音声の再生時間→' + str(audio1_duration))
    add_ms = (mov_duration - audio1_duration) * 1000;
    print(audio1_duration)
    add_silent = AudioSegment.silent(duration=add_ms) #１秒
    audio1 = audio1 + add_silent;
    print(audio1.duration_seconds )

print('mp3読み込み中')
audio2 = AudioSegment.from_file(input_mp3_fp, "mp3")

print('mp3の音量調整')
audio2 = audio2 - 10 #音量を変更

# 元音声と追加音声のミキシング
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



input_fp = 'test_data/MVI_0887.MP4'
output_mp4_fp = 'test_data/output10.mp4'
output_mp3_fp = 'test_data/output10.mp3'

splitVideoAndSound(input_fp, output_mp4_fp, output_mp3_fp)


print('Success')

print('Success!')

