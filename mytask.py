import random

def strat_game():

    print('숫자를 입력해주세요.')

    random_number = random.randint(1, 100)

    trying = 0

    while True:
        try:
            my_number = int(input())

            trying += 1

            if my_number < 1 or my_number > 100:
                print('유효한 범위내의 숫자를 입력해주세요.')
                continue

            if my_number > random_number:
                print('다운')
            elif my_number < random_number:
                print('업')
            else:
                print('정답!', f'이번게임의 시도횟수: {trying}')
                re_try()

                break

        except ValueError:
            print('숫자값만 입력가능합니다.')

def re_try():

    willing = input('다시시도하시겠습니까? (y/n)')

    if willing == 'n':
        print('게임이 종료되었습니다.')

    elif willing == 'y':
        strat_game()

    else:
        print('유효한 값을 입력해주세요.')
        re_try()


strat_game()