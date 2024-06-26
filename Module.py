#Different Methods of Importing Modules
#import Cal
import Cal as c 
#from Cal import a,show,sub,add
#from Cal import a as aa,show as sh,sub as su,add as ad
#from Cal import*
import Cls1 as k #Import Cls1 Module
print("The Value of A:",c.a) #Calling Module Variable With Module Name
x=c.add(2,3) #Calling Module Add Function 
print("The Sum of Two Numbers",x)
y=c.sub(3,15) #Calling Module Sub Function
print("The Subtract of Two Numbers",y)
c.show() #Calling Module simple Function
z=k.Math(3,5) #Making Object of Math Class from Cls1 Module 
z.disp() #Run Instance Method of Math Class
print("The Value of A:",z.A) #Print Instance Variable From Math Class With Cls1 Module Name
print("The Value of B:",z.B) #Print Instance Variable From Math Class With Cls1 Module Name