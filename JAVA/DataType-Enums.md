1. What is the order of variables in Enum?
a) Ascending order
b) Descending order
c) Random order
d) Depends on the order() method
View Answer

Answer: d
Explanation: The order of appearance of variables in Enum is their natural order (the natural order means the order in which they are declared inside Enum type). However, the compareTo() method is implemented to order the variable in ascending order.
2. Can we create an instance of Enum outside of Enum itself?
a) True
b) False
View Answer

Answer: b
Explanation: No, instances of Enum cannot be created outside of Enum boundary, because Enum does not have a public constructor.
3. What will be the output of the following Java code?

Subscribe Now: Java Newsletter | Important Subjects Newsletters
    enum Season 
    {
        WINTER, SPRING, SUMMER, FALL
    };
    System.out.println(Season.WINTER.ordinal());
a) 0
b) 1
c) 2
d) 3
View Answer

Answer: a
Explanation: ordinal() method provides number to the variables defined in Enum.
Get Free Certificate of Merit in Java Programming Now!
4. If we try to add Enum constants to a TreeSet, what sorting order will it use?
a) Sorted in the order of declaration of Enums
b) Sorted in alphabetical order of Enums
c) Sorted based on order() method
d) Sorted in descending order of names of Enums
View Answer

Answer: a
Explanation: Tree Set will sort the values in the order in which Enum constants are declared.
5. What will be the output of the following Java code snippet?

class A
{
 
}
 
enum Enums extends A
{
    ABC, BCD, CDE, DEF;
}
a) Runtime Error
b) Compilation Error
c) It runs successfully
d) EnumNotDefined Exception
View Answer

Answer: b
Explanation: Enum types cannot extend class.
6. What will be the output of the following Java code snippet?

 enum Levels 
{
    private TOP,
 
    public MEDIUM,
 
    protected BOTTOM;
}
a) Runtime Error
b) EnumNotDefined Exception
c) It runs successfully
d) Compilation Error
View Answer

Answer: d
Explanation: Enum cannot have any modifiers. They are public, static and final by default.
7. What will be the output of the following Java code snippet?

enum Enums
{
    A, B, C;
 
    private Enums()
    {
        System.out.println(10);
    }
}
 
public class MainClass
{
    public static void main(String[] args)
    {
        Enum en = Enums.B;
    }
}
a)

   10
   10
   10
b) Compilation Error
c)

   10
   10
d) Runtime Exception
View Answer

Answer: a
Explanation: The constructor of Enums is called which prints 10.
8. Which method returns the elements of Enum class?
a) getEnums()
b) getEnumConstants()
c) getEnumList()
d) getEnum()
View Answer

Answer: b
Explanation: getEnumConstants() returns the elements of this enum class or null if this Class object does not represent an enum type.
9. Which class does all the Enums extend?
a) Object
b) Enums
c) Enum
d) EnumClass
View Answer

Answer: c
Explanation: All enums implicitly extend java.lang.Enum. Since Java does not support multiple inheritance, an enum cannot extend anything else.
10. Are enums are type-safe?
a) True
b) False
View Answer

Answer: a
Explanation: Enums are type-safe as they have own name-space.
