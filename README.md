# 파이썬 체스 엔진
python의 python-chess 모듈을 활용하여 만든 체스 엔진입니다. 2024년 12월 29일 기준 chess.com에서 Isabel(1600)과 Wally(1800) 봇을 이기는 것을 확인했습니다.

## 파일 구성
* bot.py: 엔진 코드입니다. base 함수는 포지션과 기물 점수를 고려한 점수를, val 함수는 base 결과와 minimax, alpha-beta pruning 알고리즘을 함께 적용한 점수를, move 함수는 val 결과를 바탕으로 한 엔진 추천 수를 반환합니다.

* pos.py: bot.py의 base 함수가 참조하는 위치에 따른 기물 점수 테이블(PST)입니다. score는 오프닝과 미들게임에서 쓰이는 PST, end는 엔드게임에서 쓰이는 PST입니다.

* game.py: 엔진과 게임을 할 수 있도록 하는 파일입니다.

## 사용 방법
1. python-chess 라이브러리를 다운로드합니다. pip을 이용할 경우 ```pip install chess``` 명령어를 명령 프롬프트에 입력합니다.
2. bot.py, pos.py, game.py를 모두 다운로드합니다.
3. game.py를 실행합니다.
4. 본인이 플레이할 색을 입력합니다. (백의 경우 W, 흑의 경우 B)
5. 본인의 차례가 되면 수를 (시작위치)(도착위치)의 형식으로 입력합니다. [예시: e2e4] 캐슬링은 킹을 두 칸 움직이는 것으로, 프로모션은 원래 표기 뒤에 승진 기물을 소문자로 표기하는 것으로 합니다. [예시: e1g1 = 0-0, d7e8q = dxe8Q]
6. 엔진이 수를 둘 때까지 기다립니다. 수의 표기 방식은 앞서 언급한 것과 같습니다.
