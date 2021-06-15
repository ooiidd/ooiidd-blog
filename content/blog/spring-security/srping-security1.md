---
title: 'Spring Security(1)'
date: 2021-06-15
category: 'spring security'
draft: true
---

## Spring Security
스프링 시큐리티는 이름 그대로 보안을 담당하는 프레임워크이다.
스프링 시큐리티는 Filter 기반으로 동작하고 스프링 프레임워크에서 지원하는
Filter의 개수는 총 15개 이다. 이 Filter들을 옵션을 통해 사용하거나 사용하지 않거나 설정이 가능하다.
그리고 Filter를 오버라이딩하거나, 추가하는것 또한 가능하다.

### 용어
- 주체(Principal) : 접근하는 유저
- 인증(Autenticatie) : 누구인가?
- 인가(Authorize) : 이 접근주체가 접근 가능한가?

### Architecture
![Spring Security Architecture](./img/Spring-Security.png)