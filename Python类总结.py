class  Person(object):    #创建对象方式：变量名 = 类名（参数）
	
	
	#注意：在类中，所有属性和方法的调用其前面都必须有self【实例化对象】或cls【类】或super()【类对象】标识
	contry = "国家"   #类属性
	
	def __init__(self, leg, hand):   #构造方法，第一个参数都必须是self【创建的类对象】,可以被子类继承
		self.leg = leg       #实例化属性
		self.hand = hand
		self.__sex = "男"   #私有属性，标识符的开头必须是两个下划线，不能被继承，只能在类内部访问
	
	def make_cake(self, milk):  #实例化方法，第一个参数必须是self【创建的类对象】
		print("做牛奶的原材料是%s" %milk)
		
	@classmethod
	def drink(cls):  #类方法，第一个参数必须是cls【代表这个类】类和对象都可以调用，不能在里面使用实例化属性
		print("喝水", cls.contry)  
		
	def __eat(self):     #私有方法，标识符的开头必须是两个下划线，不能被继承，只能在类内部访问
		print("吃饭")
		
		
class Man(Object):
	  def __init__(self, leg, hand)
		self.leg = leg
		self.hand = hand
		
class Child(Person, Man)  #多继承，如果继承的方法中有重复的方法（方法名和参数相同），则默认只调用第一个父类的方法
	  pass                #重写父类的方法（方法名和参数保持相同，更改方法体）
	                      #重写父类的属性：属性名与父类相同，更改属性值即可
	                      #在子类中调用父类方法和属性     super().父类方法名（参数） super().父类属性名




	
	
	
		

	
	
	