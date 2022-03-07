---
title: 'Spring Batch(1) - OverView'
date: 2022-03-04
category: 'spring batch'
draft: false
---

## @EnableBatchProcessing
- 총 4개의 설정 클래스 실행
- 스프링 배치의 모든 초기화 및 실행 구성

    ### 1. BatchAutoConfiguration
    - Job을 수행하는 JobLauncherApplicationRunner 빈을 생성
    
    ### 2. SimpleBatchConfiguration
    - JobBuilderFactory와 StepBuilderFactory 생성
    - 스프링 배츼의 주요 구성 요소 생성 - 프록시 객체로 생성됨
    
    ### 3. BacthConfigurerConfiguration
    - BasicBatchConfigurer
        - SimpleBatchConfiguration에서 생성한 프록시 객체의 실제 대상 객체를 생성
    - JpaBatchConfigurer
        - JPA 관련 객체를 생성

##Job,Step 생성
### 1. JobBuilderFactory
- Job을 생성하는 빌더 팩토리
### 2. StepBuilderFactory
- Step을 생성하는 빌더팩토리

```java
@RequiredArgsConstructor
@Configuration
public class JobConfiguration {
    private final JobBuilderFactory jobBuilderFactory;
    private final StepBuilderFactory stepBuilderFactory;

    @Bean
    public Job firstJob() {
        return jobBuilderFactory.get("firstJob")
                .start(firstStep())
                .next(secondStep())
                .build();
    }

    @Bean
    public Step firstStep(){
        return stepBuilderFactory.get("firstStep")
                .tasklet(new Tasklet() {
                    @Override
                    public RepeatStatus execute(StepContribution stepContribution, ChunkContext chunkContext) throws Exception {
                        //Buisness Logic
                        System.out.println("first Step");
                        return RepeatStatus.FINISHED;
                    }
                })
                .build();
    }
    @Bean
    public Step secondStep(){
        return stepBuilderFactory.get("secondStep")
                .tasklet(new Tasklet() {
                    @Override
                    public RepeatStatus execute(StepContribution stepContribution, ChunkContext chunkContext) throws Exception {
                        //Buisness Logic
                        System.out.println("Second Step");
                        return RepeatStatus.FINISHED;
                    }
                })
                .build();
    }
}
```


#Spring Batch Schema
##JOB 관련 테이블
### 1. BATCH_JOB_INSTANCE
- Job이 실행될 때, JobInstance정보가 저장됨.
- Key (job_name,job_key)
   ####Columns
  - JOB_INSTANCE_ID
  - VERSION
  - JOB_NAME
  - JOB_KEY
  
### 2. BATCH_JOB_EXECUTION
- Job의 실행정보가 저장
- Job생성, 시작시간, 종료시간, 싱행상태, 메시지 등 관리
  ####Columns
    -  JOB_EXECUTION_ID
    -  VERSION
    -  JOB_INSTANCE_ID
    -  CREATE_TIME
    -  START_TIME
    -  END_TIME
    -  STATUS
    -  EXIT_CODE
    -  EXIT_MESSAGE
    -  LAST_UPDATED
    -  JOB_CONFIGURATION_LOCATION
### 3. BATCH_JOB_EXECUTION_PARAMS
- Job과 함께 싱행되는 Job Parameter 정보 저장
  ####Columns
    -  JOB_EXECUTION_ID
    -  TYPE_CD
    -  KEY_NAME
    -  STRING_VAL
    -  DATE_VAL
    -  LONG_VAL
    -  DOUBLE_VAL
    -  IDENTIFYING
### 4. BATCH_JOB_EXECUTION_CONTEXT
- Job의 실행동안 여러가지 상태정보, 공유 데이터를 Json형식으로 저장
- Step간 서로 공유 가능
  ####Columns
    - JOB_EXECUTION_ID
    - SHORT_CONTEXT
    - SERIALIZED_CONTEXT

##STEP 관련 테이블
### 5. BATCH_STEP_EXECUTION
- Step의 실행정보 저장
- 생성, 시작, 종료 시간, 실행상태, 메시지 등을 관리
  ####Columns
    - STEP_EXECUTION_ID
    - VERSION
    - STEP_NAME
    - JOB_EXECUTION_ID
    - START_TIME
    - END_TIME
    - STATUS
    - COMMIT_COUNT
    - READ_COUNT
    - FILTER_COUNT
    - WRITE_COUNT
    - READ_SKIP_COUNT
    - WRITE_SKIP_COUNT
    - PROCESS_SKIP_COUNT
    - ROLLBACK_COUNT
    - EXIT_CODE
    - EXIT_MESSAGE
    - LAST_UPDATED
### 6. BATCH_STEP_EXECUTION_CONTEXT
- Step의 실행동안 여러가지 상태정보, 공유데이터를 Json형식으로 저장
- Step별로 저장되며 Step간 서로 공유 불가
  ####Columns
    - STEP_EXECUTION_ID
    - SHORT_CONTEXT
    - SERIALIZED_CONTEXT