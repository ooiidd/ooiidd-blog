---
title: 'Spring Batch(2) - Job'
date: 2022-03-04
category: 'spring batch'
draft: true
---

#Job
##Job
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
  
  ####Class 구조
```java
public class SimpleJob extends AbstractJob {
  private List<Step> steps;
}
public class FlowJob extends AbstractJob {
  protected Flow flow;
  private Map<String, Step> stepMap = new ConcurrentHashMap();
}
public abstract class AbstractJob implements Job, StepLocator, BeanNameAware, InitializingBean {
  private String name;
  private boolean restartable = true;
  private JobRepository jobRepository;
  private CompositeJobExecutionListener listener = new CompositeJobExecutionListener();
  private JobParametersIncrementer jobParametersIncrementer;
  private JobParametersValidator jobParametersValidator = new DefaultJobParametersValidator();
  private StepHandler stepHandler;
}
public interface Job {
  String getName();
  boolean isRestartable();
  void execute(JobExecution var1);
  @Nullable
  JobParametersIncrementer getJobParametersIncrementer();
  JobParametersValidator getJobParametersValidator();
}
```


---

##JobInstance
- Job이 실행될 때 생성되는 Job의 논리적 실행 단위 객체
- 고유하게 식별 가능한 작업 실행
- Job의 설정과 구성은 동일하지만, Job이 실행되는 시점에 처리하는 내용은 다르기 때문에 Job의 실행을 구분해야함.
- Job Instance 생성 및 실행
  - 처음 시작하는 Job + JobParameter 일 경우 새로운 JobInstance생성
  - 이전과 동일한 Job + JobParameter 일 경우 이미 존재하는 JobInstance 리턴 (실행 안함)
    - 내부적으로 JobName + jobKey(jobParameters의 Hash값)를 가지고 JobInstance 객체를 얻기 때문에
- Job과는 1:M 관계

---
  
##JobParameter
- Job을 실행할 때 함께 포함되어 사용되는 파라미터를 가진 도메인 객체
- 하나의 Job에 존재할 수 있는 여러개의 JobInstance를 구분하기위한 용도
- JobParameters와 JobInstance는 1:1 관계

  ###생성 및 바인딩
  - 어플리케이션 실행 시 주입 
    - Java -jar LogBatch.jar requestDate=20220304
  - 코드로 생성
    - JobParameterBuilder, DefaultJobParametersConverter
  - SpEL 이용
    - @Value("#{jobParameter[requestDate]}"), @JobScope, @StepScope 선언 필수
    
  ###Class구조
```java
public class JobParameters implements Serializable {
  private final Map<String, JobParameter> parameters;
}
public class JobParameter implements Serializable {
  private final Object parameter;
  private final JobParameter.ParameterType parameterType;
  private final boolean identifying;
  
  public static enum ParameterType {
    STRING,
    DATE,
    LONG,
    DOUBLE;

    private ParameterType() {
    }
  }
}

```
---

##JobExecution

---

##Job 실행 순서
1. SimpleJobBuilder에서 Step 등록
1. BatchAutoConfiguration에서 Runner Bean 등록
1. JobLauncherApplicationRunner에서 execute
1. JobLauncher에서 execute