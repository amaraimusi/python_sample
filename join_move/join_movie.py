


import cv2
import glob
from pydub import AudioSegment #音声操作用　mp3関連の処理
import ffmpeg

print('動画連結ツール ver 0.1.0')
# 動画リストを連結する。 mp4のみ対応
# - movie_fns [] 動画ファイルリスト（入力）
# - output_fn string 出力ファイル名（動画連結後のファイル名）
def join_movie(movie_fns, output_fn):

    # mp4を設定
    fourcc = cv2.VideoWriter_fourcc('m','p','4','v')

    # 動画リストの先頭動画からfps,画面幅を取得する
    movie = cv2.VideoCapture(movie_fns[0])
    fps = movie.get(cv2.CAP_PROP_FPS) # 動画のFPS
    height = movie.get(cv2.CAP_PROP_FRAME_HEIGHT)
    width = movie.get(cv2.CAP_PROP_FRAME_WIDTH)

    print('fps=' + str(fps))
    print('height=' + str(height))
    print('width=' + str(width))
    
    # pydubを使ってmp4ファイルの読み込み
    audio0 = AudioSegment.from_file(movie_fns[0], "mp4")

    # 出力ファイルを作成する。
    output = cv2.VideoWriter(output_fn, int(fourcc), fps, (int(width), int(height)))

    first_loop_flg = True
    for movie_fn in (movie_fns):
        print(movie_fn)
        
        if first_loop_flg == True:
            first_loop_flg = False
        else:
            # 音声ファイルの結合
            audio = AudioSegment.from_file(movie_fn, "mp4")
            audio0 += audio
        
        # 動画ファイルを読み込む
        movie = cv2.VideoCapture(movie_fn)

        # 動画連結処理
        ret = False
        if movie.isOpened() == True: # 読み込みに成功した場合
            ret, frame = movie.read() # 最初の1フレーム(1コマ）を取得する

        while ret:
            output.write(frame) # 1フレームずつ出力動画へ書き込む
            ret, frame = movie.read() # 次のフレームを取得する

    audio0.export("./output/audio.mp3", format="mp3")
    



print ('inputフォルダ内の動画を連結します。')

# inputフォルダ内の動画ファイル名をすべて取得する。
movie_fns = glob.glob("./input/*.mp4")
movie_fns = sorted(movie_fns) # 動画ファイル名リストを並べ替える。


# 連結後の動画ファイル名（出力ファイル名）
output_fn = "./output/movie_only.mp4"

join_movie(movie_fns, output_fn)

# 映像を読みこむ
stream_video = ffmpeg.input("./output/movie_only.mp4")

#オーディオを読み込む
stream_audio = ffmpeg.input("./output/audio.mp3")

#合成
stream = ffmpeg.output(stream_video, stream_audio, "./output/output.mp4", vcodec="copy", acodec="copy")
ffmpeg.run(stream)

print('Success')










