# Test_fabrick
Test_fabrick

## Клонируем реппозиторий:
```
git clone https://github.com/Cxatek18/Test_fabrick.git
cd mailing-service
```

## Ставим виртуальное окружение и заходим в него для linux:
```
python -m venv venv
source venv/bin/activate
```
## Ставим виртуальное окружение и заходим в него для Windows:
```
python -m venv venv
source venv/Scripts/activate
```

## Заходим в проект и запускаем Docker:
```
cd mailing-service
docker-compose up
```

## Выключаем Docker и выходим из виртуального окружения:
```
docker-compose down
deactivate
```
