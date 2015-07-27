# -*- coding: utf-8 -*-

welcome_text = (
'Здравствуйте! Если хотите установить новую напоминалку, выберите команду /newalarm\n\n'
' Пожалуйста, учтите, что в данный момент возможно добавление не более 5 напоминаний')

guide_timezone = (
'Укажите Ваш часовой пояс в формате +x или -x (дробное время не поддерживается)\n\n'
'Внимание! Часовой пояс необходимо указывать относительно Москвы (GMT+3)\n\n')
guide_time = ('Укажите время напоминания. Примеры:\n\n'
              '1. 20:00 - Отправит напоминание сегодня, если ещё нет 20 часов, или завтра в это время\n\n'
              '2. 15:57 20.12.2017 - Отправит напоминание в указанный день и время\n\n'
              '3. утром, днём, вечером, ночью - Отправит напоминание в 08:00, 14:00, 20:00 и в 02:00 соотвественно\n\n'
              'Поддерживаются даты до 31.12.2016 включительно')

reply_is_correct_time = "Я смог определить дату и время как {0!s}\n" \
                        "Если всё правильно, введите текст заметки.\n" \
                        "Если Вы считаете, что я неправильно что-то определил, " \
                        "пожалуйста, нажмите /cancel и начните заново"

reply_too_long_note = ('Заметка не может быть длиннее 1000 символов\n'
                       'Пожалуйста, укоротите заметку и повторите')
