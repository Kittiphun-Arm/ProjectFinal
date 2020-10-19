from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy
from pythainlp import word_tokenize
import pymongo
import schedule
import time
import random
name = '' #ชื่อ Account Twitter
consumer_key = '' #คีย์ Twiter Consumer API keys
consumer_secret = '' #คีย์ Twiter Consumer API keys
access_token = ''#คีย์ Twiter Access token & access token secret
access_secret = ''#คีย์ Twiter  Access token & access token secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)



#Database 
monggo = pymongo.MongoClient("") #คีย์ MongoDB
db = monggo.DATAPROJECT #ชื่อ คลัสเตอร์
col = db["dataDisaster"] # ชื่อ collection
colsave = db["savedataDisaster"]
countla = random.uniform(0.015,0.027)
countlong = random.uniform(0.015,0.027)
myquery = { "Subtraction ": "Solo" }
datanoti = ''
def crawler():
    count = 0
    for status in tweepy.Cursor(api.user_timeline, screen_name=name, tweet_mode="extended").items():
        if count > 4:
            break
        messages = status.full_text.splitlines()
        proc = ''
        score = []
        disaster = []
        province = []
        noti = ''
        time = ''
        timete = ''

        x=[]
        severity = ''
        score1 = ''
        disaster1 = ''
        province1 = ''
        score2 = []
        disaster2 = []
        province2 = []
        countdata = 1
        for i in messages:
            proc = word_tokenize(i, engine='newmm')

            score = [s for s in proc if ('บาดเจ็บ' in s) or ('บาดเจ็บสาหัส' in s) or ('สาหัส' in s) or (
                'ตาย' in s) or ('เสียชีวิต' in s) or ('เสียหาย' in s) or ('ความเสียหาย' in s) or ('สูญหาย' in s) or ('สูญเสีย' in s) or ('เหยื่อ' in s) or ('แขนขาด' in s) or ('ขาขาด' in s) or ('พบศพ' in s)]

            disaster = [s for s in proc if ('พายุ' in s) or ('ไฟไหม้' in s) 
            or ('ไฟป่า' in s) or ('น้ำท่วม' in s) or ('ดินถล่ม' in s) or ('แผ่นดินไหว' in s)
            or ('ภัยแล้ง' in s) or ('พายุฝนฟ้าคะนอง' in s) or ('น้ำ' in s) or ('น้ำป่า' in s) or ('ฝนตก' in s) or ('สึนามิ' in s)]

            province = [s for s in proc if ('กรุงเทพมหานคร' in s) or ('กทม.' in s) or ('กรุงเทพฯ' in s) or ('เชียงใหม่' in s)
            	or ('เชียงราย' in s) or ('น่าน' in s) or ('พะเยา' in s) or ('แพร่' in s) or ('แม่ฮ่องสอน' in s) or ('ลำปาง' in s) or ('ลำพูน' in s)
            	or ('อุตรดิตถ์' in s) or ('กาฬสินธุ์ ' in s) or ('ขอนแก่น ' in s) or ('ชัยภูมิ' in s) or ('นครพนม' in s) or ('นครราชสีมา' in s)
            	or ('บึงกาฬ' in s) or ('บุรีรัมย์' in s) or ('มหาสารคาม' in s) or ('มุกดาหาร' in s) or ('ยโสธร' in s) or ('ร้อยเอ็ด ' in s) or ('เลย' in s)
            	or ('สกลนคร' in s) or ('สุรินทร์' in s) or ('ศรีสะเกษ' in s) or ('หนองคาย' in s) or ('หนองบัวลำภู' in s)
                or ('อุดรธานี' in s) or ('อุบลราชธานี' in s) or ('อำนาจเจริญ' in s) or ('กำแพงเพชร' in s)
                or ('ชัยนาท' in s) or ('นครนายก' in s) or ('นครปฐม' in s) or ('นครสวรรค์' in s) or ('นนทบุรี' in s) or ('ปทุมธานี' in s)
                or ('พระนครศรีอยุธยา' in s) or ('พิจิตร' in s) or ('พิษณุโลก' in s) or ('เพชรบูรณ์' in s) or ('ลพบุรี' in s) or ('สมุทรปราการ' in s)
                or ('สมุทรสงคราม' in s) or ('สมุทรสาคร' in s) or ('สิงห์บุรี' in s) or ('สุโขทัย' in s) or ('สุพรรณบุรี' in s) or ('สระบุรี' in s)
                or ('อ่างทอง' in s) or ('อุทัยธานี' in s) or ('จันทบุรี' in s) or ('ฉะเชิงเทรา' in s) or ('ชลบุรี' in s) or ('ตราด' in s)
                or ('ปราจีนบุรี' in s) or ('ระยอง' in s) or ('สระแก้ว' in s) or ('กาญจนบุรี' in s) or ('จังหวัดตาก' in s) or ('ประจวบคีรีขันธ์' in s)
                or ('เพชรบุรี' in s) or ('ราชบุรี' in s) or ('กระบี่' in s) or ('ชุมพร' in s) or ('ตรัง' in s) or ('นครศรีธรรมราช' in s)
                or ('นราธิวาส' in s) or ('ปัตตานี' in s) or ('พังงา' in s) or ('พัทลุง' in s) or ('ภูเก็ต' in s) or ('ระนอง' in s)
                or ('สตูล' in s) or ('สงขลา' in s) or ('สุราษฎร์ธานี' in s) or ('ยะลา' in s)]


                
            
            if len(score and disaster and province ) != 0:
                
                noti = status.full_text
                time = status.created_at
                for x in colsave.find({"time" : time}):
                    continue
                if len(x) == 0:
                        retweet = status.retweet_count
                        like = status.favorite_count
                        idpost = status.id
                        link = "https://twitter.com/"+name+"/"+"status/"+str(idpost)
                        score2 = score
                        print(score)
                        disaster2 = disaster
                        print(disaster)
                        province2 = province
                        print(province)
                        disaster1 = disaster2[0]
                        score1 = score2[0]
                        province1 = province2[0]
                        def lati(la):
                            switcher = {
                                "กรุงเทพมหานคร": 13.7278956,
                                "กทม.": 13.7278956,
                                "กรุงเทพฯ": 13.7278956,
                                "กระบี่": 8.0862997,
                                "กาญจนบุรี": 14.0227797,
                                "กาฬสินธุ์": 16.4314078,
                                "กำแพงเพชร": 16.4827798,
                                "ขอนแก่น": 16.4419355,
                                "จันทบุรี": 12.61134,
                                "ฉะเชิงเทรา": 13.6904194,
                                "ชลบุรี": 13.3611431,
                                "ชัยนาท": 15.1851971,
                                "ชัยภูมิ": 15.8068173,
                                "ชุมพร": 10.4930496,
                                "เชียงราย": 19.9071656,
                                "เชียงใหม่": 18.7877477,
                                "ตรัง": 7.5593851,
                                "ตราด": 12.2427563,
                                "ตาก": 16.8839901,
                                "นครนายก": 14.2069466,
                                "นครปฐม": 13.8199206,
                                "นครพนม": 17.392039,
                                "นครราชสีมา": 14.9798997,
                                "นครศรีธรรมราช": 8.4303975,
                                "นครสวรรค์": 15.6930072,
                                "นนทบุรี": 13.8621125,
                                "นราธิวาส": 6.4254607,
                                "น่าน": 18.7756318,
                                "บุรีรัมย์": 14.9930017,
                                "ปทุมธานี": 14.0208391,
                                "ประจวบคีรีขันธ์": 11.812367,
                                "ปราจีนบุรี": 14.0509704,
                                "ปัตตานี": 6.869484399999999,
                                "พระนครศรีอยุธยา": 14.3532128,
                                "พะเยา": 19.1664789,
                                "พังงา": 8.4407456,
                                "พัทลุง": 7.6166823,
                                "พิจิตร": 16.4429516,
                                "พิษณุโลก": 16.8298048,
                                "เพชรบุรี": 13.1111601,
                                "เพชรบูรณ์": 16.4189807,
                                "แพร่": 18.1445774,
                                "ภูเก็ต": 7.9810496,
                                "มหาสารคาม": 16.1850896,
                                "มุกดาหาร": 16.542443,
                                "แม่ฮ่องสอน": 19.2990643,
                                "ยโสธร": 15.792641,
                                "ยะลา": 6.541147,
                                "ร้อยเอ็ด": 16.0538196,
                                "ระนอง": 9.9528702,
                                "ระยอง": 12.6833115,
                                "ราชบุรี": 13.5282893,
                                "ลพบุรี": 14.7995081,
                                "ลำปาง": 18.2888404,
                                "ลำพูน": 18.5744606,
                                "เลย": 17.4860232,
                                "ศรีสะเกษ": 15.1186009,
                                "สกลนคร": 17.1545995,
                                "สงขลา": 7.1756004,
                                "สตูล": 6.6238158,
                                "สมุทรปราการ": 13.5990961,
                                "สมุทรสงคราม": 13.4098217,
                                "สมุทรสาคร": 13.5475216,
                                "สระแก้ว": 13.824038,
                                "สระบุรี": 14.5289154,
                                "สิงห์บุรี": 14.8936253,
                                "สุโขทัย": 17.0055573,
                                "สุพรรณบุรี": 14.4744892,
                                "สุราษฎร์ธานี": 9.1382389,
                                "สุรินทร์": 14.882905,
                                "หนองคาย": 17.8782803,
                                "หนองบัวลำภู": 17.2218247,
                                "อ่างทอง": 14.5896054,
                                "อำนาจเจริญ": 15.8656783,
                                "อุดรธานี": 17.4138413,
                                "อุตรดิตถ์": 17.6200886,
                                "อุทัยธานี": 15.3835001,
                                "อุบลราชธานี": 15.2286861,
                                "บึงกาฬ": 18.3609104,

                            }
                            return switcher.get(la)
                        #หน้าละติจูด 
                        def longti(long):
                            switcher = {
                                "กรุงเทพมหานคร":100.52412349999997,
                                "กระบี่":98.90628349999997,
                                "กาญจนบุรี": 99.53281149999998,
                                "กาฬสินธุ์": 103.5058755,
                                "กำแพงเพชร": 99.52266179999992,
                                "ขอนแก่น": 102.8359921,
                                "จันทบุรี":102.10385459999998,
                                "ฉะเชิงเทรา": 101.07795959999999,
                                "ชลบุรี": 100.98467170000004,
                                "ชัยนาท": 100.12512500000003,
                                "ชัยภูมิ": 102.03150270000003,
                                "ชุมพร": 99.18001989999993,
                                "เชียงราย": 99.83095500000002,
                                "เชียงใหม่": 98.99313110000003,
                                "ตรัง": 99.61100650000003,
                                "ตราด": 102.51747339999997,
                                "ตาก":  99.12584979999997,
                                "นครนายก":  101.21305110000003,
                                "นครปฐม":  100.06216760000007,
                                "นครพนม":  104.76955079999993,
                                "นครราชสีมา":  102.09776929999998,
                                "นครศรีธรรมราช": 99.96312190000003,
                                "นครสวรรค์":  100.12255949999997,
                                "นนทบุรี":  100.51435279999998,
                                "นราธิวาส": 101.82531429999995,
                                "น่าน": 100.77304170000002,
                                "บุรีรัมย์": 103.10291910000001,
                                "ปทุมธานี": 100.52502759999993,
                                "ประจวบคีรีขันธ์": 99.79732709999996,
                                "ปราจีนบุรี":  101.37274389999993,
                                "ปัตตานี":  101.25048259999994,
                                "พระนครศรีอยุธยา": 100.56895989999998,
                                "พะเยา":  99.9019419,
                                "พังงา":  98.51930319999997,
                                "พัทลุง":  100.07402309999998,
                                "พิจิตร":  100.34823289999997,
                                "พิษณุโลก":  100.26149150000003,
                                "เพชรบุรี":  99.93913069999996,
                                "เพชรบูรณ์":  101.15509259999999,
                                "แพร่":  100.14028310000003,
                                "ภูเก็ต":  98.36388239999997,
                                "มหาสารคาม":  103.30264609999995,
                                "มุกดาหาร":  104.72091509999996,
                                "แม่ฮ่องสอน":  97.96562259999996,
                                "ยโสธร":  104.14528270000005,
                                "ยะลา":  101.28039469999999,
                                "ร้อยเอ็ด":  103.65200359999994,
                                "ระนอง":  98.60846409999999,
                                "ระยอง":  101.23742949999996,
                                "ราชบุรี":  99.81342110000003,
                                "ลพบุรี":  100.65337060000002,
                                "ลำปาง":  99.49087399999996,
                                "ลำพูน":  99.0087221,
                                "เลย":  101.72230020000006,
                                "ศรีสะเกษ":  104.32200949999992,
                                "สกลนคร":  104.1348365,
                                "สงขลา":  100.61434699999995,
                                "สตูล":  100.06737440000006,
                                "สมุทรปราการ":  100.59983190000003,
                                "สมุทรสงคราม":  100.00226450000002,
                                "สมุทรสาคร":  100.27439559999993,
                                "สระแก้ว":  102.0645839,
                                "สระบุรี":  100.91014210000003,
                                "สิงห์บุรี":  100.39673140000002,
                                "สุโขทัย":  99.82637120000004,
                                "สุพรรณบุรี":  100.11771279999994,
                                "สุราษฎร์ธานี": 99.32174829999997,
                                "สุรินทร์":  103.49371070000007,
                                "หนองคาย":  102.74126380000007,
                                "หนองบัวลำภู":  102.42603680000002,
                                "อ่างทอง": 100.45505200000002,
                                "อำนาจเจริญ":  104.62577740000006,
                                "อุดรธานี": 102.78723250000007,
                                "อุตรดิตถ์":  100.09929420000003,
                                "อุทัยธานี":  100.02455269999996,
                                "อุบลราชธานี":  104.85642170000006,
                                "บึงกาฬ": 103.64644629999998,
                            }
                            return switcher.get(long)

                        def deset(de):
                              switcher = {
                                     "เสียชีวิต":"ความรุนแรงระดับ 4",
                                     "ตาย":"ความรุนแรงระดับ 4",
                                     "พบศพ":"ความรุนแรงระดับ 4",
                                     "สูญหาย":"ความรุนแรงระดับ 4",
                                     "แขนขาด":"ความรุนแรงระดับ 3",
                                     "ขาขาด":"ความรุนแรงระดับ 3",
                                     "สูญเสีย":"ความรุนแรงระดับ 3",
                                     "บาดเจ็บสาหัส":"ความรุนแรงระดับ 3",
                                     "สาหัส":"ความรุนแรงระดับ 3",
                                     "เสียหาย":"ความรุนแรงระดับ 2",
                                     "ความเสียหาย":"ความรุนแรงระดับ 2",
                                     "เหยื่อ":"ความรุนแรงระดับ 2",
                                     "บาดเจ็บ":"ความรุนแรงระดับ 1",
                              }
                              return switcher.get(de)

                        latitude = lati(province1)
                        latitude = latitude + countla
                        longtitude = longti(province1)
                        longtitude = longtitude + countlong
                        severity = deset(score1)
                        print(score1)
                        print(disaster1)
                        print(province1)
                        print(longtitude)
                        print(latitude)
                        print(severity)
                        print(noti)
                        print(time)
                        print(idpost)
                        print(link) 
                        colsave.insert_one({"disaster":disaster1,"province":province1,"score":score1,"longtitude":longtitude,"latitude":latitude,"noti":noti,"time":time,"severity":severity,"link": link })
                        col.insert_one({"disaster":disaster1,"province":province1,"score":score1,"longtitude":longtitude,"latitude":latitude,"noti":noti,"time":time,"severity":severity,"link": link ,"Subtraction ": "Solo"})
                else:
                        print("Information is not updated. Is duplicate")
                        break
            elif len(score or disaster or province) == 0:
                continue;
                print("Can't find information about the disaster")
            else:
                countdata+= 1
                print("Can't find information about the disaster")
                # break
        if noti != '':
            break

        # f.write(f'index:{count} message:{status.full_text}')
        count += 1
      
    # for x in col.find():
    #     print(x)
    # return noti, time
    
    
    
    
crawler()

def delete():
 col.delete_one(myquery)
 print("The data has been deleted.")

schedule.every(30).seconds.do(crawler)
schedule.every(65).seconds.do(delete)
i = 0
while True:
    schedule.run_pending()
    time.sleep(1)

    # random.uniform(0.005,0.007)
    i = i+1







