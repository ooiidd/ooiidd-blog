---
title: 'JUnit5-1'
date: 2020-12-15
category: 'TDD'
draft: true
---

#Spring + JUnit5(1)

##1. JUnit Annotation
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
- assertEquals
- assertAll
  - assertion을 그룹화 하여 실행.
  - 실패의 경우가 있더라도 그룹에 있는 assertion 구문 모두 실행
  ```java
  class Assertion{
    @Test
    void assertAllTest(){
      assertAll("person",
        () -> assertEquals(1,1),
        () -> assertEquals(2,2)
      );
    }
  }
  ```

##3.SpringJUnit Annotation
- @SpringJUnitConfig
  - @ExtendWith 어노테이션과 @ContextConfiguration 어노테이션을 합친 어노테이션이다.
- @SpringJUnitWebConfig
  - 위의 @SpringJUnitConfig 어노테이션에서 @WebAppConfiguration이 추가된 어노테이션이다.
