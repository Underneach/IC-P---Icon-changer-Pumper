# IC&P - Icon-changer-Pumper


![icp](https://github.com/Underneach/ICP---Icon-changer-Pumper/assets/137613889/9b150788-914e-4e99-aa25-456427e79159)

## Общая информация

    Написано на PyQt5
    Возможность закрепления окна поверх остальных
    Сделана обработка ошибок практически везде
    Работа с файлом происходит в отдельных потоках (UI не будет зависать)
    Работа с .exe / .scr
    Смена иконки работает с Meta/Redline и Pyinstaller билдами (так же должно работать и с остальными билдами)
    Не несу ответственность за отстук и работоспособность билда, сомневаетесь в работе - проверьте его

## Смена иконки
    Происходит через CLI обращение к бинарнику Resource Hacker, намного ускоряет работу по сравнению с ручной сменой иконки через сам RH.
    Есть две маски - для Native и Net/Pyinstaller билдов.

## Pumper
Дописывает нули в конец файла, увеличивая его вес, при работе с архивами не забудьте указать нулевое сжатие, иначе памп пропадёт

    b_fSize = self.pump_size * pow(1024, 2)
    buffer = 256
    pumpFile = open(file_path, "wb")
    for i in range(int(b_fSize / buffer)):
        pumpFile.write((b"0" * buffer))
    pumpFile.close()

## Скачать
    https://github.com/Underneach/ICP---Icon-changer-Pumper/releases/tag/1.3
