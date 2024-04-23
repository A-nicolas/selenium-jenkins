import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    # Initialiser le navigateur
    driver = webdriver.Chrome()
    yield driver
    # Fermer le navigateur à la fin du test
    driver.quit()

def test_google_page(browser):
    # Charger la page Google
    browser.get("https://www.google.com")
    # Vérifier que le titre de la page contient "Google"
    assert "Google" in browser.title
