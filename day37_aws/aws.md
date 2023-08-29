# AWS
- 목차
    - [AWS란?](#aws란)
    - [AWS 대표 서비스](#aws-대표-서비스)
    - [IAM MFA 등록하기](#iam-mfa-등록하기)
    - [컨테이너](#컨테이너)
    - [아키텍처란?](#아키텍처란)
    - [유튜브 클론 코딩 시스템 아키텍처](#유튜브-클론-코딩-시스템-아키텍처-다이아그램오버뷰버드아이뷰)
    - [무중단 배포 기법](#무중단-배포-기법)
        - [블루그린 배포](#블루그린-배포)
        - [Rolling 배포](#rolling-베포)
    - [자동 배포](#자동-배포)
    - [Scale up vs Scale out](#scale-up-vs-scale-out)

<br>

## AWS란?
- Amazon Web Service
- 클라우드 컴퓨팅을 제공하는 아마존의 서비스
- 간단할수록 비쌈
- 물리적인 서버를 구입하고 관리하는 노력과 비용을 절감할 수 있음
- 장점
    - 컴퓨터, 스토리지, DB, 분석 등 다양한 서비스 제공
    - 탄력적인 확장성 (그래서 스타트업이 많이 씀)
    - 안정성과 신뢰성
    - 물리적, 네트워크, 암호화, 접근제어 등 다양한 보안 수준 제공
    - 비용을 효율적으로 관리할 수 있음
    - 글로벌 인프라 구축가능
    - 다양한 운영체제, DB, 언어, 플랫폼과의 통합 지원

<br>

## AWS 대표 서비스
- EC2: Elastic Compute Cloud. 가상 컴퓨터
- S3: 파일 시스템
- Lambda: Serverless (파이썬 코드만 있으면 돌아가도록 해주는 것)
- Cloud Front: CDN
- RDS: 관계형 데이터베이스
- Route53: DNS 서버
- IAM: 인증, 보안

<br>

## IAM MFA 등록하기
![](https://velog.velcdn.com/images/superkingyj/post/aac0c1a2-62ff-41f3-a84e-27a0bb24dd40/image.png)
- IAM 서비스 들어가기

![](https://velog.velcdn.com/images/superkingyj/post/a813de0b-5a89-4848-98b2-4e5b48150bf6/image.png)
- MFA 기기 등록

<br>

## 컨테이너
- 소프트웨어 프로그램들을 패키징 하는 기술
- 패키징한 이미지를 복사하여 다른 환경에 배포할 수 있음
- ex. Docker, Kubernetes

<br>

## 아키텍처란?
- 시스템이나 소프트웨어의 구조, 구성요소, 상호 작용 방식, 설계 원칙을 정의하는 것
- 시스템이나 소프트웨어 개발시 구조를 명확하게 볼 수 있음

<br>

## 유튜브 클론 코딩 시스템 아키텍처 다이아그램(오버뷰,버드아이뷰)
![](https://velog.velcdn.com/images/superkingyj/post/3799ba11-5c7b-4d38-897c-f56cafd3f2d8/image.jpg)

<br>

## 무중단 배포 기법

### 블루/그린 배포
![](https://velog.velcdn.com/images/superkingyj/post/9dca4f5b-0a73-4b32-ab0f-0750bf96a36e/image.png)
- 블루: 구버전
- 그린: 신버전
- 운영중인 구버전과 동일하게 신버전의 인스턴스를 구성한 후 로드밸런서를 통해 모든 트래픽을 한번에 신버전 쪽으로 전환
- 장점
    - 구버전의 인스턴스가 그대로 남아있어서 손쉬운 롤백이 가능
    - 구버전의 환경을 다음 배포에 재사용할 수 있음
    - 운영환경에 영향을 주지 않고 새 버전 테스트 가능
- 단점
    - 시스템 자원이 두배로 필요
    - 새로운 환경에 대한 테스트가 전제되어야 함

<br>

### Rolling 베포
![](https://velog.velcdn.com/images/superkingyj/post/e38bd6cf-3fa4-4457-b60a-a9ce6f64f76c/image.png)
- 롤링 배포는 사용 중인 인스턴스 내에서 새 버전을 점진적으로 교체하는 것
- 무중단 배포의 가장 기본적인 방식이다
- 서비스 중인 인스턴스 하나를 로드밸런서에서 라우팅하지 않도록 한 뒤, 새 버전을 적용하여 다시 라우팅
- 장점
    - 인스턴스마다 차례로 배포를 진행하기에 상황에 따라 손쉽게 롤백이 가능
    - 추가적인 인스턴스를 늘리지 않아도 됨
- 단점
    - 새 버전을 배포할때 인스턴스의 수가 감소하기 때문에 사용중인 인스턴스에 트래픽이 몰릴 수 있음
    - 배포가 진행될때 구버전과 신버전이 공존하기에 **호환성 문제가 발생할 수 있음**
    - 사용자들은 균일한 서비스를 받지 못함

<br>


## 자동 배포 
- AWS codeploy와 Git Action을 통해 자동 배포를 할 수 있음

<br>

## Scale up vs Scale out
- Scale up(수직적 확장) <-> Scale down 
    - 하나의 더 성능이 좋은 서버로 확장
    - 기존 설계 변경 없이 확장 가능
    - **변경을 위해선 Downtime(점검시간) 필요**
    - **Single Point of Failure** 발생 가능
- Scale out(수평적 확장) <-> Scale in
    - 비슷한 성능의 여러 개 서버로 확장
    - Downtime 필요없음
    - **확장 가능한 설계**가 필요
