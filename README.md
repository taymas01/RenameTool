# RenameTool
-------------------------------------------------------------ENGLISH

⚠ Warning: This code is in an early version and not yet fully completed. Use with caution.

RenameTool-v1.3.py

A Tkinter-based GUI tool for batch renaming files and changing file extensions in a folder. It also supports renaming music files with an author name, playing audio files (.mp3, .wav), displaying images (.jpg, .png), and includes a progress tracker for file modifications.

Features
- Batch rename files in a folder.
- Change file extensions in bulk.
- Rename music files by adding an author name.
- Play audio files (.mp3, .wav).
- Display images (.jpg, .png).
- Progress tracker for file modifications.

Installation

Prerequisites
To run this application, you need the following Python libraries:
- tkinter
- Pillow (for image display)
- pygame (for audio playback)

You can install the required dependencies using pip:

pip install pillow pygame

Running the Application
1. Clone or download the repository.
2. Navigate to the folder where the code is located.
3. Run the script:

python RenameTool-v1.3.py

This will open the GUI where you can select a folder, change file extensions, rename files, and more.

Usage

1. Select a Folder
   Click the "Select" button to choose a folder containing the files you want to modify.

2. Change File Extensions
   Enter the new extension (without the dot) in the "New Extension" field and click "Change" to update all files in the selected folder.

3. Rename Files
   Select a file from the list. Then, in the "Name" field, enter the new file name. Optionally, add an author name in the "Author" field. Click "Apply Changes" to rename the file.

4. Preview Files
   If the file is an audio or image, it will be played or displayed when selected from the list:
   - Audio files (.mp3, .wav) will be played with a message box notification.
   - Image files (.jpg, .png) will be displayed in the window.

5. Progress Bar
   A progress bar will display the status of the operations, showing how many files have been changed.

License
This project is licensed under the MIT License – see the LICENSE file for details.


|||||||||||||||||||||||||||||||||||


----------------------------------RUSSIAN
RenameTool-v1.3.py

⚠ Внимание: Этот проект находится на ранней стадии разработки и ещё не завершён.

Программа с графическим интерфейсом на Tkinter для массового переименования файлов и изменения расширений в папке. Также поддерживает переименование музыкальных файлов с добавлением имени автора, воспроизведение аудиофайлов (.mp3, .wav), отображение изображений (.jpg, .png) и включает индикатор прогресса для модификаций файлов.

Особенности
- Массовое переименование файлов в папке.
- Массовое изменение расширений файлов.
- Переименование музыкальных файлов с добавлением имени автора.
- Воспроизведение аудиофайлов (.mp3, .wav).
- Отображение изображений (.jpg, .png).
- Индикатор прогресса для изменения файлов.

Установка

Необходимые библиотеки
Для работы приложения нужны следующие библиотеки Python:
- tkinter
- Pillow (для отображения изображений)
- pygame (для воспроизведения аудио)

Вы можете установить необходимые зависимости через pip:

pip install pillow pygame

Запуск приложения
1. Клонируйте или скачайте репозиторий.
2. Перейдите в папку с кодом.
3. Запустите скрипт:

python RenameTool-v1.3.py

Это откроет графический интерфейс, в котором можно выбрать папку, изменить расширения файлов, переименовать файлы и многое другое.

Использование

1. Выбор папки
   Нажмите кнопку "Выбрать", чтобы выбрать папку с файлами, которые нужно изменить.

2. Изменение расширений файлов
   Введите новое расширение (без точки) в поле "Новое расширение" и нажмите "Изменить", чтобы обновить все файлы в выбранной папке.

3. Переименование файлов
   Выберите файл из списка. Затем в поле "Название" введите новое имя файла. При желании добавьте имя автора в поле "Автор". Нажмите "Применить изменения", чтобы переименовать файл.

4. Просмотр файлов
   Если файл является аудиофайлом или изображением, он будет воспроизведен или отображен при его выборе:
   - Аудиофайлы (.mp3, .wav) будут воспроизведены с уведомлением.
   - Изображения (.jpg, .png) будут отображены в окне.

5. Индикатор прогресса
   Индикатор прогресса будет показывать статус выполнения операций, указывая, сколько файлов было изменено.

Лицензия
Этот проект лицензирован на условиях MIT License – подробности см. в файле LICENSE.
