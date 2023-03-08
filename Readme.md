# Требования
## 1. Программа для компиляции кода, например:
+ ### PyCharm **(Рекомендуемая)** - [ссылка для скачивания](https://www.jetbrains.com/ru-ru/pycharm/download/#section=windows)
+ ### Visual Studio Code - [ссылка для скачивания](https://code.visualstudio.com/download)
## 2. Три скачанных файла:
+ ### `img-to-xlsx.py`
+ ### `xlsx-to-img.py`
+ ### `test.png`
## 3. Библиотеки Python:
+ ### `Pillow` - для обработки изображения
+ ### `openpyxl` - для взаимодействия с электронными таблицами
+ ### `numpy` - для работы с большими массивами данных
--------
--------

# Получение необходимых файлов:

### Для этого нажмем на зеленую кнопку `Code`:
<img src="https://github.com/Z0DEN/images/blob/main/Contest/Code-button.png" width="90%" height="90%"/>

### Затем `Download ZIP`:
<img src="https://github.com/Z0DEN/images/blob/main/Contest/Download.png" width="55%" height="55%"/>

### Следующим этапом необходимо распаковать скачанный архив в папку `Загрузки`
---
---
# Установка библиотек для `Python`
## 1. Откроем программму-компилятор:
+ ### Pycharm  
+ ### Visual Code
## 2. Откроем терминал:
 + ###  Для PyCharm: **`ALT` + `F12`**
 + ### Для Visual Code: **`CTRL`** + **`SHIFT`** + **`**
## 3. Установим библиотеки, введем команду:
```
pip install Pillow openpyxl numpy
```
<img src="https://github.com/Z0DEN/images/blob/main/Contest/libraries.png" width="80%" height="80%"/>

---
---
# Перевод картинки в `Excel`
## Запуск при помощи `PyCharm`
## 1. Откроем файл `img-to-xlsx.py`

## 2. Запустим код:
### Нажмем комбинацию клавиш **`CTRL` + `SHIFT` + `F10`**
### Во время выполнения программы в консоле вывода будет показан прогресс работы:
<img src="https://github.com/Z0DEN/images/blob/main/Contest/end.png" width="65%" height="65%"/>

## 3. Результат мы можем увидеть открыв файл `img-to-xlsx.xlsx` в папке с кодом: `Загрузки/Excel/Excel/`
<img src="https://github.com/Z0DEN/images/blob/main/Contest/Excel.png" width="65%" height="65%"/>

## Запуск при помощи `Visual Code`
## 1. Откроем файл `img-to-xlsx.py`
## 2. Перед запуском необходимо будет установить сам язык програмирования в виде расширения:
<img src="https://github.com/Z0DEN/images/blob/main/Contest/extension.png" width="50%" height="50%"/>

## 3. Затем запустить программу нажав кнопку в правом верхем углу:
<img src="https://github.com/Z0DEN/images/blob/main/Contest/start.png" width="65%" height="65%"/>

## 4. Результат мы можем увидеть открыв файл `img-to-xlsx.xlsx` в папке с кодом: `Загрузки/Excel/Excel/`
<img src="https://github.com/Z0DEN/images/blob/main/Contest/Excel.png" width="65%" height="65%"/>

---
---
# Перевод изображения из `Excel` в `png`

## Запуск при помощи `PyCharm`
## 1. Откроем файл `img-to-xlsx.py`
## 2. Запустим код:
### Нажмем комбинацию клавиш **`CTRL` + `SHIFT` + `F10`**
### В консоле увидим следующий вывод:
<img src="https://github.com/Z0DEN/images/blob/main/Contest/ENTER.png" width="65%" height="65%"/>

### Строка `"Press Enter to continue..."` означает что прогармма ждет нажатия клавиши `ENTER`, время ожидания неограничено.
## 3. Следующим этапом необходимо открыть файл `pixel_art.xlsx` в папке с кодом. 
### Нарисуем картинку путем закрашивания ячеек. Рисовать необходимо в голубой области.
### Например: 
<img src="https://github.com/Z0DEN/images/blob/main/Contest/PIxel_Art.png" width="65%" height="65%"/>

### Затем закроем электронную таблицу, сохранив файл и перейдем обратно в программу-компилятор. Нажмем клавишу `ENTER`.
## 4. Результат
###  В конечном итоге нарисованная картинка откроется в виде `PNG` Изображения 
## Запуск при помощи `Visual Code`
### Действия для данного компилятора аналогичны действиям в `Pycharm`, однако для запуска необходимо нажать кнопку в правом верхем углу:
<img src="https://github.com/Z0DEN/images/blob/main/Contest/start.png" width="65%" height="65%"/>

---
---
 