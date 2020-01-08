# ----------------------------
# gal for python (galpy)
# 2019.10.05 Sat. by A.Arimura
# ----------------------------
import random
import yaml
import re
import MeCab

tagger = MeCab.Tagger('/usr/local/lib/mecab/dic/mecab-ipadic-neologd')

class GalPy:
    def __init__(self, name): 
        # メインテーブルのkeyとvalue(keyは正規表現をコンパイルしたもの)のリストを取得

        # 反応する言葉のリスト
        #self.keys = list(map(lambda x: re.compile(x[0]), gPats))
        # 返す言葉のリスト
        #self.values = list(map(lambda x: x[1], gPats))

        with open('./vocab/responce_key.yaml', mode='r') as f:
            d = yaml.load(f, Loader=yaml.SafeLoader)
            self.keys = list(map(lambda x: re.compile(x[0]), d))
            self.values = list(map(lambda x: x[1], d))
        ## テスト用 ##
        print('reaction words:\n {}'.format(self.keys))
        print('respond words:\n {}'.format(self.values))
        ## テストここまで ##

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
# ----------------------------------------
# translate(str, dict):
# strの中からdict(gReflects)のkeyと一致する言葉があればそのvalueを返す
# ----------------------------------------
    def translate(self, str, dict):
        '''
        translate(str, dict):
        strを形態素解析し、dictのkeyと一致する言葉があればそのvalueに変換する\n
        最終的に変換した文字列を返す
        '''
        # 形態素解析
        node = tagger.parseToNode(str)
        ws = ''
        while node:
            ws += node.surface + ' '
            node = node.next
        words = ws.split()
        keys = dict.keys()
        for i in range(0, len(words)):
            # 1単語ずつkeyと比較し、dictにあればそのvalueに変換
            if words[i] in keys:
                words[i] = dict[words[i]]
        return ''.join(words)

# ----------------------------------------
# respond:
# 会話の言葉に対する返答を選ぶ
# gPotsの語彙から選ぶ
# ----------------------------------------
    def respond(self, str):
        '''
        返答システム部分
        '''
        for i in range(0, len(self.keys)):
            # 反応する言葉のリストにあるような文体がきたら一致する返答パターンリストから乱択して返す
            # 文字列の左から一致するものを探す
            # re.compile('反応パターン').matchで一致結果を格納
            match = self.keys[i].match(str)
            if match:
                resp = random.choice(self.values[i])
                # str.find(s): str内のsがある位置のindexを返す(ない場合-1を返す)
                pos = resp.find('%')
                while pos > -1:
                    # resp内の最後の%までrespを更新
                    # %の横の数字がnum
                    # matchしている部分を変換して返す
                    num = int(resp[pos+1:pos+2])
                    resp = resp[:pos] + \
                            self.translate(match.group(num), gReflections) + \
                            resp[pos+2:]
                    pos = resp.find('%')
                return resp

    def get_name(self, name, name_list):
        '''
        ギャルの名前選択
        '''
        s = ''
        if name == 'rand' or name == '':
            s = random.choice(name_list)
            return s
        else:
            s = name
            return s

    def kotaeru(self, word):
        '''
        旧返答システム部分
        '''
        keys = ('ガンバ', '頑張', 'がんば')
        ans = ''
        judge = lambda x: x in word
        if any(map(judge, keys)):
            ans = 'すごみ is ある'
            return ans
        else:
            ans = random.choice(self.responses)
            return ans

# ------------------------------------------
# nameに対してあーしとかウチとかで返すやつのペア 
# ------------------------------------------
gReflections = {
                'きみ' : 'あーし',
                '君' : 'あーし',
                'おまえ': 'あーし',
                'お前': 'あーし'
               }
# ------------------------------------------
# メインテーブル
# gPats[i][0]は反応する言葉の正規表現のかたち
# gPats[i][1][j]は反応した言葉に対する回答パターンのレパートリー
# ------------------------------------------
'''
Pats = [
            [r'(.*)ほしい',
                ['なんで%1なの?',
                 'ほんとに%1なの?'
                ]
            ],

            [r'なんで([^\?]i*)',
                ['ホントにあーし%1しちゃダメ?',
                 #'たぶんタピりながら%1するｗ',
                 'あーしに%1してほしいの?'
                ]
            ],
            [r'(.*)',
                [#"なになに??",
                 #"どゆこと😂??",
                 #"ごめん、ちょいわからんっ😅",
                 "ふーん(よくわからんw)"
                ]
            ]
        ]
'''