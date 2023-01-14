import time

from selene.support.shared import browser

LOGIN = "evgeniylukyanov2016@yandex.ru"
PASSWORD = "qweAsdzxc1"


def first_cv():

    browser.open_url("https://hh.ru/account/login")
    browser.element("[data-qa=expand-login-by-password]").click()
    browser.element("[data-qa=login-input-username]").send_keys(LOGIN)
    browser.element("[data-qa=login-input-password]").send_keys(PASSWORD)
    browser.element("[data-qa=account-login-submit]").click()
    browser.element("[data-qa=mainmenu_myResumes]").click()
    try:
        browser.element(
            '[data-qa-id="194293263"] [data-qa="resume-update-button_actions"]'
        ).click()
        print("Поднял первое резюме")

    except:
        print("Не вижу кнопки, может уже нажата")
    time.sleep(5)
    browser.open_url(
        'https://hh.ru/applicant/resumes?hhtmFrom=main&hhtmFromLabel=header'
    )


def second_cv():

    try:

        browser.element(
            '[data-qa-id="194303297"] [data-qa="resume-update-button_actions"]'
        ).click()
        print("Поднял второе резюме")

    except:
        print("Не вижу кнопки, может уже нажата")
    time.sleep(5)
    browser.open_url(
        'https://hh.ru/applicant/resumes?hhtmFrom=main&hhtmFromLabel=header'
    )


def third_cv():

    try:

        browser.element(
            '[data-qa-id="194303349"] [data-qa="resume-update-button_actions"]'
        ).click()
        print("Поднял третье резюме")
    except:
        print("Не вижу кнопки, может уже нажата")
    time.sleep(5)
    browser.quit()
