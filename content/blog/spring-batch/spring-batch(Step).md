---
title: 'Spring Batch(2) - Step'
date: 2022-03-04
category: 'spring batch'
draft: true
---

#Step
##Step
- 배치 계층에서 가장 상위에 있는 배치 작업 자체를 말함
- Job을 구성하기위한 최상위 인터페이스
- 스프링 배치가 기본 구현체를 제공
- 여러 Step 포함
- 최소 하나 이상의 Step으로 구성
    ####구현체
    1. SimpleJob
        - 순차적 Step 실행
    2. FlowJob
        - 특정한 조건과 흐름에 따라 Step 구성
##StepExecution
##StepContribution