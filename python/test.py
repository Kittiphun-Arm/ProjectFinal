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
province1 ="บึงกาฬ"
longtitude = longti(province1)
print(longtitude)