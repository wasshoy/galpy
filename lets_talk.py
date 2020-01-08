import time
import random
import sys
import galpy as gp
def interface(): 
    time_start  =time.time()
    print('-'*29 + 'ギャルとお話しよう!!(v.0.0.20)' + '-'*29)
    user_name = input('your name >>> ')
    if user_name == '':
        user_name = 'you'
    name_conf = input('gal name >>> ')
    gal = gp.GalPy(name_conf)
    gal_name = gal.name

    # 始まりの挨拶
    if user_name == 'you':
        print('({}) {}'.format(gal_name, random.choice(gal.open_greets)))
    else:
        print('({}) {} {}'.format(gal_name, user_name, random.choice(gal.open_greets)))
    
    # 返答部分
    while(1):
        # 自分の入力
        mine = input('({}) '.format(user_name))
        time.sleep(0.1)    # 人間味
        # ':q' で終了コマンド
        if ':q' in mine:
            # お別れの挨拶
            goodby = '({}) {}'.format(gal_name, random.choice(gal.end_greets))
            print(goodby)
            time_end = time.time()
            elapsed_time = time_end - time_start
            print('-'*30 + '君は{}秒を{}に費やしたよ!'.format(int(elapsed_time), gal_name) + '-'*30)
            print('-'*30 + 'さあ、論文を読もう!!' + '-'*38)
            sys.exit()
        # 返答
        # print('({}) {}'.format(gal_name, gal.kotaeru(mine)))
        print('({}) {}'.format(gal_name, gal.respond(mine)))

if __name__ == '__main__':
    interface()
