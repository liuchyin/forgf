#UI自动化测试脚本

1. 解决方案  
我采用了selenium+phantomjs来实现UI自动化测试。selenium是流行的web UI自动化测试框架，不再赘述。选择phantomjs是因为它是脱离实际浏览器的UI测试引擎，可以部署在服务端。
2. 编写脚本  
selenium编写自动化脚本的思路主要是通过id、xpath定位页面上的元素，再模拟点击、输入等操作，最后通过UI元素判断执行结果是否符合预期。  
以addBook功能的测试脚本为例，详细介绍一个脚本的编写思路。

		#找到图书管理按钮并点击
		driver.find_element_by_id("treeview-1015-record-book_manage").click()
		#等待页面渲染
		time.sleep(2)
		#找到添加按钮并点击
		driver.find_element_by_id("button-1045-btnIconEl").click()
		time.sleep(2)
		
		#找到弹出的对话框中的5个输入框。这几个输入框是动态id，使用name来定位元素
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

		#找到确定按钮并点击。按钮是动态id并且没有name，使用xpath定位元素
		comfirmButton = driver.find_element_by_xpath('//*[@id="input_form"]/div[3]/div/div/a[1]')
		comfirmButton.click()

		time.sleep(2)
		
		#根据弹出的信息，确认结果是否符合预期
		message = driver.find_element_by_id('messagebox-1001-displayfield-inputEl')

		assert "添加书籍成功" == message.text

3. 单元测试框架  
单元测试框架采用了unittest，可以方便的进行用例管理和输出测试结果

4. 测试case  
由于时间关系，实现了如下case:
	1. 增加一本新书
	2. 增加一本id已经存在的书
	3. 删除一本书
	4. 修改一本书的作者
	5. 将一本书ID改为新ID
	6. 将一本书ID改为另一本书

5. 执行结果  
第6个case执行失败，实际结果是修改了另一本书的内容。

#接口自动化测试脚本

1. 解决方案  
我采用了pyresttest框架进行接口自动化测试
2. 编写脚本  
pyresttest封装了网络请求，结果解析等底层操作，只需按照格式编写测试case即可。下面以getBookList接口的测试进行说明。

		- test:  #一个case
	    	- group: "getBookList"   #casesuit命名
	    	- name: "getBookList"	#case命名
	    	- url: "/test/book/getBookList" #测试url
	    	- method: "POST"		#请求方法
	    	- validators:		#返回值校验脚本
	    		#检验书本数量大于0
	        	- compare: {jsonpath_mini: "totalProperty",     comparator: "gt",    expected: 0}	
	        	#检验书本数量和书本数组长度一致
	        	- compare: {jsonpath_mini: "root",     comparator: "count_eq",    expected: {jsonpath_mini: "totalProperty"}}
	        	#检验year字段是否存在
	        	- extract_test: {jsonpath_mini: "root.0.year",     test: 'exists'}
	        	#检验year字段类型为int
	        	- compare: {jsonpath_mini: "root.0.year",     comparator: "type",    expected: "int"}
	        	- extract_test: {jsonpath_mini: "root.0.id",     test: 'exists'}
	        	- compare: {jsonpath_mini: "root.0.id",     comparator: "type",    expected: "int"}
	        	- extract_test: {jsonpath_mini: "root.0.name",     test: 'exists'}
	        	- compare: {jsonpath_mini: "root.0.name",    comparator: "type",    expected: "string"}
	        	- extract_test: {jsonpath_mini: "root.0.author",     test: 'exists'}
	        	- compare: {jsonpath_mini: "root.0.author",    comparator: "type",    expected: "string"}
	        	- extract_test: {jsonpath_mini: "root.0.digest",     test: 'exists'}
	        	- compare: {jsonpath_mini: "root.0.digest",    comparator: "type",    expected: "string"}
	        	#检验所有的id都大于0
	        	- compare: {jmespath: "min_by(root, &id).id",     comparator: 'gt', expected: 0}
4. 测试case  
时间关系，编写了如下测试case
	1. 获取书本列表
	2. 增加一本新书
	3. 删除一本新书，id已经存在	
	4. 修改一本书的属性
	5. 修改一本书的属性，但id不存在
	6. 删除一本书
	7. 删除一本书，但id不存在

4. 测试结果  
case全部测试通过
