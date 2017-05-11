# BDD框架之Lettuce #

## 什么是BDD ##

1）**TDD:测试驱动开发**（Test-Driven Development)

TDD是敏捷开发中的一项核心实践和技术，TDD的原理是在开发功能代码之前，先编写单元测试用例代码，测试代码确定需要编写什么产品代码。
TDD的基本思路就是通过测试来推动整个开发的进行，但测试驱动开发并不只是单纯的测试工作，而是吧需求分析、设计和质量控制量化的过程。

2）**ATDD： 验收测试驱动开发**（Acceptance Test Driven Development)

验收测试驱动开发是一种实践，在准备实施一个功能或特性之前，团队**<font color=blue>首先需要定义出期望的质量标准和验收细则</font>**，以明确且达成共识的验收测试计划来驱动开发人员的功能开发实现和测试人员的测试脚本开发。

3）**BDD: 行为驱动开发**（Behavior Driven Development)

行为驱动开发是一种敏捷软件开发技术，它鼓励软件项目中的开发者，QA、非技术人员或商业参与者之间的协作。**<font color=blue>主要是从用户的需求出发，强调系统行为。</font>**

# **Lettuce** #

   Lettuce 使开发和测试过程变得很容易，它有很好的可扩展行、可靠性、它允许我们用自然语言去描述一个系统的行为，

语法：

- Feature(功能）
- Scenario(情景）
- Given(给定）
- And(和)
- When(当)
- Then(则）


## Lettuce 关键字的含义与unittest 中概念的对比 ##
-------------------------------------------------
	Lettuce								unittest
	Feature(功能）	 -------> 			test suite(测试用力集)
	Scenario(情景）   -------> 		test case（测试用例）
	Given(给定）      -------> 		setup（测试步骤)
	And(和)			 -------> 
	when(当)			 -------> 		 test run(触发测试执行)
	Then(则）		 -------> 			assert(断言，验证结果)



目录结构：

	tests/
		|___features/
			|__zero.feture (测试场景)
				|__setps.py (逻辑代码实现)

zero.feature
	
    Feature: Compute factorial
     In order to play with lettuce
     As beginners
     We'll implement factorial
    
    Scenario: Factorial of 0
     Given  I have the number 0
     When   I compute its factorial
     Then   I see the number 1
    
    Scenario: Factorial of 1
     Given I have the number 1
      When I compute its factorial
      Then I see the number 1
    
    Scenario: Factorial of 2
     Given I have the number 2
     When I have the number 2
     Then I see the number 2
    

![alt text](atmuch/Lettuce/iconlettuce_feature.jpg "Title")
    