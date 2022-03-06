---
title: 'Spring Batch(3) - Step'
date: 2022-03-06
category: 'spring batch'
draft: true
---

#Step
##Step
- Batch Job을 구성하는 독립적인 하나의 단계로서 실제 배치처리를 정의하고 컨트롤하는데 필요한 모든 정보를 가지고 있는 도메인 객체
- 입력과 처리, 출력과 관련된 비즈니스 로직을 포함하는 모든 설정을 담음
- Job의 세부 작업을 Task기반으로 설정하고 명세해 놓은 객체
    ####기본 구현체
    1. TaskletStep
       - 가장 기본이 되는 클래스로서 Tasklet 타입의 구현체들을 제어함
    1. PartitionStep
       - 멀티 스레드 방식으로 Step을 여러개로 분리해서 실행
    1. JobStep
       - Step 내에서 Job을 실행하도록한다
    1. FlowStep
       - Step 내에서 Flow를 실행하도록한다 
    
---
##StepExecution
- Step에 대한 한번의 시도를 의미하는 객체
- Step 실행중에 발생한 정보들을 저장하고 있는 객체
- Step이 매번 시도될 때마다 생성되며 각 Step 별로 생성됨
- Job이 재시작 하더라도 이미 성공적으로 완료된 Step은 재 실행되지 않고 실패한 Step만 실행됨
- Step Execution이 모두 정상적으로 완료 되어야 JobExecution이 정상적으로 완료된다.
- Step의 StepExecution중 하나라도 실패하면 JobExecution은 실패한다.
---
##StepContribution