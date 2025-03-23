### 인스타그램 자동 포스팅
- SKN 최종 프로젝트에서 담당한 파트
- 인스타그램에 올라갈 게시물을 자동으로 생성하고 업로드

준비사항
- 게시글 생성을 위한 openai api
- 인스타 업로드를 위한 instagram api key, instagram accoun id, filestack api key.

사용 모듈
- beautifulsoup
- dotenv
- filestack
- langchain
- pandas
- pillow
- requests
- selenium

진행순서
- main.py를 실행하면, 3가지 주제를 선택가능
- 넷플릭스 -> 지금많이보는, 주간순위, 신작으로 추가적인 선택을 하면 게시물 생성을 진행
- 박스오피스 -> 한주간 많은 관람객이 본 영화 10편을 정리하여 게시물로 선택
- 새영화뉴스 -> 연합뉴스의 새영화 뉴스를 요약하여 게시물 생성
- 게시물이 생성되면, 확인후 업로드 진행

결과
- 정해진 주제에 따라 게시물을 생성하고, 업로드까지 완료

추가 코멘트
- GPT4o-mini를 사용하여도 충분한 요약 및 한줄 리뷰가 생성됨을 확인. 비용이 감당된다면 GPT4o를 사용하면 더 좋을듯 함
- 인스타 자동 업로드를 위해 임시로 filestack을 사용하였으나, 비용을 감당할수 있다면 AWS를 활용하여도 될것으로 보임
