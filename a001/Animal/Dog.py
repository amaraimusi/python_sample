class Dog:
    
    # コンストラクタ
    def __init__(self):
        print('犬のコンストラクタ')
        self.type_a = 'xxx' # publicメンバ
        self.__type_b = '犬科' # privateメンバ

    # publicメソッド
    def bark(self, animal_name):
        print(f'{animal_name}がほえる')
        print(self.type_a) # メンバにアクセス
        print(self.__type_b)
        print(self.__work()) # 同クラス内のメソッドの呼び出し
        
    # privateメソッド
    def __work(self):
        print('犬もあるけば棒にあたる')