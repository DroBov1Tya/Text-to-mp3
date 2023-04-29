from gtts import gTTS  # pip install gtts, art
from art import tprint
from pathlib import Path

print('[Для работы программы необходимо написать полный путь к искомому файлу, учитывая расширение .psd.\nP.S. необходимо чтобы файл с кирилицей имел расширение UTF-8 для корректной работы.\n(Важное примечание!) файлы с изображениями вероятнее всего не будут обработаны] ')

# Создание переменной которая принимает введеный текст
test_text = input('\nEnter your text:')
text = input('\nEnter creating text file name:')

choose = int(input(
    'Если хотите записать текст в файл введите 1, в противном случае введите 2: '))


if choose == 1:
    # создание функции проверяющей наличие файла и его формата
    def text_to_mp3(file_path, language):
        # Создание файла формата .txt, с возможностью перезаписи нового текста поверх стараго в случае повторного запуска
        your_file = open(text +'.txt', "w+")
        your_file.write(test_text)  # Запись текста в файл
        your_file.close  # Закрытие файла для сохранения данных
        if Path(file_path).is_file() and Path(file_path).suffix == '.txt':
            print('[+] Processing...')

            my_audio = gTTS(text=test_text, lang=language)
            file_name = Path(file_path).stem
            my_audio.save(f'{file_name}.mp3')

            return f'[+] {file_name}.mp3 saved succesfull!\n---good luck 888! '
        else:
            return '[File not exists!]'

    def main():
        tprint('TEXT --->> TO --->> MP3', font='bulbhead')
        file_path = input('\nEnter your file path:')
        langugae = input("\nChoose file language, for example 'en': ")
        print(text_to_mp3(file_path=file_path, language=langugae))

    if __name__ == '__main__':
        main()


elif choose == 2:
    def text_to_mp3(language):
        if test_text == test_text:
            print('[+] Processing...')
            my_audio = gTTS(text=test_text, lang=language)
            file_name = 'audio'
            my_audio.save(f'{file_name}.mp3')

            return f'[+] {file_name}.mp3 saved succesfull!\n---good luck 888! '
        else:
            return '[text not exists!]'


    def main():
        tprint('TEXT --->> TO --->> MP3', font='bulbhead')
        langugae = input("\nChoose file language, for example 'en': ")
        print(text_to_mp3(language = langugae))        

    if __name__ == '__main__':
        main()

else:
    ...