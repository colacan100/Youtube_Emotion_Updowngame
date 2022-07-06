# Youtube_Emotion_Updowngame

### 1. Project background
- 기존에 존재하던 구글 검색량 UpDown 게임을 이용한 게임입니다.
- 일반적으로 Computer Vision을 이용한 컨텐츠들은 많이 알려져있지만 ( AI 사진 합성 사이트, 자동채색 사이트 등) NLP를 이용한 컨텐츠는 보기 힘듭니다.
- 구글 검색량 UpDown 게임도 단순히 검색량만을 이용하기에 컨텐츠가 부족합니다.
- 위를 이용하여 컨텐츠가 부족한 UpDown 게임에 새로운 방식의 추가적인 요소를 넣었습니다.

### 2. Project Contents
- 감성 분석 : 저희 컨텐츠의 핵심입니다. NLP로 할 수 있는 키워드 추출등과 같은 컨텐츠 중에서 가장 사용자의 흥미를 이끌어 낼 수 있을 것이라고 생각했습니다. 또한 특정 영화에 관한 대중의 정보를 얻을 수 있다는 점에서도 큰 이점이 작용합니다.
- 7가지의 감정 : NLP에는 긍정, 부정을 구분하는 방법도 있지만 심화적으로 나아가 7가지 감정을 구분하는 모델도 구현할 수 있습니다. 기쁨, 슬픔, 놀람, 분노, 공포, 혐오, 중립의 감정 레이블링을 통해서 사용자들은 더 다양한 감정에 대해서 게임을 진행할 수 있습니다.
- 영화 선택 : 사용자들이 관심을 가질만한 최근 영화를 통해서 감정분석을 진행하고자 하였으나 코로나19, 전체적인 영화 흥행의 부재로 인해서 댓글의 수가 적습니다. 따라서 차선책으로 역대 흥행 영화의 리스트를 뽑아 상위 50개의 영화에 대한 Youtube 댓글 감정분석을 진행했습니다. 또한 모든 댓글을 수집하기에는 주어진 시간이 한정적이기에 영화마다 1000개의 댓글을 수집하여 총 50000개의 데이터를 이용했습니다.

### 3. Project Structure
- Youtube API 크롤링 $\rightarrow$ 
MongoDB 데이터적재 $\rightarrow$ 
CNN 혹은 KoBERT 로 감정분류 모델 생성 $\rightarrow$
Flask 로 웹 애플리케이션 구현 $\rightarrow$
AWS EC2 를 통하여 배포
- Youtube API 크롤링 $\rightarrow$
MySQL 데이터적재 $\rightarrow$
데이터 시각화

### 4. Project Stacks
- Youtube API, AWS EC2, MongoDB, MySQL, Flask, Pytorch (KoBERT, CNN)

### 5. Project Effect
- 게임이라는 방식을 통해서 NLP 에 관한 대중의 인식 및 홍보효과를 일으킬 수 있습니다. UI와 데이터의 양을 늘려
- 요소를 늘려 서비스를 배포하면서 광고 수익등을 얻을 수 있습니다.
