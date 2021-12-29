
# 設定データの取得
# auther kenji uehara
# version 1.0.0
# since 2021-11-5
class ConfigX:
    
    def getConfigs(self, text_fn):
        configs = {}
        
        # 設定ファイルを読み込み
        f = open(text_fn, 'r', encoding='UTF-8')
        text_all = f.read()
        f.close()
            
        lines = text_all.split('\n')
        for line in lines:
            if ('=' in line) == False: continue
            field = self.__stringLeft(line, '=');
            field = field.strip()
            value = self.__stringRight(line, '=');
            value = value.strip()
            configs[field] = value
            
        return configs
    
    # 文字列を左側から印文字を検索し、左側の文字を切り出す
    # @param string s 対象文字列
    # @param $mark 印文字
    # @return 印文字から左側の文字列
    def __stringLeft(self, s, mark):
        a =s.find(mark)
        res = s[0:a]
        return res
    
    
    # 文字列を左側から印文字を検索し、右側の文字を切り出す。
    # @param string s 対象文字列
    # @param $mark 印文字
    # @return 印文字から右側の文字列
    def __stringRight(self, s, mark):
        a =s.find(mark)
        res = s[a+len(mark):]
        return res
        