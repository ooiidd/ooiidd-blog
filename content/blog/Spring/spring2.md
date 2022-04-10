---
title: 'Spring(2) - ApplicationContext'
date: 2021-05-16
category: 'Spring'
draft: false
---

# ApplicationContext

## ApplicationContext는 아래의 인터페이스 들을 상속받음

1. EnvironmentCapable
    - context.getEnvironment() 로 사용가능
    - 프로파일 설정 가능
        - 프로파일 정의
        - @Profile("profileName") 으로 프로파일 설정 가능
            - 클래스 또는 메소드에 사용가능

      ex)
      ```java
      @Profile("profileName")
      public class TestClass{
      }
      ```
        - 프로파일 설정 -Dspring.profiles.active="profileName,profileB..."
        - IntelliJ에서는 프로젝트 설정에 있음.
        - 프로파일 표현식
            - ! (not)
            - & (and)
            - | (or)
    - 프로퍼티 설정값 가져오기 가능
    - JVM Options에 설정한 시스템 프로퍼티 가져오기 가능(-Dkey="value")

1. ListableBeanFactory
    - Spring Bean관리

1. HierarchicalBeanFactory

1. MessageSource
    - 국제화, 다국화 관련기능 인터페이스
    ```java
   public interface MessageSource {
        @Nullable
        String getMessage(String code, @Nullable Object[] args, @Nullable String defaultMessage, Locale locale);
        String getMessage(String code, @Nullable Object[] args, Locale locale) throws NoSuchMessageException;
        String getMessage(MessageSourceResolvable resolvable, Locale locale) throws NoSuchMessageException;
   }
    ```
   - 스프링 부트에서는 별다른 설정 없이 messages.properties,messages_ko_KR.properties 와 같은 설정파일을 생성하여 사용 가능
    

1. ApplicationEventPublisher
    - 이벤트 프로그래밍에 필요한 인터페이스 제공
    ```java
   public class MyEvent{
        private int data;
        public MyEvent(Object source, int data){
            super(source);
        }
       public int getData(){
            return data;
       }
   }
   
   @Component
   public class AppRunner implements ApplicationRunner{
        @Autowired
        ApplicationEventPublisher publisher;
        public void run(ApplicationArguments args) throws Exception{
            publishEvent.publishEvent(new MyEvent(this,2));
        }
   }
   
   @Component
   public class MyEventHandler{
        @EventListener
        public void onApplicationEvent(MyEvent event){
            System.out.println("이벤트 받음"+event.getData());
        }    
   }
    ```
   - @EventListener 와함께 @Order 어노테이션으로 순서 설정 가능
    

1. ResourcePatternResolver
    - 리소스 읽어오기
        - 파일에서 읽어오기(file:///)
        - 클래스패스에서 읽어오기(classpath:///)

## 대표적인 ApplicationContext

- ClassPathXmlApplicationContext
- AnnotationConfigApplicationContext
