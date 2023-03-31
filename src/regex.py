import re
from libs import scrape

str_list = scrape.get_all_str()

# str_list中の電話番号を正規表現で判定して、phone_numberリストに追加
phone_number = []

# 正規表現は携帯、固定電話両方対応。ハイフン含むも可。先頭番号０の国内通話に限定。
for str_item in str_list:
    m = re.search(r"0[-\d]{9,12}", str_item)
    if m:
        phone_number.append(m.group())
        
print(phone_number)