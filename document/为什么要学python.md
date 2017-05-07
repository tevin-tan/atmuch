
* **[为什么使用python](#1)**
	* [开发效率]
	* [python的缺点是什么]
* **[python与java 的对比](#2)**
	* Java的特点
	* python的特点

<h1 id="1">一 为什么使用python</h1>
	* 软件质量
	    python 注重可读性，一致性和软件质量。
	* 提高开发者效率
	    相对于C,C++和Java等编译/静态类型语言，Python代码的大小往往只有C++或java代码的1/5~1/3.
	* 程序的可移植性
	   绝大多数的Python程序不做任何改变即可在所有主流计算机平台上运行。（在linux和Windows之间移植Python代码，只需简单地在及器件复制代码即可）
	* 标准库的支持
	* 组件集成

<h2 id=2>开发效率</h2>
    python 致力于开发速度的最优化： 简单的语法，动态类型，无需编译，内置工具包等特性是程序员能够快速项目开发
## python的缺点是什么
    与C/C++这类编译语言相比，python的执行速度还不够快。
    
# 二  python与java 的对比
##Java的特点：

   	1.编译型语言，编译器会生成由字节码组成的.class文件，然后由java虚拟机来运行；
    2.静态类型语言，在编译期间就确定数据类型，变量先声明再使用；
    3.强类型语言，一旦变量被指定了某个数据类型，如果不进行强制类型转换那么它就一直是这个类型；
    4.面向对象语言，必须面向对象编程，变量和函数都有所归属的类。

##python的特点：

	1 解释型语言，解释型语言程序不需要编译，运行时会翻译成机器语言，但python程序在运行过程中会自动生成字节码文件.pyc，改善了python的性能；
	2 动态类型语言，变量的使用无需声明，在赋值的时候根据值类型自动确定；
	3 强类型语言，一旦变量被指定了某个数据类型，如果不进行强制类型转换那么它就一直是这个类型（同java）；
	4 面向对象语言，不强制以面向对象的方式编程，可以以独立的函数模块来处理逻辑而不需要放到类中。


**java**

	public class HelloWorld  	
	{  
	    public static void main( String[] args )  
	    {  
	        System.out.println( "Hello, World\n" );  
	        System.exit(0);  
	    }  
	}

**c/c++**

	#include<stdio.h>
	int main(void)
	{
		printf("hello world!\n")
	}

**python**

    print(" hello world!")

