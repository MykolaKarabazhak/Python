def chek_board(board):
    """Check board winner"""
    """Я решил реализовать 2 функции для 
    поверки доски чтобы не перегружать фунциии
    жаль но не нашлось болле элегантного решения """
    win_comb =  ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for win in win_comb:
        if board[win[0]] == board[win[1]] == board[win[2]] and board[win[1] != None]:
            winner ="Winner","X" if board[win[1]] == 1 else "0"
            print(winner,)
            break
    else:
        chek_underfind(board)

def chek_underfind(board):
    """Check board draw or UNDEFINED"""
    for i in board:
        if i == None:
            print("Underfiend")
            break
    else:
        print("Draw")



X, O, _ = 1, 0, None
board = (
    _, _, _,
    _, _, _,
    _, _, _
)
chek_board(board)




def Generate(n=str, m=int, list_tmp = None):
    """Generate combination of all permutations  """
    """Генерация всех перестанок но в 3 ряда """
    list_tmp = list_tmp or []
    if m == 0:
        print(list_tmp)
        for i in list_tmp:
            akkum.append(i)
        return akkum
    for i in n:
        list_tmp.append(i)
        Generate(n, m-1, list_tmp)
        list_tmp.pop()

akkum = []
n = "XO_"
m = 3
Generate(n,m )