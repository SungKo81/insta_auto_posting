from netflix_utils.netflix_insta import *
from new_movie_utils.new_movie_insta import *
from boxoffice_utils.boxoffice_insta import * 
from etc_utils.upload_posting import *


caption = ''

# 생성 원하는 게시물 입력
posting_type = input('''
                    원하는 게시물 타입을 선택하세요.
                    2. 넷플릭스 영화/시리즈
                    3. 박스오피스 주간 순위
                    4. 새영화 뉴스 요약 
                    q. 취소
                    ''')
while True:
    if posting_type == '2':
        caption = make_netflix_posting()
        break

    elif posting_type == '3':
        caption = make_boxoffice_posting()
        break

    elif posting_type == '4':
        caption = make_new_news_posting()
        break
    
    elif posting_type == 'q':
        print('종료되었습니다.')
        break

    else:
        print('1~4번 사이에서 선택해 주세요.')
        posting_type = input('''
                    원하는 게시물 타입을 선택하세요.
                    2. 넷플릭스 영화/시리즈
                    3. 박스오피스 주간 순위
                    4. 새영화 뉴스 요약 
                    q. 취소
                    ''')

print(caption)

upload = input('게시물을 업로드 할지 선택하세요. (Y/N)')

if upload.lower() == 'y':
    upload_images(caption)

