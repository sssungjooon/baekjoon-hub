def calculate_score(player1_hole, player1_board, player2_hole, player2_board):
    score1 = 3 * player1_hole + player1_board
    score2 = 3 * player2_hole + player2_board

    if score1 > score2:
        return 1, score1 - score2
    elif score2 > score1:
        return 2, score2 - score1
    else:
        return 0, 0

# 입력 받기
line1 = input().split()
line2 = input().split()

# 입력 값 변환
H1, B1 = map(int, line1)
H2, B2 = map(int, line2)

# 결과 계산
player, points = calculate_score(H1, B1, H2, B2)

# 결과 출력
if player == 0:
    print("NO SCORE")
else:
    print(f"{player} {points}")
