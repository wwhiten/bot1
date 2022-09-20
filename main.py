import requests
from bs4 import BeautifulSoup
from telebot import *

bot = TeleBot('5710637394:AAFafPMk6ICo1sJpEJKPiVFAN3ltohRunxw')
keyboard1 = types.ReplyKeyboardMarkup(True)
keyboard1.row('🎬Фильмы и сериалы', '📚Книги', '🔈Аудиокниги')
keyboard1.row('🎤Подкасты', '📝Тесты', 'ТВ-шоу')
keyboard1.row('📻Радио', '📊Статистика')
keyboard2 = types.ReplyKeyboardMarkup(True)
keyboard2.row('Недавние 50', '51-150', '151-250')
keyboard2.row('251-350', '351 и больше', 'Выйти')
keyboard_series = types.ReplyKeyboardMarkup(True)
keyboard_series.row('Выйти')
keyboard_books = types.ReplyKeyboardMarkup(True)
keyboard_books.row('Рекомендации', 'Адаптированные для начинающих', 'Классика английской литературы')
keyboard_books.row('Фэнтези', 'Фантастика', 'Любовные романы')
keyboard_books.row('Детективы и триллеры', 'Ужасы и мистика', 'Проза')
keyboard_books.row('Детские сказки и приключения', 'Нон-фикшн')
keyboard_books.row('Выйти', 'Поиск')
keyboard_search = types.ReplyKeyboardMarkup(True)
keyboard_search.row('Поиск', 'Рекомендации')
keyboard_books_level = types.ReplyKeyboardMarkup(True)
keyboard_books_level.row('A1', 'A2', 'B1')
keyboard_books_level.row('B2', 'C1', 'Выйти')
keyboard_tests = types.ReplyKeyboardMarkup(True)
keyboard_tests.row('На грамматику', 'На знание времён')
keyboard_tests.row('Неправильные глаголы', 'Для школьников')
keyboard_tests.row('Тест на уровень языка', 'Выйти')
answer_podcast = True
ctr_series = False
ctr_books = False
llink_series = []
text_series = []
links_series_w = []

url_tests_1 = f'https://puzzle-english.com/level-test/english-grammar-test'
response_tests_1 = requests.get(url_tests_1)
soup_tests_1 = BeautifulSoup(response_tests_1.text, 'lxml')
links_tests_1 = soup_tests_1.find_all(class_="col-xs-12 puzzle-col-smx-6 col-sm-3 puzzle_mb_20")
link_tests_1 = []
text_tests_1 = []
texts_tests_1 = []
for i in range(len(links_tests_1)):
    link_tests_1.append(f'https://puzzle-english.com{links_tests_1[i].find("a").get("href")}')
for i in range(len(link_tests_1)):
    url_tests1 = link_tests_1[i]
    response_tests1 = requests.get(url_tests1)
    soup_tests1 = BeautifulSoup(response_tests1.text, 'lxml')
    text_tests_1.append(soup_tests1.find_all('span'))
    if i != 0:
        texts_tests_1.append(f'{i}. {text_tests_1[i][4].text}')
string_tests_1 = '\n'.join(texts_tests_1)

url_tests_2 = f'https://puzzle-english.com/level-test/english-grammar-test'
response_tests_2 = requests.get(url_tests_2)
soup_tests_2 = BeautifulSoup(response_tests_2.text, 'lxml')
links_tests_2 = soup_tests_1.find_all(class_="col-xs-12 puzzle-col-smx-6 col-sm-3 puzzle_mb_20")
link_tests_2 = []
text_tests_2 = []
texts_tests_2 = []
for i in range(len(links_tests_2)):
    link_tests_2.append(f'https://puzzle-english.com{links_tests_1[i].find("a").get("href")}')
for i in range(len(link_tests_2)):
    url_tests2 = link_tests_2[i]
    response_tests2 = requests.get(url_tests2)
    soup_tests2 = BeautifulSoup(response_tests2.text, 'lxml')
    text_tests_2.append(soup_tests2.find_all('span'))
    if i != 0:
        texts_tests_2.append(f'{i}. {text_tests_1[i][4].text}')
string_tests_2 = '\n'.join(texts_tests_2)

url_tests_3 = f'https://puzzle-english.com/level-test/english-grammar-test'
response_tests_3 = requests.get(url_tests_3)
soup_tests_3 = BeautifulSoup(response_tests_3.text, 'lxml')
links_tests_3 = soup_tests_3.find_all(class_="col-xs-32 puzzle-col-smx-6 col-sm-3 puzzle_mb_20")
link_tests_3 = []
text_tests_3 = []
texts_tests_3 = []
for i in range(len(links_tests_3)):
    link_tests_3.append(f'https://puzzle-english.com{links_tests_3[i].find("a").get("href")}')
for i in range(len(link_tests_3)):
    url_tests3 = link_tests_3[i]
    response_tests3 = requests.get(url_tests3)
    soup_tests3 = BeautifulSoup(response_tests3.text, 'lxml')
    text_tests_3.append(soup_tests3.find_all('span'))
    if i != 0:
        texts_tests_3.append(f'{i}. {text_tests_3[i][4].text}')
string_tests_3 = '\n'.join(texts_tests_3)

url_tests_4 = f'https://puzzle-english.com/level-test/english-grammar-test'
response_tests_4 = requests.get(url_tests_4)
soup_tests_4 = BeautifulSoup(response_tests_4.text, 'lxml')
links_tests_4 = soup_tests_4.find_all(class_="col-xs-42 puzzle-col-smx-6 col-sm-4 puzzle_mb_20")
link_tests_4 = []
text_tests_4 = []
texts_tests_4 = []
for i in range(len(links_tests_4)):
    link_tests_4.append(f'https://puzzle-english.com{links_tests_4[i].find("a").get("href")}')
for i in range(len(link_tests_4)):
    url_tests4 = link_tests_4[i]
    response_tests4 = requests.get(url_tests4)
    soup_tests4 = BeautifulSoup(response_tests4.text, 'lxml')
    text_tests_4.append(soup_tests4.find_all('span'))
    if i != 0:
        texts_tests_4.append(f'{i}. {text_tests_4[i][4].text}')
string_tests_4 = '\n'.join(texts_tests_4)

