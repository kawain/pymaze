import random
import math
import ana
import bou


def find_dead_end(maze, i, j):
    """行き止まり地点を探す"""

    count = 0

    if maze[i-1][j] == 1:
        # 上
        count += 1
    if maze[i+1][j] == 1:
        # 下
        count += 1
    if maze[i][j-1] == 1:
        # 左
        count += 1
    if maze[i][j+1] == 1:
        # 右
        count += 1

    if count == 3:
        return True
    else:
        return False


def get_distance(t1, t2):
    """直交座標A(x,y)とB(x2,y2)の間の距離を求める関数"""

    x, y = t1
    x2, y2 = t2
    distance = math.sqrt((x2 - x) * (x2 - x) + (y2 - y) * (y2 - y))

    return distance


def longest_point(start, lst):
    """スタート地点から最長のゴール地点を探す"""

    arr = []

    for v in lst:
        distance = get_distance(start, v)
        arr.append([distance, v])

    arr.sort(reverse=True)

    return arr[0][1]


def main():
    # 迷路の大きさ 奇数
    SIZE = 31

    maze = ana.main(SIZE)
    # maze = bou.main(SIZE)

    # 行き止まり地点のリスト
    dead_end = []

    for i, _ in enumerate(maze):
        for j, _ in enumerate(maze[i]):
            if maze[i][j] == 0:
                if find_dead_end(maze, i, j):
                    dead_end.append((i, j))

    # ランダムにスタート地点を決める
    start = random.choice(dead_end)
    print("start", start)
    # 決まったスタート地点は削除
    dead_end.remove(start)

    # スタート地点から最長の行き止まり地点を探しそこをゴールにする
    goal = longest_point(start, dead_end)
    print("goal", goal)

    # 表示確認
    for i, _ in enumerate(maze):
        for j, _ in enumerate(maze[i]):
            if i == start[0] and j == start[1]:
                print("○", end="")
            elif i == goal[0] and j == goal[1]:
                print("◎", end="")
            elif maze[i][j] == 1:
                print("■", end="")
            else:
                print("□", end="")
        print()


if __name__ == "__main__":
    main()
