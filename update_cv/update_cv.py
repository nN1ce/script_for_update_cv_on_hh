import time

from update_cv.login_touch_buttons import first_cv, second_cv, third_cv

if __name__ == "__main__":

    while True:
        try:
            first_cv()
            second_cv()
            third_cv()
            print("Все резюме подняты, ждем 4 часа...")
            time.sleep(14401)

        except:
            print(
                "Все сломалось, либо скрипт не нашел кнопку. \nНо ничего страшного через 4 часа попробую еще раз"
            )
            time.sleep(14401)
