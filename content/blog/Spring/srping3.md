---
title: 'Spring(3) - Validation'
date: 2021-05-17
category: 'Spring'
draft: false
---

#Validation
- 일반적으로는 validator를 구현하여 사용 가능

ex)
```java
public class EventValidator implements Validator {

    @Override
    public boolean supports(Class<?> clazz) {
        return Event.class.equals(clazz);
    }

    @Override
    public void validate(Object target, Errors errors) {
        ValidationUtils.rejectIfEmptyOrWhitespace(errors,"title","notempty","Empty title is not allowd.");
    }
}
```


- org.springframework.boot:spring-boot-starter-validation
    - 위의 dependency를 가진다면 validator 없이 간단한 validation 가능
    - spring-boot-starter-validation에서 기본적인 validator의 구현체를 등록 해두었기 때문에 Autowired로 해당구현체를 사용하면 됨.
    
ex) 
```java
public class Event {
    Integer id;

    @NotEmpty
    String title;

    @Min(0)
    Integer limit;

    @Email
    String email;

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public Integer getLimit() {
        return limit;
    }

    public void setLimit(Integer limit) {
        this.limit = limit;
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
}
@Component
public class ValidateAppRunner implements ApplicationRunner {

    @Autowired
    Validator validator;

    @Override
    public void run(ApplicationArguments args) throws Exception {
        System.out.println(validator.getClass());
        Event event = new Event();
        event.setLimit(-3);
        event.setEmail("ttte");
        Errors errors = new BeanPropertyBindingResult(event,"event");

        validator.validate(event,errors);
        System.out.println(errors.hasErrors());
    }
}
```


