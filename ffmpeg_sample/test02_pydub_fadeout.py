print ('pydubでmp3のフェードインとフェードアウト')

# -*- coding: utf-8 -*-
from pydub import AudioSegment
# -*- coding: utf-8 -*-
#import pydub

# 音声ファイルの読み込み
sound = AudioSegment.from_file("./test_data/test1.mp3", "mp3")

# フェードイン（3秒）、フェードアウト（4秒）
sound1 = sound.fade_in(4000).fade_out(4000)

# 保存
sound1.export("./test_data/output02.mp3", format="mp3")