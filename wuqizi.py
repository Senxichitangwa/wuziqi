finish = False
flagNum = 1
flagch = '*'
x = 0
y = 0
print('\033[1;37;41m---------简易五子棋游戏（控制台版）---------\033[0m')

#棋盘初始化
checkerboard = []
for i in range(10):
    checkerboard.append([])
    for j in range(10):
        checkerboard[i].append('-')
def msg():
    #输出最后胜利的棋盘
    print("\033[1;37;41m--------------------------------")
    print("   1  2  3  4  5  6  7  8  9  10")
    for i in range(len(checkerboard)):
        print(chr(i+ord('A'))+ " ", end=' ')
        for j in range(len(checkerboard[i])):
            print(checkerboard[i][j] + " ",end=' ')
        print()
    print("--------------------------------\033[0m")

    if (flagNum == 1):
        print('\033[32m*棋胜利！***\033[0m')
    else:
        print('\033[32mo棋胜利！***\033[0m')


while not finish:

    # 打印棋盘
    print("\033[1;30;46m--------------------------------")
    print("   1  2  3  4  5  6  7  8  9  10")
    for i in range(len(checkerboard)):
        print(chr(i+ord('A'))+ " ", end=' ')
        for j in range(len(checkerboard[i])):
            print(checkerboard[i][j] + " ",end=' ')
        print()
    print("--------------------------------\033[0m")
    #判断下棋者
    if flagNum == 1:
        flagch = '*'
        print('\033[1;37;40m请*输入棋子坐标（例如A1）：\033[0m', end=' ') # 白字黑底
    else:
        flagch = 'o'
        print('\033[1;37;40m请o输入棋子坐标（例如J5）：\033[0m', end=' ') # 白字黑底
    #输入棋子坐标
    str = input()
    ch = str[0].upper()
    x = ord(ch)-65
    y = int(str[1:])-1

    if(x<0 or x>9 or y<0 or y>9):
        print('\033[31m***您输入的坐标有误请重新输入！***\033[0m')
        continue
    if (checkerboard[x][y] == '-'):
        if (flagNum == 1):
            checkerboard[x][y] = '*'
        else:
            checkerboard[x][y] = 'o'
    else:
        print('\033[31m******您输入位置已经有其他棋子，请重新输入！\033[0m')
        continue

    #判断棋子方向
    """ if (y-4 >= 0):
        if (checkerboard[x][y-1] == flagch
            and checkerboard[x][y-2] == flagch
            and checkerboard[x][y-3] == flagch
            and checkerboard[x][y-4] == flagch):
            finish = True
            msg()
    if (y + 4 <= 9):
            if (checkerboard[x][y + 1] == flagch
                    and checkerboard[x][y + 2] == flagch
                    and checkerboard[x][y + 3] == flagch
                    and checkerboard[x][y + 4] == flagch):
                finish = True
                msg()

    # 判断棋子上方
    if (x - 4 >= 0):
        if (checkerboard[x - 1][y] == flagch
                and checkerboard[x - 2][y] == flagch
                and checkerboard[x - 3][y] == flagch
                and checkerboard[x - 4][y] == flagch):
            finish = True
            msg()

    # 判断棋子下方
    if (x + 4 <= 9):
        if (checkerboard[x + 1][y] == flagch
                and checkerboard[x + 2][y] == flagch
                and checkerboard[x + 3][y] == flagch
                and checkerboard[x + 4][y] == flagch):
            finish = True
            msg()

    # 判断棋子右上方向
    if (x - 4 >= 0 and y - 4 >= 0):
        if (checkerboard[x - 1][y - 1] == flagch
                and checkerboard[x - 2][y - 2] == flagch
                and checkerboard[x - 3][y - 3] == flagch
                and checkerboard[x - 4][y - 4] == flagch):
            finish = True
            msg()

    # 判断棋子右下方向
    if (x + 4 <= 9 and y - 4 >= 0):
        if (checkerboard[x + 1][y - 1] == flagch
                and checkerboard[x + 2][y - 2] == flagch
                and checkerboard[x + 3][y - 3] == flagch
                and checkerboard[x + 4][y - 4] == flagch):
            finish = True
            msg()

    # 判断棋子左上方向
    if (x - 4 >= 0 and y + 4 <= 9):
        if (checkerboard[x - 1][y + 1] == flagch
                and checkerboard[x - 2][y + 2] == flagch
                and checkerboard[x - 3][y + 3] == flagch
                and checkerboard[x - 4][y + 4] == flagch):
            finish = True
            msg()

    # 判断棋子左下方向
    if (x + 4 <= 9 and y + 4 <= 9):
        if (checkerboard[x + 1][y + 1] == flagch
                and checkerboard[x + 2][y + 2] == flagch
                and checkerboard[x + 3][y + 3] == flagch
                and checkerboard[x + 4][y + 4] == flagch):
            finish = True
            msg() """
    for x in range(len(checkerboard)):
        for y in range(len(checkerboard[x])):
            if checkerboard[x][y] != '-':
                if y<=5:
                    if checkerboard[x][y]==checkerboard[x][y+1]==checkerboard[x][y+2]==checkerboard[x][y+3]==checkerboard[x][y+4]:
                        finish = True
                        msg()
                if x<=5:
                    if checkerboard[x][y]==checkerboard[x+1][y]==checkerboard[x+2][y]==checkerboard[x+3][y]==checkerboard[x+4][y]:
                        finish = True
                        msg()
                if x<=5 and y<=5:
                    if checkerboard[x][y]==checkerboard[x+1][y+1]==checkerboard[x+2][y+2]==checkerboard[x+3][y+3]==checkerboard[x+4][y+4]:
                        finish = True
                        msg()
                if x>=4 and y<=5:
                    if checkerboard[x][y]==checkerboard[x-1][y+1]==checkerboard[x-2][y+2]==checkerboard[x-3][y+3]==checkerboard[x-4][y+4]:
                        finish = True
                        msg()
    flagNum *= -1

    #阿里山地