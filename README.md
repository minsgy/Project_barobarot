# 📆Project_barobarot
## 🥈 2020. 11. 03. - 롯데 해커톤 **은상** 수상작  

🏆 LIKELION&amp;LOTTE 8th - Hackathon Project
![image](https://user-images.githubusercontent.com/60251579/98437952-e425f280-2129-11eb-83ba-ef88e1f12511.png)

## 🖥 DEMO

<img src="https://github.com/minsgy/Project_barobarot/blob/master/BaroBarot_DEMO/Main.gif" width="600px" />
<img src="https://github.com/minsgy/Project_barobarot/blob/master/BaroBarot_DEMO/Login.gif" width="600px" />
<img src="https://github.com/minsgy/Project_barobarot/blob/master/BaroBarot_DEMO/Detail.gif" width="600px" />
<img src="https://github.com/minsgy/Project_barobarot/blob/master/BaroBarot_DEMO/Engineer.gif" width="600px" />


## ⚡️ 서비스 소개
- 🌈 바로바롯 서비스란?
- 롯데 하이마트몰의 기존 배송 서비스를 개선하여 구성한 아이디어.
- 설치와 배송 서비스를 스케줄과 시간을 선택 후, 스케줄이 되는 설치/배송기사를 직접 리뷰를 보고 선택하는 언택트 서비스


## 👨‍👨‍👨‍👧‍👧Team member

- [최민석](https://github.com/minsgy) : Full-stack(Minseok), Readme write
- [이승준](https://github.com/g0709-19) : Front-end(LeeJun)
- [장하얀](https://github.com/white-jang) : Front-end(White)
- [박형민](https://github.com/thalals/) : Back-end(Hmin)
- [하유민](https://github.com/qhahd78) : Front-end(Umin)

## 📑 Project Specification

- [한달음 - Google Docs](https://docs.google.com/document/d/1US57lggIKGL0CG4JkgxOzRyGLcLDPqiVBlbb1MafzIs/edit?usp=sharing)
- [한달음 - Page Configuration](https://jamboard.google.com/d/1oTOr-Hq79dz_WfDCB2bpPPcNucm-LPVugLqNfSbqENk/edit?usp=sharing)
- [한달음 - Front 일정](https://jamboard.google.com/d/1Lw_6KPWb2pZOgRV8OHlK6zgUdp-2ejF4nUS2aaxNWSU/edit?usp=sharing)

## 프로젝트 실행 법

1. 가상 환경 생성 및 실행

- `python -m venv <가상환경 이름>`
- Windows `. <가상환경 이름>/scripts/activate`
- Mac `. <가상환경 이름>/bin/activate`

2. Django, Pillow, django-mathfilters 설치

- `pip install django==2.1.1`
- `pip install pillow`
- `pip install django-mathfilters`

3. 모델 등록하기

- `python manage.py makemigrations`
- `python manage.py migrate`

4. Superuser 생성하기

- `python manage.py createsuperuser`

5. Database File Create

- URL `/products_test` 붙혀서 입력. 엔지니어 모델 11개, 상품 모델 40개 DB CREATE

## Installation

- Python3 == 3.8.4
- Django==2.1.1
- HTML5
- CSS3
- JS
- JQuery

## Git Rule

- ✔ Dev : 기능 및 모듈 개발을 위한 branch
- ✔ Release : 완성 본 디버깅 과정 branch
- ✔ Master : 최종 본 branch

1. 각자 로컬에서 이름으로 된 branch 생성하기 - Minsgy, Hmin, White, Umin, Leejun
2. 각자 로컬에서 Pull Request 보낸 Commit을 **Dev Branch**에서 merge.
3. 어느 정도 개발 진행 후, 전체적인 Prototype 을 실행하는 branch.
4. **Release branch** 에서 디버깅 하여, 최종 결과물을 **Master branch**로 merge.

## Commit Rule

- 네이밍은 다음과 같이 작성함.

  - Front-end

    - templates
      - Page 참조 받는 파일 명은 "\_\_"(underbar)를 추가해 파일 명 작성
      - 예) \_\_main.html
      - VS Code - settings - format on save 켜서 코드 정리 자동화
      - 페이지 최상단에 주석으로 페이지 간략 설명, 작성일 표기
      - 백엔드가 봤을 때 필요한 기능들을 단 번에 알 수 있도록 하기
      - 참고 - [NHN 코딩 컨벤션](https://nuli.navercorp.com/data/convention/NHN_Coding_Conventions_for_Markup_Languages.pdf)
      - 한 문서에서 동일한 ID 2번 이상 사용하지 않음.
      - CSS 작성시 base.html 의 스타일을 확인한 뒤 중복된 선택자 없이 작성
      - ![image](https://user-images.githubusercontent.com/60251579/94369869-3d603680-0127-11eb-82e9-34f855569439.png)

  - Back-END

    - Model Class

      - 모델 클래스의 첫 글자는 대문자로 한다.

    - App Folder

      - APP 폴더 이름은 첫 글자는 소문자로 한다.
      - APP 폴더 이름은 기능이 복수 일 경우, 's'를 붙힌다.
      - 예) comments, users

    - View Function

      - 함수(메소드)에 낙타 표기법 적용
        - 예) getName() ...
      - 변수(필드)에 팟홀 표기법 적용
        - 예) MyFirstVariable -> my_first_variable

    - Templates

      - templates 폴더는 APP 폴더 별로 나누지 않고, 통합한다.
      - 각 해당 되는 APP 폴더 명으로 나누어, template를 저장한다.
      - ex) templates/order_list/order.html

    - Static
      - 각 App 폴더 static 폴더를 생성하여 저장한다.
      - `python manage.py collectstatic` 을 통해 모든 static 파일을 모은다.
      - css
        - css를 담는 폴더 명이며, css 명은 html과 동일 시 한다.
      - js
        - js를 담는 폴더 명이며, js 명은 html과 동일 시 한다.
