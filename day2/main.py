# class object name
class Student:
    # CONSTRUCTION FUNCTION in JAVASCRIPT
    # function Student(){
    #     console.log("student created");
    #     this.name = "Bob";
    #     this.age = 44;
    # }
    # construction function
    def __init__(self,n,a):
        print "Student Created!!"
        self.name = n
        self.age = a

    # METHOD in JAVASCRIPT
    # Student.prototype.read = function(){
    #   console.log(this.name);
    # }
    # Method of the object
    def read(self):
        print self.name

    # During editing if you want to leave it blank you can use "pass"
    def eat(self):
        pass

# Making instantiate JAVASCRIPT
# var student = new Student()
student1 = Student("Bob",10)
student2 = Student("Paul",20)

student2.read()

print student2.name + " was " + str(student2.age) + " years old."

student2.age = 100

print "Now, " + student2.name + " is " + str(student2.age) + " years old."