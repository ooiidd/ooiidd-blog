---
title: 'Web'
date: 2021-05-27 16:30
category: 'web'
draft: false
---

## Controller
```java
@RequestMapping(value = "/user/{user_no}/usage", method = RequestMethod.GET)
public Map<String, Object> getUsedList(@PathVariable("user_no")String user_no , @RequestParam("ptype")int ptype ) {
    
}
```
---
## Mapper
```xml
<select id="getUseData" parameterType="String" resultType="com.lgcns.tct.dto.UsedataDto">
    SELECT COUNT(*) AS usage_count
        , SUM(use_time) AS usage_minute
        , SUM(use_distance) AS usage_meter
        , round(SUM(use_distance)/1000*0.232, 1) AS carbon_reduction
    FROM kickboard_svc.t_svc_use
    WHERE 1=1
    AND user_no=#{user_no} 
    AND DATE(use_start_dt)>=#{start_dt}
</select>
<select id="getUsedList" parameterType="String" resultType="com.lgcns.tct.dto.UsedListDto">
    SELECT U.use_no use_no,max(use_distance) use_distance,abs(TIMESTAMPDIFF(MINUTE, max(use_end_dt), max(use_start_dt))) use_time,
	DATE_FORMAT(max(use_start_dt),'%Y-%m-%d %H:%i:%s') use_start_dt,
	DATE_FORMAT(max(use_end_dt),'%Y-%m-%d %H:%i:%s') use_end_dt,
	DATE_FORMAT(max(pay_datetime),'%Y-%m-%d %H:%i:%s') pay_datetime,
	cast(ifnull(GROUP_CONCAT(if(paymethod_code = 'C', pay_cost,null)),0) AS SIGNED integer) AS card_pay,
	cast(ifnull(GROUP_CONCAT(if(paymethod_code = 'P', pay_cost,null)),0) AS SIGNED integer) AS point_pay 
    FROM kickboard_svc.t_svc_use U
    left JOIN kickboard_svc.t_svc_use_pay P ON U.USE_NO = P.USE_NO
    left outer JOIN kickboard_svc.t_point_pay POINT ON POINT.SVC_USE_PAY_NO = P.SVC_USE_PAY_NO
    where U.USER_NO = #{user_no}
        and DATE(use_start_dt) >= #{start_dt}
    GROUP BY use_no
</select>
<select id="getUserInfo" parameterType="String" resultType="com.lgcns.tct.dto.UserInfoDto">
    SELECT USER_NO AS user_no, NAME AS name  FROM kickboard_svc.t_user WHERE user_no = #{user_no}
</select>
```
---
## Html
```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <link rel="stylesheet" type="text/css" href="./res/index.css">
    <link rel="stylesheet" type="text/css" href="./res/reset.css">
    <script src="./res/jquery-3.6.3.min.js"></script>
    <script>
      
      $(document).ready(function() {
        const USER_NO = 'ME00001';
        const getSummary = (ptype) => {
          $.ajax({
              type: "GET",
              url: `http://localhost:8080/api/v1/user/${USER_NO}/usage/summary`,
              data : {ptype : ptype},
              dataType: "json",
              success: function (result, status, xhr) {
                console.log('회원정보 가져오기 성공');
                console.table(result);
                $('#count').text(result?.usage_count + '건');
                $('#minute').text(result?.usage_minute+'분');
                $('#meter').text((result?.usage_meter/1000.0).toFixed(1)+'km');
                $('#reduction').text(result?.carbon_reduction+'kg');
              },
              error: function (xhr, status, error) {
                console.error('회원정보 가져오기 실패')
              },
        });
      }
      const getDataList = (ptype) => {
          $.ajax({
              type: "GET",
              url: `http://localhost:8080/api/v1/user/${USER_NO}/usage`,
              data : {ptype : ptype},
              dataType: "json",
              success: function (result, status, xhr) {
                console.log('회원정보 가져오기 성공');
                $('.service-list-container').empty();
                $('.service-empty').empty();
                console.table(result);
                if(result?.list){
                  if(result.list.length == 0){
                    let div = '<div class="service-empty-container">'+
                        '<div class="service-empty-message">'+
                          '조회된 정보가 없습니다.'+
                        '</div>'+
                      '</div>';
                    $('.service-empty').append(div);
                  }
                  for(let i=0;i<result.list.length;i++){
                    let cur = result.list[i];
                    console.table(cur);
                    let div = '<div class="service-list-content">'+
                    '<div class="service-list-header">'+
                      '<span>'+cur.use_distance+'km</span>'+
                      '<span class="color-gray ml-10">'+cur.use_time+'분</span>'+
                    '</div>'+
                    '<div class="service-list-body">'+
                      '<div class="color-gray">이용시간</div>'+
                      '<div>'+cur.use_start_dt+' ~ '+cur.use_end_dt+'</div>'+
                      '<div class="color-gray">결제일시</div>'+
                      '<div>'+cur.pay_datetime+'</div>'+
                      '<div class="color-gray">결제수단</div>'+
                      '<div>카드 '+cur.card_pay+'원 + 포인트 '+cur.point_pay+'P</div>'+
                    '</div>'+
                    '</div>'+
                    '<hr />';
                    $('.service-list-container').append(div);
                  }
                }
              },
              error: function (xhr, status, error) {
                $('.service-list-container').empty();
                $('.service-empty').empty();
                console.error('회원정보 가져오기 실패')
              },
        });
      }

        /*회원정보 가져오기*/
        $.ajax({
          type: "GET",
          url: `http://localhost:8080/api/v1/user/${USER_NO}`,
          dataType: "json",
          success: function (result, status, xhr) {
            console.log('회원정보 가져오기 성공');
            console.table(result);
            $('#userName').text(result?.name)
          },
          error: function (xhr, status, error) {
            console.error('회원정보 가져오기 실패')
          },
        });

        $('.tablinks').click(function(e){
          let innerHtml = e.target.innerHTML;
          $('.tablinks').removeClass('on');
          $(e.target).addClass('on');
          if(innerHtml === '1주일'){
            /*회원정보 가져오기*/
            getSummary(1);
            getDataList(1);
          }
          else if(innerHtml === '1개월'){
            getSummary(2);
            getDataList(2);
          }
          else{
            getSummary(3);
            getDataList(3);
          }
        });
      })
    </script>
  </head>
  <body>
    <div>
      <!-- Title -->
        <div class="main-title">
          <h1>서비스 이용내역</h1>
          <div id="userName"></div>
        </div>
      <hr />
      <!-- List summary  -->
      <div class="service-summary">
        <div class="service-summary-tab">
          <button class="tablinks on">1주일</button>
          <button class="tablinks">1개월</button>
          <button class="tablinks">3개월</button>
        </div>
        <div class="spacer-20"></div>
        <div class="service-summary-detail-container">
          <div class="color-gray">이용건수</div>
          <div id="count">18건</div>
          <div class="color-gray">이용시간</div>
          <div id="minute">320분</div>
          <div class="color-gray">이동거리</div>
          <div id="meter">60.2km</div>
          <div class="color-gray">탄소절감효과</div>
          <div id="reduction">8.7kg</div>
        </div>
      </div>

      <hr />

      <!-- Usage List -->
      <div class="service-list-container">
        <div class="service-list-content">
          <div class="service-list-header">
            <span>32km</span>
            <span class="color-gray ml-10">60분</span>
          </div>
          <div class="service-list-body">
            <div class="color-gray">이용시간</div>
            <div>22.01.22 08:01 ~ 22.01.22 09:01</div>
            <div class="color-gray">결제일시</div>
            <div>22.01.22 09:01</div>
            <div class="color-gray">결제수단</div>
            <div>카드 1900원 + 포인트 100P</div>
          </div>
        </div>
        <hr />
        <div class="service-list-content">
          <div class="service-list-header">
            <span>32km</span>
            <span class="color-gray ml-10">60분</span>
          </div>
          <div class="service-list-body">
            <div class="color-gray">이용시간</div>
            <div>22.01.22 08:02 ~ 22.01.22 09:02</div>
            <div class="color-gray">결제일시</div>
            <div>22.01.22 09:02</div>
            <div class="color-gray">결제수단</div>
            <div>카드 1000원</div>
          </div>
        </div>
        <hr />
      </div>

      <!-- Empty -->
      <div class="service-empty">
        <div class="service-empty-container">
          <div class="service-empty-message">
            조회된 정보가 없습니다.
          </div>
        </div>
      </div>
    </div>
  </body>
</html>
```
