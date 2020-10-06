from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy
from pythainlp import word_tokenize
import pymongo
import schedule
import time

name = '@arm68276728'
consumer_key = 'ZjqhkszxnNHLiyuGoqg9q9rTV'
consumer_secret = 'DEjDKOP5wvgrPzeTxAmbvSZehzxGZzFwdkZAyki70noCoEnr3k'
access_token = '842544748355186688-1xDuL3ityjUEsJYcIEKTD9lK1RovPnZ'
access_secret = 'NPfabP1b1ohKmhaO6UDyP69XoIZ3AOaqTKbPnxiHe7Oc5'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)



#Database 
monggo = pymongo.MongoClient("mongodb+srv://admin:68276728@projectdisasterrisk.wh8co.gcp.mongodb.net/DATAPROJECT?retryWrites=true&w=majority")
db = monggo.DATAPROJECT
col = db["dataDisaster"]

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

        score1 = ''
        disaster1 = ''
        province1 = ''

        countdata = 1
        for i in messages:
            proc = word_tokenize(i, engine='newmm')

            score = [s for s in proc if ('บาดเจ็บ' in s) or (
                'ตาย' in s) or ('เสียชีวิต' in s) or ('สูญหาย' in s) or ('สูญเสีย' in s) or ('เหยื่อ' in s) or ('แขนขาด' in s) or ('ขาขาด' in s) ]

            disaster = [s for s in proc if ('พายุ' in s) or ('ไฟไหม้' in s) 
            or ('ไฟป่า' in s) or ('น้ำท่วม' in s) or ('ดินถล่ม' in s) or ('แผ่นดินไหว' in s)
            or ('ภัยแล้ง' in s)or ('พายุฝนฟ้าคะนอง' in s)or ('น้ำ' in s)or ('น้ำป่า' in s) or ('ฝนตก' in s)]

            province = [s for s in proc if ('กรุงเทพมหานคร' in s) or ('กทม.' in s)or ('กรุงเทพฯ' in s)or ('เชียงใหม่' in s)
            	or ('เชียงราย' in s) or ('น่าน' in s) or ('พะเยา' in s) or ('แพร่' in s) or ('แม่ฮ่องสอน' in s)or ('ลำปาง' in s)or ('ลำพูน' in s)
            	or ('อุตรดิตถ์' in s)or ('กาฬสินธุ์ ' in s)or ('ขอนแก่น ' in s)or ('ชัยภูมิ' in s)or ('นครพนม' in s)or ('นครราชสีมา' in s)
            	or ('บึงกาฬ' in s)or ('บุรีรัมย์' in s)or ('มหาสารคาม' in s)or ('มุกดาหาร' in s)or ('ยโสธร' in s)or ('ร้อยเอ็ด ' in s)or ('เลย' in s)
            	or ('สกลนคร' in s)or ('สุรินทร์' in s)or ('ศรีสะเกษ' in s)or ('หนองคาย' in s)or ('หนองบัวลำภู' in s)
                or ('อุดรธานี' in s)or ('อุบลราชธานี' in s)or ('อำนาจเจริญ' in s)or ('กำแพงเพชร' in s)
                or ('ชัยนาท' in s)or ('นครนายก' in s)or ('นครปฐม' in s)or ('นครสวรรค์' in s)or ('นนทบุรี' in s)or ('ปทุมธานี' in s)
                or ('พระนครศรีอยุธยา' in s)or ('พิจิตร' in s)or ('พิษณุโลก' in s)or ('เพชรบูรณ์' in s)or ('ลพบุรี' in s)or ('สมุทรปราการ' in s)
                or ('สมุทรสงคราม' in s)or ('สมุทรสาคร' in s)or ('สิงห์บุรี' in s)or ('สุโขทัย' in s)or ('สุพรรณบุรี' in s)or ('สระบุรี' in s)
                or ('อ่างทอง' in s)or ('อุทัยธานี' in s)or ('จันทบุรี' in s)or ('ฉะเชิงเทรา' in s)or ('ชลบุรี' in s)or ('ตราด' in s)
                or ('ปราจีนบุรี' in s)or ('ระยอง' in s)or ('สระแก้ว' in s)or ('กาญจนบุรี' in s)or ('จังหวัดตาก' in s)or ('ประจวบคีรีขันธ์' in s)
                or ('เพชรบุรี' in s)or ('ราชบุรี' in s)or ('กระบี่' in s)or ('ชุมพร' in s)or ('ตรัง' in s)or ('นครศรีธรรมราช' in s)
                or ('นราธิวาส' in s)or ('ปัตตานี' in s)or ('พังงา' in s)or ('พัทลุง' in s)or ('ภูเก็ต' in s)or ('ระนอง' in s)
                or ('สตูล' in s)or ('สงขลา' in s)or ('สุราษฎร์ธานี' in s)or ('ยะลา' in s)]


                
            
            if len(score or disaster or province ) != 0:
                noti = status.full_text
                time = status.created_at
                retweet = status.retweet_count
                print(score)
                score1 = score[0]
                print(disaster)
                disaster1 = disaster[0]
                print(province)
                province1 = province[0]
            if(score and disaster and province or noti == score and disaster and province or noti):
                	continue;
            else:
                countdata+= 1
                # break
        if noti != '':
            break

        # f.write(f'index:{count} message:{status.full_text}')
        count += 1
    
    col.insert_one({"score":score1,"disaster":disaster1,"province":province1})
    
    print(noti)
    print(time) 
    print(retweet)
    for x in col.find():
        print(x)
    return noti, time



crawler()

# schedule.every(7).seconds.do(crawler)

# i = 0
# while True:
#     schedule.run_pending()
#     time.sleep(1)
#     i = i+1




