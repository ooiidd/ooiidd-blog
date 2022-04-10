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

##JobRepository
- 배치 작업 중의 정보를 저장하는 저장소 역할
- Job이 언제 수행되었고, 언제 끝났으며, 몇 번이 실행되었고 실행에 대한 결과 등의 배치 작업의 수행과 관련된 모든 meta data를 저장함.
  - JobLauncher, Job, Step 구현체 내부에서 CRUD 기능을 처리함.

###JobRepository 설정
- @EnableBatchProcessing 어노테이션만 선언하면 JobRepository 가 자동으로 빈으로 생성됨
- BatchConfigurer 인터페이스를 구현하거나 BasicBatchConfigurer를 상속해서 JobRepository 설정을 커스터마이징 할 수 있다.
  - JDBC 방식으로 설정 - JobRepositoryFactoryBean
    - 내부적으로 AOP 기술을 통해 트랜잭션 처리를 해주고 있음.
    - 트랜잭션 isolation 의 기본값은 SERIALIZEBLE로 최고 수정, 다른레벨(READ_COMMITED, REPEATABLE_READ)로 지정 가능
    - 메타테이블의 Table Prefix를 변경할 수 있음, 기본 값은 "BATCH_"
  - In Memory 방식으로 설정 - MapJobRepositoryFactoryBean
    - 성능 등의 이유로 도메인 오브젝트를 굳이 데이터베이스에 저장하고 싶지 않을 경우
    - 보통 Test나 프로토타입의 빠른 개발이 필요할 때 사용

