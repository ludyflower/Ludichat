import sqlite3
def chat(msg):
    chat_message = str(msg)
    answer = "제가 아직 모르는 말입니다."
    conn = sqlite3.connect('chat.db')
    conn = cur = conn.cursor()
    cur.execute("select * from chat")
    rows = cur.fetchall()
    for row in rows:
        if row[0] == chat_message:
            answer = row[1]
    return(answer)
def teach(q,a):
    search = chat(q)
    if search != "제가 아직 모르는 말입니다.":
        return("이미 학습된 말입니다.")
    #20180905 만들다 말음

if __name__ == '__main__':
    mode = 2
    inputstr = input("관리자 모드입니다. - 번호를 입력하세요. \n1. 데이터베이스 추가\n2. 채팅 테스트")
    if inputstr == 1: mode = 1
    if inputstr == 2: mode = 2
    if not inputstr == 1 or inputstr == 2:
        print("잘못된 명령입니다.")
        exit()
    if mode == 1:
        while(True):
            in_str = input("채팅 모드입니다. - 채팅을 입력해보세요. - 나가기 \q")
            if in_str == "\q":
                print("종료합니다.")
            else:
                chat(in_str)
