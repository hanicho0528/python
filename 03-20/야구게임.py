#야구게임 만들기

import random
answer = []

while len(answer) < 3:
    n = random.randint(0,9)
    if n not in answer:
        answer.append(n)

print(f"answer = {answer}")

try_count = 10
while try_count:
    guess = input("숫자를 입력해주세요 (ex: 0 1 2):").split()
    ball = 0
    strike = 0
    for i in range(len(guess)):
        guess[i] = int(guess[i])
    if guess[i] in answer:
        print("정답입니다")
        exit()

    for i in range(len(guess)):
        guess[i] = int(guess[i])
        if guess[i] in answer:
            if guess[i]==answer[i]:
                strike += 1
            else:
                ball +=1
    if ball == 0 and strike == 0:
        print('foul')
    else:
        print(f"ball={ball}, strike = {strike}")




print("시도횟수를 모두 소진했습니다.")
print(f"정답은: {answer}")

exit()#이 함수가 실행되면 코드 종료

# 추측값을 입력받고 answer와 guess가 같으면 정답이라고 알려주고 게임 종료
# 그게 아닐시 strike가 몇개고 Ball이 몇개인지 출력
# Strike = guess의 값이 자리까지 같을 경우
# Ball = 자리는 다루나 해당 값이 존재할 경우
# 둘 다 해당 안될시 Foul 출력
