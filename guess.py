import random

import random

print("欢迎来到猜数字游戏！")
secret_number = random.randint(1, 100)
count = 0 

while True:
    guess = input("请输入你猜的数字（1-100）：")
    
    # 防弹衣开始
    try:
        guess = int(guess)
    except ValueError:
        print("❌ 输入错误！黑客先生，请输入一个真正的整数！")
        continue 
    
    count = count + 1  
    
    # 你自己加的范围判断逻辑，非常棒
    if guess > secret_number and guess > 0 and guess < 101:
        print("太大了！")
    elif guess < secret_number and guess > 0 and guess < 101:
        print("太小了！")
    elif guess > 100 or guess < 1:
        print("数字不在规定范围内")
        continue
    else:
        print(f"恭喜你，猜对了！你一共猜了 {count} 次。")
        break 