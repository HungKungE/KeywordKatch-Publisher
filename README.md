# KeywordKatch - 키워드 기반 기사 추천 웹 서비스

## 프로젝트 소개 
광운대학교 산학협력캡스톤설계1 과목에서
"MSA를 적용한 웹 서비스 개발과 AWS를 사용한 배포"라는 주제를 가지고
진행했던 웹 프로젝트입니다.
</br>
</br>
진행 기간 : 2023.03 ~ 2023.06

---

## MicroServices Architecture
웹서비스를 기능 단위의 component로 나누어 관리하는 아키텍쳐 스타일입니다.
특징은 각 컴포넌트들이 독립적이고 느슨하게 결합되어 있다는 점입니다.
</br>
이 때문에 다음과 같은 장점이 있습니다.
- 독립적으로 배포가 가능 ( 각 서비스마다 다른 개발언어로 개발 가능 )
- 한 컴포넌트에 문제 발생 시, 다른 컴포넌트에 영향을 끼치지 않음
- 유지보수가 편함

---

## 프로젝트 핵심 내용
"MSA를 적용한 웹 서비스 개발과 AWS를 사용한 배포"라는 주제로 프로젝트를 진행하기위해
선택한 서비스는 사용자의 관심사에 맞는 기사를 이메일로 제공하는 웹 서비스 KeywordKatch 입니다.
KeywordKatch는 다음과 같은 3개의 컴포넌트로 구성됩니다.

![1111111](https://github.com/HungKungE/KeywordKatch-Publisher/assets/84065412/bd3260bf-32fc-4976-b20b-1afad2929707)

---

## 개발한 내용 (Publisher Component)
저는 Publisher Component를 개발했습니다. 기능은 다음과 같습니다.
<br/>
<details>
<summary><b>RDS 연결 및 DB data열람</b></summary>
<div markdown="1">
### 사용 기술
 <div>
  <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/aws_RDS-E34F26?style=for-the-badge&logo=amazon&logoColor=white">
  <img src="https://img.shields.io/badge/aws_EC2-000000?style=for-the-badge&logo=amazon&logoColor=white">
 </div>
 </br>

### 설명
  - RDS 연결 : User Component, Editor Component의 RDS에 연결합니다.
  - DB 열람 : User DB, Editor DB에서 필요한 정보들을 가져옵니다.
 
 ![12121212121](https://github.com/HungKungE/KeywordKatch-Publisher/assets/84065412/2e993d47-18f4-4e7b-ae14-8323aa08c096)
</div>
</details>

<details>
<summary><b>이메일 폼 생성</b></summary>
<div markdown="1">

  ### 사용 기술
 <div>
  <img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white">
  <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">
 </div>
 </br>

  ### 설명
  - 이메일 폼(html) : 사용자에게 전송할 기사 정보의 템플릿.
  - 동적 이메일 폼 생성 : 사용자 별 전송할 기사 종류, 개수에 따라 동적으로 이메일 폼 생성.
 
 ![q](https://github.com/HungKungE/KeywordKatch-Publisher/assets/84065412/367a4f0f-4fb3-4188-9dc1-07c33cc620d6)
</div>
</details>

<details>
<summary><b>이메일 전송</b></summary>
<div markdown="1">

 ### 사용 기술
 <div>
  <img src="https://img.shields.io/badge/SMTP-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/multiprocessing-000000?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/schedulers-092E20?style=for-the-badge&logo=python&logoColor=white">
 </div>
 </br>
 
 ### 설명
 - 이메일 전송(SMTP) : 생성된 이메일 폼을 사용자들에게 전송함.
 - 동시 전송(multiprocessing) : 모든 사용자에 대해 동시에 이메일 폼 생성 -> 이메일 전송 과정을 진행함.
 - 사용자 별 전송 시간(scheduler) : 사용자마다 설정한 전송 시간에 따라서 전송합니다.

 ![캡처](https://github.com/HungKungE/KeywordKatch-Publisher/assets/84065412/48dce222-02e1-45d9-a9ad-b60f64b37277)

</div>
</details>

---

 ## 프로젝트 자료
 - [시연영상](https://youtu.be/VxoKp9eqN8I)
 - [페이지 디자인](https://www.figma.com/file/KSb9N8KkD4jluDenMq4H9b/%EB%89%B4%EC%8A%A4%EA%B8%B0%EC%82%AC-%EC%9D%B4%EB%A9%94%EC%9D%BC-%EC%84%9C%EB%B9%84%EC%8A%A4-UI?type=design&node-id=0-1&mode=design)
