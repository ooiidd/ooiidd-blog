---
title: 'Spring(4) - 데이터 바인딩'
date: 2021-05-17 02:21:13
category: 'Spring'
draft: false
---
#데이터 바인딩
- 사용 되는곳
    - spring web mvc
    - properties 읽어올 때
    - spring expression language

- Spring boot에서는 Converter와 Formatter를 자동으로 등록해준다.

Formatter
```java
@Component
public class EventFormatter implements Formatter<Event> {

    @Override
    public Event parse(String text, Locale locale) throws ParseException {
        return new Event(Integer.parseInt(text));
    }

    @Override
    public String print(Event object, Locale locale) {
        return object.getId().toString();
    }
}
```

Converter
```java
public class EventConverter {

    @Component
    public static class StringToEventConverter implements Converter<String,Event>{

        @Override
        public Event convert(String source) {
            return new Event(Integer.parseInt(source));
        }
    }

    @Component
    public static class EventToStringConverter implements Converter<Event,String>{

        @Override
        public String convert(Event source) {
            return source.getId().toString();
        }
    }
}
```

- 수동 등록
```java
@Configuration
public class WebConfig implements WebMvcConfigurer {
    @Override
    public void addFormatters(FormatterRegistry registry) {
        registry.addFormatter(new EventFormatter());
        registry.addConverter(new EventConverter.EventToStringConverter());
    }
}
```