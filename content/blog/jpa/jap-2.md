---
title: 'JPA(2) - Annotation'
date: 2022-05-15
category: 'JPA'
draft: false
---

##@Entity 속성
###속성
- name
  - JPA에서 사용할 엔티티 이름을 지정함.
  - 기본값: 클래스 이름
  
##@Table
###속성
- name : 매핑할 테이블 이름
- catalog : 데이터베이스 catalog
- schema : 데이터베이스 schema
- uniqueConstraints(DDL) : DDL생성 시 유니크 제약조건 생성

---

##데이터베이스 스키마 자동 생성
- DDL을 애플리케이션 실행 시점에 자동 생성
- 테이블 중심 -> 객체중심
- 데이터베이스 방언을 활용해서 데이터베이스에 맞는 적절한 DDL생성
- 생성된 DDL은 개발 장비에서만 사용
- 생성된 DDL은 운영서버에서는 사용하지 않거나, 적절히 다듬은 후 사용
###설정방법
1. persistence.xml
   - <property name="hibernate.hbm2ddl.auto" value="create" />
2. spring
   - spring.jpa.hibernate.ddl-auto=create
###옵션
- create : 기존 테이블 삭제 후 다시생성
- create-drop : create와 같으나 종료시점에 테이블 DROP
- update : 변경분만 반영(운영DB에는 사용하면 안됨)
- validate : 엔티티와 테이블이 정상 매핑되었는지만 확인
- none : 사용하지 않음

###주의
- 개발 초기에는 create 또는 update
- 테스트 서버는 update 또는 validate
- 스테이징과 운영 서버는 validate 또는 none

---

##매핑 어노테이션
- @Column : 컬럼 매핑
- @Temporal : 날짜 타입 매핑
- @Enumerated : enum 타입 매핑
- @Lob : BLOB, CLOB 매핑
- @Transient : 특정 필드를 컬럼에 매핑하지 않음 (매핑 무시)

###@Column
- name : 필드와 매핑할 테이블의 컬럼 이름 - Default : 객체의 필드 이름
- insertable, updatable : 등록, 변경 가능 여부 - Default : TRUE
- nullable(DDL) : null 값의 허용 여부, not null 제약조건 추가됨
- unique(DDL) : @Table의 uniqueConstraints와 같지만 한 컬럼에 간단히 유니크 제약조건
- columnDefinition : 데이터베이스 컬럼 정보
- length(DDL) : 문자 길이 제약조건, String 타입에만 사용 - Default : 255
- precision, scale(DDL) : BigDecimal, BigInteger 타입에서 사용
    - precision은 소수점을 포함한 전체 자릿수
    - scale은 소수의 자릿수
    - double, float타입에는 적용되지 않는다.
  
###@Enumerated
EnumType.ORDINAL은 잘 사용하지 않음.

- EnumType.ORDINAL : enum 순서를 데이터베이스에 저장 (Default)
- EnumType.STRING : enum 이름을 데이터베이스에 저장

###Temporal
- 날짜 타입 (java.util.Date, java.util.Calendar)을 매핑할 때 사용
- LocalDate, LocalDateTime을 사용할 때는 생략 가능(최신 하이버네이트 지원)

###Lob
- DB의 BLOB,CLOB 타입과 매핑
- 매핑하는 필드 타입이 문자면 CLOB 매핑, 나머지는 BLOB매핑
  - CLOB : String, char[] , java.sql.CLOB
  - BLOB : byte[], java.sql.BLOB

###Transient
- 필드 매핑하지 않음.
- DB에 저장,조회하지 않음.
- 메모리상에서 임시로 어떤 값을 보관하고 싶을때 사용함.

---
##기본 키 매핑 어노테이션
- @Id
- @GeneratedValue

###@GeneratedValue
1. IDENTITY 전략
  - 데이터베이스에 위임
  - 주로 MySQL, PostgreSQL, SQL Server, DB2에서 사용
      - ex) MySQL의 AUTO_INCREMENT
  - JPA는 보통 트랜잭션 커밋 시점에 INSERT SQL 실행
      - 영속성 컨텍스트에서 ID가 필요하기때문.
  - AUTO_INCREMENT는 데이터베이스에 INSERT SQL을 실행한 이후에 ID값을 알 수 있음
  - IDENTITY전략은 em.persist()시점에 즉시 INSERT SQL 실행하고 DB에서 식별자를 조회

2. SEQUENCE 전략
  - 데이터베이스 시퀀스는 유일한 값을 순서대로 생성하는 특별한 데이터베이스 오브젝트
    - ex)오라클 시퀀스
  - Oracle, PostgreSQL, DB2, H2 데이터베이스에서 사용
####SequenceGenerator
- name : 식별자 생성기 이름
- sequenceName : 데이터베이스에 등록되어 있는 시퀀스 이름
- initialValue : DDL 생성 시에만 사용됨, 시퀀스 DDL을 생성할 때 처음 1 시작하는 수를 지정한다.
- allocationSize : 시퀀스 한 번 호출에 증가하는 수(성능최적화에 사용됨)
  - 데이터베이스 시퀀스 값이 하나씩 증가하도록 설정되어 있으면 이 값을 반드시 1로 설정해야 한다.
  - 기본값이 50인 이유 
    - 매번 persist마다 db에서 가져오지 않고 50번은 memory에서 가져올 수 있도록 하기 위해
    - 성능최적화.
- catalog, schema : 데이터베이스 catalog, schema 이름

3. TABLE 전략
  - 키 생성 전용 테이블을 하나 만들어서 데이터베이스 시퀀스를 흉내내는 전략
  - 장점: 모든 데이터베이스에 적용 가능
  - 단점: 성능

    
