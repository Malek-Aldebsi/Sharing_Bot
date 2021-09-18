from selenium import webdriver
import random
import time

PATH = "D:\malek\chrome_driver\chromedriver.exe"
driver = webdriver.Chrome(PATH)


#####################################################################

def click(xpath):
    while True:
        try:
            button = driver.find_element_by_xpath(xpath)
            button.click()
            time.sleep(1)
            break

        except:
            time.sleep(0.01)
            continue


def write(xpath, word):
    while True:
        try:
            search_box = driver.find_element_by_xpath(xpath)
            search_box.send_keys(word)
            time.sleep(1)
            break
        except:
            time.sleep(0.01)
            continue


def open_url(url):
    driver.get(url)


####################################################################

my_user_name = input()
password = input()
groups = ['| اكبر مجتمع عربي لبايثون Python Community',
          'Machine Learning/ Artificial Intelligence/ Data Mining/ Deep Learning',
          'تكنولوجيا الذكاء الاصطناعي| - Arduino + | AI+DP+LM',
          'مجتمع الذكاء الصناعي العربي',
          'Artificial intelligence, Machine learning, Deep learning',
          'علم البيانات, تعلم الآلة, الذكاء الاصطناعي Machine Learning , Data Science',
          'التعليم الالي بالعربي',
          'artificial intelligence | الذكاء الاصطناعي',
          'Intelligence artificielle - الذكاء الاصطناعي',
          'مجلة الذكاء الإصطناعي',
          'Zenon | هندسة الكهرباء والحاسوب | الجامعة الأردنية',
          'عائلة البرمجة',
          'المكتبة التقنية لتعلم البرمجة',
          'مساق الذكاء الاصطناعي (إدراك)',
          'تقنيات تعليم الألة و التعليم العميق Machine Learning , Deep Learning',
          'KASIT TEAM',
          'Power Unit - JU',
          'مبرمجين الاردن',
          'coders society مجتمع المبرمجين',
          'AI evolution & ML ,DLتقنيات تعليم الألة و التعليم العميق',
          'Deep Learning and Machine Learning',
          'Machine Learning - بالعربي‎ شرح',
          'Data Science World',
          'الذكاء الاصطناعي بالعربي',
          'رابطة محبي الذكاء الاصطناعى وعلوم البيانات Artificial intelligence & Data',
          'AI ، Machine learning ، Deep learning DZ',
          'python beginners مبتدء في بايثون',
          'تعلم البرمجة بلغة بايثون - Learn Python with Enigma Code',
          'مبرمجين مصر المحترفين',
          'طلاب كلية الهندسة التكنولوجية',
          'Smart Team',
          'لجنة هندسة الحاسوب | JCE Group',
          '"Zmex" اللجنة الأكاديمية في قسم الميكاترونكس',
          'سنافر الجامعة الأردنية 2020',
          'نقابة المبرمجين الأردنيين',
          'IT Questions',
          'Python Programming',
          'لغة البرمجة بايثون',
          'مبادرة المليون مبرمج عربي: فريق مبرمجين أندرويد - تجمع الطلاب',
          'Artificial Intelligence and Machine Learning',
          'تعلم البرمجة مع كودر شيار - Coder Shiyar',
          'المبرمجون العرب',
          'تعلم معنا البرمجة C++,C#,Java,SQL,Swift,Python',
          'Developers & Programming | Python, HTML, Java, SQL, Javascript, C#, C++ PHP',
          'قعدة مبرمجين',
          'إتحاد طلاب الروبوت في الوطن العربي',
          'عالم البرمجة - The world of programming',
          'Computer Vision',
          'مجتمع العربي للبرمجة',
          '√ إحترف البرمجة معنا ™']
mes = [input(),input()]
post = input()

open_url('https://ar-ar.facebook.com/')
write('//*[@id="email"]', my_user_name)
write('//*[@id="pass"]', password)
click('/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button')
open_url(post)
time.sleep(15)
print("we are go ahead")
time.sleep(5)
for i in groups:
    mess = random.choice(mes)
    click(
        "//div[starts-with(@id,'mount_0_0_')]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div[4]/div/div/div[1]/div/div[2]/div/div[3]/div/div[1]/div[2]/span")
    click(
        "//div[starts-with(@id,'mount_0_0_')]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div/div/div[1]/div/div[4]/div/div[1]/div[2]/div/div/div/div/span/span")
    write(
        "//div[starts-with(@id,'mount_0_0_')]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/div[2]/div[2]/div/div[1]/div/div/label/input",
        i)
    click(
        "//div[starts-with(@id,'mount_0_0_')]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div/div/div[2]/div/div[1]/div/div[1]/div[2]/div[1]/div/div/div[1]/span")
    write(
        "//div[starts-with(@id,'mount_0_0_')]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/form/div/div[1]/div/div/div[1]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div/div/div/div",
        mess)
    click(
        "//div[starts-with(@id,'mount_0_0_')]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/form/div/div[1]/div/div/div[1]/div/div[3]/div[2]/div/div/div/div[1]/div/span/span")