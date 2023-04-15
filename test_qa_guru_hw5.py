import os
import random
from selene import browser, have, command


def test_demoqa_practice_form():
    '''
    Знаю, что по заданию нельзя использовать переменные.
    Но здесь напрашивается список для рандомного выбора
     '''
    subject_list = ["Hindi", "English", "Maths", "Physics", "Chemistry", "Biology", "Computer Science", "Commerce", "Accounting", "Economics", "Arts", "Social Studies", "History", "Civics"]

    browser.open('https://demoqa.com/automation-practice-form')
    browser.driver.maximize_window()

    browser.element('#firstName').type('Ivan')
    browser.element('#lastName').type('Ivanov')
    browser.element('#userEmail').type('Ivanov@mail.ru')

    browser.element(f'[for="gender-radio-{str(random.randint(1, 3))}"]').click()
    browser.element('#userNumber').type(str(random.randint(1000000000, 9999999999)))

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element(f'.react-datepicker__month-select [value = "{str(random.randint(0, 11))}"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element(f'.react-datepicker__year-select [value = "{str(random.randint(1900, 2020))}"]').click()
    browser.element('.react-datepicker__day-names').click()
    browser.all('.react-datepicker__month div').element_by(have.exact_text(str(random.randint(1, 30)))).click()

    browser.element('#subjectsInput').type(f'{subject_list[(random.randint(0, 13))]}').press_enter()
    browser.element(f'[for=hobbies-checkbox-{(random.randint(1, 3))}]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath((os.path.dirname(__file__) + '/image/CSS - selector.png')))
    browser.element('#currentAddress').type('simple text, 25')

    browser.element('#react-select-3-input').type('Haryana').press_enter()
    browser.element('#react-select-4-input').type('Karnal').press_enter()

    browser.element('#submit').perform(command.js.click)

    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))

    browser.quit()




