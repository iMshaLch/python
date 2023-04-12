
import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, MessageHandler, CommandHandler, Filters, CallbackQueryHandler, CallbackContext, ConversationHandler

TOKEN = "5920446143:AAE4pV6XS738rYAmTMH4zoVZdMVfdKd0B04"

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

REG, NAME, BUTTON, FIRST, USERS = range(5)
ONE, TWO, THREE, FOUR = range(4)

reply_keyboard = [
    [
        KeyboardButton(text="Registration"),
    ]
]

markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True,input_field_placeholder="\"Registration\"ni bosing")

keyboard = [
    [
        InlineKeyboardButton("Tashkent", callback_data='Tashkent'),
        InlineKeyboardButton("Tashkent.vil", callback_data='Tashkent.vil'),
    ],
    [
        InlineKeyboardButton("Buhoro", callback_data='Buhoro'),
        InlineKeyboardButton("Samarqand", callback_data='Samarqand'),
    ],
    [
        InlineKeyboardButton("Navoiy", callback_data='Navoiy'),
        InlineKeyboardButton("Andijon", callback_data='Andijon'),
    ],
    [
        InlineKeyboardButton("Farg\'ona", callback_data='Farg\'ona'),
        InlineKeyboardButton("Namangan", callback_data='Namangan'),
    ],
    [
        InlineKeyboardButton("Surxandaryo", callback_data='Surxandaryo'),
        InlineKeyboardButton("Qashqadaryo", callback_data='Qashqadaryo'),
    ],
    [
        InlineKeyboardButton("Sirdaryo", callback_data='Sirdaryo'),
        InlineKeyboardButton("Xorazm", callback_data='Xorazm'),
    ],
    [
        InlineKeyboardButton("Qaraqalpaqstan Respublikasi", callback_data='Qaraqalpaqstan Respublikasi'),
    ],
]

reply_markup = InlineKeyboardMarkup(keyboard)


def start(update: Update, context: CallbackContext) -> None:
    
    update.message.reply_text('Salom, iltimos registraciyadan oting', reply_markup=markup)
    
    text = update.message.text

    return REG

