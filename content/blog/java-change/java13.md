---
title: 'Java13 주요 변경점'
date: 2021-05-27 10:30
category: 'Java-Change'
draft: false
---

안녕하세요 selest 입니다.

오늘은 자바 13버전 변경점을 정리해보려 합니다.

모든 변경점을 정리하지는 않았습니다.

모든 변경점을 확인하기위해서는 [여기](https://www.oracle.com/java/technologies/javase/13all-relnotes.html) 를 확인하시면 됩니다.

언제나 테클은 환영합니다.

##사용하지 않는 힙 메모리를 운영 체제에 반환하도록 ZGC가 향상되었습니다.
- 이 기능은 메모리 설치 공간이 문제가 되는 애플리케이션 및 환경에 유용합니다.
- 이 기능은 기본적으로 사용된다. 사용하지 않기를 원하면 (-XX:-ZUncommit) 명령을 사용.
- Minimum 힙 메모리 사이즈 조절 (-Xms)
- Maximum 힙 메모리 사이즈 조절 (-Xmx)
- uncommit 지연 구성 (-XX:ZUncommitDelay=<second>) (defalt 300sec)

##-XXSoftMaxHeapSize 명령줄 추가
- 해당 명령줄은 ZGC가 활성화 되었을 때만 적용됩니다. (ZGC 활성화 : -XX:+UseZGC)
- 설정된 경우 GC는 GC가 OutOfMemoryError를 방지하기 위해 힙이 필요하다고 판단하지 않는 한 지정된 크기 이상으로 증가하지 않도록 노력합니다.
- 소프트 최대 힙 크기를 최대 힙 크기(-Xmx)보다 큰 값으로 설정할 수 없습니다. 명령줄에 설정되지 않은 경우 기본값은 최대 힙 크기와 같은 값으로 설정됩니다.

##ZGC Maximum Heap Size 증가 (4TB -> 16TB)

##Switch Expressions (Preview)
- switch 문이 case ...: 와 case ... -> 두가지 형태의 문법을 사용 할 수 있습니다.
- switch 표현식에서 새로운 값 산출을 위한 추가문장을 사용할 수 있습니다.
- 이러한 변경은 일상적인 코딩 작업을 단순화 하고 switch문에서 패턴매칭을 사용할 수 있는 방법을 준비합니다.

