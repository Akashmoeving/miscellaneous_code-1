import json
from json import dumps
import requests
import time
from httplib2 import Http
from mysql.connector import MySQLConnection

from python_mysql_dbconfig import read_db_config


class BirthdayWhatsAppWindblade:
    def get_drivers_detail(self):
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        print("Connection established")
        cursor.execute(
            "SELECT tud.FLD_USER_ID, tud.FLD_LOGIN_NAME, tld.FLD_LOCATION_ID, tld.FLD_LOCATION_NAME FROM "
            "TBL_PROFILE_DETAILS tpd INNER JOIN TBL_USER_DETAILS tud ON tud.FLD_USER_ID = tpd.FLD_USER_ID "
            "inner join TBL_DRIVER_DETAILS tdd on tdd.FLD_DRIVER_USER_ID = tud.FLD_USER_ID "
            "inner join TBL_LOCATION_DETAILS tld on tld.FLD_LOCATION_ID  = tdd.FLD_OPERATING_CITY_ID  WHERE month("
            "tpd.FLD_DATE_OF_BIRTH) = month(CURRENT_DATE()) and  DAY(tpd.FLD_DATE_OF_BIRTH) = DAY( "
            "CURRENT_DATE())  and tdd.FLD_OPERATING_CITY_ID not in (46,47) and tud.FLD_STATUS = 3 and "
            "tdd.FLD_STATUS = 3 and tud.FLD_USER_ID = 7387 ")

        user_ids = cursor.fetchall()
        print(user_ids)

        url = 'https://apiURL/notification/push'

        bearer_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..'

        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Content-Type': 'application/json'
        }
        sms_messages = {
            'Mumbai': "प्रिय, तुमचा दिवस तुमच्या ड्राईव्हसारखा विलक्षण जावो! तुमचा दिवस आनंदाच्या क्षणांसह सुरक्षित आणि खुशहाल प्रवासाने भरलेला जावो!",
            'Gurgaon': "मोइविंग परिवार मंगल कामना करता है कि आने वाला साल आपकी उत्तम ड्राइविंग की तरह ही आपके लिए अतिउत्तम साबित हो.मोइविंग के साथ जुड़े रहने के लिए धन्यवाद्।",
            'Delhi': "मोइविंग परिवार मंगल कामना करता है कि आने वाला साल आपकी उत्तम ड्राइविंग की तरह ही आपके लिए अतिउत्तम साबित हो.मोइविंग के साथ जुड़े रहने के लिए धन्यवाद्।",
            'Noida': "मोइविंग परिवार मंगल कामना करता है कि आने वाला साल आपकी उत्तम ड्राइविंग की तरह ही आपके लिए अतिउत्तम साबित हो.मोइविंग के साथ जुड़े रहने के लिए धन्यवाद्।",
            'Chandigarh': "मोइविंग परिवार मंगल कामना करता है कि आने वाला साल आपकी उत्तम ड्राइविंग की तरह ही आपके लिए अतिउत्तम साबित हो.मोइविंग के साथ जुड़े रहने के लिए धन्यवाद्।",
            'Faridabad': "मोइविंग परिवार मंगल कामना करता है कि आने वाला साल आपकी उत्तम ड्राइविंग की तरह ही आपके लिए अतिउत्तम साबित हो.मोइविंग के साथ जुड़े रहने के लिए धन्यवाद्।",
            'Lucknow': "मोइविंग परिवार मंगल कामना करता है कि आने वाला साल आपकी उत्तम ड्राइविंग की तरह ही आपके लिए अतिउत्तम साबित हो.मोइविंग के साथ जुड़े रहने के लिए धन्यवाद्।",
            'Jaipur': "मोइविंग परिवार मंगल कामना करता है कि आने वाला साल आपकी उत्तम ड्राइविंग की तरह ही आपके लिए अतिउत्तम साबित हो.मोइविंग के साथ जुड़े रहने के लिए धन्यवाद्।",
            'Ludhiana': "मोइविंग परिवार मंगल कामना करता है कि आने वाला साल आपकी उत्तम ड्राइविंग की तरह ही आपके लिए अतिउत्तम साबित हो.मोइविंग के साथ जुड़े रहने के लिए धन्यवाद्।",
            'Patna': "मोइविंग परिवार मंगल कामना करता है कि आने वाला साल आपकी उत्तम ड्राइविंग की तरह ही आपके लिए अतिउत्तम साबित हो.मोइविंग के साथ जुड़े रहने के लिए धन्यवाद्।",
            'Pune': "प्रिय, तुमचा दिवस तुमच्या ड्राईव्हसारखा विलक्षण जावो! तुमचा दिवस आनंदाच्या क्षणांसह सुरक्षित आणि खुशहाल प्रवासाने भरलेला जावो!",
            'Bengaluru': "ಆತ್ಮೀಯ , ನಿಮ್ಮ ಡ್ರೈವ್ ಗಳಂತೆ ನಿಮ್ಮ ದಿನ ಕೂಡಾ ಅದ್ಭುತವಾಗಿರಲಿ ಎಂದು ಹಾರೈಸುತ್ತೇವೆ! ನಿಮ್ಮ ದಿನವು ಸಂತೋಷದಾಯಕ ಕ್ಷಣಗಳೊಂದಿಗೆ ಸುರಕ್ಷಿತ ಹಾಗೂ ಸರಾಗವಾದ ಪ್ರಯಾಣಗಳಿಂದ ತುಂಬಿರಲಿ !🎂🎊🎉",
            'Chennai': "அன்புடையீர்,  உங்கள் அருமையான ஒட்டுதலைப்போல உங்களது நாளும் இனிதே அமையட்டும்! உங்கள் நாள் மகிழ்ச்சியான தருணங்களுடன் பாதுகாப்பான மற்றும் மென்மையான சவாரிகளால் நிரப்பப்படட்டும்!🎂🎊🎉",
            'Hyderabad': "ప్రియమైన, మీ డ్రైవ్‌ల లాగానే మీకు ఒక అద్భుతమైన రోజుగా ఉండాలని మేము కోరుకుంటున్నాము! మీ రోజు సంతోషకరమైన క్షణాలతో సురక్షితమైన మరియు సులభమైన రైడ్‌లతో నిండిపోనివ్వండి!🎂🎊🎉",
            'Kolkata': "প্রিয় , আপনার ড্রাইভের মতই আপনার দিন যেন অসাধারণ কাটে! আশা করি আপনার দিনটি যেন আনন্দময় মুহূর্তগুলির সাথে নিরাপদ এবং মসৃণ রাইড দিয়ে সম্পূর্ণ হয়!🎂🎊🎉",
        }

        sms_headers = {
            'Mumbai': "MoEVing कडून वाढदिवसाच्या शुभेच्छा!",
            'Gurgaon': "मोइविंग (MoEVing ) की तरफ आपको जन्मदिन की हार्दिक शुभकामनाये",
            'Delhi': "मोइविंग (MoEVing ) की तरफ आपको जन्मदिन की हार्दिक शुभकामनाये",
            'Noida': "मोइविंग (MoEVing ) की तरफ आपको जन्मदिन की हार्दिक शुभकामनाये",
            'Chandigarh': "मोइविंग (MoEVing ) की तरफ आपको जन्मदिन की हार्दिक शुभकामनाये",
            'Faridabad': "मोइविंग (MoEVing ) की तरफ आपको जन्मदिन की हार्दिक शुभकामनाये",
            'Lucknow': "मोइविंग (MoEVing ) की तरफ आपको जन्मदिन की हार्दिक शुभकामनाये",
            'Jaipur': "मोइविंग (MoEVing ) की तरफ आपको जन्मदिन की हार्दिक शुभकामनाये",
            'Ludhiana': "मोइविंग (MoEVing ) की तरफ आपको जन्मदिन की हार्दिक शुभकामनाये",
            'Patna': "मोइविंग (MoEVing ) की तरफ आपको जन्मदिन की हार्दिक शुभकामनाये",
            'Pune': "MoEVing कडून वाढदिवसाच्या शुभेच्छा!",
            'Bengaluru': "MoEVing ಕಡೆಯಿಂದ ಹುಟ್ಟಿದಹಬ್ಬದ ಶುಭಾಶಯಗಳು !",
            'Chennai': "MoEVing இடமிருந்து பிறந்தநாள் வாழ்த்துக்கள் !",
            'Hyderabad': "MoEVing నుండి పుట్టినరోజు శుభాకాంక్షలు !",
            'Kolkata': "MoEVing (মুভিং)-এর তরফ থেকে জন্মদিনের আন্তরিক শুভেচ্ছা !",
        }

        sms_language = {
            'Mumbai': "Marathi",
            'Gurgaon': "Hindi",
            'Delhi': "Hindi",
            'Noida': "Hindi",
            'Chandigarh': "Hindi",
            'Faridabad': "Hindi",
            'Lucknow': "Hindi",
            'Jaipur': "Hindi",
            'Ludhiana': "Hindi",
            'Patna': "Hindi",
            'Pune': "Marathi",
            'Bengaluru': "Kannada",
            'Chennai': "Tamil",
            'Hyderabad': "Telugu",
            'Kolkata': "Bengali",
        }

        city_sms_count = {}

        for user_id in user_ids:
            city_name = user_id[3]
            contact = user_id[1]
            user_id = user_id[0]

            if str(city_name) in sms_messages and str(city_name) in sms_headers:
                params = {
                    "notification_type": "whatsapp",
                    "user_id": user_id,
                    "mobile_number": contact,
                    "message": sms_messages[str(city_name)],
                    "title": sms_headers[str(city_name)],
                    "notification_source": "scheduler-service"
                }

                # Convert payload to JSON string
                json_payload = json.dumps(params)

                response = requests.post(url, headers=headers, data=json_payload)

                # Increment city-wise SMS count
                city_sms_count[city_name] = city_sms_count.get(city_name, 0) + 1 if response.status_code == 200 else 0

                if response.status_code == 200:
                    print(f"User ID: {user_id} - Response: {response.json()}")
                else:
                    print(f"User ID: {user_id} - Request failed with status code: {response.status_code}")

                time.sleep(1)

        # Print-city-wise SMS counts outside the loop
        for city_name, count in city_sms_count.items():
            # print(f"City: {city_name}, SMS Count: {count}")
            if count >= 1:
                bot_message = {
                    'text': f"Birthday wish message by Whatsapp Bot from MoEVing sent to {count} {city_name} Driver(s) in {sms_language[city_name]}."}

                print(bot_message['text'].replace('```', ''))

                message_headers = {'Content-Type': 'application/json; charset=UTF-8'}
                # Prod
                # url = 'https://chat.googleapis.com/v1/spaces/AAAAl5asBn0/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=x79cYsjotrl-mTOhNSD4BO2DoH-XtSbczImQSups5qA'

                # Test
                url = 'https://chat.googleapis.com/v1/spaces/AAAAQqFHSzs/messages?key=-WEfRq3CPzqKqqsHI&token=%3D'
                http_obj = Http()
                response = http_obj.request(
                    uri=url,
                    method='POST',
                    headers=message_headers,
                    body=dumps(bot_message),
                )

                conn.close()

