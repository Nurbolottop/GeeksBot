from django.conf import settings
from telebot import TeleBot, types
from .models import TelegramUser
import re
from apps.secondary.models import AddChat

# Create your views here.
TELEGRAM_TOKEN = "6966818358:AAExpZzm8czP9vVkeP61r5bEqvn-TJOnDP8"
ADMIN_ID = "-1002082761055"

bot = TeleBot(TELEGRAM_TOKEN, threaded=False)
admin_id = ADMIN_ID


@bot.message_handler(commands=['start','go'])
def start(message: types.Message):
    # Проверяем, существует ли пользователь, и создаем, если нет
    user, created = TelegramUser.objects.get_or_create(
        id_user=message.from_user.id,
        defaults={
            'username': message.from_user.username,
            'first_name': message.from_user.first_name,
            'last_name': message.from_user.last_name,
        }
    )
    if created:
        bot.send_message(message.chat.id, f"Привет {message.from_user.full_name}")
    else:
        bot.send_message(message.chat.id, f"С возвращением, {message.from_user.first_name}!")

class Mail:
    def __init__(self): 
        self.description = None

mail = Mail()

    
def get_chat_title(chat_id):
    try:
        chat = bot.get_chat(chat_id)
        return chat.title
    except Exception as e:
        print(f"Ошибка при получении информации о чате: {e}")
        return None
    
def get_message(message:types.Message):
    mail.description = message.text 
    users = TelegramUser.objects.all()
    for user in users:
        bot.send_message(user.id_user, mail.description)
    bot.send_message(message.chat.id, "Рассылка окончена")

def send_message_to_group_day(day_mailing_instance):
    chat_id = day_mailing_instance.group.chat_id
    message_text = f"Здравствуйте, ребята, у вас сегодня урок в {day_mailing_instance.lesson_time.strftime('%H:%M')}"
    try:
        result = bot.send_message(chat_id, message_text)
        print(f"Сообщение успешно отправлено. Результат: {result}")
    except Exception as e:
        print(f"Ошибка при отправке сообщения в Telegram: {e}")

def send_message_to_group(start_mailing_instance):
    chat_id = start_mailing_instance.group.chat_id
    message = create_message(start_mailing_instance)
    try:
        bot.send_message(chat_id, message)
    except Exception as e:
        print(f"Ошибка при отправке сообщения в Telegram: {e}")

def clean_html_for_telegram(html_text):
    html_text = html_text.replace('&nbsp;', ' ')
    # Удаление всех HTML-тегов
    clean_text = re.sub('<[^<]+?>', '', html_text)
    return clean_text

def send_message_with_image(mailing_group_instance):
    modified_html_description = clean_html_for_telegram(mailing_group_instance.descriptions)

    # Проверяем, установлен ли флаг 'send_to_all' или есть ли выбранные группы
    if mailing_group_instance.send_to_all or not mailing_group_instance.group.exists():
        groups = AddChat.objects.all()
    else:
        groups = mailing_group_instance.group.all()

    # Отправляем сообщение каждой группе
    for group in groups:
        chat_id = group.chat_id
        if mailing_group_instance.image:  # Проверяем, есть ли фотография
            with open(mailing_group_instance.image.path, 'rb') as photo:
                bot.send_photo(chat_id, photo, caption=modified_html_description, parse_mode='HTML')
        else:
            bot.send_message(chat_id, modified_html_description, parse_mode='HTML')


def create_message(start_mailing_instance):
    # Формируем сообщение, используя данные из start_mailing_instance
    message = (
        f"Добрый день! 🌟 Вас приветствует школа программирования Geeks.\n\n"
        f"🗓 Сегодня, {start_mailing_instance.date.strftime('%d %B %Y')} года, в {start_mailing_instance.hours.title} начнется ваше первое увлекательное занятие по {start_mailing_instance.devop.title}, для {start_mailing_instance.mounth.title}. Мы ждем всех без опозданий и с нетерпением хотим представить вам преподавателя первого месяца, {start_mailing_instance.teacher.name} @{start_mailing_instance.teacher.usrname} . 🚀\n"
        f"Добрый день! 🌟 Вас приветствует школа программирования Geeks.\n\n"
        f"📢 Просим также обратить внимание, что студенты, пожалуйста, не забудьте приносить оплату за обучение во время занятия. 💰\n\n"
        f"📊 Кроме того, мы внедряем учебные стендапы в нашем процессе обучения. Студенты будут представлять свои успехи и планы на следующий урок. Это поможет нам следить за вашим прогрессом и обеспечить максимально эффективное обучение. 📈\n\n"
        f"Если у вас возникнут вопросы по организации занятий или стендапам, не стесняйтесь обращаться к вашему куратору по направлению, {start_mailing_instance.admin.name} @{start_mailing_instance.admin.usrname} 😉\n\n"
        f"📅 Дата начала курса: {start_mailing_instance.date.strftime('%d %B %Y')}\n"
        f"🕗 Время начала: {start_mailing_instance.hours.title}\n"
        f"🗓 График занятий: {start_mailing_instance.day.day}"
    )
    return message
@bot.message_handler(commands=['mailing'])
def send_mailing(message:types.Message):
    if message.chat.id != int(admin_id):
        bot.send_message(message.chat.id, "Эта команда доступна только админу")
        return
    msg = bot.send_message(message.chat.id, "Введите текст для рассылки: ")
    bot.register_next_step_handler(msg, get_message)

def get_text(message):
    bot.send_message(admin_id, message, parse_mode='HTML')

def get_text_doctor(message, id):
    bot.send_message(id, message)


@bot.message_handler()  
def echo(message:types.Message):
    # bot.delete_message(message.chat.id, message.message_id)  
    bot.send_message(message.chat.id, "Я вас не понял")
