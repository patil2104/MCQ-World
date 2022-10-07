1. Who invented OOP?
a) Andrea Ferro
b) Adele Goldberg
c) Alan Kay
d) Dennis Ritchie
View Answer

Answer: c
Explanation: Alan Kay invented OOP, Andrea Ferro was a part of SmallTalk Development. Dennis invented C++ and Adele Goldberg was in team to develop SmallTalk but Alan actually had got rewarded for OOP.
2. Which is not a feature of OOP in general definitions?
a) Efficient Code
b) Code reusability
c) Modularity
d) Duplicate/Redundant data
View Answer

Answer: d
Explanation: Duplicate/Redundant data is dependent on programmer and hence can’t be guaranteed by OOP. Code reusability is done using inheritance. Modularity is supported by using different code files and classes. Codes are more efficient because of features of OOP.
3. Which was the first purely object oriented programming language developed?
a) Kotlin
b) SmallTalk
c) Java
d) C++
View Answer

Answer: b
Explanation: SmallTalk was the first programming language developed which was purely object oriented. It was developed by Alan Kay. OOP concept came into the picture in 1970’s.
4. When OOP concept did first came into picture?
a) 1980’s
b) 1995
c) 1970’s
d) 1993
View Answer

Answer: c
Explanation: OOP first came into picture in 1970’s by Alan and his team. Later it was used by some programming languages and got implemented successfully, SmallTalk was first language to use pure OOP and followed all rules strictly.
5. Which feature of OOP indicates code reusability?
a) Abstraction
b) Polymorphism
c) Encapsulation
d) Inheritance
View Answer

Answer: d
Explanation: Inheritance indicates the code reusability. Encapsulation and abstraction are meant to hide/group data into one element. Polymorphism is to indicate different tasks performed by a single entity.
6. Which header file is required in C++ to use OOP?
a) OOP can be used without using any header file
b) stdlib.h
c) iostream.h
d) stdio.h
View Answer

Answer: a
Explanation: We need not include any specific header file to use OOP concept in C++, only specific functions used in code need their respective header files to be included or classes should be defined if needed.
7. Why Java is Partially OOP language?
a) It allows code to be written outside classes
b) It supports usual declaration of primitive data types
c) It does not support pointers
d) It doesn’t support all types of inheritance
View Answer

Answer: b
Explanation: As Java supports usual declaration of data variables, it is partial implementation of OOP. Because according to rules of OOP, object constructors must be used, even for declaration of variables.
8. Which among the following doesn’t come under OOP concept?
a) Data hiding
b) Message passing
c) Platform independent
d) Data binding
View Answer

Answer: c
Explanation: Platform independence is not feature of OOP. C++ supports OOP but it’s not a platform independent language. Platform independence depends on the programming language.
9. Which is the correct syntax of inheritance?
a) class base_classname :access derived_classname{ /*define class body*/ };
b) class derived_classname : access base_classname{ /*define class body*/ };
c) class derived_classname : base_classname{ /*define class body*/ };
d) class base_classname : derived_classname{ /*define class body*/ };
View Answer

Answer: b
Explanation: Firstly, keyword class should come, followed by the derived class name. Colon is must followed by access in which base class has to be derived, followed by the base class name. And finally the body of class. Semicolon after the body is also must.
10. Which feature of OOP is indicated by the following code?

class student{  int marks;  };
class topper:public student{  int age;  topper(int age){ this.age=age; } };
a) Encapsulation and Inheritance
b) Inheritance and polymorphism
c) Polymorphism
d) Inheritance
View Answer

Answer: a
Explanation: Encapsulation is indicated by use of classes. Inheritance is shown by inheriting the student class into topper class. Polymorphism is not shown here because we have defined the constructor in the topper class but that doesn’t mean that default constructor is overloaded.
11. The feature by which one object can interact with another object is _____________
a) Message reading
b) Message Passing
c) Data transfer
d) Data Binding
View Answer

