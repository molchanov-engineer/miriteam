# -*- coding: utf-8 -*-
import telebot
from telebot import types
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import math

bot = telebot.TeleBot('6890216286:AAHztvDm1AFM4Dq0uhL3RrHJgp3qruhJ0FY')
opros=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
otv1=0
otv2=0
otv3=0
otv4=0

  


@bot.message_handler(commands=["start"])
def button(message):
    global otv1, otv2, otv3, otv4
    otv1, otv2, otv3, otv4 = 0, 0, 0, 0
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("Новости", callback_data="qst1")
    item2 = types.InlineKeyboardButton("Профориентация", callback_data="qst2")
    item3 = types.InlineKeyboardButton("Помощь абитуриентам", callback_data="qst70")
    markup.add(item1,item2,item3)
    bot.send_message(message.chat.id, "*Добро пожаловать в телеграм-бот от ПИШ* \nДанный бот создан для того, чтобы обеспечить комфорт в получении информации об отделе ПИШ в ВУЗе НГТУ. \nЗдесь предствалены такие разделы, как: \n-Профильная ориентация, где вы сможете определить какое направление, предоставленное отделом ПИШ в НГТУ, подходит вам больше всего \n-Новости, которые покажут вам новейшие события, происходящие в отделе ПИШ НГТУ \n-Помощь абитуриентам, которая предоставит информацию о нужных документах и местах подачи заявления в отдел ПИШ НГТУ, а также предоставит ссылку для регистрации на олимпиаду",parse_mode="Markdown", reply_markup=markup)
    

