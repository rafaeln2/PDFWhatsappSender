import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from dotenv import load_dotenv

CONTACT = os.getenv("WHATSAPP_CONTACT") # Nome do contato na agenda
PDF_FOLDER = os.getenv("PDF_FOLDER") # pasta onde vai ter os arquivos PDF
CHROMEDRIVER_PATH = os.getenv("CHROMEDRIVER_PATH") # driver do navegador chrome

load_dotenv()

def send_pdfs():
    service = Service(CHROMEDRIVER_PATH)
    driver = webdriver.Chrome(service=service)

    driver.get("https://web.whatsapp.com")
    input("📲 Escaneie o QR Code e aperte ENTER...")

    # Buscar contato
    search_box = driver.find_element(By.XPATH, "//div[@contenteditable='true'][@data-tab='3']")
    search_box.click()
    search_box.send_keys(CONTACT)
    time.sleep(2)
    search_box.send_keys(Keys.ENTER)
    time.sleep(2)

    # Enviar PDFs
    for arquivo in os.listdir(PDF_FOLDER):
        if arquivo.lower().endswith(".png"):
            caminho = os.path.join(PDF_FOLDER, arquivo)
            print(f"📤 Enviando: {arquivo}")

            clip_button = driver.find_element(By.XPATH, "//div[@title='Anexar']")
            clip_button.click()
            time.sleep(1)

            file_input = driver.find_element(By.XPATH, "//input[@accept='*']")
            file_input.send_keys(caminho)
            time.sleep(2)

            send_button = driver.find_element(By.XPATH, "//span[@data-icon='send']")
            send_button.click()
            time.sleep(1)

    print("✔ Todos PDFs enviados!")
    driver.quit()


if __name__ == "__main__":
    send_pdfs()