from core.list_func import *
import game_config as conf
SCENES = {
    'start_menu': {
        'text': f'Добро пожаловать в игру {conf.name_game}!',
        'name_unit': "pes",
        'unit': "[ng",
        'bg': 'png',
        'vars_return': (
            {
                'text': 'новая игра',
                'func': new_stage,
                'args': 'Stage1.1',
            },

        ),
        'scale_unit': 1,
        'unit_offset_y': 150,
        'unit_offset_x': -150,
    },
    'Stage1.1': {
        'text': 'На часах 23 00, я засыпал под звук моего старого холодильника.',
        'name_unit': "Игорь",
        'unit': "игорь",
        'bg': 'хата',
        'vars_return': (
            {
                'text': 'Далее...',
                'func': new_stage,
                'args': 'Stage1.2',
            },

        ),
        'scale_unit': conf.size3,
        'unit_offset_y': conf.y3,
        'unit_offset_x': conf.x3,
    },
    'Stage1.2': {
        'text': 'Ночь казалась спокойней чем обычно, на улице была кромешная тишина.',
        'name_unit': "Игорь",
        'unit': "игорь",
        'bg': 'хата',
        'vars_return': (
            {
                'text': 'Далее...',
                'func': new_stage,
                'args': 'Stage1.3',
            },

        ),
        'scale_unit': conf.size3,
        'unit_offset_y': conf.y3,
        'unit_offset_x': conf.x3,
    },
    'Stage1.3': {
        'text': 'Вот-вот я уже должен был предаться сну…',
        'name_unit': "Игорь",
        'unit': "игорь",
        'bg': 'хата',
        'vars_return': (
            {
                'text': 'Далее...',
                'func': new_stage,
                'args': 'Stage1.4',
            },

        ),
        'scale_unit': conf.size3,
        'unit_offset_y': conf.y3,
        'unit_offset_x': conf.x3,
    },
    'Stage1.4': {
        'text': 'Но вдруг из ниоткуда раздался громкий стук по батареям',
        'name_unit': "Игорь",
        'unit': "игорь",
        'bg': 'хата',
        'vars_return': (
            {
                'text': 'Далее...',
                'func': new_stage,
                'args': 'Stage1.5',
            },

        ),
        'scale_unit': conf.size3,
        'unit_offset_y': conf.y3,
        'unit_offset_x': conf.x3,
    },
    'Stage1.5': {
        'text': 'Это было не все, за первым ударом последовал второй, а за вторым третий и так далее…',
        'name_unit': "Игорь",
        'unit': "игорь",
        'bg': 'хата',
        'vars_return': (
            {
                'text': 'Далее...',
                'func': new_stage,
                'args': 'Stage1.6',
            },

        ),
        'scale_unit': conf.size3,
        'unit_offset_y': conf.y3,
        'unit_offset_x': conf.x3,
    },
    'Stage1.6': {
        'text': 'Черт побери какой придурок в час ночи занимается этим бредом!!!',
        'name_unit': "Игорь",
        'unit': "игорьзлой",
        'bg': 'хата',
        'vars_return': (
            {
                'text': 'Далее...',
                'func': new_stage,
                'args': 'Stage1.7',
            },

        ),
        'scale_unit': conf.size3,
        'unit_offset_y': conf.y3,
        'unit_offset_x': conf.x3,
    },
    'Stage1.7': {
        'text': 'Я был крайне недоволен. Зубы крепко стиснулись от злобы, вены на лбу набухли.',
        'name_unit': "Игорь",
        'unit': "игорьзлой",
        'bg': 'хата',
        'vars_return': (
            {
                'text': 'Лечь спать обратно',
                'func': new_stage,
                'args': 'Stage1.8Choice1.1',
            },
                        {
                'text': 'Разобраться с источником шума',
                'func': new_stage,
                'args': 'Stage1.8Choice2.1',
            },

        ),
        'scale_unit': conf.size3,
        'unit_offset_y': conf.y3,
        'unit_offset_x': conf.x3,
    },
    'Stage1.8Choice1.1': {
        'text': 'Я попытался смириться с данным непотребством.',
        'name_unit': "Игорь",
        'unit': "игорьуспокоится",
        'bg': 'хата',
        'vars_return': (
            {
                'text': 'Далее...',
                'func': new_stage,
                'args': 'Stage1.8Choice1.2',
            },

        ),
        'scale_unit': conf.size3,
        'unit_offset_y': conf.y3,
        'unit_offset_x': conf.x3,
    },
    'Stage1.8Choice1.2': {
        'text': 'Лег в постель, укрылся одеялом, закрыл глаза.',
        'name_unit': "Игорь",
        'unit': "игорьуспокоится",
        'bg': 'хата',
        'vars_return': (
            {
                'text': 'Далее...',
                'func': new_stage,
                'args': 'Stage1.8Choice1.3',
            },

        ),
        'scale_unit': conf.size3,
        'unit_offset_y': conf.y3,
        'unit_offset_x': conf.x3,
    },
    'Stage1.8Choice1.3': {
        'text': 'Упорно пытаясь не обращать внимания на удары по батареям я пролежал минут 15.',
        'name_unit': "Игорь",
        'unit': "игорьуспокоится",
        'bg': 'хата',
        'vars_return': (
            {
                'text': 'Далее...',
                'func': new_stage,
                'args': 'Stage1.8Choice1.4',
            },

        ),
        'scale_unit': conf.size3,
        'unit_offset_y': conf.y3,
        'unit_offset_x': conf.x3,
    },
    'Stage1.8Choice1.4': {
        'text': 'Но этот гад, что стучал по батареям все никак не мог угомониться.',
        'name_unit': "Игорь",
        'unit': "игорьуспокоится",
        'bg': 'хата',
        'vars_return': (
            {
                'text': 'Далее...',
                'func': new_stage,
                'args': 'Stage1.8Choice1.5',
            },

        ),
        'scale_unit': conf.size3,
        'unit_offset_y': conf.y3,
        'unit_offset_x': conf.x3,
    },
    'Stage1.8Choice1.5': {
        'text': 'Из-за этой неудачной попытки заснуть я стал еще злее.',
        'name_unit': "Игорь",
        'unit': "игорьзлой",
        'bg': 'хата',
        'vars_return': (
            {
                'text': 'Далее...',
                'func': new_stage,
                'args': 'Stage1.8Choice1.6',
            },

        ),
        'scale_unit': conf.size3,
        'unit_offset_y': conf.y3,
        'unit_offset_x': conf.x3,
    },
    'Stage1.8Choice1.6': {
        'text': 'Немедля ни секунды спрыгнул с кровати и пошел искать квартиру откуда исходил источник шума.',
        'name_unit': "Игорь",
        'unit': "игорьзлой",
        'bg': 'хата',
        'vars_return': (
            {
                'text': 'Далее...',
                'func': new_stage,
                'args': 'Stage2.1',
            },

        ),
        'scale_unit': conf.size3,
        'unit_offset_y': conf.y3,
        'unit_offset_x': conf.x3,
    },
    'Stage1.8Choice2.1': {
        'text': 'Я не собирался мириться с этим непотребством…',
        'name_unit': "Игорь",
        'unit': "игорьзадумчивый",
        'bg': 'хата',
        'vars_return': (
            {
                'text': 'Далее...',
                'func': new_stage,
                'args': 'Stage1.8Choice2.2',
            },

        ),
        'scale_unit': conf.size3,
        'unit_offset_y': conf.y3,
        'unit_offset_x': conf.x3,
    },
    'Stage1.8Choice2.2': {
        'text': 'Недолго думая я сообразил что источник шума находиться в квартире подомной.',
        'name_unit': "Игорь",
        'unit': "игорьзадумчивый",
        'bg': 'хата',
        'vars_return': (
            {
                'text': 'Далее...',
                'func': new_stage,
                'args': 'Stage1.8Choice2.3',
            },

        ),
        'scale_unit': conf.size3,
        'unit_offset_y': conf.y3,
        'unit_offset_x': conf.x3,
    },
    'Stage1.8Choice2.3': {
        'text': 'Что-ж, пора надавать подзатыльников этому дураку.',
        'name_unit': "Игорь",
        'unit': "игорьзлой",
        'bg': 'хата',
        'vars_return': (
            {
                'text': 'Далее...',
                'func': new_stage,
                'args': 'Stage2.1',
            },

        ),
        'scale_unit': conf.size3,
        'unit_offset_y': conf.y3,
        'unit_offset_x': conf.x3,
    },
    'Stage2.1': {
        'text': 'За мгновение я добрался до квартиры',
        'name_unit': "Игорь",
        'unit': "игорьзад",
        'bg': 'дверьсосед',
        'vars_return': (
            {
                'text': 'Далее...',
                'func': new_stage,
                'args': 'Stage2.2',
            },

        ),
        'scale_unit': conf.size1,
        'unit_offset_y': conf.y1,
        'unit_offset_x': -310,
    },
    'Stage2.2': {
        'text': 'Ну держись гаденыш, сейчас я тебе настучу по голове',
        'name_unit': "Игорь",
        'unit': "игорьзад",
        'bg': 'дверьсосед',
        'vars_return': (
            {
                'text': 'Начать агрессивно стучать',
                'func': new_stage,
                'args': 'Stage2.3Choice1.1',
            },
            {
                'text': 'Попробовать дернуть ручку двери',
                'func': new_stage,
                'args': 'Stage2.3Choice2.1',
            },
            {
                'text': 'Игорь переосмысливает свое существования',
                'func': new_stage,
                'args': 'Stage2.3Choice3.1',
            },

        ),
        'scale_unit': conf.size1,
        'unit_offset_y': conf.y1,
        'unit_offset_x': -310,
    },
    'Stage2.3Choice1.1': {
        'text': 'Тук Тук Тук',
        'name_unit': "Игорь",
        'unit': "игорьзад",
        'bg': 'дверьсосед',
        'vars_return': (
            {
                'text': 'Далее...',
                'func': new_stage,
                'args': 'Stage2.3Choice1.2',
            },

        ),
        'scale_unit': conf.size1,
        'unit_offset_y': conf.y1,
        'unit_offset_x': -310,
    },
    'Stage2.3Choice1.2': {
        'text': 'Хммм… Неужели он так сильно увлекся своим мракобесием….?',
        'name_unit': "Игорь",
        'unit': "игорьзад",
        'bg': 'дверьсосед',
        'vars_return': (
            {
                'text': 'Далее...',
                'func': new_stage,
                'args': 'Stage2.3Choice1.3',
            },

        ),
        'scale_unit': conf.size1,
        'unit_offset_y': conf.y1,
        'unit_offset_x': -310,
    },
    'Stage2.3Choice1.3': {
        'text': 'Эй, ты там! А ну открывай! Время первый час ночи! Ты совсем кукухой поехал?',
        'name_unit': "Игорь",
        'unit': "игорьзад",
        'bg': 'дверьсосед',
        'vars_return': (
            {
                'text': 'Далее...',
                'func': new_stage,
                'args': 'Stage2.3Choice1.4',
            },

        ),
        'scale_unit': conf.size1,
        'unit_offset_y': conf.y1,
        'unit_offset_x': -310,
    },
    'Stage2.3Choice1.4': {
        'text': 'Внутри квартиры никто не отвечает. Звуки ударов стихли на несколько мгновений, а затем возобновились с тройной силой',
        'name_unit': " ",
        'unit': "игорьзад",
        'bg': 'дверьсосед',
        'vars_return': (
            {
                'text': 'Далее...',
                'func': new_stage,
                'args': 'Stage2.3Choice1.5',
            },

        ),
        'scale_unit': conf.size1,
        'unit_offset_y': conf.y1,
        'unit_offset_x': -310,
    },
    'Stage2.3Choice1.5': {
        'text': 'Это уже переходит все границы. Мое терпение лопнуло окончательно.',
        'name_unit': "Игорь",
        'unit': "игорьзад",
        'bg': 'дверьсосед',
        'vars_return': (
            {
                'text': 'Забить',
                'func': new_stage,
                'args': 'Stage2.3Choice1.5.1',
            },
            {
                'text': 'Дернуть дверь',
                'func': new_stage,
                'args': 'Stage2.3Choice1.5.2.1',
            },
            {
                'text': 'Продолжить стучать',
                'func': new_stage,
                'args': 'Stage2.3Choice1.5.3.1',
            },

        ),
        'scale_unit': conf.size1,
        'unit_offset_y': conf.y1,
        'unit_offset_x': -310,
    },
    'Stage2.3Choice2.1': {
        'text': 'Ладно, попробуем зайти по-плохому. Я протягиваю руку к старой металлической ручке.',
        'name_unit': "Игорь",
        'unit': "игорьзад",
        'bg': 'дверьсосед',
        'vars_return': (
            {
                'text': 'Далее...',
                'func': new_stage,
                'args': 'Stage2.3Choice2.2',
            },

        ),
        'scale_unit': conf.size1,
        'unit_offset_y': conf.y1,
        'unit_offset_x': -310,
    },
    'Stage2.3Choice2.2': {
        'text': 'Она поддается. Дверь оказалась совершенно не заперта. Какой нормальный человек оставляет квартиру открытой ночью?',
        'name_unit': "Игорь",
        'unit': "игорьзад",
        'bg': 'дверьсосед',
        'vars_return': (
            {
                'text': 'Далее...',
                'func': new_stage,
                'args': 'Stage2.3Choice2.3',
            },

        ),
        'scale_unit': conf.size1,
        'unit_offset_y': conf.y1,
        'unit_offset_x': -310,
    },
    'Stage2.3Choice2.3': {
        'text': 'Я медленно приоткрываю дверь. Изнутри пахнет сыростью и старыми газетами',
        'name_unit': "Игорь",
        'unit': "игорьзад",
        'bg': 'дверьсоседоткрыта',
        'vars_return': (
            {
                'text': 'Далее...',
                'func': new_stage,
                'args': 'Stage3.1',
            },

        ),
        'scale_unit': conf.size1,
        'unit_offset_y': conf.y3,
        'unit_offset_x': conf.x3,
    },
    'Stage2.3Choice3.1': {
        'text': 'Я поднял руку над дверь и тут… Я вспомнил своих друзей, свою первую любовь, свои первые шаги…',
        'name_unit': "Игорь",
        'unit': "игорьгрустный",
        'bg': 'дверьсосед',
        'vars_return': (
            {
                'text': 'Далее...',
                'func': new_stage,
                'args': 'Stage2.3Choice3.2',
            },

        ),
        'scale_unit': conf.size1,
        'unit_offset_y': conf.y3,
        'unit_offset_x': -310,
    },
    'Stage2.3Choice3.2': {
        'text': 'Я, с тоской на лице, методично напевал мотивы, немного смахивающие на молодежный Кьют-рок, развернулся и ушел назад к себе в квартиру',
        'name_unit': "Игорь",
        'unit': "игорьгрустный",
        'bg': 'дверьсосед',
        'vars_return': (
            {
                'text': 'Далее...',
                'func': new_stage,
                'args': 'Stage2.3Choice3.3',
            },

        ),
        'scale_unit': conf.size1,
        'unit_offset_y': conf.y3,
        'unit_offset_x': -310,
    },
    'Stage2.3Choice3.3': {
        'text': 'Я лег в свою мягкую, советскую кровать и достал пачку каких-то препаратов из свертка старых, постсоветских газет',
        'name_unit': "Игорь",
        'unit': "игорьгрустный",
        'bg': 'хатастеликом',
        'vars_return': (
            {
                'text': 'Далее...',
                'func': new_stage,
                'args': 'Stage2.3Choice3.4',
            },

        ),
        'scale_unit': conf.size1,
        'unit_offset_y': conf.y3,
        'unit_offset_x': conf.x3,
    },
    'Stage2.3Choice3.4': {
        'text': 'Я принял одну из столь красивых таблеток. Больше меня ничего не волновало: ни шум его старого холодильник, ни стук по облезшим батареям, ни гул, разносившийся откуда-то с улицы…',
        'name_unit': "Игорь",
        'unit': "игорьгрустный",
        'bg': 'хатастеликом',
        'vars_return': (
            {
                'text': 'Далее...',
                'func': new_stage,
                'args': 'Stage2.3Choice3.5',
            },

        ),
        'scale_unit': conf.size1,
        'unit_offset_y': conf.y3,
        'unit_offset_x': conf.x3,
    },
    'Stage2.3Choice3.5': {
        'text': 'На следующее утро тело Игоря нашли в его кровати бездушным и оставшим',
        'name_unit': " ",
        'unit': "игорьгрустный",
        'bg': 'конецигра',
        'vars_return': (
            {
                'text': 'Новая игра',
                'func': new_stage,
                'args': 'Stage1.1',
            },

        ),
        'scale_unit': conf.size1,
        'unit_offset_y': conf.y3,
        'unit_offset_x': -6000,
    },
    'Stage2.3Choice1.5.1': {
        'text': 'Я, бормоча себе под нос кучу грязных ругательств, решаюсь на еще одну попытку',
        'name_unit': "Игорь",
        'unit': "игорьзад",
        'bg': 'дверьсосед',
        'vars_return': (
            {
                'text': 'Далее...',
                'func': new_stage,
                'args': 'Stage2.3Choice3.1',
            },

        ),
        'scale_unit': conf.size1,
        'unit_offset_y': conf.y3,
        'unit_offset_x': -310,
    },
    'Stage2.3Choice1.5.2.1': {
        'text': 'Я вспоминаю, как мы с батей ездили на рыбалку. После рыбалки мы всегда заходили к другу отца, Дяде Паше, я мог обсудить с ним почти все, начиная от прогулок в лесу, заканчивая тем, на что лучше ловить маленьких карасиков для ебли. Паша вел отшельнический образ жизни и поэтому очень часто не запирал входную дверь. ',
        'name_unit': "Игорь",
        'unit': "игорьзад",
        'bg': 'дверьсосед',
        'vars_return': (
            {
                'text': 'Далее...',
                'func': new_stage,
                'args': 'Stage2.3Choice1.5.2.2',
            },

        ),
        'scale_unit': conf.size1,
        'unit_offset_y': conf.y3,
        'unit_offset_x': -310,
    },
    'Stage2.3Choice1.5.2.2': {
        'text': 'И тут я подумал, была не была…',
        'name_unit': "Игорь",
        'unit': "игорьзад",
        'bg': 'дверьсосед',
        'vars_return': (
            {
                'text': 'Попробовать дернуть ручку двери',
                'func': new_stage,
                'args': 'Stage2.3Choice2.1',
            },

        ),
        'scale_unit': conf.size1,
        'unit_offset_y': conf.y3,
        'unit_offset_x': -310,
    },
    'Stage2.3Choice1.5.3.1': {
        'text': 'Я решаю попробовать новые поз.. способы стука и вспоминаю мультик феечки винкс. Я достал волшебную пыль из кармана, наполнил ею кулак и сделал три легкий касания двери',
        'name_unit': "Игорь",
        'unit': "игорьзад",
        'bg': 'дверьсосед',
        'vars_return': (
            {
                'text': 'Далее...',
                'func': new_stage,
                'args': 'Stage2.3Choice1.5.3.2',
            },

        ),
        'scale_unit': conf.size1,
        'unit_offset_y': conf.y3,
        'unit_offset_x': -310,
    },
    'Stage2.3Choice1.5.3.2': {
        'text': 'Тук, тук, тук',
        'name_unit': "Игорь",
        'unit': "игорьзад",
        'bg': 'дверьсосед',
        'vars_return': (
            {
                'text': 'Продолжить стучать',
                'func': new_stage,
                'args': 'Stage2.3Choice1.5.3.3',
            },
            {
                'text': 'Забить',
                'func': new_stage,
                'args': 'Stage2.3Choice3.1',
            },

        ),
        'scale_unit': conf.size1,
        'unit_offset_y': conf.y3,
        'unit_offset_x': -310,
    },
    'Stage2.3Choice1.5.3.3': {
        'text': 'Как говорится: “Бог любит троицу”, но сосед с трех раз не открыл.',
        'name_unit': "Игорь",
        'unit': "игорьзад",
        'bg': 'дверьсосед',
        'vars_return': (
            {
                'text': 'Далее...',
                'func': new_stage,
                'args': 'Stage2.3Choice1.5.3.4',
            },

        ),
        'scale_unit': conf.size1,
        'unit_offset_y': conf.y3,
        'unit_offset_x': -310,
    },
    'Stage2.3Choice1.5.3.4': {
        'text': 'Я решился на крайние меры. Я намотал свой пиджак на руку и начал неумолимо долбить в дверь. От таких действий даже посыпалась старая советская штукатурка со стен вокруг двери',
        'name_unit': "Игорь",
        'unit': "игорьзад",
        'bg': 'дверьсосед',
        'vars_return': (
            {
                'text': 'Далее...',
                'func': new_stage,
                'args': 'Stage2.3Choice1.5.3.5',
            },

        ),
        'scale_unit': conf.size1,
        'unit_offset_y': conf.y3,
        'unit_offset_x': -310,
    },
    'Stage2.3Choice1.5.3.5': {
        'text': 'ТУК, ТУК, ТУК',
        'name_unit': "Игорь",
        'unit': "игорьзад",
        'bg': 'дверьсосед2',
        'vars_return': (
            {
                'text': 'Далее...',
                'func': new_stage,
                'args': 'Stage2.3Choice1.5.3.6',
            },

        ),
        'scale_unit': conf.size1,
        'unit_offset_y': conf.y3,
        'unit_offset_x': -310,
    },
    'Stage2.3Choice1.5.3.6': {
        'text': 'ТУК, ТУК',
        'name_unit': "Игорь",
        'unit': "игорьзад",
        'bg': 'дверьсосед2',
        'vars_return': (
            {
                'text': 'Далее...',
                'func': new_stage,
                'args': 'Stage2.3Choice1.5.3.7',
            },

        ),
        'scale_unit': conf.size1,
        'unit_offset_y': conf.y3,
        'unit_offset_x': -310,
    },
    'Stage2.3Choice1.5.3.7': {
        'text': 'ТУК',
        'name_unit': "Игорь",
        'unit': "игорьзад",
        'bg': 'дверьсосед2',
        'vars_return': (
            {
                'text': 'Далее...',
                'func': new_stage,
                'args': 'Stage2.3Choice1.5.3.8',
            },

        ),
        'scale_unit': conf.size1,
        'unit_offset_y': conf.y3,
        'unit_offset_x': -310,
    },
    'Stage2.3Choice1.5.3.8': {
        'text': 'Так я стучал до самого утра… Примерно в 6 часов по Москве я почувствовал, что мои ноги начали подкашиваться, глаза начали закрываться и я упал на холодный, кафельный пол… *Игорь теряет сознание*',
        'name_unit': "Игорь",
        'unit': "игорьзад",
        'bg': 'дверьсосед2',
        'vars_return': (
            {
                'text': 'Далее...',
                'func': new_stage,
                'args': 'Stage4.1',
            },

        ),
        'scale_unit': conf.size1,
        'unit_offset_y': conf.y3,
        'unit_offset_x': -310,
    },
    'Stage3.1': {
        'text': 'Я перешагиваю порог. В коридоре полнейшая темнота, только трубы вдоль стен тускло поблескивают.',
        'name_unit': "Игорь",
        'unit': "игорьзад",
        'bg': 'соседхата',
        'vars_return': (
            {
                'text': 'Далее...',
                'func': new_stage,
                'args': 'Stage3.2',
            },

        ),
        'scale_unit': conf.size1,
        'unit_offset_y': conf.y3,
        'unit_offset_x': -6000,
    },
    'Stage3.2': {
        'text': 'Эй! Хозяева! Я сейчас полицию вызову, если не прекратите этот дурдом!',
        'name_unit': "Игорь",
        'unit': "игорьзад",
        'bg': 'соседхата',
        'vars_return': (
            {
                'text': 'Далее...',
                'func': new_stage,
                'args': 'Stage3.3',
            },

        ),
        'scale_unit': conf.size1,
        'unit_offset_y': conf.y3,
        'unit_offset_x': -6000,
    },
    'Stage3.3': {
        'text': 'Ответа нет. Только ритмичный, оглушительный грохот, который теперь идет как будто отовсюду.',
        'name_unit': "Игорь",
        'unit': "игорьзад",
        'bg': 'соседхата',
        'vars_return': (
            {
                'text': 'Далее...',
                'func': new_stage,
                'args': 'Stage3.4',
            },

        ),
        'scale_unit': conf.size1,
        'unit_offset_y': conf.y3,
        'unit_offset_x': -6000,
    },
    'Stage3.4': {
        'text': 'Я прохожу дальше по коридору. В темноте, прямо перед окном, стоит высокая, неестественно огромная фигура. Она выглядела так словно большого африканского мальчика напичкали всеми видами анаболиков',
        'name_unit': "Игорь",
        'unit': "игорьзад",
        'bg': 'соседсилует',
        'vars_return': (
            {
                'text': 'Далее...',
                'func': new_stage,
                'args': 'Stage3.5',
            },

        ),
        'scale_unit': conf.size1,
        'unit_offset_y': conf.y3,
        'unit_offset_x': -6000,
    },
    'Stage3.5': {
        'text': 'Руки этой фигуры кажутся слишком огромными, а голова наклонена под неестественным углом.',
        'name_unit': "Игорь",
        'unit': "игорьзад",
        'bg': 'соседсилует',
        'vars_return': (
            {
                'text': 'Далее...',
                'func': new_stage,
                'args': 'Stage3.6',
            },

        ),
        'scale_unit': conf.size1,
        'unit_offset_y': conf.y3,
        'unit_offset_x': -6000,
    },
    'Stage3.6': {
        'text': 'Эй, мужик... с тобой все нормально? - мой голос начинает дрожать, злость сменяется страхом.',
        'name_unit': "Игорь",
        'unit': "игорьзад",
        'bg': 'соседсилует',
        'vars_return': (
            {
                'text': 'Далее...',
                'func': new_stage,
                'args': 'Stage3.7',
            },

        ),
        'scale_unit': conf.size1,
        'unit_offset_y': conf.y3,
        'unit_offset_x': -6000,
    },
    'Stage3.7': {
        'text': 'Фигура медленно разворачивается ко мне. У меня перехватывает дыхание, в глазах темнеет, и я падаю без чувств. *Игорь теряет сознание*',
        'name_unit': "Игорь",
        'unit': "игорьзад",
        'bg': 'соседсилует',
        'vars_return': (
            {
                'text': 'Далее...',
                'func': new_stage,
                'args': 'Stage4.1',
            },

        ),
        'scale_unit': conf.size1,
        'unit_offset_y': conf.y3,
        'unit_offset_x': -6000,
    },
}
