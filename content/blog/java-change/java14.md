---
title: 'Java15 변경점'
date: 2021-05-23 18:00
category: 'Java-Change'
draft: false
---

안녕하세요 홍성훈 입니다.

오늘은 자바 15버전 변경점을 정리해보려 합니다.

모든 변경점을 정리하지는 않았습니다.

모든 변경점을 확인하기위해서는 [여기](https://www.oracle.com/java/technologies/javase/15all-relnotes.html) 를 확인하시면 됩니다.

언제나 테클은 환영합니다.

##CharSequence 인터페이스에 isEmpty 메서드 추가
- CharSequence인터페이스에서 isEmpty메서드 추가됨에따라 이를 구현하는 StringBuffer, StringBuilder, String 등에서
isEmpty메서드를 사용가능하다.
  
  
##TreeMap 클래스 putIfAbsent, computeIfAbsent, computeIfPresent, compute, merge methods 추가
- 위의 메서드들이 추가되었지만 computeIfAbsent메서드는 Java16버전에서 버그가 수정되었다. 그러므로 computeIfAbsent메서드를 15버전에서
사용하는 경우 16버전으로 업그레이드 하거나 재정의해서 사용할것.
- [버그 픽스](http://jdk.java.net/16/release-notes#JDK-8259622)