def info(update: Update, context: CallbackContext) -> None: 

    keyboard = [
        [
            InlineKeyboardButton("Saytga o\'tish", url='https://youtube.com')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Youtubega o\'tish uchun bosing', reply_markup=reply_markup)
    



def reg(update: Update, context: CallbackContext) -> None:

    update.message.reply_text('Ismingiz va familyangizni kiriting')
    
    return NAME


def fullname(update: Update, context: CallbackContext) -> None:
    
    text = update.message.text
    
    context.user_data["FIO : "] = text
    
    update.message.reply_text('O\'z shahringizni tanlang :', reply_markup=reply_markup)

    return BUTTON

def language(update: Update, context: CallbackContext) -> None:

    query = update.callback_query

    query.answer()

    context.user_data["Shaxringiz : "] = query.data

    keyboard = [
        [
            InlineKeyboardButton("Rus tili", callback_data=str(ONE)),
            InlineKeyboardButton("Ingliz tili", callback_data=str(TWO)),
        ],
        [
            InlineKeyboardButton("Done", callback_data='Done'),
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    query.edit_message_text(text="Biladigan tillaringizni tasdiqlang", reply_markup=reply_markup)

    return FIRST


def one(update: Update, context: CallbackContext) -> None:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("✅Rus tili", callback_data=str(FOUR)),
            InlineKeyboardButton("Ingliz tili", callback_data=str(THREE)),
        ],
        [
            InlineKeyboardButton("Done", callback_data='Done'),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    context.user_data["Biladigan tillar : "] = "Rus tili"

    query.edit_message_text(
        text="Biladigan tillaringizni tasdiqlang", reply_markup=reply_markup
    )
    return FIRST



def two(update: Update, context: CallbackContext) -> None:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Rus tili", callback_data=str(THREE)),
            InlineKeyboardButton("✅Ingliz tili", callback_data=str(FOUR)),
        ],
        [
            InlineKeyboardButton("Done", callback_data='Done'),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    context.user_data["Biladigan tillar : "] = "Ingliz tili"

    query.edit_message_text(
        text="Biladigan tillaringizni tasdiqlang", reply_markup=reply_markup
    )
    return FIRST


def three(update: Update, context: CallbackContext) -> None:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("✅Rus tili", callback_data=str(TWO)),
            InlineKeyboardButton("✅Ingliz tili", callback_data=str(ONE)),
        ],
        [
            InlineKeyboardButton("Done", callback_data='Done'),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    context.user_data["Biladigan tillar : "] = "Rus tili, Ingliz tili"

    query.edit_message_text(
        text="Biladigan tillaringizni tasdiqlang", reply_markup=reply_markup
    )
    # Transfer to conversation state `SECOND`
    return FIRST


def four(update: Update, context: CallbackContext) -> None:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Rus tili", callback_data=str(ONE)),
            InlineKeyboardButton("Ingliz tili", callback_data=str(TWO)),
        ],
        [
            InlineKeyboardButton("Done", callback_data='Done'),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    context.user_data["Biladigan tillar : "] = "Hechqanday til"

    query.edit_message_text(
        text="Biladigan tillaringizni tasdiqlang", reply_markup=reply_markup
    )
    return FIRST

def done(update: Update, context: CallbackContext) -> None: 

    if "Biladigan tillar : " not in context.user_data.keys():
        context.user_data["Biladigan tillar : "] = "Hechqanday til"

    query = update.callback_query

    query.answer()

    facts = [f'{key} {value}' for key, value in context.user_data.items()]

    context.bot_data[context.user_data['FIO : ']] = facts

    print(context.bot_data)

    query.edit_message_text('Ma\'lumotlaringiz :\n' + "\n".join(facts).join(['\n', '\n']) + '\nSaytga o\'tish uchun /info komandasini yuboring')

def users(update: Update, context: CallbackContext) -> None: 

    keyboard = [
            [InlineKeyboardButton(text=(str(key) + " haqida ma\'lumot"), callback_data=str(key))]
        for key, value in context.bot_data.items()
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(text="Kim haqida ma\'lumot kerak", reply_markup=reply_markup)

def callback_users(update: Update, context: CallbackContext) -> None: 

    query = update.callback_query

    query.answer()

    name = list(context.bot_data)[int(query.data)]

    query.edit_message_text(
        '{} ma\'lumotlaringiz :\n' + "\n".join(context.bot_data[name]).join(['\n', '\n']) + 
        + '\nSaytga o\'tish uchun /info komandasini yuboring'.format(name)
    )






def cancel(update: Update, context: CallbackContext) -> None: 
    return ConversationHandler.END


def main() -> None:

    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            REG: [
                MessageHandler(
                    Filters.regex('^Registration$'), reg
                ),
            ],
            NAME: [ 
                MessageHandler(
                    Filters.text, fullname
                ),
            ],
            BUTTON: [
                CallbackQueryHandler(language)
            ],
            FIRST: [
                CallbackQueryHandler(one, pattern='^' + str(ONE) + '$'),
                CallbackQueryHandler(two, pattern='^' + str(TWO) + '$'),
                CallbackQueryHandler(three, pattern='^' + str(THREE) + '$'),
                CallbackQueryHandler(four, pattern='^' + str(FOUR) + '$'),
                CallbackQueryHandler(done, pattern='^Done$'),
            ],
            USERS: [
                CommandHandler("users", users)
            ],
            CALLBACK: [
                
            ]

        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    # dispatcher.add_handler(CommandHandler("start", start))

    dispatcher.add_handler(conv_handler)

    dispatcher.add_handler(CommandHandler("info", info))

    # dispatcher.add_handler(CommandHandler("users", users))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()