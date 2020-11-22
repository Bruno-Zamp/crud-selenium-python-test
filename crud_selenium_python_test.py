import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):
    # define number of repetitions
    rep = 5

    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver')

    def test_1_clear_all_items(self):
        driver = self.driver
        driver.get("http://localhost:3000/")
        self.assertIn("Crud Reactjs", driver.title)
        # get musics length
        app_list = driver.find_element_by_class_name("App-list")
        app_items = app_list.find_elements_by_class_name("App-item")
        app_items_len = len(app_items)
        print('number of itens found: ' + str(app_items_len))
        # remove all itens
        for i in reversed(range(app_items_len)):
            print('rem child [' + str(i) + ']')
            button = app_items[i].find_element_by_name('remove_button')
            if button: button.click()
        # compare if all musics are removed
        app_list = driver.find_element_by_class_name("App-list")
        app_items = app_list.find_elements_by_class_name("App-item")
        app_items_len = len(app_items)
        self.assertEqual(0 , app_items_len)

    def test_2_add_item(self):
        driver = self.driver
        driver.get("http://localhost:3000/")
        self.assertIn("Crud Reactjs", driver.title)
        # get musics length
        app_list = driver.find_element_by_class_name("App-list")
        app_items = app_list.find_elements_by_class_name("App-item")
        app_items_len = len(app_items)
        # input music information
        app_form = driver.find_element_by_class_name("App-form")
        for i in range(self.rep):
            musica = app_form.find_element_by_name('musica')
            musica.clear()
            musica.send_keys(f'Musica {i}')
            banda = app_form.find_element_by_name('banda')
            banda.clear()
            banda.send_keys(f'Banda {i}')
            ano = app_form.find_element_by_name('ano')
            ano.clear()
            ano.send_keys('1234')
            genero = app_form.find_element_by_name('genero')
            genero.clear()
            genero.send_keys(f'Genero {i}')
            # add new music
            button = app_form.find_element_by_name('adicionar')
            button.click()
        # compare with added value
        app_list = driver.find_element_by_class_name("App-list")
        app_items = app_list.find_elements_by_class_name("App-item")
        app_items_len_new = len(app_items)
        self.assertEqual(app_items_len_new , app_items_len + self.rep)
        # remove item

    def test_3_remove_item(self):
        driver = self.driver
        driver.get("http://localhost:3000/")
        self.assertIn("Crud Reactjs", driver.title)
        # get itens
        app_list = driver.find_element_by_class_name("App-list")
        app_items = app_list.find_elements_by_class_name("App-item")
        app_items_len = len(app_items)
        # remove itens
        for i in reversed(range(self.rep)):
            print('rem child [' + str(i) + ']')
            button = app_items[i].find_element_by_name('remove_button')
            if button: button.click()
        # compare with length value removed
        app_list = driver.find_element_by_class_name("App-list")
        app_items = app_list.find_elements_by_class_name("App-item")
        app_items_len_new = len(app_items)
        self.assertEqual(app_items_len_new , app_items_len - self.rep)

    def tearDown(self):
        print('finishing...')
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
