---
title: 'Spring(1)'
date: 2021-05-15
category: 'Spring'
draft: false
---

## 스프링부트 2.0

- Java 8 이상의 버전만 지원
- Spring Framework 5.X
- HTTP/2 지원
- Gradle 4.X 이상버전 사용해야함
- 코틀린 지원
- 커넥션 풀 변경 톰캣 -> HikariCP (매우 뛰어난 성능과 속도를 제공한다고 함.)

## 스프링부트의 특징
- 애플리케이션 신속하게 세팅 가능.
- 추가 WAS설치 없이 embeded tomcat으로 실행.
- 번거로운 개발 세팅을 대신해줌.

## Spring IOC
- 제어의 역전.
- 객체의 생성부터 Life Cycle을 관리하고 제어 해주는것을 의미함.
- 제어권이 스프링 프레임워크로 넘어오게 되면서 DI(의존성 주입), AOP(관점 지향 프로그래밍) 등을 가능하게 함.
- 싱글톤 레지스트리
  - 스프링은 IoC컨테이너일 뿐 아니라, 고전적인 싱글톤 패턴을 대신해 싱글톤을 만들고 관리해주는 싱글톤 레지스트리이다.

## Spring Container
- 객체의 Life Cycle을 관리함
- ApplicationContext, BeanFactory

## DI(의존성 주입)
- 각 클래스간의 의존관계를 빈 설정 정보를 바탕으로 외부 컨테이너에서 주입하는 개념.
- 의존관계
    - A -> B : A가 B에 의존한다.
    - 의존대상(B)이 변하면 그 영향이 의존하는 대상(A)으로 전달되는 것.
    - B가 변경이 됨으로 인해 A가 변경되어야 하는 상황이 발생.
  