Answer: b
Explanation: The interaction between two object is called the message passing feature. Data transfer is not a feature of OOP. Also, message reading is not a feature of OOP.
12. Which among the following, for a pure OOP language, is true?
a) The language should follow at least 1 feature of OOP
b) The language must follow only 3 features of OOP
c) The language must follow all the rules of OOP
d) The language should follow 3 or more features of OOP
View Answer

Answer: c
Explanation: The language must follow all the rules of OOP to be called a purely OOP language. Even if a single OOP feature is not followed, then it’s known to be a partially OOP language.
13. How many types of access specifiers are provided in OOP (C++)?
a) 4
b) 3
c) 2
d) 1
View Answer

Answer: b
Explanation: Only 3 types of access specifiers are available. Namely, private, protected and public. All these three can be used according to the need of security of members.
14. In multilevel inheritance, which is the most significant feature of OOP used?
a) Code efficiency
b) Code readability
c) Flexibility
d) Code reusability
View Answer

Answer: d
Explanation: The classes using multilevel inheritance will use the code in all the subsequent subclasses if available. Hence the most significant feature among the options given is code reusability. This feature is generally intended to use the data values and reuse the redundant functions.
15. What is encapsulation in OOP?
a) It is a way of combining various data members and member functions that operate on those data members into a single unit
b) It is a way of combining various data members and member functions into a single unit which can operate on any data
c) It is a way of combining various data members into a single unit
d) It is a way of combining various member functions into a single unit
View Answer

Answer: a
Explanation: It is a way of combining both data members and member functions, which operate on those data members, into a single unit. We call it a class in OOP generally. This feature have helped us modify the structures used in C language to be upgraded into class in C++ and other languages.
16. Which of the following is not true about polymorphism?
a) Helps in redefining the same functionality
b) Increases overhead of function definition always
c) It is feature of OOP
d) Ease in readability of program
View Answer

Answer: b
Explanation: It never increases function definition overhead, one way or another if you don’t use polymorphism, you will use the definition in some other way, so it actually helps to write efficient codes.
17. Which constructor will be called from the object created in the below C++ code?

class A
{ 
	int i;
	A()
	{ 
		i=0; cout&lt;&lt;i; 
	}
	A(int x=0)
	{ 
		i=x;  cout&lt;&lt;I;  
	}
};
A obj1;
a) Parameterized constructor
b) Default constructor
c) Run time error
d) Compile time error
View Answer

Answer: d
Explanation: When a default constructor is defined and another constructor with 1 default value argument is defined, creating object without parameter will create ambiguity for the compiler. The compiler won’t be able to decide which constructor should be called, hence compile time error.
18. What is an abstraction in object-oriented programming?
a) Hiding the implementation and showing only the features
b) Hiding the important data
c) Hiding the implementation
d) Showing the important data
View Answer

Answer: a
Explanation: It includes hiding the implementation part and showing only the required data and features to the user. It is done to hide the implementation complexity and details from the user. And to provide a good interface in programming.
19. Which among the following can show polymorphism?
a) Overloading &&
b) Overloading <<
c) Overloading ||
d) Overloading +=
View Answer

Answer: b
Explanation: Only insertion operator can be overloaded among all the given options. And the polymorphism can be illustrated here only if any of these is applicable of being overloaded. Overloading is type of polymorphism.
20. In which access should a constructor be defined, so that object of the class can be created in any function?
a) Any access specifier will work
b) Private
c) Public
d) Protected
View Answer

21. Which among the following is correct for the class defined below?

class student
{
    int marks;
    public: student(){}
    student(int x)
    { 
         marks=x; 
    }
};
main()
{
    student s1(100);
    student s2();
    student s3=100;
    return 0;
}
a) Program will give compile time error
b) Object s3, syntax error
c) Only object s1 and s2 will be created
d) Program runs and all objects are created
View Answer

