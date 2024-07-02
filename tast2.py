import random

def start_game():

    wining = 0

    draw = 0

    losing = 0

    while True:
        try:

            random_number = random.choice(['가위', '바위', '보'])

            my_number = input(str('가위, 바위, 보 중 한가지를 선택하세요.:'))

            if random_number == '가위':
                if my_number == random_number:
                    print('무승부!')
                    draw += 1

                elif my_number == '보':
                    print('패배!')
                    losing += 1

                elif my_number == '바위':
                    print('승리!')
                    wining += 1

                else:
                    print('유효한 값을 입력하세요.')

            if random_number == '바위':
                if my_number == random_number:
                    print('무승부!')
                elif my_number == '가위':
                    print('패배!')
                elif my_number == '보':
                    print('승리!')
                else:
                    print('유효한 값을 입력하세요.')

            if random_number == '보':
                if my_number == random_number:
                    print('무승부!')
                elif my_number == '바위':
                    print('패배!')
                elif my_number == '가위':
                    print('승리!')
                else:
                    print('유효한 값을 입력하세요.')

        except ValueError:
            print('유효한 값을 입력하세요.')



start_game()
