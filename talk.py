import time
import random
import sys
import galpy as gp
def interface(): 
    time_start  =time.time()
    print('-'*29 + 'ギャルとお話しよう!!(v.0.0.20)' + '-'*29)
    user_name = input('your name >>> ')
    name_conf = input('gal name >>> ')
    gal = gp.GalPy(name_conf)
    gal_name = gal.name

    print('({}) {}'.format(gal_name, random.choice(gal.open_greets)))
    while(1):
        try: mine = input('({}) '.format(user_name))
        except EOFerror: mine = ':q'
        time.sleep(0.1)
        if ':q' in mine:
            goodby = '({}) {}'.format(gal_name, random.choice(gal.end_greets))
            print(goodby)
            time_end = time.time()
            elapsed_time = time_end - time_start
            print('-'*30 + '君は{}秒を{}に費やしたよ!'.format(int(elapsed_time), gal_name) + '-'*30)
            print('-'*30 + 'さあ、論文を読もう!!' + '-'*38)
            sys.exit()
        #print('({}) {}'.format(gal_name, gal.kotaeru(mine)))
        print('({}) {}'.format(gal_name, gal.respond(mine)))

if __name__ == '__main__':
    interface()