# for i in range(28):
#     try:
#         url_series = f'http://lelang.su/english/series-in-english/page/{i + 1}/'
#         response_series = requests.get(url_series)
#         soup_series = BeautifulSoup(response_series.text, 'lxml')
#         links_series = soup_series.find_all("a")
#         for link_series in links_series:
#             if any(['субтитрами' in link_series.text, 'Сериалы' not in link_series.text, 'Extra English' not in link_series.text]):
#                 llink_series.append(f'{link_series.get("href")}')
#                 text_series.append(link_series.text)
#         url_series = f'http://lelang.su/english/series-in-english/page/{i + 2}/'
#     except:
#         break
# print('end')
# llink_series.append(
#     'http://lelang.su/english/video-kurs/serial-extra-english-s-russkimi-i-anglijskimi-subtitrami/')
# text_series.append('Сериал Extra English с русскими и английскими субтитрами')
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет! Если хочешь выучить английский язык - ты попал по адресу=)'
                                      '\nТут ты сможешь найти:'
                                      '\n🎬Фильмы и сериалы в оригинале с русскими и английскими субтитрами'
                                      '\n📚Книги на английском языке с переводом'
                                      '\n🔈Аудиокниги на английском'
                                      '\n🎤Подкасты'
                                      '\n📝Тесты для проверки твоего уровня английского'
                                      '\n📜Статьи на английском языке'
                                      '\n🎧Английскую музыку'
                                      '\n📊Статистику твоей работы каждый день', reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def send_text(message):
    global answer_podcast, ctr_series, ctr_books
    if answer_podcast:
        if message.text == '🎬Фильмы и сериалы' or ctr_series:
            # links_series_w = []
            # ctr_series = True
            # bot.send_message(message.chat.id, 'Введите название сериала, который хотели бы посмотреть',
            #                  reply_markup=keyboard_series)
            # def find_series(message):
            #     bot.register_next_step_handler(message, series_name)
            # def series_name(message):
            #     global ctr_series
            #     counter_series = 0
            #     if message.text == 'Выйти':
            #         bot.send_message(message.chat.id, 'Выбери функцию на клавиатуре', reply_markup=keyboard1)
            #         ctr_series = False
            #         return
            #     else:
            #         ctr_message_series = 0
            #         for i in range(len(text_series)):
            #             if message.text in text_series[i]:
            #                 x_series = True
            #                 counter_series += 1
            #                 n = text_series[i]
            #                 if any(['1' in n, '2' in n, '3' in n, '4' in n, '5' in n, '6' in n, '7' in n, '8' in n,
            #                         '9' in n]):
            #                     links_series_w.append(llink_series[i])
            #                     if i == len(text_series)-1:
            #                         if ctr_message_series == 0:
            #                             bot.send_message(message.chat.id, 'Выберите сезон сериала (пишите только цифру!!!)')
            #                         def react_series(message):
            #                             bot.register_next_step_handler(message, react_series_f)
            #                         def react_series_f(message):
            #                             for j in range(len(links_series_w)):
            #                                 if message.text in links_series_w[j]:
            #                                     bot.send_message(message.chat.id, llink_series[j])
            #                         react_series(message)
            #                         ctr_message_series += 1
            #                         def number_series(message):
            #                             bot.register_next_step_handler(message, number_series_f)
            #                         def number_series_f(message):
            #                             for i in range(len(text_series)):
            #                                 if message.text in text_series[i] and x_series:
            #                                     bot.send_message(message.chat.id, llink_series[i])
            #                                     bot.send_message(message.chat.id,
            #                                                      'Перейдя по этой ссылке, можно посмотреть сериал=)'
            #                                                      'Выберите новый сериал или нажмите кнопку "Выйти"',
            #                                                     reply_markup=keyboard_series)
            #                                     return
            #                         number_series(message)
            #                 else:
            #                     bot.send_message(message.chat.id, llink_series[i])
            #                     bot.send_message(message.chat.id,
            #                         'Перейдя по этой ссылке, можно посмотреть сериал=)'
            #                         'Выберите новый сериал или нажмите кнопку "Выйти"'
            #                         '\nА ещё напишите что-нибудь рандомное в следующем сообщении, а то бот не сработает',
            #                                      reply_markup=keyboard_series)
            #                     return
            #             elif i == len(text_series)-1 and not message.text in text_series[i]:
            #                 if counter_series == 0:
            #                     bot.send_message(message.chat.id, 'Не удалось найти такой сериал=('
            #                         '\nПопробуйте написать ключевое слово в названии сериала или найдите новый!'
            #                         '\nА ещё напишите что-нибудь рандомное в следующем сообщении, а то бот не сработает',
            #                             reply_markup=keyboard_series)
            #                     return
            # find_series(message)
            pass
        elif message.text == '📚Книги' or ctr_books:
            ctr_books = True
            texts_books = []
            if message.text == '📚Книги':
                bot.send_message(message.chat.id, 'Выберите жанр книги из предложенных или найдите свою!)',
                                 reply_markup=keyboard_books)

                def def_books(message):
                    bot.register_next_step_handler(message, def_books_1)

                def def_books_1(message):
                    if message.text == 'Выйти':
                        bot.send_message(message.chat.id, 'Выберите фунцию на клавиатуре', reply_markup=keyboard1)
                        ctr_books = False
                        return
                    elif message.text == 'Адаптированные для начинающих':
                        bot.send_message(message.chat.id, 'Выберите свой уровень английского на клавиатуре)'
                                                          '\nЕсли затрудняетесь ответить, всегда можно пройти тест на знание языка во вкладке "Тесты"!',
                                         reply_markup=keyboard_books_level)

                        def step2_books(message):
                            bot.register_next_step_handler(message, next2_step_books)

                        def next2_step_books(message):
                            if message.text == 'A1':
                                bot.send_message(message.chat.id, 'и тут всё работает...')
                                llink_books_A1 = []
                                texts_books_A1 = []
                                level_books_A1 = []
                                btext_books_A1 = []
                                url_books_adapted = f'https://2books.su/tags/adapted/'
                                response_books_A1 = requests.get(url_books_adapted)
                                soup_books_A1 = BeautifulSoup(response_books_A1.text, 'lxml')
                                links_books_A1 = soup_books_A1.find_all(class_="book-item")
                                for i in range(len(links_books_A1) - 7):
                                    llink_books_A1.append(
                                        f'https://2books.su/{links_books_A1[i + 2].find("a").get("href")}')
                                    text_A1 = links_books_A1[i + 2].find("p").text
                                    texts_books_A1.append(text_A1)
                                    if "A1" in text_A1:
                                        level_books_A1.append(links_books_A1[i + 2].find("p").text)
                                        btext_books_A1.append((f'{i + 1}. {text_A1[:len(text_A1) - 24]}'))
                                string_books_A1 = "\n".join(btext_books_A1)
                                bot.send_message(message.chat.id, string_books_A1)
                                bot.send_message(message.chat.id, 'Выберите номер книги, которую хотите почитать!',
                                                 reply_markup=keyboard_series)

                                def nextstep_books_A1(message):
                                    bot.register_next_step_handler(message, step_books_A1)

                                def step_books_A1(message):
                                    try:
                                        bot.send_message(message.chat.id, llink_books_A1[int(message.text) - 1])
                                        bot.send_message('Выберите другую книгу или нажмите "Выйти"')
                                        def_books(message)
                                    except:
                                        if message.text == 'Выйти':
                                            bot.send_message(message.chat.id, 'Выбери функцию на клавиатуре',
                                                             reply_markup=keyboard_books)
                                            def_books(message)
                                        else:
                                            reply_markup = keyboard_books
                                            def_books(message)

                                nextstep_books_A1(message)
                            elif message.text == 'A2':
                                bot.send_message(message.chat.id, 'и тут всё работает...')
                                llink_books_A2 = []
                                texts_books_A2 = []
                                level_books_A2 = []
                                btext_books_A2 = []
                                url_books_adapted = f'https://2books.su/tags/adapted/'
                                response_books_A2 = requests.get(url_books_adapted)
                                soup_books_A2 = BeautifulSoup(response_books_A2.text, 'lxml')
                                links_books_A2 = soup_books_A2.find_all(class_="book-item")
                                for i in range(len(links_books_A2) - 7):
                                    llink_books_A2.append(
                                        f'https://2books.su/{links_books_A2[i + 2].find("a").get("href")}')
                                    text_A2 = links_books_A2[i + 2].find("p").text
                                    texts_books_A2.append(text_A2)
                                    if "A2" in text_A2:
                                        level_books_A2.append(links_books_A2[i + 2].find("p").text)
                                        btext_books_A2.append((f'{i - 20}. {text_A2[:len(text_A2) - 24]}'))
                                string_books_A2 = "\n".join(btext_books_A2)
                                bot.send_message(message.chat.id, string_books_A2)
                                bot.send_message(message.chat.id, 'Выберите номер книги, которую хотите почитать!')

                                def nextstep_books_A2(message):
                                    bot.register_next_step_handler(message, step_books_A2)

                                def step_books_A2(message):
                                    try:
                                        bot.send_message(message.chat.id, llink_books_A2[int(message.text) + 20])
                                        bot.send_message('Выберите другую книгу или нажмите "Выйти"',
                                                         reply_markup=keyboard_books)
                                        def_books(message)
                                    except:
                                        if message.text == 'Выйти':
                                            bot.send_message(message.chat.id, 'Выбери функцию на клавиатуре',
                                                             reply_markup=keyboard_books)
                                            def_books(message)
                                        else:
                                            reply_markup = keyboard_books
                                            def_books(message)

                                nextstep_books_A2(message)
                            elif message.text == 'B2':
                                bot.send_message(message.chat.id, 'и тут всё работает...')
                                llink_books_B2 = []
                                texts_books_B2 = []
                                level_books_B2 = []
                                btext_books_B2 = []
                                url_books_adapted = f'https://2books.su/tags/adapted/'
                                response_books_B2 = requests.get(url_books_adapted)
                                soup_books_B2 = BeautifulSoup(response_books_B2.text, 'lxml')
                                links_books_B2 = soup_books_B2.find_all(class_="book-item")
                                for i in range(len(links_books_B2) - 2):
                                    llink_books_B2.append(
                                        f'https://2books.su/{links_books_B2[i + 2].find("a").get("href")}')
                                    text_B2 = links_books_B2[i + 2].find("p").text
                                    texts_books_B2.append(text_B2)
                                    if "B2" in text_B2:
                                        level_books_B2.append(links_books_B2[i + 2].find("p").text)
                                        btext_books_B2.append((f'{i - 85}. {text_B2[:len(text_B2) - 22]}'))
                                string_books_B2 = "\n".join(btext_books_B2)
                                bot.send_message(message.chat.id, string_books_B2)
                                bot.send_message(message.chat.id, 'Выберите номер книги, которую хотите почитать!')

                                def nextstep_books_B2(message):
                                    bot.register_next_step_handler(message, step_books_B2)

                                def step_books_B2(message):
                                    try:
                                        bot.send_message(message.chat.id, llink_books_B2[int(message.text) + 85])
                                        bot.send_message('Выберите другую книгу или нажмите "Выйти"',
                                                         reply_markup=keyboard_books)
                                        def_books(message)
                                    except:
                                        if message.text == 'Выйти':
                                            bot.send_message(message.chat.id, 'Выбери функцию на клавиатуре',
                                                             reply_markup=keyboard_books)
                                            def_books(message)
                                        else:
                                            reply_markup = keyboard_books
                                            def_books(message)

                                nextstep_books_B2(message)
                            elif message.text == 'B1':
                                bot.send_message(message.chat.id, 'и тут всё работает...')
                                llink_books_B1 = []
                                texts_books_B1 = []
                                level_books_B1 = []
                                btext_books_B1 = []
                                url_books_adapted = f'https://2books.su/tags/adapted/'
                                response_books_B1 = requests.get(url_books_adapted)
                                soup_books_B1 = BeautifulSoup(response_books_B1.text, 'lxml')
                                links_books_B1 = soup_books_B1.find_all(class_="book-item")
                                for i in range(len(links_books_B1) - 2):
                                    llink_books_B1.append(
                                        f'https://2books.su/{links_books_B1[i + 2].find("a").get("href")}')
                                    text_B1 = links_books_B1[i + 2].find("p").text
                                    texts_books_B1.append(text_B1)
                                    if "B1" in text_B1:
                                        level_books_B1.append(links_books_B1[i + 2].find("p").text)
                                        btext_books_B1.append((f'{i - 50}. {text_B1[:len(text_B1) - 22]}'))
                                string_books_B1 = "\n".join(btext_books_B1)
                                bot.send_message(message.chat.id, string_books_B1)
                                bot.send_message(message.chat.id, 'Выберите номер книги, которую хотите почитать!')

                                def nextstep_books_B1(message):
                                    bot.register_next_step_handler(message, step_books_B1)

                                def step_books_B1(message):
                                    try:
                                        bot.send_message(message.chat.id, llink_books_B1[int(message.text) + 50])
                                        bot.send_message('Выберите другую книгу или нажмите "Выйти"',
                                                         reply_markup=keyboard_books)
                                        def_books(message)
                                    except:
                                        if message.text == 'Выйти':
                                            bot.send_message(message.chat.id, 'Выбери функцию на клавиатуре',
                                                             reply_markup=keyboard_books)
                                            def_books(message)
                                        else:
                                            reply_markup = keyboard_books
                                            def_books(message)

                                nextstep_books_B1(message)
                            elif message.text == 'C1':
                                bot.send_message(message.chat.id, 'и тут всё работает...')
                                llink_books_C1 = []
                                texts_books_C1 = []
                                level_books_C1 = []
                                btext_books_C1 = []
                                url_books_adapted = f'https://2books.su/tags/adapted/'
                                response_books_C1 = requests.get(url_books_adapted)
                                soup_books_C1 = BeautifulSoup(response_books_C1.text, 'lxml')
                                links_books_C1 = soup_books_C1.find_all(class_="book-item")
                                for i in range(len(links_books_C1) - 2):
                                    llink_books_C1.append(
                                        f'https://2books.su/{links_books_C1[i + 2].find("a").get("href")}')
                                    text_C1 = links_books_C1[i + 2].find("p").text
                                    texts_books_C1.append(text_C1)
                                    if "C1" in text_C1:
                                        level_books_C1.append(links_books_C1[i + 2].find("p").text)
                                        btext_books_C1.append((f'{i - 109}. {text_C1[:len(text_C1) - 22]}'))
                                string_books_C1 = "\n".join(btext_books_C1)
                                bot.send_message(message.chat.id, string_books_C1)
                                bot.send_message(message.chat.id, 'Выберите номер книги, которую хотите почитать!')

                                def nextstep_books_C1(message):
                                    bot.register_next_step_handler(message, step_books_C1)

                                def step_books_C1(message):
                                    try:
                                        bot.send_message(message.chat.id, llink_books_C1[int(message.text) + 109])
                                        bot.send_message('Выберите другую книгу или нажмите "Выйти"',
                                                         reply_markup=keyboard_books)
                                        def_books(message)
                                    except:
                                        if message.text == 'Выйти':
                                            bot.send_message(message.chat.id, 'Выбери функцию на клавиатуре',
                                                             reply_markup=keyboard_books)
                                            def_books(message)
                                        else:
                                            reply_markup = keyboard_books
                                            def_books(message)

                                nextstep_books_C1(message)
                            elif message.text == 'Выйти':
                                bot.send_message(message.chat.id, 'Выбери функцию на клавиатуре',
                                                 reply_markup=keyboard_books)
                                def_books(message)

                        step2_books(message)
                    elif message.text == 'Классика английской литературы':
                        topics_books_classic = []
                        url_books_classic = f'https://2books.su/tags/classics/'
                        response_books_classic = requests.get(url_books_classic)
                        soup_books_classic = BeautifulSoup(response_books_classic.text, 'lxml')
                        texts_books_classic = soup_books_classic.find_all('h2')
                        smth_books_classic = soup_books_classic.find_all(class_="book-list book-list-wide")
                        smthbooks_classic = []
                        for i in range(len(smth_books_classic)):
                            smthbooks_classic.append(smth_books_classic[i].find_all(class_="book-item"))
                        for j in range(len(texts_books_classic)):
                            topics_books_classic.append(f'{j + 1}. {texts_books_classic[j].text}')
                        string_books_classic = "\n".join(topics_books_classic)
                        bot.send_message(message.chat.id, string_books_classic)
                        bot.send_message(message.chat.id, 'Выберите цифру серии, которую хотели бы прочесть',
                                         reply_markup=keyboard_series)

                        def step_books_classic(message):
                            bot.register_next_step_handler(message, stepbooks_classic)

                        def stepbooks_classic(message):
                            texts_books_classic = []
                            llink_books_classic = []
                            try:
                                for j in range(len(smthbooks_classic[int(message.text) - 1])):
                                    texts_books_classic.append(
                                        f'{j + 1}. {smthbooks_classic[int(message.text) - 1][j].find("p").text}')
                                    llink_books_classic.append(
                                        f"https://2books.su{smthbooks_classic[int(message.text) - 1][j].find('a').get('href')}")
                                stringbooks_classic = '\n'.join(texts_books_classic)
                                bot.send_message(message.chat.id, stringbooks_classic)
                                bot.send_message(message.chat.id, 'Выберите цифру книги, которую хотите прочесть',
                                                 reply_markup=keyboard_series)

                                def nextstep_books_classic(message):
                                    bot.register_next_step_handler(message, nextstepbooks_classic)

                                def nextstepbooks_classic(message):
                                    try:
                                        bot.send_message(message.chat.id, llink_books_classic[int(message.text) - 1],
                                                         reply_markup=keyboard_books)
                                        def_books(message)
                                    except:
                                        if message.text == 'Выйти':
                                            reply_markup = keyboard_books
                                            def_books(message)
                                        else:
                                            nextstep_books_classic(message)

                                nextstep_books_classic(message)
                            except:
                                if message.text == 'Выйти':
                                    reply_markup = keyboard_books
                                    def_books(message)
                                else:
                                    bot.send_message(message.chat.id, 'Введите только цифру!')
                                    step_books_classic(message)

                        step_books_classic(message)
                    elif message.text == 'Фэнтези':
                        topics_books_fantasy = []
                        url_books_fantasy = f'https://2books.su/tags/fantasy/'
                        response_books_fantasy = requests.get(url_books_fantasy)
                        soup_books_fantasy = BeautifulSoup(response_books_fantasy.text, 'lxml')
                        texts_books_fantasy = soup_books_fantasy.find_all('h2')
                        smth_books_fantasy = soup_books_fantasy.find_all(class_="book-list book-list-wide")
                        smthbooks_fantasy = []
                        for i in range(len(smth_books_fantasy)):
                            smthbooks_fantasy.append(smth_books_fantasy[i].find_all(class_="book-item"))
                        for j in range(len(texts_books_fantasy)):
                            topics_books_fantasy.append(f'{j + 1}. {texts_books_fantasy[j].text}')
                        string_books_fantasy = "\n".join(topics_books_fantasy)
                        bot.send_message(message.chat.id, string_books_fantasy)
                        bot.send_message(message.chat.id, 'Выберите цифру серии, которую хотели бы прочесть',
                                         reply_markup=keyboard_series)

                        def step_books_fantasy(message):
                            bot.register_next_step_handler(message, stepbooks_fantasy)

                        def stepbooks_fantasy(message):
                            texts_books_fantasy = []
                            llink_books_fantasy = []
                            try:
                                for j in range(len(smthbooks_fantasy[int(message.text) - 1])):
                                    texts_books_fantasy.append(
                                        f'{j + 1}. {smthbooks_fantasy[int(message.text) - 1][j].find("p").text}')
                                    llink_books_fantasy.append(
                                        f"https://2books.su{smthbooks_fantasy[int(message.text) - 1][j].find('a').get('href')}")
                                stringbooks_fantasy = '\n'.join(texts_books_fantasy)
                                bot.send_message(message.chat.id, stringbooks_fantasy)
                                bot.send_message(message.chat.id, 'Выберите цифру книги, которую хотите прочесть',
                                                 reply_markup=keyboard_series)

                                def nextstep_books_fantasy(message):
                                    bot.register_next_step_handler(message, nextstepbooks_fantasy)

                                def nextstepbooks_fantasy(message):
                                    try:
                                        bot.send_message(message.chat.id, llink_books_fantasy[int(message.text) - 1],
                                                         reply_markup=keyboard_books)
                                        def_books(message)
                                    except:
                                        if message.text == 'Выйти':
                                            reply_markup = keyboard_books
                                            def_books(message)
                                        else:
                                            nextstep_books_fantasy(message)

                                nextstep_books_fantasy(message)
                            except:
                                if message.text == 'Выйти':
                                    reply_markup = keyboard_books
                                    def_books(message)
                                else:
                                    bot.send_message(message.chat.id, 'Введите только цифру!')
                                    step_books_fantasy(message)

                        step_books_fantasy(message)
                    elif message.text == 'Фантастика':
                        topics_books_fantastic = []
                        url_books_fantastic = f'https://2books.su/tags/science-fiction/'
                        response_books_fantastic = requests.get(url_books_fantastic)
                        soup_books_fantastic = BeautifulSoup(response_books_fantastic.text, 'lxml')
                        texts_books_fantastic = soup_books_fantastic.find_all('h2')
                        smth_books_fantastic = soup_books_fantastic.find_all(class_="book-list book-list-wide")
                        smthbooks_fantastic = []
                        for i in range(len(smth_books_fantastic)):
                            smthbooks_fantastic.append(smth_books_fantastic[i].find_all(class_="book-item"))
                        for j in range(len(texts_books_fantastic)):
                            topics_books_fantastic.append(f'{j + 1}. {texts_books_fantastic[j].text}')
                        string_books_fantastic = "\n".join(topics_books_fantastic)
                        bot.send_message(message.chat.id, string_books_fantastic)
                        bot.send_message(message.chat.id, 'Выберите цифру серии, которую хотели бы прочесть',
                                         reply_markup=keyboard_series)

                        def step_books_fantastic(message):
                            bot.register_next_step_handler(message, stepbooks_fantastic)

                        def stepbooks_fantastic(message):
                            texts_books_fantastic = []
                            llink_books_fantastic = []
                            try:
                                for j in range(len(smthbooks_fantastic[int(message.text) - 1])):
                                    texts_books_fantastic.append(
                                        f'{j + 1}. {smthbooks_fantastic[int(message.text) - 1][j].find("p").text}')
                                    llink_books_fantastic.append(
                                        f"https://2books.su{smthbooks_fantastic[int(message.text) - 1][j].find('a').get('href')}")
                                stringbooks_fantastic = '\n'.join(texts_books_fantastic)
                                bot.send_message(message.chat.id, stringbooks_fantastic)
                                bot.send_message(message.chat.id, 'Выберите цифру книги, которую хотите прочесть',
                                                 reply_markup=keyboard_series)

                                def nextstep_books_fantastic(message):
                                    bot.register_next_step_handler(message, nextstepbooks_fantastic)

                                def nextstepbooks_fantastic(message):
                                    try:
                                        bot.send_message(message.chat.id, llink_books_fantastic[int(message.text) - 1],
                                                         reply_markup=keyboard_books)
                                        def_books(message)
                                    except:
                                        if message.text == 'Выйти':
                                            reply_markup = keyboard_books
                                            def_books(message)
                                        else:
                                            nextstep_books_fantastic(message)

                                nextstep_books_fantastic(message)
                            except:
                                if message.text == 'Выйти':
                                    reply_markup = keyboard_books
                                    def_books(message)
                                else:
                                    bot.send_message(message.chat.id, 'Введите только цифру!')
                                    step_books_fantastic(message)

                        step_books_fantastic(message)
                    elif message.text == 'Любовные романы':
                        topics_books_romance = []
                        url_books_romance = f'https://2books.su/tags/romance/'
                        response_books_romance = requests.get(url_books_romance)
                        soup_books_romance = BeautifulSoup(response_books_romance.text, 'lxml')
                        texts_books_romance = soup_books_romance.find_all('h2')
                        smth_books_romance = soup_books_romance.find_all(class_="book-list book-list-wide")
                        smthbooks_romance = []
                        for i in range(len(smth_books_romance)):
                            smthbooks_romance.append(smth_books_romance[i].find_all(class_="book-item"))
                        for j in range(len(texts_books_romance)):
                            topics_books_romance.append(f'{j + 1}. {texts_books_romance[j].text}')
                        string_books_romance = "\n".join(topics_books_romance)
                        bot.send_message(message.chat.id, string_books_romance)
                        bot.send_message(message.chat.id, 'Выберите цифру серии, которую хотели бы прочесть',
                                         reply_markup=keyboard_series)

                        def step_books_romance(message):
                            bot.register_next_step_handler(message, stepbooks_romance)

                        def stepbooks_romance(message):
                            texts_books_romance = []
                            llink_books_romance = []
                            try:
                                for j in range(len(smthbooks_romance[int(message.text) - 1])):
                                    texts_books_romance.append(
                                        f'{j + 1}. {smthbooks_romance[int(message.text) - 1][j].find("p").text}')
                                    llink_books_romance.append(
                                        f"https://2books.su{smthbooks_romance[int(message.text) - 1][j].find('a').get('href')}")
                                stringbooks_romance = '\n'.join(texts_books_romance)
                                bot.send_message(message.chat.id, stringbooks_romance)
                                bot.send_message(message.chat.id, 'Выберите цифру книги, которую хотите прочесть',
                                                 reply_markup=keyboard_series)

                                def nextstep_books_romance(message):
                                    bot.register_next_step_handler(message, nextstepbooks_romance)

                                def nextstepbooks_romance(message):
                                    try:
                                        bot.send_message(message.chat.id, llink_books_romance[int(message.text) - 1],
                                                         reply_markup=keyboard_books)
                                        def_books(message)
                                    except:
                                        if message.text == 'Выйти':
                                            reply_markup = keyboard_books
                                            def_books(message)
                                        else:
                                            nextstep_books_romance(message)

                                nextstep_books_romance(message)
                            except:
                                if message.text == 'Выйти':
                                    reply_markup = keyboard_books
                                    def_books(message)
                                else:
                                    bot.send_message(message.chat.id, 'Введите только цифру!')
                                    step_books_romance(message)

                        step_books_romance(message)

                    elif message.text == 'Детективы и триллеры':
                        topics_books_detective = []
                        url_books_detective = f'https://2books.su/tags/detective/'
                        response_books_detective = requests.get(url_books_detective)
                        soup_books_detective = BeautifulSoup(response_books_detective.text, 'lxml')
                        texts_books_detective = soup_books_detective.find_all('h2')
                        smth_books_detective = soup_books_detective.find_all(class_="book-list book-list-wide")
                        smthbooks_detective = []
                        for i in range(len(smth_books_detective)):
                            smthbooks_detective.append(smth_books_detective[i].find_all(class_="book-item"))
                        for j in range(len(texts_books_detective)):
                            topics_books_detective.append(f'{j + 1}. {texts_books_detective[j].text}')
                        string_books_detective = "\n".join(topics_books_detective)
                        bot.send_message(message.chat.id, string_books_detective)
                        bot.send_message(message.chat.id, 'Выберите цифру серии, которую хотели бы прочесть',
                                         reply_markup=keyboard_series)

                        def step_books_detective(message):
                            bot.register_next_step_handler(message, stepbooks_detective)

                        def stepbooks_detective(message):
                            texts_books_detective = []
                            llink_books_detective = []
                            try:
                                for j in range(len(smthbooks_detective[int(message.text) - 1])):
                                    texts_books_detective.append(
                                        f'{j + 1}. {smthbooks_detective[int(message.text) - 1][j].find("p").text}')
                                    llink_books_detective.append(
                                        f"https://2books.su{smthbooks_detective[int(message.text) - 1][j].find('a').get('href')}")
                                stringbooks_detective = '\n'.join(texts_books_detective)
                                bot.send_message(message.chat.id, stringbooks_detective)
                                bot.send_message(message.chat.id, 'Выберите цифру книги, которую хотите прочесть',
                                                 reply_markup=keyboard_series)

                                def nextstep_books_detective(message):
                                    bot.register_next_step_handler(message, nextstepbooks_detective)

                                def nextstepbooks_detective(message):
                                    try:
                                        bot.send_message(message.chat.id, llink_books_detective[int(message.text) - 1],
                                                         reply_markup=keyboard_books)
                                        def_books(message)
                                    except:
                                        if message.text == 'Выйти':
                                            reply_markup = keyboard_books
                                            def_books(message)
                                        else:
                                            nextstep_books_detective(message)

                                nextstep_books_detective(message)
                            except:
                                if message.text == 'Выйти':
                                    reply_markup = keyboard_books
                                    def_books(message)
                                else:
                                    bot.send_message(message.chat.id, 'Введите только цифру!')
                                    step_books_detective(message)

                        step_books_detective(message)

                    elif message.text == 'Ужасы и мистика':
                        topics_books_horror = []
                        url_books_horror = f'https://2books.su/tags/horror/'
                        response_books_horror = requests.get(url_books_horror)
                        soup_books_horror = BeautifulSoup(response_books_horror.text, 'lxml')
                        texts_books_horror = soup_books_horror.find_all('h2')
                        smth_books_horror = soup_books_horror.find_all(class_="book-list book-list-wide")
                        smthbooks_horror = []
                        for i in range(len(smth_books_horror)):
                            smthbooks_horror.append(smth_books_horror[i].find_all(class_="book-item"))
                        for j in range(len(texts_books_horror)):
                            topics_books_horror.append(f'{j + 1}. {texts_books_horror[j].text}')
                        string_books_horror = "\n".join(topics_books_horror)
                        bot.send_message(message.chat.id, string_books_horror)
                        bot.send_message(message.chat.id, 'Выберите цифру серии, которую хотели бы прочесть',
                                         reply_markup=keyboard_series)

                        def step_books_horror(message):
                            bot.register_next_step_handler(message, stepbooks_horror)

                        def stepbooks_horror(message):
                            texts_books_horror = []
                            llink_books_horror = []
                            try:
                                for j in range(len(smthbooks_horror[int(message.text) - 1])):
                                    texts_books_horror.append(
                                        f'{j + 1}. {smthbooks_horror[int(message.text) - 1][j].find("p").text}')
                                    llink_books_horror.append(
                                        f"https://2books.su{smthbooks_horror[int(message.text) - 1][j].find('a').get('href')}")
                                stringbooks_horror = '\n'.join(texts_books_horror)
                                bot.send_message(message.chat.id, stringbooks_horror)
                                bot.send_message(message.chat.id, 'Выберите цифру книги, которую хотите прочесть',
                                                 reply_markup=keyboard_series)

                                def nextstep_books_horror(message):
                                    bot.register_next_step_handler(message, nextstepbooks_horror)

                                def nextstepbooks_horror(message):
                                    try:
                                        bot.send_message(message.chat.id, llink_books_horror[int(message.text) - 1],
                                                         reply_markup=keyboard_books)
                                        def_books(message)
                                    except:
                                        if message.text == 'Выйти':
                                            reply_markup = keyboard_books
                                            def_books(message)
                                        else:
                                            nextstep_books_horror(message)

                                nextstep_books_horror(message)
                            except:
                                if message.text == 'Выйти':
                                    reply_markup = keyboard_books
                                    def_books(message)
                                else:
                                    bot.send_message(message.chat.id, 'Введите только цифру!')
                                    step_books_horror(message)

                        step_books_horror(message)

                    elif message.text == 'Проза':
                        topics_books_fiction = []
                        url_books_fiction = f'https://2books.su/tags/fiction/'
                        response_books_fiction = requests.get(url_books_fiction)
                        soup_books_fiction = BeautifulSoup(response_books_fiction.text, 'lxml')
                        texts_books_fiction = soup_books_fiction.find_all('h2')
                        smth_books_fiction = soup_books_fiction.find_all(class_="book-list book-list-wide")
                        smthbooks_fiction = []
                        for i in range(len(smth_books_fiction)):
                            smthbooks_fiction.append(smth_books_fiction[i].find_all(class_="book-item"))
                        for j in range(len(texts_books_fiction)):
                            topics_books_fiction.append(f'{j + 1}. {texts_books_fiction[j].text}')
                        string_books_fiction = "\n".join(topics_books_fiction)
                        bot.send_message(message.chat.id, string_books_fiction)
                        bot.send_message(message.chat.id, 'Выберите цифру серии, которую хотели бы прочесть',
                                         reply_markup=keyboard_series)

                        def step_books_fiction(message):
                            bot.register_next_step_handler(message, stepbooks_fiction)

                        def stepbooks_fiction(message):
                            texts_books_fiction = []
                            llink_books_fiction = []
                            try:
                                for j in range(len(smthbooks_fiction[int(message.text) - 1])):
                                    texts_books_fiction.append(
                                        f'{j + 1}. {smthbooks_fiction[int(message.text) - 1][j].find("p").text}')
                                    llink_books_fiction.append(
                                        f"https://2books.su{smthbooks_fiction[int(message.text) - 1][j].find('a').get('href')}")
                                stringbooks_fiction = '\n'.join(texts_books_fiction)
                                bot.send_message(message.chat.id, stringbooks_fiction)
                                bot.send_message(message.chat.id, 'Выберите цифру книги, которую хотите прочесть',
                                                 reply_markup=keyboard_series)

                                def nextstep_books_fiction(message):
                                    bot.register_next_step_handler(message, nextstepbooks_fiction)

                                def nextstepbooks_fiction(message):
                                    try:
                                        bot.send_message(message.chat.id, llink_books_fiction[int(message.text) - 1],
                                                         reply_markup=keyboard_books)
                                        def_books(message)
                                    except:
                                        if message.text == 'Выйти':
                                            reply_markup = keyboard_books
                                            def_books(message)
                                        else:
                                            nextstep_books_fiction(message)

                                nextstep_books_fiction(message)
                            except:
                                if message.text == 'Выйти':
                                    reply_markup = keyboard_books
                                    def_books(message)
                                else:
                                    bot.send_message(message.chat.id, 'Введите только цифру!')
                                    step_books_fiction(message)

                        step_books_fiction(message)

                    elif message.text == 'Детские сказки и приключения':
                        topics_books_childrens = []
                        url_books_childrens = f'https://2books.su/tags/childrens/'
                        response_books_childrens = requests.get(url_books_childrens)
                        soup_books_childrens = BeautifulSoup(response_books_childrens.text, 'lxml')
                        texts_books_childrens = soup_books_childrens.find_all('h2')
                        smth_books_childrens = soup_books_childrens.find_all(class_="book-list book-list-wide")
                        smthbooks_childrens = []
                        for i in range(len(smth_books_childrens)):
                            smthbooks_childrens.append(smth_books_childrens[i].find_all(class_="book-item"))
                        for j in range(len(texts_books_childrens)):
                            topics_books_childrens.append(f'{j + 1}. {texts_books_childrens[j].text}')
                        string_books_childrens = "\n".join(topics_books_childrens)
                        bot.send_message(message.chat.id, string_books_childrens)
                        bot.send_message(message.chat.id, 'Выберите цифру серии, которую хотели бы прочесть',
                                         reply_markup=keyboard_series)

                        def step_books_childrens(message):
                            bot.register_next_step_handler(message, stepbooks_childrens)

                        def stepbooks_childrens(message):
                            texts_books_childrens = []
                            llink_books_childrens = []
                            try:
                                for j in range(len(smthbooks_childrens[int(message.text) - 1])):
                                    texts_books_childrens.append(
                                        f'{j + 1}. {smthbooks_childrens[int(message.text) - 1][j].find("p").text}')
                                    llink_books_childrens.append(
                                        f"https://2books.su{smthbooks_childrens[int(message.text) - 1][j].find('a').get('href')}")
                                stringbooks_childrens = '\n'.join(texts_books_childrens)
                                bot.send_message(message.chat.id, stringbooks_childrens)
                                bot.send_message(message.chat.id, 'Выберите цифру книги, которую хотите прочесть',
                                                 reply_markup=keyboard_series)

                                def nextstep_books_childrens(message):
                                    bot.register_next_step_handler(message, nextstepbooks_childrens)

                                def nextstepbooks_childrens(message):
                                    try:
                                        bot.send_message(message.chat.id, llink_books_childrens[int(message.text) - 1],
                                                         reply_markup=keyboard_books)
                                        def_books(message)
                                    except:
                                        if message.text == 'Выйти':
                                            reply_markup = keyboard_books
                                            def_books(message)
                                        else:
                                            nextstep_books_childrens(message)

                                nextstep_books_childrens(message)
                            except:
                                if message.text == 'Выйти':
                                    reply_markup = keyboard_books
                                    def_books(message)
                                else:
                                    bot.send_message(message.chat.id, 'Введите только цифру!')
                                    step_books_childrens(message)

                        step_books_childrens(message)

                    elif message.text == 'Нон-фикшн':
                        topics_books_non_fiction = []
                        url_books_non_fiction = f'https://2books.su/tags/non-fiction/'
                        response_books_non_fiction = requests.get(url_books_non_fiction)
                        soup_books_non_fiction = BeautifulSoup(response_books_non_fiction.text, 'lxml')
                        texts_books_non_fiction = soup_books_non_fiction.find_all('h2')
                        smth_books_non_fiction = soup_books_non_fiction.find_all(class_="book-list book-list-wide")
                        smthbooks_non_fiction = []
                        for i in range(len(smth_books_non_fiction)):
                            smthbooks_non_fiction.append(smth_books_non_fiction[i].find_all(class_="book-item"))
                        for j in range(len(texts_books_non_fiction)):
                            topics_books_non_fiction.append(f'{j + 1}. {texts_books_non_fiction[j].text}')
                        string_books_non_fiction = "\n".join(topics_books_non_fiction)
                        bot.send_message(message.chat.id, string_books_non_fiction)
                        bot.send_message(message.chat.id, 'Выберите цифру серии, которую хотели бы прочесть',
                                         reply_markup=keyboard_series)

                        def step_books_non_fiction(message):
                            bot.register_next_step_handler(message, stepbooks_non_fiction)

                        def stepbooks_non_fiction(message):
                            texts_books_non_fiction = []
                            llink_books_non_fiction = []
                            try:
                                for j in range(len(smthbooks_non_fiction[int(message.text) - 1])):
                                    texts_books_non_fiction.append(
                                        f'{j + 1}. {smthbooks_non_fiction[int(message.text) - 1][j].find("p").text}')
                                    llink_books_non_fiction.append(
                                        f"https://2books.su{smthbooks_non_fiction[int(message.text) - 1][j].find('a').get('href')}")
                                stringbooks_non_fiction = '\n'.join(texts_books_non_fiction)
                                bot.send_message(message.chat.id, stringbooks_non_fiction)
                                bot.send_message(message.chat.id, 'Выберите цифру книги, которую хотите прочесть',
                                                 reply_markup=keyboard_series)

                                def nextstep_books_non_fiction(message):
                                    bot.register_next_step_handler(message, nextstepbooks_non_fiction)

                                def nextstepbooks_non_fiction(message):
                                    try:
                                        bot.send_message(message.chat.id,
                                                         llink_books_non_fiction[int(message.text) - 1],
                                                         reply_markup=keyboard_books)
                                        def_books(message)
                                    except:
                                        if message.text == 'Выйти':
                                            reply_markup = keyboard_books
                                            def_books(message)
                                        else:
                                            nextstep_books_non_fiction(message)

                                nextstep_books_non_fiction(message)
                            except:
                                if message.text == 'Выйти':
                                    reply_markup = keyboard_books
                                    def_books(message)
                                else:
                                    bot.send_message(message.chat.id, 'Введите только цифру!')
                                    step_books_non_fiction(message)

                        step_books_non_fiction(message)
                    elif message.text == 'Поиск':
                        bot.send_message(message.chat.id, 'Найдите книгу, которую хотели бы прочесть',
                                         reply_markup=keyboard_series)
                        url_books_search = f'https://2books.su/library'
                        response_books_search = requests.get(url_books_search)
                        soup_books_search = BeautifulSoup(response_books_search.text, 'lxml')
                        smth_books_search = soup_books_search.find_all('a', class_="table-link")
                        names_books_search = []
                        links_books_search = []
                        for i in range(len(smth_books_search)):
                            names_books_search.append(smth_books_search[i].text)
                            links_books_search.append(f'https://2books.su{smth_books_search[i].get("href")}')

                        def step_books_search(message):
                            bot.register_next_step_handler(message, books_search)

                        def books_search(message):
                            ctr_books_search = 0
                            for j in range(len(names_books_search)):
                                if message.text in names_books_search[j]:
                                    bot.send_message(message.chat.id, links_books_search[j],
                                                     reply_markup=keyboard_books)
                                    ctr_books_search += 1
                                    def_books(message)
                                    if j == len(names_books_search) - 1:
                                        def_books(message)
                                else:
                                    if message.text == 'Выйти':
                                        reply_markup = keyboard_books
                                        def_books(message)
                                    elif j == len(names_books_search) - 1 and ctr_books_search == 0:
                                        bot.send_message(message.chat.id, 'К сожалению, такой книги не нашлось(('
                                                                          ' Попробуйте ввести ключевое слово в названии или найдите другую книгу!',
                                                         reply_markup=keyboard_books)
                                        def_books(message)

                        step_books_search(message)

                def_books(message)
        elif message.text == '🔈Аудиокниги':
            bot.send_message(message.chat.id, 'Функция закрыта на ремонт')
        elif message.text == '🎤Подкасты':
            answer_podcast = False
            bot.send_message(message.chat.id,
                             'Что бы вы хотели послушать? \nВыберите подкаст из списка недавних или зайдите в библиотеку подкастов',
                             reply_markup=keyboard2)
        elif message.text == '📝Тесты':
            # bot.send_message(message.chat.id, 'Выберите категорию тестов', reply_markup=keyboard_tests)
            #
            # def step_tests(message):
            #     bot.register_next_step_handler(message, steptests)
            #
            # def steptests(message):
            #     if message.text == 'Выйти':
            #         bot.send_message(message.chat.id, 'Выберите функцию из предложенных на клавиатуре',
            #                          reply_markup=keyboard1)
            #         send_text(message)
            #     elif message.text == 'На грамматику':
            #         bot.send_message(message.chat.id, string_tests_1)
            #         bot.send_message(message.chat.id, 'Выберите цифру теста, который хотите пройти',
            #                          reply_markup=keyboard_series)
            #         def step_tests_1(message):
            #             bot.register_next_step_handler(message, step_tests1)
            #         def step_tests1(message):
            #             try:
            #                 bot.send_message(message.chat.id, link_tests_1[int(message.text)],
            #                                  reply_markup=keyboard_tests)
            #                 step_tests(message)
            #             except:
            #                 if message.text == 'Выйти':
            #                     bot.send_message(message.chat.id, 'Выберите функцию на клавиатуре',
            #                                      reply_markup=keyboard_tests)
            #                     step_tests(message)
            #         step_tests_1(message)
            #     elif message.text == 'На знание времён':
            #         bot.send_message(message.chat.id, string_tests_2)
            #         bot.send_message(message.chat.id, 'Выберите цифру теста, который хотите пройти',
            #                          reply_markup=keyboard_series)
            #
            #         def step_tests_2(message):
            #             bot.register_next_step_handler(message, step_tests2)
            #
            #         def step_tests2(message):
            #             try:
            #                 bot.send_message(message.chat.id, link_tests_2[int(message.text)],
            #                                  reply_markup=keyboard_tests)
            #                 step_tests(message)
            #             except:
            #                 if message.text == 'Выйти':
            #                     bot.send_message(message.chat.id, 'Выберите функцию на клавиатуре',
            #                                      reply_markup=keyboard_tests)
            #                     step_tests(message)
            #
            #         step_tests_2(message)
            #
            #     elif message.text == 'Неправильные глаголы':
            #         bot.send_message(message.chat.id, string_tests_3)
            #         bot.send_message(message.chat.id, 'Выберите цифру теста, который хотите пройти',
            #                          reply_markup=keyboard_series)
            #
            #         def step_tests_3(message):
            #             bot.register_next_step_handler(message, step_tests3)
            #
            #         def step_tests3(message):
            #             try:
            #                 bot.send_message(message.chat.id, link_tests_3[int(message.text)],
            #                                  reply_markup=keyboard_tests)
            #                 step_tests(message)
            #             except:
            #                 if message.text == 'Выйти':
            #                     bot.send_message(message.chat.id, 'Выберите функцию на клавиатуре',
            #                                      reply_markup=keyboard_tests)
            #                     step_tests(message)
            #
            #         step_tests_3(message)
            #
            #     elif message.text == 'Для школьников':
            #         bot.send_message(message.chat.id, string_tests_4)
            #         bot.send_message(message.chat.id, 'Выберите цифру теста, который хотите пройти',
            #                          reply_markup=keyboard_series)
            #
            #         def step_tests_4(message):
            #             bot.register_next_step_handler(message, step_tests4)
            #
            #         def step_tests4(message):
            #             try:
            #                 bot.send_message(message.chat.id, link_tests_4[int(message.text)],
            #                                  reply_markup=keyboard_tests)
            #                 step_tests(message)
            #             except:
            #                 if message.text == 'Выйти':
            #                     bot.send_message(message.chat.id, 'Выберите функцию на клавиатуре',
            #                                      reply_markup=keyboard_tests)
            #                     step_tests(message)
            #
            #         step_tests_4(message)
            #     elif message.text == 'Тест на уровень языка':
            #         bot.send_message(message.chat.id, 'https://www.efset.org/ru/ef-set-50/')
            # step_tests(message)
            pass
        elif message.text == 'ТВ-шоу':
            links_show = []
            names_show = []
            url_show = 'https://speechyard.com/video/'
            response_show = requests.get(url_show)
            soup_show = BeautifulSoup(response_show.text, 'lxml')
            smth_show = soup_show.find('ul', class_="clearfix paginate-me").find_all('a', class_="name ajax")
            bot.send_message(message.chat.id, f'{len(smth_show)}')
            for i in range(len(smth_show)):
                links_show.append(f'https://speechyard.com{smth_show[i].get("href")}')
                names_show.append(f'{i+1}. {smth_show[i].text}')
            string_show = '\n'.join(names_show)
            bot.send_message(message.chat.id, string_show)
            bot.send_message(message.chat.id, 'Введите цифру шоу, которое хотели бы посмотреть',
                             reply_markup=keyboard_series)
            def step_show(message):
                bot.register_next_step_handler(message, stepshow)
            def stepshow(message):
                try:
                    bot.send_message(message.chat.id, links_show[int(message.text)-1], reply_markup=keyboard1)
                    send_text(message)
                except:
                    if message.text == 'Выйти':
                        bot.send_message(message.chat.id, 'Выберите функцию на клавиатуре', reply_markup=keyboard1)
                        send_text(message)
                    else:
                        bot.send_message(message.chat.id, 'Введите только цифру!!!')
                        step_show(message)
            step_show(message)
        elif message.text == '📻Радио':
            bot.send_message(message.chat.id, 'Функция закрыта на ремонт')
        elif message.text == '📊Статистика':
            bot.send_message(message.chat.id, 'Функция закрыта на ремонт')
    else:
        r = 0
        answer_podcast = True
        ctr_podcasts = True
        url_podcasts = 'https://www.bbc.co.uk/learningenglish/english/features/6-minute-english'
        response = requests.get(url_podcasts)
        soup = BeautifulSoup(response.text, 'lxml')
        links3 = soup.find_all("a")
        llink1 = []
        text1 = []
        listened_podcasts = []
        for i in range(len(links3)):
            if '/learningenglish' and '/6-minute-english' and 'ep' in links3[i].get("href"):
                if 'http://' in links3[i].get("href") or 'themed_weeks' in links3[i].get("href"):
                    pass
                else:
                    if i % 2 == 0:
                        llink1.append(f'https://www.bbc.co.uk{links3[i].get("href")}')
                        text1.append(f'{int(i / 2 - 90)}. {links3[i].text}')
        reply_markup = keyboard2

        @bot.message_handler(commands=['text'])
        def podc_text(message, r):
            if message.text == 'Выйти':
                r += 1
                return r
            else:
                if message.text == 'Недавние 50':
                    bot.send_message(message.chat.id, '\n'.join(text1[0:50]))
                elif message.text == '51-150':
                    bot.send_message(message.chat.id, "\n".join(text1[50:150]))
                elif message.text == '151-250':
                    bot.send_message(message.chat.id, "\n".join(text1[150:250]))
                elif message.text == '251-350':
                    bot.send_message(message.chat.id, "\n".join(text1[250:350]))
                elif message.text == '351 и больше':
                    bot.send_message(message.chat.id, "\n".join(text1[350:]))
                else:
                    bot.send_message(message.chat.id, 'Выберите один из вариантов, предложенных на клавиатуре))')
                return r

        podc_text(message, r)
        r = podc_text(message, r)
        if r == 0:
            bot.send_message(message.chat.id, 'Введите номер подкаста, который хотели бы послушать')

            def podc_number_message(message):
                bot.register_next_step_handler(message, podc_number)

            def podc_number(message):
                if message.text != '/start':
                    podc_value = int(message.text) - 1
                    bot.send_message(message.chat.id, llink1[podc_value])
                    listened_podcasts.append(text1[podc_value])
                    text1[podc_value] = f'✅{int(i / 2 - 90)}. {links3[i].text}'

            podc_number_message(message)
        elif ctr_podcasts:
            bot.send_message(message.chat.id, 'Выбери функцию на клавиатуре', reply_markup=keyboard1)
            ctr_podcasts = False
            return


bot.polling()

# llink_books_A1 = []
# texts_books_A1 = []
# level_books_A1 = []
# btext_books_A1 = []
# url_books_adapted = f'https://2books.su/tags/adapted/'
# response_books_A1 = requests.get(url_books_adapted)
# soup_books_A1 = BeautifulSoup(response_books_A1.text, 'lxml')
# links_books_A1 = soup_books_A1.find_all(class_="book-item")
# for i in range(len(links_books_A1) - 7):
#     llink_books_A1.append(f'https://2books.su/{links_books_A1[i + 2].find("a").get("href")}')
#     text_A1 = links_books_A1[i + 2].find("p").text
#     texts_books_A1.append(text_A1)
#     if "A1" in text_A1:
#         level_books_A1.append(links_books_A1[i + 2].find("p").text)
#         btext_books_A1.append((f'{i + 1}. {text_A1[:len(text_A1) - 24]}'))
#     # print(llink_books_A1[int(message.text)])
# string_books_A1 = "\n".join(btext_books_A1)
# print(string_books_A1)
