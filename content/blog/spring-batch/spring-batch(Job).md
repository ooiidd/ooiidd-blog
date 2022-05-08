---
title: 'Spring Batch(2) - Job' date: 2022-03-04 category: 'spring batch' draft: false
---

# Job

## Job

- 배치 계층에서 가장 상위에 있는 배치 작업 자체를 말함
- Job을 구성하기위한 최상위 인터페이스
- 스프링 배치가 기본 구현체를 제공
- 여러 Step 포함
- 최소 하나 이상의 Step으로 구성
  #### 구현체
    1. SimpleJob
        - 순차적 Step 실행
    2. FlowJob
        - 특정한 조건과 흐름에 따라 Step 구성

  #### Class 구조

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

## JobInstance

- Job이 실행될 때 생성되는 Job의 논리적 실행 단위 객체
- 고유하게 식별 가능한 작업 실행
- Job의 설정과 구성은 동일하지만, Job이 실행되는 시점에 처리하는 내용은 다르기 때문에 Job의 실행을 구분해야함.
- Job Instance 생성 및 실행
    - 처음 시작하는 Job + JobParameter 일 경우 새로운 JobInstance생성
    - 이전과 동일한 Job + JobParameter 일 경우 이미 존재하는 JobInstance 리턴 (실행 안함)
        - 내부적으로 JobName + jobKey(jobParameters의 Hash값)를 가지고 JobInstance 객체를 얻기 때문에
- Job과는 1:M 관계

---

## JobParameter

- Job을 실행할 때 함께 포함되어 사용되는 파라미터를 가진 도메인 객체
- 하나의 Job에 존재할 수 있는 여러개의 JobInstance를 구분하기위한 용도
- JobParameters와 JobInstance는 1:1 관계

  ### 생성 및 바인딩
    - 어플리케이션 실행 시 주입
        - Java -jar LogBatch.jar requestDate=20220304 seq(long)=2L date(date)=2021/01/01 age(double)=16.5
    - 코드로 생성
        - JobParameterBuilder, DefaultJobParametersConverter
    - SpEL 이용
        - @Value("#{jobParameter[requestDate]}"), @JobScope, @StepScope 선언 필수

  ### Class구조

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

## JobExecution

- JobInstance에 대한 한번의 시도를 의미하는 객체로서 Job 실행중에 발생한 정보들을 저장하고 있는 객체
- JobExecution은 Failed 또는 Completed등의 Job의 실행 결과 상태를 가지고 있음
- JobExecution의 실행상태 결과가 Completed면 JobInstance실행이 완료되지 않은것으로 간주해서 재실행이 가능함
- JobExecution의 실행 상태결과가 'Completed' 될 때까지 하나의 JobInstance 내에서 여러번의 시도가 생길 수 있음.

---

## Job 실행 순서

1. SimpleJobBuilder에서 Step 등록
2. BatchAutoConfiguration에서 Runner Bean 등록
3. JobLauncherApplicationRunner에서 execute
4. JobLauncher에서 execute

---

# Job Validator

- Job실행 시에 꼭 필요한 Parameter를 검증하는 용도
- DefaultJobParametersValidator(기본 구현체)를 제공하며 인터페이스 직접 구현도 가능하다.
- DefaultJobParametersValidator는 requiredKeys, optionalKeys 두가지를 생성자 혹은 setter로 받아서 사용가능하다.

```java
@Override
public void validate(JobParameters jobParameters) throws JobParametersInvalidException{
    if(jobParameters.getString("name")==null){
        throw new JobParametersInvalidException("name parameter is not found.");
    }
}
```

#PreventRestart
- Job이 실패를 해도 재시작이 안되게하는 API

#incrementer
- JobParameters 에서 필요한 값을 증가시켜서 다음에 실행할 JobParameters를 리턴
- 기존 JobParameter변경 없이 다음번 Job실행도 가능하도록 하게 해주는 API
- 기본 구현체로 RunIdIncrementer가 있고, JobParametersIncrementer 인터페이스를 구현하여 사용도 가능함.
- 
