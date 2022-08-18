from enum import Enum


class Language(Enum):
    RUS = 'ru'
    ENG = 'en'


CONTEXT = {
    Language.RUS: {
        'title': 'Личный сайт - Алексея Матюнина',
        'fullname': 'Матюнин Алексей',
        'nav': {
            'profile': 'Обо мне',
            'cv': 'Резюме',
            'projects': 'Портфолио',
            'contacts': 'Контакты',
            'language': [
                {'title': 'Русский', 'class': 'dropdown-item bg-light disabled', 'link': '#'},
                {'title': 'Английский', 'class': 'dropdown-item bg-light', 'link': 'en'}
            ],
        },
        'promo': {
            'title': 'Все преодолимо,<br>когда у тебя есть цель!',
            'subtitle': 'Python Developer / Team lead с навыками Scrum Master.<br>Люблю работать в команде и выстраивать процессы по Agile.',
            'button': 'Узнать больше обо мне'
        },
        'profile': {
            'title': 'Профессиональный опыт',
            'button': 'Подробнее в резюме',
            'subtitle': 'Участник олимпиад ICPC 2010-2012. Работаю программистом с 2013 года. <br>Прошел путь от Junior до Senior Developer. Являюсь ментором для новых сотрудников.<br>Пишу чистый код и автотесты, используя TDD. ',
            'python': {
                'title': 'Python 3.9',
                'subtitle': 'Основной язык для работы. Раньше писал на C# C++'
            },
            'experience': {
                'title': '> 8 лет опыта',
                'subtitle': '...<br>Сбербанк с 2019<br>Align Technology c 2021<br>VK Cloud Solutions 2022'
            },
            'courses': {
                'title': 'Прошел курсы',
                'subtitle': 'Scrum Master (КУ Сбербанка) Middle Python (Яндекс)'
            },
        },
        'cv': {
            'title': 'Резюме',
            'cv_card': {
                'title': 'Скачать PDF',
                'subtitle': 'Описание мест работы. И полная информация о себе!',
                'link': '../static/cv/in_russian.pdf'
            },
            'git_hub': {
                'title': 'Git Hub',
                'subtitle': 'Мой профиль на GitHub.',
                'link': 'https://github.com/tiraill'
            }
        },
        'projects': {
            'hdl': {
                'title': 'HDL Automation',
                'subtitle': 'Сайт российского дистрибьютора устройств для "умного дома"<br>от международной компании HDL'
            },
            'agc': {
                'title': 'AGC Solution',
                'subtitle': 'Компания по производству изделий из стекла и дизайну интерьеров'
            }
        },
        'contacts': {
            'title': 'Остаемся на связи!',
            'subtitle': 'Готовы начать сотрудничество со мной? Напишите мне в телеграм или отправьте email, я отвечу вам как можно скорее!'
        },
        'instagram': 'А еще загляните в мой Instagram'
    },
    Language.ENG: {
        'title': 'Aleksey Matyunin\'s site',
        'fullname': 'Aleksey Matyunin',
        'nav': {
            'profile': 'Profile',
            'cv': 'CV',
            'projects': 'Projects',
            'contacts': 'Contacts',
            'language': [
                {'title': 'English', 'class': 'dropdown-item bg-light disabled', 'link': '#'},
                {'title': 'Russian', 'class': 'dropdown-item bg-light', 'link': 'ru'},
            ],
        },
        'promo': {
            'title': 'Everything is possible<br>when you have a purpose!',
            'subtitle': 'Python Developer / Team lead with Scrum Master skills.<br>I like working in a team and build processes using Agile.',
            'button': 'Learn more about me'
        },
        'profile': {
            'title': 'Professional experience',
            'button': 'Read more in CV',
            'subtitle': 'Participant of ICPC 2010-2012 Olympiad. I work as a developer since 2013.<br>Went from Junior to Senior Developer. I am a mentor for new employees.<br>I write a pure code and autotests using TDD. ',
            'python': {
                'title': 'Python 3.9',
                'subtitle': 'Main language for work.<br>Used to use C# C ++'
            },
            'experience': {
                'title': '> 8 years of experience',
                'subtitle': '...<br>Sberbank 2019<br>Align Technology 2021<br>VK Cloud Solutions 2022'
            },
            'courses': {
                'title': 'Courses',
                'subtitle': 'Scrum Master (Sberbank)<br>Advanced Python (Yandex)'
            },
        },
        'cv': {
            'title': 'CV',
            'cv_card': {
                'title': 'Download PDF',
                'subtitle': 'Description of the places of work. And detailed information about me!',
                'link': '../static/cv/in_english.pdf'
            },
            'git_hub': {
                'title': 'Git Hub',
                'subtitle': 'My profile on GitHub.',
                'link': 'https://github.com/tiraill'
            }
        },
        'projects': {
            'hdl': {
                'title': 'HDL Automation',
                'subtitle': 'Site of the Russian distributor of smart home devices<br>from the international company HDL'
            },
            'agc': {
                'title': 'AGC Solution',
                'subtitle': 'Glassware & Interior Design Company'
            }
        },
        'contacts': {
            'title': 'Keep in touch!',
            'subtitle': 'Are you ready to start working with me? Please contact me on telegram or send an email, I will reply you as soon as possible!'
        },
        'instagram': 'Follow me on Instagram'
    }
}