Answer: d
Explanation: It is a special case of constructor with only 1 argument. While calling a constructor with one argument, you are actually implicitly creating a conversion from the argument type to the type of class. Hence you can directly specify the value of that one argument with assignment operator.
22. The copy constructors can be used to ________
a) Copy an object so that it can be passed to another primitive type variable
b) Copy an object for type casting
c) Copy an object so that it can be passed to a function
d) Copy an object so that it can be passed to a class
View Answer

23. Which constructor will be called from the object obj2 in the following C++ program?

class A
{
	int i;
	A()
	{  
		i=0;  
	}
	A(int x)
	{  
		i=x+1;  
	}
	A(int y, int x)
	{  
		i=x+y;  
	}
};
A obj1(10);
A obj2(10,20);
A obj3;
a) A(int y, int x)
b) A(int y; int x)
c) A(int y)
d) A(int x)
View Answer

Answer: a
Explanation: The two argument constructor will be called as we are passing 2 arguments to the object while creation. The arguments will be passed together and hence compiler resolves that two argument constructor have to be called.
24. Which among the following represents correct constructor?
a) –classname()
b) classname()
c) ()classname
d) ~classname()
View Answer

Answer: b
Explanation: The constructors must contain only the class name. The class name is followed by the blank parenthesis or we can have parameters if some values are to be passed.
25. What happens when an object is passed by reference?
a) Destructor is called at end of function
b) Destructor is called when called explicitly
c) Destructor is not called
d) Destructor is called when function is out of scope
View Answer

Answer: c
Explanation: The destructor is never called in this situation. The concept is that when an object is passed by reference to the function, the constructor is not called, but only the main object will be used. Hence no destructor will be called at end of function.
26. Which access specifier is usually used for data members of a class?
a) Protected
b) Private
c) Public
d) Default
View Answer

Answer: b
Explanation: All the data members should be made private to ensure the highest security of data. In special cases we can use public or protected access, but it is advised to keep the data members private always.
27. How to access data members of a class?
a) Dot, arrow or direct call
b) Dot operator
c) Arrow operator
d) Dot or arrow as required
View Answer

Answer: d
Explanation: The data members can never be called directly. Dot operator is used to access the members with help of object of class. Arrow is usually used if pointers are used.
28. Which feature of OOP reduces the use of nested classes?
a) Inheritance
b) Binding
c) Abstraction
d) Encapsulation
View Answer

Answer: a
Explanation: Using inheritance we can have the security of the class being inherited. The subclass can access the members of parent class. And have more feature than a nested class being used.
29. Which keyword among the following can be used to declare an array of objects in java?
a) allocate
b) arr
c) new
d) create
View Answer

Answer: c
Explanation: The keyword new can be used to declare an array of objects in java. The syntax must be specified with an object pointer which is assigned with a memory space containing the required number of object space. Even initialization can be done directly.
30. Which operator can be used to free the memory allocated for an object in C++?
a) Unallocate
b) Free()
c) Collect
d) delete
View Answer

Answer: d
Explanation: The delete operator in C++ can be used to free the memory and resources held by an object. The function can be called explicitly whenever required. In C++ memory management must be done by the programmer. There is no automatic memory management in C++.
31. Which of the following is not a property of an object?
a) Properties
b) Names
c) Identity
d) Attributes
View Answer

Answer: b
Explanation: The names are not property of an object. The identity can be in any form like address or name of object but name can’t be termed as only identity of an object. The objects contain attributes that define what type of data an object can store.
32. Which type of members can’t be accessed in derived classes of a base class?
a) All can be accessed
b) Protected
c) Private
d) Public
View Answer

Answer: c
Explanation: The private members can be accessed only inside the base class. If the class is derived by other classes. Those members will not be accessible. This concept of OOP is made to make the members more secure.
33. Which among the following best describes the Inheritance?
a) Using the data and functions into derived segment
b) Using already defined functions in a programming language
c) Using the code already written once
d) Copying the code already written
View Answer

