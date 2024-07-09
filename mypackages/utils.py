#小さいほうに更新、aとbを比較してbのほうが小さかったら、aをbにする
def chmin(a,b):
    if a > b:
        a = b
        return True
    return None

#大きいほうに更新
def chmax(a,b):
    if a < b:
        a = b
        return True
    return None

#n進数に変換
def convertBase_n(a, n):
    for i in [i for i in range(9,-1,-1)]:
        wari = n**i
        print((a//wari)%n, end='')


