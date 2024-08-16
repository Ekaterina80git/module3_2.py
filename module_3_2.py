import re


def send_email(message,recipient,*,sender = "university.help@gmail.com"):
   # recipient = "vasyok1337@gmail.com"
   # проверка домен
    if "@" not  in sender or'@' not in recipient or not(recipient.endswith((".com",".ru",".net")) and sender.endswith((".com",".ru","net"))):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.')
        return
    if  sender == recipient:
         print("Нельзя отправить письмо самому себе!")
         return
    if sender == "university.help@gmail.com":
         print(f"Письмо успешно отправлено  адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ!Письмо отправленос адреса {sender} на адрес {recipient}.")


send_email("это сообщение для проверки связи","vasyok1337@gmail.com")
send_email("вы видите это сообщение как лучший студент курса!","urban.fan@gmail.ru",sender ="urban.info@gmail.com")
send_email("Пожалуйста исправьте домашнее задание","urban.student@gmail.ru",sender="urban.teacher@mail.uk")
send_email("Напоминаю самому себе о вебинаре",'urban.teacher@gmail.ru',sender="urban.teacher@gmail.ru")




