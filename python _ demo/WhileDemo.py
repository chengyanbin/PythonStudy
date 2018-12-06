
#!/usr/bin/python3

# while用法

number  = 7
guess = -1
while guess != number:
    guess = int(input("请输入你猜的数字"))
    if guess == number:
        print("恭喜猜对了")
    elif guess < number:
        print("猜小了")
    else:
        print("猜大了")
