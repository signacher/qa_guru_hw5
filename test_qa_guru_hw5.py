import os
from selene import browser, have, command


def test_demoqa_practice_form():
    browser.open('/automation-practice-form')

    browser.element('#firstName').type('Ivan')
    browser.element('#lastName').type('Ivanov')
    browser.element('#userEmail').type('Ivanov@mail.ru')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').type('8977777777')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('.react-datepicker__month-select [value = "10"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('.react-datepicker__year-select [value = "1985"]').click()
    browser.element('.react-datepicker__day-names').click()
    browser.all('.react-datepicker__month div').element_by(have.exact_text('12')).click()

    browser.element('#subjectsInput').type('English').press_enter()
    browser.element('[for=hobbies-checkbox-2]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath((os.path.dirname(__file__) + '/image/CSS_selector.png')))
    browser.element('#currentAddress').type('simple text, 25')

    browser.element('#react-select-3-input').type('Haryana').press_enter()
    browser.element('#react-select-4-input').type('Karnal').press_enter()

    browser.element('#submit').perform(command.js.click)

    browser.all('tbody tr').should(have.exact_texts('Student Name Ivan Ivanov', 'Student Email Ivanov@mail.ru', 'Gender Male',
                         'Mobile 8977777777', 'Date of Birth 12 November,1985', 'Subjects English',
                         'Hobbies Reading',
                         'Picture CSS_selector.png', 'Address simple text, 25',
                         'State and City Haryana Karnal'))

    browser.quit()



