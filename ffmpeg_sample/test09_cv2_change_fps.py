


import cv2
import glob
from pydub import AudioSegment #音声操作用　mp3関連の処理
import ffmpeg

print('FPS変更 動画再生速度の変更を検証する')


# 動画の再生速度を変更する
# @param string input_fp 入力動画ファイルパス
# @param string output_fp 出力動画ファイルパス
# @param rete 変更後の再生速度倍率 　例:0.5→1/2のスローモーション, 2.0→2倍速再生
# 
def chageMovieSpeed(input_fp, output_fp, rate):
    # mp4を設定
    fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
    
    movie = cv2.VideoCapture(input_fp)
    fps = int(movie.get(cv2.CAP_PROP_FPS))  
    print(f'変更前fps={str(fps)}')
    
    width = movie.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = movie.get(cv2.CAP_PROP_FRAME_HEIGHT)
    
    fps2 = fps * rate
    print(f'変更後fps={str(fps2)}')
    output = cv2.VideoWriter(output_fp, int(fourcc), fps2, (int(width), int(height)))
    
    while True:
        ret, frame = movie.read()        # フレームを取得
        output.write(frame)               # 動画を保存する
        # フレームが取得できない場合はループを抜ける
        if not ret:
            break
        
    # 撮影用オブジェクトとウィンドウの解放
    movie.release()
    



input_fp = 'test_data/MVI_0887.MP4'
output_fp = 'test_data/output09.mp4'
rate = 0.5 # 変更後の再生速度倍率 　例:0.5→1/2のスローモーション, 2.0→2倍速再生


chageMovieSpeed(input_fp, output_fp, rate)


print('Success')


