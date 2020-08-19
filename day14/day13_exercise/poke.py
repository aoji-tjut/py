#   2. 模拟斗地主游戏发牌,牌共54张
#      黑桃('\u2660'), 梅花('\u2663'), 红桃('\u2666')
#      方块('\u2665')
#      大小王
#      数字: A2~10JQK
#      三个人,每人发17张牌,底牌留三张
#      输入回车,打印第一个人的17张牌
#      输入回车,打印第二个人的17张牌
#      输入回车,打印第三个人的17张牌
#      输入回车,打印3张底牌

# 花色
kinds = ['\u2660', '\u2663', '\u2666', '\u2665']
numbers = ['A']  # 2~10JQK
numbers += [str(x) for x in range(2, 11)]
numbers += list("JQK")
poke = ['大王', '小王']  # 用来保存扑克的文字
for x in kinds:
    for y in numbers:
        poke.append(x + y)

poke2 = poke.copy() # 复制一份
import random
# 洗牌
random.shuffle(poke2)
# print(poke2)

# 发牌
player1 = poke2[:17]
player2 = poke2[17:34]
player3 = poke2[34:51]
last = poke2[51:]
# 输入回车,打印第一个人的17张牌
input()
print(player1)
# 输入回车,打印第二个人的17张牌
input()
print(player2)
# 输入回车,打印第三个人的17张牌
input()
print(player3)
# 输入回车,打印3张底牌
input()
print(last)



