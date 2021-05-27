---
title: 'Java12 주요 변경점'
date: 2021-05-27 13:30
category: 'Java-Change'
draft: false
---

안녕하세요 selest 입니다.

오늘은 자바 12버전 변경점을 정리해보려 합니다.

모든 변경점을 정리하지는 않았습니다.

모든 변경점을 확인하기위해서는 [여기](https://www.oracle.com/java/technologies/javase/12all-relnotes.html) 를 확인하시면 됩니다.

언제나 테클은 환영합니다.

##Z Garbage Collector 클래스 언로드 지원
- ZGC가 사용되지 않는 클래스를 언로드하면 이러한 클래스와 관련된 데이터 구조를 해제 하여 애플리케이션의 전체 공간을 줄일 수 있습니다.
- ZGC에서 클래스 언로딩은 Java 애플리케이션 스레드의 실행을 중지하지 않고 동시에 발생하므로 GC 일시 중지 시간에 영향을 미치지 않습니다.
- 이 기능은 기본적으로 활성화되어 있지만 명령줄 옵션 (-XX:-ClassUnloading)을 사용하여 비활성화할 수 있습니다.