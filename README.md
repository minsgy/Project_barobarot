# Project_barobarot

🏆 LIKELION&amp;LOTTE 8th - Hackathon Project BaroBarot

## 👨‍👨‍👨‍👧‍👧Team member

- [최민석](https://github.com/minsgy) : Back-end, Minsgy
- [이승준](https://github.com/g0709-19) : Front-end, LeeJun
- [장하얀](https://github.com/white-jang) : Front-end, White
- [박형민](https://github.com/thalals/) : Back-end, Hmin
- [하유민](https://github.com/qhahd78) : Front-end, Umin

## Git Rule

- ✔ Dev : 기능 및 모듈 개발을 위한 branch
- ✔ Release : 완성 본 디버깅 과정 branch
- ✔ Master : 최종 본

1. 각자 로컬에서 이름으로 된 branch 생성하기 - Minsgy, Hmin, White, Umin, Leejun
2. 각자 로컬에서 Pull Request 보낸 Commit을 **Dev Branch**에서 merge.
3. 어느 정도 개발 진행 후, 전체적인 Prototype 을 실행하는 branch.
4. **Release branch** 에서 디버깅 하여, 최종 결과물을 **Master branch**로 merge.

## Commit Rule

- 네이밍은 다음과 같이 작성함.

  - Front-end

    - templates

        - Page 참조 받는 파일 명은 "\_\_"(underbar)를 추가해 파일 명 작성
        - 예) \_\_main.html,

  - Back-END

    - Model Class

      - 모델 클래스의 첫 글자는 대문자로 한다.

    - App Folder

      - APP 폴더 이름은 첫 글자는 대문자로 한다.
      - APP 폴더 이름은 기능이 복수 일 경우, 's'를 붙힌다.
      - 예) comments, Users

    - View Function

      - 함수(메소드)에 낙타 표기법 적용
        - 예) getName() ...
      - 변수(필드)에 팟홀 표기법 적용
        - 예) MyFirstVariable -> my_first_variable

    - Templates
      - templates 폴더는 APP 폴더 별로 나누지 않고, 통합
