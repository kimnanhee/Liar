import os, random, time

words = [] # 단어 리스트

try:
    with open("word.txt", "r", encoding="utf-8") as f: # 텍스트 파일 열기
        while True:
            line = f.readline() # 한 줄씩 읽어오기
            if not line:
                break
            words.append(line.split()[0]) # 공백 기준으로 단어 자르기
except Exception:
    print("단어 파일을 여는데 문제가 발생했습니다.")
    print("파일이 올바른 위치에 있는지 확인해주세요.")
    exit(-1)

while True:
    os.system("cls") # 화면 지우기
    print("라이어 게임에 오신 것을 환영합니다.") 
    print("게임에 참가하시는 겜블러들의 수를 입력해주세요.")
    gambler = int(input()) # 겜블러의 수

    liar = random.randint(1, gambler) # 라이버의 번호
    word = random.randint(0, len(words)-1) # 문제의 번호

    for i in range(1, gambler+1):
        os.system("cls") # 화면 지우기
        print("{}번 겜블러의 제시어입니다.".format(i))
        input()

        print(word, len(words))
        print("당신은 라이어입니다." if i==liar else words[word])
        time.sleep(2) # 2초

    os.system("cls") # 화면 지우기
    print("제시어를 확인하신 겜블러들은 순서대로 제시어에 대해서 설명해주세요.")
    print("순서대로 설명을 다 하셨을 경우, 엔터를 입력해주세요.")
    input() # 입력 기다리기

    arr = [0 for _ in range(gambler)] # 겜블러의 라이어 투표 결과
    for i in range(1, gambler+1):
        os.system("cls") # 화면 지우기
        print("{}번 겜블러님, 라이어로 의심되는 겜블러의 번호를 입력해주세요.".format(i))
        arr[int(input())-1] += 1
        time.sleep(1) # 1초

    os.system("cls") # 화면 지우기
    print(arr)

    if arr.index(max(arr))+1 == liar: # 라이어 찾기 성공
        print("라이어를 찾아내는데에 성공했습니다.")
        print("라이어는 제시어라고 생각되는 단어를 입력해주세요.")
        print("만약 라이어가 제시어를 맞출 경우, 라이어의 승리입니다.")
        answer = input() # 제시어 입력

        if answer==words[word]:
            print("라이어가 제시어를 맞추었으므로, 라이어의 승리입니다.")

    else: #라이어 찾기 실패
        print("라이어를 찾아내는데에 실패했습니다.")
        print("라이어인 겜블러는 {}번 입니다.".format(liar))

    print("\n라이어 게임을 한 번 더 하시겠습니까? (Y/N)")
    answer = input()
    if answer not in ["y", "Y", "yes", "Yes"]:
        break