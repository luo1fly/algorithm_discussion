# Python简单算法分析 #
## 排序算法 ##
> 通常算法复杂度越低时间复杂度越高，python內建的排序算法是经过很多优化的，与其自己去实现不如直接调用，我们这边的讨论单纯是为了进行思路分析，实际运用中需要仔细衡量
### 冒泡排序 ###
> 思想：从列表第一个数开始，往后的数依次与它进行比较，如果遇到比它小的数，则交换位置，一轮循环结束后，可确保第一个数为列表最小值；然后进行二轮循环，从第二个数开始，同样的方式进行，二轮结束后，第二个数为第二小的值；到循环结束后，列表排序完成

	def sort_bubble(lst1):
	    """
		不直接操作待排序列表，思考原因
	    """
	    lst = lst1[:]
	    for i in range(len(lst)):
	        for j in range(i+1, len(lst)):
	            if lst[j] < lst[i]:
	                lst[i], lst[j] = lst[j], lst[i]
	    return lst
### 选择排序 ###
> 思想：从列表第一个数开始，先假定它为最小，记录下标minimum，往后的数依次与它进行比较，如果遇到小于它的数，则记录下标到minimum，一轮循结束后，将下标minimum对应的数和第一个数进行交换位置，可确保第一个数为列表最小值；然后进行第二轮循环，从第二个数开始，同样的方式进行，二轮结束后，第二个数为第二小的值；到循环结束后，列表完成排序

	def sort_select(lst1):
	    """
		选择排序比冒泡排序少了几次赋值过程，效率有微小的提升
	    """
	    lst = lst1[:]
	    for i in range(len(lst)):
	        minimum = i
	        for j in range(i+1, len(lst)):
	            if lst[j] < lst[minimum]:
	                minimum = j
	        lst[i], lst[minimum] = lst[minimum], lst[i]
	    return lst
### 插入排序 ###
> 思想：比较难以表述，看代码吧...

	def sort_insert(lst1):
	    """
	    这是一个给每个数寻找合适位置的游戏
	    """
	    lst = lst1[:]
	    for i in range(1, len(lst)):
	        current = lst[i]
	        j = i
	        while j > 0 and current < lst[j-1]:
	            lst[j] = lst[j-1]
	            j -= 1
	        lst[j] = current
	    return lst
## 设计模式之单例模式 ##
> 下面介绍两种实现方式，装饰器和类继承
### 装饰器实现 ###
> 之前装饰器都是用来装饰函数，这次用来装饰类，所以这种方式其实也是一种工厂模式的体现，下面是代码实现
	
	def singleton(cls):
	    instances = {}
	
	    def wrapper(*args, **kwargs):
	        if cls not in instances:
	            instances[cls] = cls(*args, **kwargs)
	        return instances[cls]
	    return wrapper
	
	
	@singleton
	class MyClass:
	    def __init__(self, name):
	        self.name = name
	
1.	维护一个实例字典，将类作为key，实例作为value
2.	判断实例是否存在，不存在则创建一个实例，存在则直接返回已存在的，这样保证了当前进程管理的内存中一个类只有一个对象实例
3.	装饰器的优势在于不需要对类进行修改，而把对单个实例的控制放在外部函数中，这种方式相对灵活，对程序的改动量较小；另外由于是通过外部函数返回了类的实例，也是一种工厂模式的运用，这种方法也可以称为工厂函数实现单例模式
4.	这种方式就没有局限性吗，也不是，后面我们再来分析
### 类继承实现 ###
> 先来复习一下类实例化的过程，\__init\__方法执行会先对对象属性进行赋值，再调用\__new\__方法创建出这个对象，这个过程要搞清楚，然后我们来看代码实现

	class Singleton(object):
	    def __new__(cls, *args, **kwargs):
	        if not hasattr(cls, '_instance'):
	            cls._instance = super(Singleton, cls).__new__(cls)
	        return cls._instance
	
	
	class MyClass(Singleton):
	    def __init__(self, name):
	        self.name = name
1.	写一个父类Singleton，重写其\__new\__方法，加一层判断如果类没有实例则创建一个，否则返回已有实例
2.	子类直接继承父类Singleton即可，子类并没有显式的重写\__new__方法，所以直接调用父类的，根据广度优先法则，MyClass类实例化时调用的是Singleton改写过后的\__new\__方法，所以他只会创建一个实例
3.	我们来分析一下这种方式的特点，对原类有细微改动继承了Singleton类，要对类实例化过程有一定的认知度
### 两种方式对比 ###
> 我们设计了main方法来执行这两个脚本


	if __name__ == '__main__':
	    m1 = MyClass('caining')
	    print(
	        'id of m1:%s' % id(m1),
	        'name of m1:%s' % m1.name,
	        sep='\n'
	    )
	    m2 = MyClass('shabi')
	    print(
	        'id of m2:%s' % id(m2),
	        'name of m2:%s' % m2.name,
	        sep='\n'
	    )
> 执行结果分别如下：

1.	装饰器方式

		id of m1:2420770751600
		name of m1:caining
		id of m2:2420770751600
		name of m2:caining
2.	类继承方式
		
		id of m1:2216736122192
		name of m1:caining
		id of m2:2216736122192
		name of m2:shabi
> 分析：

1.	两种方式分别创建的m1和m2对象id相等，说明是单一实例
2.	装饰器方式m1和m2的name属性值相等，而类继承方式m1和m2的name属性却不同；原因在于装饰器方式在外部函数中判断实例是否存在，存在则直接返回，有点类似于直接赋值m2=m1，而继承的方式是在创建实例的过程中进行判断的，并且属性赋值是在判断之前发生，所以尽管返回的是同一个对象，但属性name的值被修改了，这就导致了两种方式的差异之处
3.	如何选用这两种方式呢，看需求咯，如果你要求所有属性唯一，不能修改，那么选用装饰器，如果你需要动态的修改部分属性且不想（不能）创建多个实例的话，选类继承

