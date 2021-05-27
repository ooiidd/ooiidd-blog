---
title: 'Java14 주요 변경점'
date: 2021-05-25 18:00
category: 'Java-Change'
draft: false
---

안녕하세요 홍성훈 입니다.

오늘은 자바 14버전 변경점을 정리해보려 합니다.

모든 변경점을 정리하지는 않았습니다.

모든 변경점을 확인하기위해서는 [여기](https://www.oracle.com/java/technologies/javase/14all-relnotes.html) 를 확인하시면 됩니다.

언제나 테클은 환영합니다.

##통화 형식 지원
- NumberFormat에서 통화형식을 지원합니다.

```java
public class NumberFormatTest {
    public static void main(String[] args) {
        NumberFormat format = NumberFormat.getCurrencyInstance(Locale.CANADA);
        System.out.println(format.format(123));
        System.out.println(NumberFormat.getCurrencyInstance(Locale.KOREA).format(123));
    }
}
```
```text
$123.00
₩123
```

##Z Garbage Collector를 실험적으로 사용 가능하다.

##Parallel GC 향상
- Parallel GC는 병렬 작업을 예약하기 위해 다른 수집기와 동일한 작업 관리 메커니즘을 채택했다. 이로인해 성능이 크게 향상되었다.

##G1 GC에서 NUMA 인식 메모리 할당
- 이제 G1 가비지 수집기는 가비지 수집 간에 젊은 세대의 동일한 NUMA 노드에 개체를 할당하고 유지하려고 시도합니다. 이는 병렬 GC NUMA 인식과 유사합니다.
- G1은 엄격한 인터리브를 사용하여 사용 가능한 모든 NUMA 노드에 Humongous 및 Old 영역을 균등하게 배포하려고 시도합니다. 젊은 세대에서 오래된 세대로 복사된 개체를 배치하는 것은 무작위입니다.

##Concurrent Mark and Sweep(CMS) Garbage Collector 제거

##Thread Suspend/Resume Deprecated
다음의 메서드들이 삭제를위해 Deprecated되었다.
- Thread.suspend()
- Thread.resume()
- ThreadGroup.suspend()
- ThreadGroup.resume()
- ThreadGroup.allowThreadSuspension(boolean)

##ParallelScavenge + Serial Old GC 조합 Deprecated