Answer: a
Explanation: It can only be indicated by using the data and functions that we use in derived class, being provided by parent class. Copying code is nowhere similar to this concept, also using the code already written is same as copying. Using already defined functions is not inheritance as we are not adding any of our own features.
34. Single level inheritance supports _____________ inheritance.
a) Language independency
b) Multiple inheritance
c) Compile time
d) Runtime
View Answer

Answer: d
Explanation: The runtime inheritance is done when object of a class is created to call a method. At runtime the function is searched if it is in class of object. If not, it will search in its parent classes and hierarchy for that method.
35. How to overcome diamond problem?
a) Using seperate derived class
b) Using virtual keyword with same name function
c) Can’t be done
d) Using alias name
View Answer

Answer: b
Explanation: To overcome the ambiguity and conflict we can use keyword virtual. This will help us to differentiate the functions with same name that came to last derived class in diamond problem.
36. Which keyword is used to declare virtual functions?
a) virt
b) virtually
c) virtual
d) anonymous
View Answer

Answer: c
Explanation: The virtual keyword is used to declare virtual functions. Anonymous keyword is used with classes and have a different meaning. The virtual functions are used to call the intended function of the derived class.
37. What happens if non static members are used in static member function?
a) Executes fine
b) Compile time error
c) Executes if that member function is not used
d) Runtime error
View Answer

38. What is friend member functions in C++?
a) Non-member functions which have access to all the members (including private) of a class
b) Member function which doesn’t have access to private members
c) Member function which can modify any data of a class
d) Member function which can access all the members of a class
View Answer

Answer: a
Explanation: A non-member function of a class which can access even the private data of a class is a friend function. It is an exception on access to private members outside the class. It is sometimes considered as a member functions since it has all the access that a member function in general have.
39. Where is the memory allocated for the objects?
a) Cache
b) ROM
c) HDD
d) RAM
View Answer

Answer: d
Explanation: The memory for the objects or any other data is allocated in RAM initially. This is while we run a program all the memory allocation takes place in some RAM segments. Arrays in heap and local members in stack etc.
40. Which of the following best describes member function overriding?
a) Member functions having the same name in derived class only
b) Member functions having the same name and different signature inside main function
c) Member functions having the same name in base and derived classes
d) Member functions having the same name in base class only
View Answer

Answer: c
Explanation: The member function which is defined in base class and again in the derived class, is overridden by the definition given in the derived class. This is because the preference is given more to the local members. When derived class object calls that function, definition from the derived class is used.
41. Encapsulation and abstraction differ as ____________
a) Hiding and hiding respectively
b) Binding and Hiding respectively
c) Hiding and Binding respectively
d) Can be used any way
View Answer

Answer: b
Explanation: Abstraction is hiding the complex code. For example, we directly use cout object in C++ but we don’t know how is it actually implemented. Encapsulation is data binding, as in, we try to combine a similar type of data and functions together.
42. Which feature of OOP is exhibited by the function overriding?
a) Polymorphism
b) Encapsulation
c) Abstraction
d) Inheritance
View Answer

Answer: a
Explanation: The polymorphism feature is exhibited by function overriding. Polymorphism is the feature which basically defines that same named functions can have more than one functionalities.
43. How to access the private member function of a class?
a) Using class address
b) Using object of class
c) Using object pointer
d) Using address of member function
View Answer

Answer: d
Explanation: Even the private member functions can be called outside the class. This is possible if address of the function is known. We can use the address to call the function outside the class.
44. Which keyword should be used to declare static variables?
a) const
b) common
c) static
d) stat
View Answer

Answer: c
Explanation: The keyword used to declare static variables is static. This is must be used while declaring the static variables. The compiler can make variables static if and only if they are mentioned with static keyword.
45. Which is correct syntax for declaring pointer to object?
a) *className objectName;
b) className* objectName;
c) className objectName();
d) className objectName;
View Answer

