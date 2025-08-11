# install: pip install selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ใช้ Chrome (ปรับตาม webdriver ที่คุณมี)
driver = webdriver.Chrome()  

try:
    # เปิดไฟล์ local (ปรับ path ให้ตรงเครื่องของคุณ)
    driver.get("file:///full/path/to/index.html")  # ตัวอย่าง: file:///C:/Users/me/local_test.html

    wait = WebDriverWait(driver, 10)

    # รอ input ชื่อ ป้อนค่า
    name_input = wait.until(EC.presence_of_element_located((By.ID, "name")))
    name_input.clear()
    name_input.send_keys("สมชาย")

    # เลือกจำนวน (ตัวอย่างเลือก 2)
    qty = driver.find_element(By.ID, "qty")
    for option in qty.find_elements(By.TAG_NAME, "option"):
        if option.text == "2":
            option.click()
            break

    # รอปุ่ม แล้วคลิก
    buy_btn = wait.until(EC.element_to_be_clickable((By.ID, "buy-btn")))
    buy_btn.click()

    # ตรวจสถานะ
    status = wait.until(EC.text_to_be_present_in_element((By.ID, "status"), "จองเรียบร้อย"))
    print("Status text updated — test successful")

finally:
    driver.quit()