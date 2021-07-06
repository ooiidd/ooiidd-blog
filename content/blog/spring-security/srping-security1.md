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
- 인증(Autenticate) : 누구인가?
- 인가(Authorize) : 이 접근주체가 접근 가능한가?

### Architecture
![Spring Security Architecture](./img/Spring-Security.png)


###인증(Autheticate)에 관여하는 클래스 및 인터페이스
- AuthenticationManager (인터페이스)
- ProviderManager (클래스)
- AuthenticationProvider (인터페이스) -> 로그인 로직 구현체 AbstractUserDetailsAuthenticationProvider
- UserDetailsService (인터페이스) -> 보통 이 인터페이스를 구현하여 사용자를 DB에서 조회하여 사용

위의 방법으로 로드한 User의 정보는 Thread Local에 등록되어 같은 Thread내에서 사용 가능하다.
- Thread Local에서 authetication 객체 꺼내기
```java
    Authentication authetication = SecurityContextHolder.getContext().getAuthentication();
```

###FilterChainProxy
1. WebAsyncManagerIntergrationFilter
2. SecurityContextPersistenceFilter
3. HeaderWriterFilter
4. CsrfFilter
5. LogoutFilter
6. UsernamePasswordAuthenticationFilter
7. DefaultLoginPageGeneratingFilter
8. DefaultLogoutPageGeneratingFilter
9. BasicAuthenticationFilter
10. RequestCacheAwareFilter
11. SecurityContextHolderAwareRequestFilter
12. AnonymouseAuthenticationFilter
13. SessionManagementFilter
14. ExeptionTranslationFilter
15. FilterSecurityInterceptor