@bot.callback_query_handler(func=lambda call:True)
def main_callback(call):
    global otv1, otv2, otv3, otv4, divs
    if call.message:
        #помощь аб
        if call.data == "qst70":
            markup = types.InlineKeyboardMarkup(row_width=3)
            item1 = types.InlineKeyboardButton("Назад", callback_data="qst3")
            item2 = types.InlineKeyboardButton("Дальше", callback_data="qst71")
            markup.add(item1, item2)
            bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.id, text = "*НЕОБХОДИМЫЕ ДОКУМЕНТЫ:* \n1. Документ, удостоверяющий личность, гражданство. \n2. Документ об образовании (аттестат или диплом и/или копия). \n3. Страховой номер индивидуального лицевого счета (СНИЛС). \n4. Приписное свидетельство или военный билет для юношей (можно предоставить после зачисления). \n5. Медицинская справка по форме 086-У для направлений, требующих предварительного медицинского осмотра (можно предоставить после зачисления). \n6. Документы, подтверждающие право на льготы. \n7. Документы, подтверждающие индивидуальные достижения. \n8. Результаты ЕГЭ (абитуриент сообщает в заявлении). ", parse_mode="Markdown", reply_markup=markup)  
        if call.data == "qst71":
            markup = types.InlineKeyboardMarkup(row_width=3)
            item1 = types.InlineKeyboardButton("Назад", callback_data="qst70")
            item2 = types.InlineKeyboardButton("Регистрация", url='https://org.mephi.ru/register/pupil')
            markup.add(item1, item2)
            bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.id, text = "*КАК ПОДАТЬ ДОКУМЕНТЫ В НГТУ ИМ. Р.Е. АЛЕКСЕЕВА?* \nПрием документов абитуриентов, поступающих в НГТУ имени Р. Е. Алексеева, ведется с 20 июня. \n*Места приема документов:* \n1. Нижегородский государственный технический университет 603950, Нижний Новгород, ул. Минина, 28 (4 корпус НГТУ) (8(831)436-73-43) \n2. Автозаводская высшая школа управления и технологий 603083, Нижний Новгород, ул. Лескова, 68 (8(831)256-29-78). \n3. Арзамасский политехнический институт (филиал НГТУ) 607227, Арзамас, ул. Калинина, 19 (8(831)477-10-42). \n6. Дзержинский политехнический институт (филиал НГТУ) 606026, Дзержинск, ул. Гайдара, 49 (8(831)334-23-96). \n7. *Для онлайн регистрации воспользуйтесь системой Госуслуг* \n8. Подробнее на сайте https://www.nntu.ru/content/abiturientam/abiturient2024/common \n*Здесь придоставлена ссылка для регистрации на олимпиаду*", parse_mode="Markdown", reply_markup=markup)
        
        if call.data == "qst1":   

            driver = webdriver.Chrome()
            soup = BeautifulSoup(driver.page_source, "lxml")
            driver.get(f"https://www.nntu.ru/news/all/vse-novosti?tag=%23ПИШ")
            soup = BeautifulSoup(driver.page_source, "lxml")
            divs = 'https://www.nntu.ru'+soup.find('div', class_='item-title dot').find('a', class_='item-link is-popover').get('href')
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Назад", callback_data="qst3")
            item2 = types.InlineKeyboardButton("Последние новости", url = 'https://www.nntu.ru'+soup.find('div', class_='item-title dot').find('a', class_='item-link is-popover').get('href'))
            markup.add(item1, item2)
            bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.id, text = f"*Новости НГТУ.* \nЗдесь вы сможете найти самые последние новости из нашего ВУЗа.",parse_mode="Markdown", reply_markup=markup)
        if call.data == "qst2":
            markup = types.InlineKeyboardMarkup(row_width=3)
            item1 = types.InlineKeyboardButton("Назад", callback_data="qst3")
            item2 = types.InlineKeyboardButton("Пройти тестирование", callback_data="qst4")
            markup.add(item1, item2)
            bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.id, text = "Вы хотите пройти тестирование?", reply_markup=markup)
        
        if call.data == "qst3":
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Новости", callback_data="qst1")
            item2 = types.InlineKeyboardButton("Профориентация", callback_data="qst2")
            item3 = types.InlineKeyboardButton("Помощь абитуриентам", callback_data="qst70")
            markup.add(item1,item2, item3)
            bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.id, text = "*Добро пожаловать в телеграм-бот от ПИШ* \nДанный бот создан для того, чтобы обеспечить комфорт в получении информации об отделе ПИШ в ВУЗе НГТУ. \nЗдесь предствалены такие разделы, как: \n-Профильная ориентация, где вы сможете определить какое направление, предоставленное отделом ПИШ в НГТУ, подходит вам больше всего \n-Новости, которые покажут вам новейшие события, происходящие в отделе ПИШ НГТУ \n-Помощь абитуриентам, которая предоставит информацию о нужных документах и местах подачи заявления в отдел ПИШ НГТУ, а также предоставит ссылку для регистрации на олимпиаду",parse_mode="Markdown", reply_markup=markup)

        if call.data == "qst4":
            markup1 = types.InlineKeyboardMarkup(row_width=3)
            item1 = types.InlineKeyboardButton("Да", callback_data="qst5")
            item2 = types.InlineKeyboardButton("Нет", callback_data="qst6")
            markup1.add(item1, item2)
            bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.id, text = "1. Исчезает ли информация при отключении компьютера из оперативной памяти?", reply_markup=markup1)
        #ответ yes
        if call.data == "qst5":
            markup1 = types.InlineKeyboardMarkup(row_width=3)
            item1 = types.InlineKeyboardButton("Да", callback_data="qst9")
            item2 = types.InlineKeyboardButton("Нет", callback_data="qst10")
            markup1.add(item1, item2)
            bot.send_message(call.message.chat.id, text = "2. Является ли BMP наиболее распространённым расширением в имени текстовых файлов?", reply_markup=markup1)
            otv1 += 1
        if call.data == "qst9":
            markup1 = types.InlineKeyboardMarkup(row_width=3)
            item1 = types.InlineKeyboardButton("Да", callback_data="qst13")
            item2 = types.InlineKeyboardButton("Нет", callback_data="qst14")
            markup1.add(item1, item2)
            bot.send_message(call.message.chat.id, text = "3. Текстовый файл имеет расширение txt, rtf, doc?", reply_markup=markup1)
            otv1 += 0
        if call.data == "qst13":
            markup1 = types.InlineKeyboardMarkup(row_width=3)
            item1 = types.InlineKeyboardButton("Да", callback_data="qst17")
            item2 = types.InlineKeyboardButton("Нет", callback_data="qst18")
            markup1.add(item1, item2)
            bot.send_message(call.message.chat.id, text = "4. Является ли DOC\PROBA.TXT расширением, определяющим тип файла C:\DOC\PROBA.TXT", reply_markup=markup1)
            otv1 += 1
        if call.data == "qst17":
            markup1 = types.InlineKeyboardMarkup(row_width=3)
            item1 = types.InlineKeyboardButton("Да", callback_data="qst21")
            item2 = types.InlineKeyboardButton("Нет", callback_data="qst22")
            markup1.add(item1, item2)
            bot.send_message(call.message.chat.id, text = "5. Являются ли ядерная энергетика и создание атомной бомбы звенья и одной цепи?", reply_markup=markup1)
            otv1 += 0
        if call.data == "qst21":
            markup1 = types.InlineKeyboardMarkup(row_width=3)
            item1 = types.InlineKeyboardButton("Да", callback_data="qst25")
            item2 = types.InlineKeyboardButton("Нет", callback_data="qst26")
            markup1.add(item1, item2)
            bot.send_message(call.message.chat.id, text = "6. Безопасны ли реакторы на быстрых нейтронах?", reply_markup=markup1)
            otv2 += 1
        if call.data == "qst25":
            markup1 = types.InlineKeyboardMarkup(row_width=3)
            item1 = types.InlineKeyboardButton("Да", callback_data="qst29")
            item2 = types.InlineKeyboardButton("Нет", callback_data="qst30")
            markup1.add(item1, item2)
            bot.send_message(call.message.chat.id, text = "7. Ядерной реакцией называется процесс взаимодействия атомных ядер друг с другом", reply_markup=markup1)
            otv2 += 0
        if call.data == "qst29":
            markup1 = types.InlineKeyboardMarkup(row_width=3)
            item1 = types.InlineKeyboardButton("Да", callback_data="qst33")
            item2 = types.InlineKeyboardButton("Нет", callback_data="qst34")
            markup1.add(item1, item2)
            bot.send_message(call.message.chat.id, text = "8. Камера Вильсона позволяет фотографировать треки ядерных частиц в магнитном поле?", reply_markup=markup1)
            otv2 += 0
        if call.data == "qst33":
            markup1 = types.InlineKeyboardMarkup(row_width=3)
            item1 = types.InlineKeyboardButton("Да", callback_data="qst37")
            item2 = types.InlineKeyboardButton("Нет", callback_data="qst38")
            markup1.add(item1, item2)
            bot.send_message(call.message.chat.id, text = "9. Сечением ядерной реакции называется величина, характеризующая вероятность осуществления данной реакции?", reply_markup=markup1)
            otv2 += 1
        if call.data == "qst37":
            markup1 = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Да", callback_data="qst41")
            item2 = types.InlineKeyboardButton("Нет", callback_data="qst42")
            markup1.add(item1, item2)
            bot.send_message(call.message.chat.id, text = "10. Равен ли 1 ангестрему² в системе СИ 1 барн?", reply_markup=markup1)
            otv3 += 1
        if call.data == "qst41":
            markup1 = types.InlineKeyboardMarkup(row_width=3)
            item1 = types.InlineKeyboardButton("Да", callback_data="qst45")
            item2 = types.InlineKeyboardButton("Нет", callback_data="qst46")
            markup1.add(item1, item2)
            bot.send_message(call.message.chat.id, text = "11. Ядерным фотоэффектом называется процесс рассеяния гамма-квантовой на ядре?", reply_markup=markup1)
            otv3 += 0
        if call.data == "qst45":
            markup1 = types.InlineKeyboardMarkup(row_width=3)
            item1 = types.InlineKeyboardButton("Да", callback_data="qst49")
            item2 = types.InlineKeyboardButton("Нет", callback_data="qst50")
            markup1.add(item1, item2)
            bot.send_message(call.message.chat.id, text = "12. Ядерной реакцией называется процесс взаимодействия нуклонов друг с другом?", reply_markup=markup1)
            otv3 += 0
        if call.data == "qst49":
            markup1 = types.InlineKeyboardMarkup(row_width=3)
            item1 = types.InlineKeyboardButton("Да", callback_data="qst53")
            item2 = types.InlineKeyboardButton("Нет", callback_data="qst54")
            markup1.add(item1, item2)
            bot.send_message(call.message.chat.id, text = "13. Динамика изучает законы равновесия жидкости и распределения в ней давления?", reply_markup=markup1)
            otv4 += 0
        if call.data == "qst53":
            markup1 = types.InlineKeyboardMarkup(row_width=3)
            item1 = types.InlineKeyboardButton("Да", callback_data="qst57")
            item2 = types.InlineKeyboardButton("Нет", callback_data="qst58")
            markup1.add(item1, item2)
            bot.send_message(call.message.chat.id, text = "14. Даниил Бернулли - создатель гидродинамики?", reply_markup=markup1)
            otv4 += 1
        if call.data == "qst57":
            markup1 = types.InlineKeyboardMarkup(row_width=3)
            item1 = types.InlineKeyboardButton("Да", callback_data="qst61")
            item2 = types.InlineKeyboardButton("Нет", callback_data="qst62")
            markup1.add(item1, item2)
            bot.send_message(call.message.chat.id, text = "15. Уравнение Бернулли выражает собой закон сохранения механической энергии в идеальной жидкости?", reply_markup=markup1)
            otv4 += 1
        if call.data == "qst61":
            markup1 = types.InlineKeyboardMarkup(row_width=3)
            item1 = types.InlineKeyboardButton("Да", callback_data="qst63")
            item2 = types.InlineKeyboardButton("Нет", callback_data="qst64")
            markup1.add(item1, item2)
            bot.send_message(call.message.chat.id, text = "16. Давление на дне озера глубиной 5 м при атмосферном давлении, равном 100 кПа, равно 150 килопаскалям?", reply_markup=markup1)
            otv4 += 1
        if call.data == "qst63":
            markup1 = types.InlineKeyboardMarkup(row_width=1)
            item1 = types.InlineKeyboardButton("Показать результат", callback_data="qst65")
            markup1.add(item1)
            bot.send_message(call.message.chat.id, text = 'Вы прошли тестирование!', reply_markup=markup1)
            otv4 += 1
        #ответ no
        if call.data == "qst6":
            markup1 = types.InlineKeyboardMarkup(row_width=3)
            item1 = types.InlineKeyboardButton("Да", callback_data="qst9")
            item2 = types.InlineKeyboardButton("Нет", callback_data="qst10")
            markup1.add(item1, item2)
            bot.send_message(call.message.chat.id, text = "2. Является ли BMP наиболее распространённым расширением в имени текстовых файлов?", reply_markup=markup1)
            otv1 += 0
        if call.data == "qst10":
            markup1 = types.InlineKeyboardMarkup(row_width=3)
            item1 = types.InlineKeyboardButton("Да", callback_data="qst13")
            item2 = types.InlineKeyboardButton("Нет", callback_data="qst14")
            markup1.add(item1, item2)
            bot.send_message(call.message.chat.id, text = "3. Текстовый файл имеет расширение txt, rtf, doc?", reply_markup=markup1)
            otv1 += 1
        if call.data == "qst14":
            markup1 = types.InlineKeyboardMarkup(row_width=3)
            item1 = types.InlineKeyboardButton("Да", callback_data="qst17")
            item2 = types.InlineKeyboardButton("Нет", callback_data="qst18")
            markup1.add(item1, item2)
            bot.send_message(call.message.chat.id, text = "4. Является ли DOC\PROBA.TXT расширением, определяющим тип файла C:\DOC\PROBA.TXT", reply_markup=markup1)
            otv1 += 0
        if call.data == "qst18":
            markup1 = types.InlineKeyboardMarkup(row_width=3)
            item1 = types.InlineKeyboardButton("Да", callback_data="qst21")
            item2 = types.InlineKeyboardButton("Нет", callback_data="qst22")
            markup1.add(item1, item2)
            bot.send_message(call.message.chat.id, text = "5. Являются ли ядерная энергетика и создание атомной бомбы звенья и одной цепи?", reply_markup=markup1)
            otv1 += 1
        if call.data == "qst22":
            markup1 = types.InlineKeyboardMarkup(row_width=3)
            item1 = types.InlineKeyboardButton("Да", callback_data="qst25")
            item2 = types.InlineKeyboardButton("Нет", callback_data="qst26")
            markup1.add(item1, item2)
            bot.send_message(call.message.chat.id, text = "6. Безопасны ли реакторы на быстрых нейтронах? ", reply_markup=markup1)
            otv2 += 0
        if call.data == "qst26":
            markup1 = types.InlineKeyboardMarkup(row_width=3)
            item1 = types.InlineKeyboardButton("Да", callback_data="qst29")
            item2 = types.InlineKeyboardButton("Нет", callback_data="qst30")
            markup1.add(item1, item2)
            bot.send_message(call.message.chat.id, text = "7. Ядерной реакцией называется процесс взаимодействия атомных ядер друг с другом", reply_markup=markup1)
            otv2 += 1
        if call.data == "qst30":
            markup1 = types.InlineKeyboardMarkup(row_width=3)
            item1 = types.InlineKeyboardButton("Да", callback_data="qst33")
            item2 = types.InlineKeyboardButton("Нет", callback_data="qst34")
            markup1.add(item1, item2)
            bot.send_message(call.message.chat.id, text = "8. Камера Вильсона позволяет фотографировать треки ядерных частиц в магнитном поле?", reply_markup=markup1)
            otv2 += 1
        if call.data == "qst34":
            markup1 = types.InlineKeyboardMarkup(row_width=3)
            item1 = types.InlineKeyboardButton("Да", callback_data="qst37")
            item2 = types.InlineKeyboardButton("Нет", callback_data="qst38")
            markup1.add(item1, item2)
            bot.send_message(call.message.chat.id, text = "9. Сечением ядерной реакции называется величина, характеризующая вероятность осуществления данной реакции?", reply_markup=markup1)
            otv2 += 0
        if call.data == "qst38":
            markup1 = types.InlineKeyboardMarkup(row_width=3)
            item1 = types.InlineKeyboardButton("Да", callback_data="qst41")
            item2 = types.InlineKeyboardButton("Нет", callback_data="qst42")
            markup1.add(item1, item2)
            bot.send_message(call.message.chat.id, text = "10. Равен ли 1 ангестрему² в системе СИ 1 барн?", reply_markup=markup1)
            otv3 += 0
        if call.data == "qst42":
            markup1 = types.InlineKeyboardMarkup(row_width=3)
            item1 = types.InlineKeyboardButton("Да", callback_data="qst45")
            item2 = types.InlineKeyboardButton("Нет", callback_data="qst46")
            markup1.add(item1, item2)
            bot.send_message(call.message.chat.id, text = "11. Ядерным фотоэффектом называется процесс рассеяния гамма-квантовой на ядре?", reply_markup=markup1)
            otv3 += 1
        if call.data == "qst46":
            markup1 = types.InlineKeyboardMarkup(row_width=3)
            item1 = types.InlineKeyboardButton("Да", callback_data="qst49")
            item2 = types.InlineKeyboardButton("Нет", callback_data="qst50")
            markup1.add(item1, item2)
            bot.send_message(call.message.chat.id, text = "12. Ядерной реакцией называется процесс взаимодействия нуклонов друг с другом?", reply_markup=markup1)
            otv3 += 1
        if call.data == "qst50":
            markup1 = types.InlineKeyboardMarkup(row_width=3)
            item1 = types.InlineKeyboardButton("Да", callback_data="qst53")
            item2 = types.InlineKeyboardButton("Нет", callback_data="qst54")
            markup1.add(item1, item2)
            bot.send_message(call.message.chat.id, text = "13. Динамика изучает законы равновесия жидкости и распределения в ней давления?", reply_markup=markup1)
            otv3 += 1
        if call.data == "qst54":
            markup1 = types.InlineKeyboardMarkup(row_width=3)
            item1 = types.InlineKeyboardButton("Да", callback_data="qst57")
            item2 = types.InlineKeyboardButton("Нет", callback_data="qst58")
            markup1.add(item1, item2)
            bot.send_message(call.message.chat.id, text = "14. Даниил Бернулли - создатель гидродинамики?", reply_markup=markup1)
            otv4 += 0
        if call.data == "qst58":
            markup1 = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Да", callback_data="qst61")
            item2 = types.InlineKeyboardButton("Нет", callback_data="qst62")
            markup1.add(item1, item2)
            bot.send_message(call.message.chat.id, text = "15. Уравнение Бернулли выражает собой закон сохранения механической энергии в идеальной жидкости?", reply_markup=markup1)
            otv4 += 0
        if call.data == "qst62":
            markup1 = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Да", callback_data="qst63")
            item2 = types.InlineKeyboardButton("Нет", callback_data="qst64")
            markup1.add(item1, item2)
            bot.send_message(call.message.chat.id, text = "16. Давление на дне озера глубиной 5 м при атмосферном давлении, равном 100 кПа, равно 150 килопаскалям?", reply_markup=markup1)
            otv4 += 0
        if call.data == "qst64":
            markup1 = types.InlineKeyboardMarkup(row_width=1)
            item1 = types.InlineKeyboardButton("Показать результат", callback_data="qst65")
            markup1.add(item1)
            bot.send_message(call.message.chat.id, text = 'Вы прошли тестирование!', reply_markup=markup1)
            otv4 += 0

        if call.data == "qst65":
               
            otv1 = math.ceil((otv1/4)*100)
           
            otv2 = math.ceil((otv2/4)*100)
            
            otv3 = math.ceil((otv3/4)*100)
            
            otv4 = math.ceil((otv4/4)*100)
            if otv1 > otv2 and otv1 > otv3 and otv1 > otv4:
                markup1 = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton("Назад на главную", callback_data="qst66")
                markup1.add(item1)
                bot.send_message(call.message.chat.id, f"Вы прошли тест. У вас Информатика: {otv1}%, Ядерная энергетика и теплофизика: {otv2}%, Ядерная физика и технологии: {otv3}%, Вычислительная гидродинамика и теплообмен в реакторных установок: {otv4}%. \nВы больше процентов набрали по области Информатика и вычислительная техника. \nПодходящие профессии: \n1. Devops - инженер \n2. Системный инженер  \n3. Администратор баз данных \n4. Инженер - электронщик \n5. Инженер - программист  \n6. Инженер связи", reply_markup=markup1)
            if otv2 > otv1 and otv2 > otv3 and otv2 > otv4:
                markup1 = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton("Назад на главную", callback_data="qst66")
                markup1.add(item1)
                bot.send_message(call.message.chat.id, f"Вы прошли тест. У вас Информатика: {otv1}%, Ядерная энергетика и теплофизика: {otv2}%, Ядерная физика и технологии: {otv3}%, Вычислительная гидродинамика и теплообмен в реакторных установок: {otv4}%. \nВы больше процентов набрали по области Ядерная энергетика и теплофизика. \nПодходящие профессии: \n1. Инженер - ядерщик \n2. Теплотехник \n3. Физик - ядерщик \n4. Инженер - атомщик \n5. Инженер - теплофизик", reply_markup=markup1)
            if otv3 > otv2 and otv3 > otv1 and otv3 > otv4:
                markup1 = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton("Назад на главную", callback_data="qst66")
                markup1.add(item1)
                bot.send_message(call.message.chat.id, f"Вы прошли тест. У вас Информатика: {otv1}%, Ядерная энергетика и теплофизика: {otv2}%, Ядерная физика и технологии: {otv3}%, Вычислительная гидродинамика и теплообмен в реакторных установок: {otv4}%. \nВы больше процентов набрали по Ядерная физика и технологии. \nПодходящие професии: \n1. Лаборант \n2. Инженер - дозиметрист \n3. Гидроэнергетик \n4. Физик - ядерщик \n5. Программист", reply_markup=markup1)
            if otv4 > otv2 and otv4 > otv3 and otv4 > otv1:
                markup1 = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton("Назад на главную", callback_data="qst66")
                markup1.add(item1)
                bot.send_message(call.message.chat.id, f"Вы прошли тест. У вас Информатика: {otv1}%, Ядерная энергетика и теплофизика: {otv2}%, Ядерная физика и технологии: {otv3}%, Вычислительная гидродинамика и теплообмен в реакторных установок: {otv4}%. \nВы больше процентов набрали по области Гидродинамики. \nПодходящие профессии: \n1. Инженер-гидродинамик \n2. Авиастроитель \n3. Инженер-кораблестроитель \n4. Специалист по судостроению", reply_markup=markup1)
            otv1, otv2, otv3, otv4 = 0, 0, 0, 0
        if call.data == "qst66":
            markup1 = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Новости", callback_data="qst1")
            item2 = types.InlineKeyboardButton("Профориентация", callback_data="qst2")
            item3 = types.InlineKeyboardButton("Помощь абитуриентам", callback_data="qst70")
            markup1.add(item1,item2,item3)
            bot.send_message(call.message.chat.id, "*Добро пожаловать в телеграм-бот от ПИШ* \nДанный бот создан для того, чтобы обеспечить комфорт в получении информации об отделе ПИШ в ВУЗе НГТУ. \nЗдесь предствалены такие разделы, как: \n-Профильная ориентация, где вы сможете определить какое направление, предоставленное отделом ПИШ в НГТУ, подходит вам больше всего \n-Новости, которые покажут вам новейшие события, происходящие в отделе ПИШ НГТУ \n-Помощь абитуриентам, которая предоставит информацию о нужных документах и местах подачи заявления в отдел ПИШ НГТУ, а также предоставит ссылку для регистрации на олимпиаду",parse_mode="Markdown", reply_markup=markup1)
            otv1, otv2, otv3, otv4 = 0, 0, 0, 0
        
                    

bot.polling(none_stop=True, interval=0)
