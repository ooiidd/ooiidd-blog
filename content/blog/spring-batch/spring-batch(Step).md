---
title: 'Spring Batch(3) - Step'
date: 2022-03-06
category: 'spring batch'
draft: false
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
- 청크 프로세스의 변경 사항을 버퍼링한 후 StepExecution 상태를 업데이트하는 도메인객체
- 청크 커밋 직전에 StepExecution의 apply 메서드를 호출하여 상태를 업데이트 함
- ExitStatus의 기본 종료코드외 사용자 정의 종료코드를 생성해서 적용할 수 있음

##ExecutionContext
- 프레임워크에서 유지 및 관리하는 키/값으로 된 컬렉션
- StepExecution, JobExecution 객체의 상태를 저장하는 공유객체
- DB에 직렬화한 값으로 저장됨
- 공유범위
    - Step 범위 : 각 Step의 StepExecution에 저장되며, Step간 서로 공유 안됨
    - Job 범위 : 각 Job의 JobExecution에 저장되며, Job간 서로 공유 안되고 해당 Job의 Step간 서로 공유됨
- Job 재시작 시 이미 처리한 Row데이터는 건너뛰고 이후로 수행하도록 할 때 상태 정보를 활용함

```java
@Component
public class ExecutionContextTasklet implements Tasklet{
    @Override
    public RepeatStatus execute(StepContribution contribution, ChunkContext chunkContext) throws Exception{
        ExecutionContext jobExecutionContext = contribution.getStepExecution().getJobExecution().getExecutionContext();
        ExecutionContext stepExecutionContext = contribution.getStepExecution().getExecutionContext();
    }
}
```