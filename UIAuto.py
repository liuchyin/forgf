#encoding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from selenium import webdriver
import time
import unittest

class gfTest(unittest.TestCase):

		def setUp(self):
				self.driver = webdriver.PhantomJS('/usr/local/bin/phantomjs')
				self.driver.set_window_size(1366, 768) 
				self.driver.get('http://127.0.0.1:8080/')
		
		def test_addNewBook(self):
				'''增加id为10的新书'''
				driver = self.driver
				time.sleep(10)
				driver.find_element_by_id("treeview-1015-record-book_manage").click()
				time.sleep(2)
				driver.find_element_by_id("button-1045-btnIconEl").click()
				time.sleep(2)
				inputid = driver.find_element_by_name("id")
				inputid.send_keys('10')


				inputname = driver.find_element_by_name("name")
				inputname.send_keys('hello')


				inputauthor = driver.find_element_by_name("author")
				inputauthor.send_keys("liuchyin")


				inputyear = driver.find_element_by_name("year")
				inputyear.send_keys("1989")


				inputdigest = driver.find_element_by_name("digest")
				inputdigest.send_keys("myworkd is hello")

				comfirmButton = driver.find_element_by_xpath('//*[@id="input_form"]/div[3]/div/div/a[1]')
				comfirmButton.click()

				time.sleep(2)

				message = driver.find_element_by_id('messagebox-1001-displayfield-inputEl')

				assert "添加书籍成功" == message.text

		def test_addExistedBook(self):
				'''新增id为2的书'''
				driver = self.driver
				time.sleep(10)
				driver.find_element_by_id("treeview-1015-record-book_manage").click()
				time.sleep(2)
				driver.find_element_by_id("button-1045-btnIconEl").click()
				time.sleep(2)
				inputid = driver.find_element_by_name("id")
				inputid.send_keys('2')


				inputname = driver.find_element_by_name("name")
				inputname.send_keys('hello')


				inputauthor = driver.find_element_by_name("author")
				inputauthor.send_keys("liuchyin")


				inputyear = driver.find_element_by_name("year")
				inputyear.send_keys("1989")


				inputdigest = driver.find_element_by_name("digest")
				inputdigest.send_keys("myworkd is hello")

				comfirmButton = driver.find_element_by_xpath('//*[@id="input_form"]/div[3]/div/div/a[1]')
				comfirmButton.click()

				time.sleep(2)

				message = driver.find_element_by_id('messagebox-1001-displayfield-inputEl')

				assert "errorNo:1,errorInfo:该id已存在。" == message.text


		def atest_deleteBook(self):
				'''删除id为5的书'''
				driver = self.driver

				driver.find_element_by_id("treeview-1015-record-book_manage").click()
				time.sleep(2)

				driver.find_element_by_id("gridview-1043-record-4").click()

				driver.find_element_by_id("button-1046-btnInnerEl").click()
				time.sleep(2)
				
				driver.find_element_by_id("button-1006-btnIconEl").click()
				time.sleep(2)

				message = driver.find_element_by_id("messagebox-1001-displayfield-inputEl")
				assert "删除书籍成功！" == message.text

		def atest_modifyAuthor(self):
				'''修改id=3的书的作者'''
				driver = self.driver
				driver.find_element_by_id("treeview-1015-record-book_manage").click()
				time.sleep(2)


				driver.find_element_by_id("gridview-1043-record-3").click()

				driver.find_element_by_id("button-1047-btnInnerEl").click()
				time.sleep(2)

#inputid = driver.find_element_by_name("id")
#inputid.clear()
#inputid.send_keys("10")
#time.sleep(2)
				inputauthor = driver.find_element_by_name("author")
				inputauthor.clear()
				inputauthor.send_keys("liuchyin")


				comfirmButton = driver.find_element_by_xpath('//*[@id="input_form"]/div[3]/div/div/a[1]')
				comfirmButton.click()


				message = driver.find_element_by_id("messagebox-1001-displayfield-inputEl")
				assert  message.text == "更新成功"

		def atest_modifyNewID(self):
				'''将书的ID修改为新的ID12'''
				driver = self.driver
				driver.find_element_by_id("treeview-1015-record-book_manage").click()
				time.sleep(2)


				driver.find_element_by_id("gridview-1043-record-3").click()

				driver.find_element_by_id("button-1047-btnInnerEl").click()
				time.sleep(2)

				inputid = driver.find_element_by_name("id")
				inputid.clear()
				inputid.send_keys("12")
				time.sleep(2)


				comfirmButton = driver.find_element_by_xpath('//*[@id="input_form"]/div[3]/div/div/a[1]')
				comfirmButton.click()


				message = driver.find_element_by_id("messagebox-1001-displayfield-inputEl")
				assert  message.text == "errorNo:1,errorInfo:该id不存在。"

		def atest_modifyExistedID(self):
				'''将书的ID修改为已存在的ID1'''
				driver = self.driver
				driver.find_element_by_id("treeview-1015-record-book_manage").click()
				time.sleep(2)


				driver.find_element_by_id("gridview-1043-record-5").click()

				driver.find_element_by_id("button-1047-btnInnerEl").click()
				time.sleep(2)

				inputid = driver.find_element_by_name("id")
				inputid.clear()
				inputid.send_keys("1")
				time.sleep(2)


				comfirmButton = driver.find_element_by_xpath('//*[@id="input_form"]/div[3]/div/div/a[1]')
				comfirmButton.click()


				message = driver.find_element_by_id("messagebox-1001-displayfield-inputEl")
				assert  message.text == "errorNo:1,errorInfo:该id已存在。"




		def tearDown(self):
				self.driver.close()

if __name__ == "__main__":
		unittest.main()

