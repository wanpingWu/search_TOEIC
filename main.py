from telegram.ext import Updater, CommandHandler
import requests
from bs4 import BeautifulSoup
import time
import random

def getTOEIC(bot, update):
    while True:
        r = requests.get("https://www.examservice.com.tw/Product/ExamInfoByTestTime?storeId=&type=Toeic&testTime=202003150930") #將此頁面的HTML GET下來
        #print(r.text) #印出HTML
        soup = BeautifulSoup(r.text,"html.parser") #將網頁資料以html.parser
        sel = soup.select("div.school_checkbox input") #取HTML標中的 <div class="title"></div> 中的<a>標籤存入sel
        cnt=0
        for s in sel:
            if s["name"]!="subProductNo":     
                #if isEnable(s) :
                if s.get("disabled","False") == "False" :
                    print(s["data-address"], s.text) 
                    update.message.reply_text(s["data-address"])
                    cnt=cnt+1
        if cnt==0:
            update.message.reply_text("都額滿了QQ")
        else :
            update.message.reply_text("還有{}個地方有名額 快去報名".format(cnt))
        sleepTime = random.randint(10,30)
        update.message.reply_text("休息{}秒".format(sleepTime))
        print("sleep "+ str(sleepTime) +" sec")
        time.sleep(sleepTime)

        

updater = Updater('telegram bot')
updater.dispatcher.add_handler(CommandHandler('getTOEIC', getTOEIC))
updater.start_polling()
updater.idle()