* [软件测试分类](#1)
	- 测试阶段
	- 黑白盒测试
	- 功能、性能测试
	- 手工、自动化
	- 冒烟、回归等测试概念
* [什么样的项目适合自动化测试](#2)
*  [分层的自动化测试](#3)
	- [单元测试](#单元)
	- [接口测试](#接口)
	- [UI测试](#UI)
*	[前端web技术](#前端)
*	[元素定位](#元素定位)
*	[鼠标事件ActionChains](#鼠标事件)
*	[expect_conditions](#expect_conditions)
*	[操作cookie](#操作cookie)
*	[自动化前端技术](#前端)
*	[自动化测试模型](#模型)

# 一 软件测试分类
##  1. 根据项目流程阶段划分软件测试
	
	   * 单元测试： 对程序中的单个子程序或具有独立功能的代码段进行测试的过程
	   * 集成测试:  在单元测试的基础上，先通过单元模块组装成系统或子系统，再进行测试，重点是检查模块之间的接口是否正确。
	   * 系统测试： 对整个产品系统进行测试，验证系统是否满足需求规格的定义，以及软件系统的正确性和性能是否满足其需求规格的要求
	   * 验收测试： 确保软件准备就绪，向软件购买者展示该软件系统能够满足用户的需求。

##   2. 白盒测试，黑盒测试，灰盒测试

	-  黑盒测试，
	       指的是把被测的软件看作一个黑盒子，我们不去关心盒子里面的结构是什么样子的，只关心软件的输入数据和数据结果。
	它只检查程序呈现给用户的功能是否按照需求规格说明书的规定正常使用、程序是否能接受输入数据并产生正确的输出信息。黑盒测试
	着眼于外部结构，不考虑内部逻辑结构。主要针对软件界面及软件功能进行测试。
	
	- 白盒测试：
	        指把盒子打开，去研究里面的源代码和程序执行结果。
	 它是按照程序内部的结构测试程序，同故宫测试来检测铲平内部动作是否按照设计规格说ing书的规定正常进行，检验程序中的每条逻辑路径
	是否都能按预定要求正确工作。

	-  灰盒测试：
	    介于黑盒测试与白盒测试

##  3. 功能测试与性能测试
	- 功能测试：
	        主要检查实际功能是否符合用户的需求；
	细分很多种：逻辑功能测试、界面测试、易用性测试、安装测试、兼容性测试。
	
	- 性能测试：
	      通过测试工具模拟多种正常、峰值及一场负载条件来对系统的各项性能指标进行的测试
	      性能测试包括很多方面：主要有时间性能和空间性能两种。
	  时间性能： 一个具体事件的响应时间。例如一个登录所需要的时间
	  空间性能：主要指软件运行所消耗的系统资源，例如硬件资源，CPU、内存、网络带宽消耗等。

##  4. 手工测试与自动化测试
	
	手工测试
	自动化测试
	    是把人为的驱动测试行为转换为机器执行的一种过程。 通常， 在设计用例并通过评审之后，有测试人员根据测试描述的规则流程一步步执行测试，
	把得到的实际结果与期望结果进行比较。在此过程中，为了节省人力，时间和硬件资源，提高测试效率，变引入了自动化测试的概念。
		功能自动化测试
	    性能自动化测试

##  5. 冒烟测试、回归测试、随机测试、探索性测试和安全测试

	-  冒烟测试
	    是指在对一个新版本进行大规模的系统测试前，先验证一下软件的基本功能是否实现，是否具备可测性
	先投入较少的人力和时间验证一个软件的主要功能，如果主要功能都没欸有运行通过，则大会开发组重新开发。这样做的好处是可以节省时间和人力投入到不可测的项目中。
	- 回归测试
	    指修改了旧代码和偶，重新进行测试以确认修改该后没有引入新的错误或导致其他代码产生错误。
	次轮验证首轮测试中发现的问题是否得以修复。
	-  随机测试
	    是指测试中所有输入数据都是随机生成的，其目的是模拟yoghurt的真实操作，并发现一些边缘性的错误。
	
	- 探索性测试
	    主观测试

	- 安全测试

<h1 id=2><font color=blue> 什么样的项目适合自动化测试</font> </h1>
	
	1) 任务测试明确， 不会频繁变动
	2) 每日构建后的测试验证
	3）比较频繁的回归测试
	4）软件系统界面稳定，变动少
	5）需要在多平台上运行的相同的测试用例、组合遍历的测试，大量的重复任务
	6）软件维护周期长
	7）项目进度压力不太大
	8）被测试软件系统开发比较规范，能够保证系统的可测试性
	9）测试人员具备编程能力

 一般满足三个条件就可以对项目开展自动化测试 
	
	1）软件需求变动不频繁
	    自动化测试脚本变化的大小与频率决定了自动化测试的维护成本，如果软件需求变动过于频繁，那么测试人员就需要根据变动
	的需求来不断的更新自动化测试用例，从而适应新的功能。而脚本的维护其实就是一个开发代码的过程，需要扩展，修改、调试、又是
	需要对架构做出调整。如果所花费的维护成本高于利用其节省的测试成本，那么自动化测试就失去了其价值与意义，一般对系统中相
	对稳定的模块与功能进行自动化测试，而变动较大的部分用手工测试
	
	2）项目周期长
	    由于自动化测试需求确定、自动化测试框架设计、脚本的开发与调试均需要时间来完成，而这个过程本身是一个软件的开发过程，
	如果项目的周期较短，没有足够的时间区支持这样一个过程的话，那么就不需要进行自动化测试了。

	3）自动化测试脚本可重复使用

<h1><font color=blue>二  分层的自动化测试 </font></h1>

测试金字塔:

	单元——>服务接口——>UI
	Unit -> Service - >UI

<h2 id="单元"><font color=MediumSpringGreen> 1 单元自动化测试：</font> </h2>
	 指对软件中的最小可测试单元进行检查和验证，如C语言中单元是指一个函数，Java中单元是指一个类， 图形化的软件中单元是指一个窗口
	或一个菜单等。单元就是人为规定的最小的被测功能模块。规范的进行单元测试需要借助单元测试框架，如unittest, pytest

<h2 id="接口"><font color=MediumSpringGreen>2 接口自动化测试</font></h2>
###<font color=green> 1）模块接口测试：</font> ###
		主要测试模块之间的调用与返回。当然，我们也可以将其看作用是单元测试的基础。它主要强调对一个类方法或函数的调用，并对返回结果的验证，
	所用到测试工具与单元自动化测试相同。

### <font color=green> 2) web 接口测试</font> ###
	分为两类： 服务器接口测试和外部接口测试
	服务口接口测试：
		web开发一般分为前端和后台， 前端开发人员用HTML/CSS/JAVA/JavaScript等技术,后台开发人员用PHP/Java/C#/Python等各种
	语言，用户是前端操作的，需要后台服务器提供接口，前端通过调用这些接口来获取需要的数据，通过HTTP协议实现前后端的数据传递。
	
	外部接口测试：
		第三方系统提供，典型的列子就是第三方登录

<h3> <font color=green> 3）常用接口测试工具 </font></h3>
	HttpUnit、Postman 等

<h2 id="UI"><font color=blue> UI测试</font> </h2>
UI测试是用户使用产品的入口，所有功能都通过这一层提供并展示给用户，所有用户的大量工作都集中在这一层。



> 主流测试工具有 UFT、 Watir、Robot Framwork、Selenium等。

#### UFT ####

		UFT(unified Functional Testing) 由QTP（Quick Test Professional software) 与ST(service Test)合并而来,HP公司开发
	是一款企业级自动化测试工具，提供了强大易用的录制回放功能，支持B/S与C/S

#### Robot Framework ####
		
		Robot Framework 是一款基于Python语言编写的自动化测试框架， 具体良好的可扩展性，支持关键字驱动， 可以同时测试多种测试
	类型的客户端或者接口， 可以进行分布式测试。


<h4> Watir</h4>
	
		Watir(Web Application Testing in Ruby) 是一个基于Web 模式的自动化功能测试工具。Watir是一个基于Ruby
	语言库，使用Ruby 语言进行脚本开发


#### Selenium  ####
	
	Selenium 用于web应用程序测试的工具，支持多平台、多浏览器、多语言去实现自动化测试。

<h1 id="前端"><font color=blue>前端web技术</font> </h1>

- HTML
- JavaScript
- XML

<h1 id="插件"><font color=blue>web插件</font> </h1>

###  seleniumIDE ###
录制回放工具

### firebug： ###
开发类插件，集HTML 查看和编辑、Javascript控制台、网络状况监视器、Cookie查看于一体，是开发Javascript、CSS、HTML和Ajax
的得力助手

### firepath ###
FirePath 是FireBug插件扩展的一个工具，用来编辑、检查和生成XPath1.0表达式、CSS 3选择器以及jQuery 选择器。
	

<h1 id="元素定位"><font color=blue>元素定位</font> </h1>

	find_element_by_class_name
	find_element_by_id
	find_element
	find_element_by_css_selector
	find_element_by_link_text
	find_element_by_name
	find_element_by_partial_link_text
	find_element_by_tag_name
	find_element_by_xpath
	find_elements


<h1 id="鼠标事件"><font color=blue> 鼠标事件 </font> </h1>

**ActionChains**　类提供

- perfrom()	： 执行所有Action Chains 中存储的行为
- context_click():	右击
- doubule_click(): 双击
- drag_and_drop(): 拖动
- move_to_element(): 鼠标悬停


<h1 id=警告框处理><font color=blue> 警告框处理</font> </h1>

在WebDriver中处理JavaScript 所生成的alert、confirm以及prompt十分简单，具体做法是使用<font color=red> **switch_to_alert()**</font> **方法定位到alert/confirm/prompt, 然后使用text/accpet/dismiss/send_keys**等方法进行操作.

- text: 	返回 alert/confirm/prompt 中的文字信息
- accpet(): 接受现有警告框
- dismiss(): 解散现有警告框
- send_keys(keysToSend): 发送文本至警告框。 
- keysToSend: 将文本发送至警告框

<h1 id="键盘事件"><font color=blue> 键盘事件</font> </h1>
    
    from selenium.webdriver.common.keys import Keys
在使用键盘按键的方法前需要先导入keys类。

以下为常用的键盘操作：

	send_keys(Keys.BACK_SPACE)		删除键（BackSpace)
	send_keys(Keys.SPACE)			空格键（Space）
	send_keys(Keys.TAB)				制表键（Tab）
	send_keys(Keys.ESCAPE)			回退键（ESC）
	send_keys(Keys.ENTER)			回车键（ENTER)
	send_keys(Keys.CONTROL,'a')		全选（ctrl+a)
	send_keys(Keys.CONTROL,'c')		复制（Ctrl+c)
	send_keys(Keys.CONTROL,'x')		剪切（ctrl+x)
	send_keys(Keys.CONTROL,'v')		粘贴(ctrl+v)
	send_keys(Keys.F1)				键盘F1
	....
	send_keys(Keys.F12)				键盘F12



<h1 id="expect_conditions"><font color=blue>expect_conditions</font></h1>

	from selenium.webdriver.support import expected_conditions

方法

	方法											说明
	title_is									判断当前页面的标题是否等于预期
	title_contains								判断当前页面的标题是否包含预期字符串
	presence_of_element_located					判断元素是否被加载DOM树里，并不代表该元素一定可见
	visibility_of								与上一个方法作用相同，只是上一个方法参数为设定，该方法接收的参数为定位后的数
	visibility_of_element_located				判断元素是否可见
	presence_of_all_elements_located			判断是否至少有一个元素存在于DOM树中，例如，
												在这个页面中有n个元素为class 为"wp"，那么只要有一个存在就返回true
	text_to_be_present_in_element				判断某个元素中的text是否包含了预期的字符串
	text_to_be_present_in_element_value			判断某个元素中的value是否包含了预期的字符串
	frame_to_be_available_and_switch_to_it		判断改表单是否可以切换进去，如果可以，返回true并且switch进去，否则返回False
	invisibility_of_element_located				判断某个元素是否不存在于DOM树或不可见
	element_to_be_clickable						判断元素是否可见并且是可以点击的
	staleness_of								等待一个元素从DOM树中移除
	element_to_be_selected						判断某个元素是否被选中，一般用在下拉列表
	element_selection_state_to_be				判断某个元素的选中状态是否符合预期
	element_located_selection_state_to_be		与上一个方法作用相同，只是上一个方法参数为定位后的元素，该方法接收的参数为定位
	alert_is_present							判断页面上是否存在alert

	
<h1 id="操作cookie"><font color=blue> 操作cookie</font></h1>

有时候我们需要验证浏览器中cookie是否正确，因为基于真实cookie的测试是无法同故宫白盒和集成测试的，webDriver提供了操作cookie的相关
方法，可以读取、添加和删除cookie信息.
	
webdriver操作cookie的方法：

- get_cookies():			获得所有cookie信息
- get_cookie(name):			返回字典的key为“name" 的 cookie 信息
- add_cookie(cookie_dict)	添加cookie. "cookie_dict"指字典对象，必须有name和value值。
- delete_cookie(name,optionsString): 	删除cookie信息。 "name" 是要删除的cookie的名称，"optionsString" 是该cookie 的选项，目前支持的选项包括“路径”，“域”。
- delete_all_cookies():		删除所有cookie信息


<h1 id="前端"><font color=blue>自动化前端技术</font></h1>

- 熟练掌握XPath\CSS 定位的使用，这样在遇到各种难以定位的问题时才会变的束手无策。
- 准备一份 WedDriver API 文档， 以便随时查阅 WebDriver 所提供的方法。
- 学习掌握 JavaScript、 jQuery 技术， 它可以让我们使用该技术去操作 Web 页面。


<h1 id="模型"><font color=blue> 自动化测试模型 </font><h1>

### 框架 ###
框架是为解决一个或一类问题而开发的产品

### 自动化测试模型 ###
- **线性测试**
	- 通过录制或编写对应用例的操作步骤产生相应的线性脚本，每个测试脚本相对独立，且不产生其他依赖与调用。
		1. 开发成本很高，测试用例之间可能会存在重复的操作，不得不为每一个用力去录制或编写这些重复的操作，例如每个用力的登录和退出操作等
		2. 维护成本高

- **模块化驱动测试**
	- 把重复的操作独立成公共模块，当用例执行过程中需要用到这一模块操作时则被调用
		- 提高了开发效率，不用重复编写相同的操作脚本，例如，写好一个登录模块，后续测试用例在需要登录的地方调用即可。
		- 简化了维护的复杂性，加入登录按钮的定位发生了变化，那么只需修改登录模块的脚本即可，对于所有调用模块的测试脚本来说不需要做任何修改

- 数据驱动测试
	- 数据从模块中剥离
	- 数据的改变从而驱动自动化测试的执行，最终引起测试结果的改变。
	- 进一步增强脚本的复用性
		
- 关键字驱动测试


<H1 id="BDD"><font color=blue>BDD框架之Lettuce入门</font></H1>

## 什么是BDD ##

1）TDD:测试驱动开发（Test-Driven Development)

TDD是敏捷开发中的一项核心实践和技术，TDD的原理是在开发功能代码之前，先编写单元测试用例代码，测试代码确定需要编写什么产品代码。
TDD的基本思路就是通过测试来推动整个开发的进行，但测试驱动开发并不只是单纯的测试工作，而是吧需求分析、设计和质量控制量化的过程。

2）ATDD： 验收测试驱动开发（Acceptance Test Driven Development)

验收测试驱动开发是一种实践，在准备实施一个功能或特性之前，团队首先需要定义出期望的质量标准和验收细则，以明确且达成共识的验收测试
计划来驱动开发人员的功能开发实现和测试人员的测试脚本开发。

3）BDD: 行为驱动开发（Behavior Driven Development)

行为驱动开发是一种敏捷软件开发技术，它鼓励软件项目中的开发者，QA、非技术人员或商业参与者之间的协作。**<font color=green>主要是从用户的需求出发，强调系统行为。</font>**

不同语言下的BDD框架

	Cucumber(Ruby)		https://cucumber.io
	Jdave(Java)			http://jdave.org
	Behat(PHP)			http://docs.behat.org/en/v2.5
	Behave(PYthon)		http://pythonhosted.org/behave
	Lettuce(Python)		http://Lettue.it

**Lettuce**
   Lettuce 使开发和测试过程变得很容易，它有很好的可扩展行、可靠性、它允许我们用自然语言去描述一个系统的行为，

- 描述的行为
- 用Python定义步骤
- 运行并观看它失败
- 编写代码以使其通过

语法：
-----------------------------	
	Feature(功能）	 ----> test suite(测试用力集)
	Scenario(情景）   -----> test case（测试用例）
	Given(给定）      ------> （测试步骤)
	And(和)			 -------> 
	when(当)			 -------> test run(触发测试执行)
	Then(则）		 -------> assert(断言，验证结果)

----------------------------

