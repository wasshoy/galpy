# ----------------------------
# gal for python (galpy)
# 2019.10.05 Sat. by A.Arimura
# 2020.1.1 Wed. by A.Arimura
# ----------------------------
import random
import yaml
#import re
# import MeCab

# mecab = MeCab.Tagger('/usr/local/lib/mecab/dic/mecab-ipadic-neologd')

class GalPy:
    def __init__(self, name): 
        with open('./vocab/config_02.yaml', mode='r') as f:
            self.conf = yaml.load(f, Loader=yaml.SafeLoader)
            # ギャルの名前のリスト
            self.name_list = self.conf['name']
            # 返答のリスト
            self.responses = self.conf['answer_words']
            # 出会いの挨拶リスト
            self.open_greets = self.conf['open_greets']
            # お別れの挨拶のリスト
            self.end_greets = self.conf['end_greets']
            # 名前決め
            self.name = self.get_name(name, self.name_list)

    def get_name(self, name, name_list):
        s = ''
        if name == 'rand':
            s = random.choice(name_list)
            return s
        else:
            s = name
            return s

    def kotaeru(self, word):
        keys = ('ガンバ', '頑張', 'がんば')
        ans = ''
        judge = lambda x: x in word
        if any(map(judge, keys)):
            ans = 'すごみ is ある'
            return ans
        else:
            ans = random.choice(self.responses)
            return ans
