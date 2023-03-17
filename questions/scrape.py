import time , tqdm
 
import pandas as pd 
from selenium import webdriver 
from selenium.webdriver import Chrome 
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# start by defining the options 
options = webdriver.ChromeOptions() 
options.add_argument("--headless")
options.page_load_strategy = 'none' 

chrome_path = ChromeDriverManager().install() 
chrome_service = Service(chrome_path) 
driver = Chrome(options=options, service=chrome_service) 
driver.implicitly_wait(5)

url = "https://www.proprofs.com/quiz-school/quizshow.php?title=ymca-level-3-anatomy-and-physiology-300-question-revision-mock-paper-final-version_60y" 
 
driver.get(url) 
time.sleep(4)


driver.execute_script("document.querySelector('button[name=\"mySubmit\"]').click()")

time.sleep(4)


collection = []
timeout = 10
wait = WebDriverWait(driver, timeout)


def scratch(q):

    driver.execute_script(f'return jumpQuestion_free({q}, true)')

    wait.until(
        lambda driver: driver.current_url.split('=')[-1] == str(q)
    )

    question = wait.until(
        EC.visibility_of_element_located((By.ID, "m_question_desc"))
    ).text

    answers = driver.execute_script('return [...document.querySelectorAll(\'div[class="text_style 1"]\')].map(d=>d.outerText)')

    driver.execute_script('document.querySelectorAll(\'label[class="labelHover"]\')[0].click()')


    correct = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[class="correctTxt"]'))).text

    return question, correct, answers



failed=[]
for q in tqdm.tqdm(range(1,301)):
    
    try: 
        a = scratch(q)
        collection.append(a)
    except:
        print('!!!!!!!! fail !!!!!!!!!: ',q)
        failed.append(q)



# rework any fails 
print(len(failed))
for f in tqdm.tqdm(failed):
    try: collection.append(scratch(f))
    except:...


df = pd.DataFrame(collection,columns=['question', 'correct', 'options'])

df.to_csv('l3ap.csv')