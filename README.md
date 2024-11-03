# Сайт с интерактивной картой Москвы

## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` в корневом каталоге проекта и 
запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Доступны 4 переменные:
- `SECRET_KEY`= секретный ключ проекта
- `DEBUG`= дебаг-режим. Поставьте True, чтобы увидеть отладочную информацию в случае ошибки.
- `ALLOWED_HOSTS` — см. [документацию Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts)
- `DB_NAME` = название вашей БД(Например: ` 'db.sqlite3' `)

## Как установить
Python3.10 должен быть уже установлен. Затем используйте `pip` для установки зависимостей:

```
pip install -r requirements.txt
```

Создать БД:

```
python manage.py migrate
```

Создать суперпользователя:

```
python manage.py createsuperuser
```

Запустить сервер командой:

```
python manage.py runserver
```

Для того чтобы перейти на сервер, воспользуйтесь [локальным адресом](http://127.0.0.1:8000/)

## Сценарии использования

Если необходимо использовать проект на локальном компьютере, то перейдите в [админ панель](http://127.0.0.1:8000/admin)

1. Далее выбрать `Места`
2. Добавить новое место на карту, заполняя все пункты
3. Нажать кнопку сохранить.
4. Перейти обратно на сайт и проверить добавленное место.

Также проект задеплоен на сервере, для его просмотра перейдите по ссылке [Яндекс афиша](https://mishaone.pythonanywhere.com/)

Для того чтобы перейти в админку необходимо перейти по ссылке [Админка](https://mishaone.pythonanywhere.com/admin/) и ввести логин и пароль

- Логин - User
- Пароль - 1234

Если вам необходимо добавить место или несколько мест и у вас есть правильно заполненный файл json, например:

```
{
    "title": "Водопад Радужный",
    "imgs": [
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/7252a5cbb831eec01d98f3c234f2dfc5.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/c0191d876a75c05d72d9845251758b34.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/3daa4472d29bc5e3c82a62edb7ea6cfe.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/b6bd1cb01af50fa7ab1ffd09ac7b0f58.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/17cf1ed6097edcf70824e87c414ed420.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/b6a19f8f3daa32bdf904c1d7bf80f940.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/6cc194af04b385b4b439dab0f81ebdda.jpg"
    ],
    "description_short": "Центральная Россия — край водопадов! Не верите? А зря.",
    "description_long": "<p>Вас привлекает романтика природы? Горные ручьи и водопады грезятся во снах и видениях, а до отпуска ещё как до луны? Не переживайте: всего в сорока пяти километрах от столицы вас ждёт удивительное природное творение — водопад Радужный. Ради него стоит прокатиться по Калужской автостраде практически до населённого пункта Папино, затем повернуть направо около моста через речку Нару возле заправочной станции, а там — после монумента героям Великой Отечественной войны по просёлочному тракту метров тридцать, и вы уже слышите манящий шум падающей воды.</p><p>Ваша настойчивость будет щедро вознаграждена. Крутая излучина реки Нара открывает взору удивительную долину семи ключей. Пробившись из-под земли, они сливаются в один мощный поток, который срывается с обрыва высотой в несколько метров. Радуга играет в брызгах чистейшей ледяной воды, а дальше с густо покрытого мхом берега стекают ручейки поменьше и совсем крошечные, образующие каскад уровнем ниже.</p><p>Проведите день в таком месте, побродите под сенью деревьев, усладив свой взор и слух, и вы со спокойной душой доживёте до ближайшего отпуска.</p>",
    "coordinates": {
        "lng": "36.940988",
        "lat": "55.20653999999999"
    }
}
```

То для его загрузки напишите в консоль команду и укажите ссылку на raw из Github:

Для одного места:

```
python manage.py load_place https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/Водопад%20Радужный.json     
```

Для нескольких мест:

```
python manage.py load_place 'https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/Водопад%20Радужный.json', 'https://raw.githubusercontent.com/devmanorg/where-to-go-places/refs/heads/master/places/Антикафе%20Bizone.json',
'https://raw.githubusercontent.com/devmanorg/where-to-go-places/refs/heads/master/places/Арт-пространство%20«Бункер%20703».json'
```

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman.org](https://dvmn.org).
