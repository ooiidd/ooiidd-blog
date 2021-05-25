---
title: 'Spring Boot(1)'
date: 2021-05-24
category: 'spring boot'
draft: true
---

## 스프링부트 2.5.0 System Requirement
- Java 8 ~ 16
- Spring Framework 5.3.7 이상
- Maven 3.5 이상
- Gradle 6.8.x, 6.9.x, 7.x

## 스프링부트의 내장 Servlet Containers
- Tomcat9.0
- Jetty 9.4
- Jetty 10.0
- Undertow 2.0

## Runner
- SpringApplication이 시작된 후 특정 코드를 실행해야하는 경우 사용
- ApplicationRunner 또는 CommandLineRunner 인터페이스를 구현하여 사용
- Applicaion.run(...)이 완료되기 직전에 한번 실행됨

ex)
```java
@Component
public class MyCommandLineRunner implements CommandLineRunner {
    @Override
    public void run(String... args) {
        // Do something...
    }
}
```
