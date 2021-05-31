---
title: 'Spring Boot(1) : auto-configuration'
date: 2021-05-31 03:19
category: 'spring boot'
draft: false
---

## auto-configuration
@EnableAutoConfiguration 어노테이션이 있을때 모듈을 dependency에 추가하여 사용가능

### 방법
1. project 생성

2. dependency 추가
   - Maven
     ```xml
     <project>
         <dependencies>
             <dependency>
                 <groupId>org.springframework.boot</groupId>
                 <artifactId>spring-boot-autoconfigure</artifactId>
                 <version>2.5.0</version>
             </dependency>
         
             <dependency>
                 <groupId>org.springframework.boot</groupId>
                 <artifactId>spring-boot-autoconfigure-processor</artifactId>
                 <version>2.5.0</version>
                 <optional>true</optional>
             </dependency>
         </dependencies>
         <dependencyManagement>
             <dependencies>
                 <dependency>
                     <groupId>org.springframework.boot</groupId>
                     <artifactId>spring-boot-dependencies</artifactId>
                     <version>2.5.0</version>
                     <type>pom</type>
                     <scope>import</scope>
                 </dependency>
             </dependencies>
         </dependencyManagement>
     </project>
     ```

   - Gradle
      ```groovy
      plugins {
          id 'java'
          id 'maven-publish'
      }
      dependencies {
          implementation 'org.springframework.boot:spring-boot-autoconfigure:2.5.0'
          implementation 'org.springframework.boot:spring-boot-autoconfigure-processor:2.5.0'
          implementation platform('org.springframework.boot:spring-boot-dependencies:2.5.0')
      }
      publishing{
          publications{
              maven(MavenPublication){
                  groupId = 'com.hong'
                  artifactId = 'song-boot-starter'
                  version = '1.0'
      
                  from components.java
              }
          }
      }
      ```
3. 자바 Bean과 Spring Configuration 추가
    ```java
    public class Item {
        private String name;
        private int number;
    
        public String getName() {
            return name;
        }
    
        public void setName(String name) {
            this.name = name;
        }
    
        public int getNumber() {
            return number;
        }
    
        public void setNumber(int number) {
            this.number = number;
        }
    
        @Override
        public String toString() {
            return "Item{" +
                    "name='" + name + '\'' +
                    ", number=" + number +
                    '}';
        }
    }
    @Configuration
    public class ItemConfiguration {
        @Bean
        public Item item(){
            Item item = new Item();
            item.setName("hong");
            item.setNumber(10);
            return item;
        }
    }
    ```

4. Maven Local Repo로 publish
   - Maven : mvn install
   - Gradle : gradle publishToMavenLocal

5. 사용
   - Maven : dependency에 위의 2번내용에서 추가한 artifact를 등록하여 사용.
   - Gradle : Maven과 마찬가지인데 repositories에 mavenLocal() 추가
      ```groovy
      repositories {
          mavenCentral()
          mavenLocal()
      }
      ```
6. 확인
   ```java
   @SpringBootApplication
   public class SongbootstartertestApplication {
   
       public static void main(String[] args) {
           SpringApplication.run(SongbootstartertestApplication.class, args);
       }
   
   }
   ```
   ```java
   @Component
   public class SongRunner implements ApplicationRunner {
       @Autowired
       Item item;
       
       @Override
       public void run(ApplicationArguments args) throws Exception {
           System.out.println(item);
       }
   }
   ```
7. 출력
   Item{name='hong', number=10}

@SpringBootApplication 어노테이션이 기본적으로 @EnableAutoConfiguration 어노테이션을 사용하므로
추가하지 않아도 동작함.

---
###문제는 Override 되지 않음!
어떤 프로젝트에서 @Bean 을 사용하여 Item을 바꾸려고 함.
```java
@SpringBootApplication
public class SongbootstartertestApplication {

    public static void main(String[] args) {
        SpringApplication.run(SongbootstartertestApplication.class, args);
    }

    @Bean
    public Item item(){
        Item item = new Item();
        item.setName("Change Name");
        item.setNumber(200);
        return item;
    }
}
```

위의 코드를 실행해 보면

A bean with that name has already been defined in com.example.songbootstartertest.SongbootstartertestApplication and overriding is disabled.

라는 에러가 뜨는것을 확일할 수 있다.

###해결

@ConditionalOnMissingBean 어노테이션 사용

위에서 만든 Configuration에서 어노테이션을 추가함.

```java
@Configuration
public class ItemConfiguration {
    @Bean
    @ConditionalOnMissingBean
    public Item item(){
        Item item = new Item();
        item.setName("hong");
        item.setNumber(10);
        return item;
    }
}
```

다시 publish 하고 실행해보면 예상했던 결과를 얻을 수 있다.

Item{name='Change Name', number=200}

###properties 파일 기반
@Bean 으로 주입 받지 않고, properties 파일 기반으로 name과 number를 설정해 보자.

1. ConfigurationProperties 추가
   ```java
   @ConfigurationProperties("item")
   public class ItemProperties {
       private String name;
       private int number;
   
       public String getName() {
           return name;
       }
   
       public void setName(String name) {
           this.name = name;
       }
   
       public int getNumber() {
           return number;
       }
   
       public void setNumber(int number) {
           this.number = number;
       }
   }
   ```


2. Configuration에서 해당 Properties를 사용하도록 변경
   ```java
   @Configuration
   @EnableConfigurationProperties(ItemProperties.class)
   public class ItemConfiguration {
       @Bean
       @ConditionalOnMissingBean
       public Item item(ItemProperties properties){
           Item item = new Item();
           item.setName(properties.getName());
           item.setNumber(properties.getNumber());
           return item;
       }
   }
   ```

3. 프로젝트의 application.properties에 추가
   ```properties
   item.name=propName
   item.number=5000
   ```

4. 확인

   Item{name='propName', number=5000} 출력