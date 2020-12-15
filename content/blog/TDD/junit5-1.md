---
title: 'JUnit5-1'
date: 2020-12-15
category: 'TDD'
draft: true
---

#JUnit5 - 기본(1)

##1. Annotation
- @BeforeAll 
   - 현재 클래스의 모든 테스트 메서드보다 먼저 실행.
   - static 이어야함.
- @BeforeEach
   - 각 테스트 메서드 전에 실행.
- @AfterAll
   - 현재 클래스의 모든 테스트 메서드보다 먼저 실행.
   - static 이어야함.
- @AfterEach
   - 각 테스트 메서드 후에 실행.
- DisplayName
   - 테스트 메서드의 이름 정의
- Disabled
   - 테스트 메서드 or 클래스 비활성화

##2.Assertion
- assertTrue
- assertThat
- assertAll