Answer: b
Explanation: The syntax must contain * symbol after the className as the type of object. This declares an object pointer. This can store address of any object of the specified class.
46. Which class/set of classes can illustrate polymorphism in the following C++ code?

abstract class student
{
   public : int marks;
   calc_grade();
}
class topper:public student
{
    public : calc_grade()
    { 
        return 10; 
    }
};
class average:public student
{ 
     public : calc_grade()
     {
         return 20; 
     }
};
class failed{ int marks; };
a) Only class student and topper together can show polymorphism
b) Only class student can show polymorphism
c) Class failed should also inherit class student for this code to work for polymorphism
d) All class student, topper and average together can show polymorphism
View Answer

Answer: d
Explanation: Since Student class is abstract class and class topper and average are inheriting student, class topper and average must define the function named calc_grade(); in abstract class. Since both the definition are different in those classes, calc_grade() will work in different way for same input from different objects. Hence it shows polymorphism.
47. If data members are private, what can we do to access them from the class object?
a) Private data members can never be accessed from outside the class
b) Create public member functions to access those data members
c) Create private member functions to access those data members
d) Create protected member functions to access those data members
View Answer

Answer: b
Explanation: We can define public member functions to access those private data members and get their value for use or alteration. They can’t be accessed directly but is possible to be access using member functions. This is done to ensure that the private data doesn’t get modified accidentally.
48. Which among the following is not a necessary condition for constructors?
a) Its name must be same as that of class
b) It must not have any return type
c) It must contain a definition body
d) It can contains arguments
View Answer

Answer: c
Explanation: Constructors are predefined implicitly, even if the programmer doesn’t define any of them. Even if the programmer declares a constructor, it’s not necessary that it must contain some definition.
49. Object being passed to a copy constructor ___________
a) Must not be mentioned in parameter list
b) Must be passed with integer type
c) Must be passed by value
d) Must be passed by reference
View Answer

Answer: d
Explanation: This is mandatory to pass the object by reference. Otherwise, the object will try to create another object to copy its values, in turn a constructor will be called, and this will keep on calling itself. This will cause the compiler to give out of memory error.
50. If in multiple inheritance, class C inherits class B, and Class B inherits class A. In which sequence are their destructors called if an object of class C was declared?
a) ~A() then ~B() then ~C()
b) ~C() then ~A() then ~B()
c) ~C() then ~B() then ~A()
d) ~B() then ~C() then ~A()
View Answer

Answer: c
Explanation: The destructors are always called in the reverse order of how the constructors were called. Here class A constructor would have been created first if Class C object is declared. Hence class A destructor is called at last.
51. Instance of which type of class can’t be created?
a) Parent class
b) Abstract class
c) Anonymous class
d) Nested class
View Answer

Answer: b
Explanation: Instance of abstract class can’t be created as it will not have any constructor of its own, hence while creating an instance of class, it can’t initialize the object members. Actually the class inheriting the abstract class can have its instance because it will have implementation of all members.
52. ___________ underlines the feature of Polymorphism in a class.
a) Virtual Function
b) Inline function
c) Enclosing class
d) Nested class
View Answer

Answer: a
Explanation: Virtual Functions can be defined in any class using the keyword virtual. All the classes which inherit the class containing the virtual function, define the virtual function as required. Redefining the function on all the derived classes according to class and use represents polymorphism.
53. Which feature in OOP is used to allocate additional functions to a predefined operator in any language?
a) Function Overloading
b) Function Overriding
c) Operator Overloading
d) Operator Overriding
View Answer

Answer: c
Explanation: The feature is operator overloading. There is not a feature named operator overriding specifically. Function overloading and overriding doesn’t give addition function to any operator.
54. Which feature can be implemented using encapsulation?
a) Polymorphism
b) Overloading
c) Inheritance
d) Abstraction
View Answer

Answer: d
Explanation: Data abstraction can be achieved by using encapsulation. We can hide the operation and structure of actual program from the user and can show only required information by the user.
