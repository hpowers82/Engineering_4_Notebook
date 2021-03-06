# Engineering_4_Notebook

## Table of Contents
* [Basics](#Basics)
* [Python_Dice_Roller](#PythonDiceRoller)
* [Python_Calculator](#Python_Calculator)
* [Quadratic_CalcStrings_and_Loops](#Quadratic_Calculator)
* [Strings_and_Loops](#Strings_and_Loops)
* [MSP](#MSP)
---

## Basics
You can delete this section from your own personal readme. 

### Assignment Description

Write your assignment description here. It should be at least a few sentences.

### Evidence 

Pictures / Gifs of your work should go here.  You need to communicate what your thing does. For code only assignments like the Python calculator, include a screenshot of the output of the code.

### Wiring

This may not be applicable to all assignments. Anything where you wire something up, include the wiring diagram here.

### Reflection

What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience?  Your ultimate goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person. Think about your audience for this one, which may be "future you" (when you realize you need some of this code in three months), me, or your college admission committee!

** Don't forget to **COMMENT YOUR CODE** before you upload to Github!

## Python_Dice_Roller

### Assignment Description

The purpose of this assignment was to create a program that can automatically roll dice. The program also took user input to decide whether another dice should be rolled, or if the program should exit. The spicy version added complexity by asking the user to specify the number of sides on the dice and the number of dice to be rolled at a time. The user was then asked whether they wanted to roll again with the same settings, change the settings, or exit the program. 

### Evidence 

Vanilla version:

![Screenshot 2021-09-10 3 15 26 PM](https://user-images.githubusercontent.com/89222808/133513775-a3eafb43-f836-4e4f-8aa6-e28ca584901f.png)

Spicy version:

![Screenshot 2021-09-10 3 18 38 PM](https://user-images.githubusercontent.com/89222808/133513750-727cdb6c-1c27-4c8a-83d4-50ea9136a221.png)

### Wiring

N/A

### Reflection

This assignment was relatively simple, but was challenging because I had not coded in Python for several months. I learned that I could import parts of toolboxes without importing the entire thing, but that changes the syntax of how I call the function later. I also learned about using a while loop to control whether a user wants to exit the program. For the spicy version, I needed to use nested loops. Python determines what is inside a loop by the indent level of each line of text, rather than brackets like some other coding styles. That means I need to be really careful with my tabs!


## Python_Calculator

### Assignment Description

The goal of this assignment was to create a programn that can automatically calculate several numbers from two inputs. This program should accomplish this through a function.

### Evidence 

![Capture2](https://user-images.githubusercontent.com/60944294/135727860-4486bbd8-1208-4c09-8f83-520a1b8da275.PNG)

### Wiring

N/A

### Reflection

This assignment taught me the uses and syntax for functions. They are very usefull when you want to run a similar command many times within your code, and don't want to type it out every time. I had some trouble figuring out how to get variables in and out of the function, but discovered that inside the function is kind of its own thing, and you must do specific things to get things in and out.

## Quadratic_Calculator

### Assignment Description

The goal of this assignement is to calculate the roots of a function by inputting the values of a, b, and c for y=ax^2+bx+c.

### Evidence

![Capture3](https://user-images.githubusercontent.com/60944294/135728704-25887227-789c-4b42-96a0-d0e0db76d2ae.PNG)

### Wiring

N/A

### Reflection

This assignment tested my knowledge of quadratics, it was actaully a pretty good refresher for my math class lol. The elif command is a very useful thing i learned while doing this.

## Strings_and_Loops

### Assignment Description

The goal of the strings and loops assignments was to teach me how to use for loops and edit strings and lists.

### Evidence

![Capture4](https://user-images.githubusercontent.com/60944294/136056379-0f0da36c-82a7-4f6f-be8e-59f62506f6e6.PNG)

### Wiring

N/A

### Reflection

The strings and loops assignment was very usefull, especially concidering the MSP assignment. 

## MSP

### Assignment Description

The goal of the MSP assignment was to create a full game of hangman within python. every time you made a mistake, a part should be added to the hangman. Every time you correctly guess a letter, it should add that letter to the correct spots in an array with letters you have not guessed yet as blanks.

### Evidence

![Screenshot 2021-09-30 10 14 58 PM](https://user-images.githubusercontent.com/60944294/136057854-354e55ec-f4b7-47d2-b957-d6c493c74448.png)

### Wiring

N/A

### Reflection

The MSP assignment was incredibly difficult. I actually completely started over because my code had become so conveluted and unable to be understood. One thing that helped a lot was Wills code for changing the letters in the blanks array: you can find that [here](https://github.com/willhk10/Engineering_4_Notebook/blob/main/Python/PerfectHangman.py#L72)

## CAD

### Assignment Description

The goal of the CAD assignment is to create a skateboard while teaching me some elements of Onshape CAD design. This is done by checking whether the weight of the object is correct.

### Evidence

![image](https://user-images.githubusercontent.com/60944294/139372868-5448ca82-9bc9-4995-9bc1-83f0c2dfe453.png)

### Wiring

N/A

### Reflection

This assignment was pretty difficult. a couple of times, i found that my weight was not quite correct, and I had to go back and fix it. most of the time, the issues were with making sure that items are grouped well, which seemed to be a major element of the challenge. I am very happy that I know the basics of Onshape now.

## RPi Safe Shutdown Button

### Assignment Description

The goal of the safe shutdown button is to use preexisting code in order to wire a button that shuts down your pi when it is pressed.

### Evidence

![IMG_20211129_120046](https://user-images.githubusercontent.com/60944294/143911229-4511ed28-258f-4877-92cd-b95255ad72af.jpg)

### Wiring

![WIN_20220113_11_59_52_Pro (2)](https://user-images.githubusercontent.com/60944294/149380536-714a80be-2def-42e3-8995-4b81cb6f173c.jpg)

### Reflection

I had a few hiccups while completing this assignment. First, I put the file in the wrong folder in my pi. Then, It would not work due to me not uncommenting the code you need to use when you are not using a reistor. This assignment taught me how to have code running at all times, and will be benifical when I am doing work without an interface and need to shut down the pi without a console.

## GPIO Pins

### Assignment Description

The point of this assignment is to display the data from the accelerometer onto the screen. 

### Evidence

![image](https://github.com/hpowers82/Engineering_4_Notebook/blob/main/pictures/ezgif-2-e3f66f9ade.gif)

### Wiring

![WIN_20220113_11_59_52_Pro (2)](https://user-images.githubusercontent.com/60944294/149380520-e5dc2ef1-67e7-41de-ae97-4cb2b2d10706.jpg)

### Reflection

This assignment gave me some trouble due to the difficulties I had with the LCD screen. From what I have learned, I believe that the proper order is:

```python
import Adafruit_SSD1306
RST = 24
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3d)

width = disp.width
height = disp.height
image = Image.new('1', (width, height))

disp.begin()

draw = ImageDraw.Draw(image)

draw.rectangle((0,0,width,height), outline=0, fill=0) #clears the screen

#draw whatever you want to here

disp.image(image)
disp.display()
```

## Headless Accelerometer

### Assignment Description

The point of this assignment is to run code that graphically displays the data from the accelerometer without a PC.

### Evidence

![image](https://github.com/hpowers82/Engineering_4_Notebook/blob/main/pictures/ezgif-2-8e17b67012.gif)

### Wiring

![WIN_20220113_11_59_52_Pro (2)](https://user-images.githubusercontent.com/60944294/149380520-e5dc2ef1-67e7-41de-ae97-4cb2b2d10706.jpg)

### Reflection

This assignment

## Pi Camera

### Assignment Description

The goal of this assignment is to create two programs: one that takes one picture when run, and one that takes 5 using different camera effects.

### Evidence

![image_15](https://user-images.githubusercontent.com/60944294/151026715-1d4c93b1-0ec5-44b1-81b8-ee7f729f4b47.jpg)

### Wiring

n/a

### Reflection

This assignment was pretty easy. I had little trouble with the first section, as the code to take a picture is rather simple, but i purposefull made it more complicated for myself by making it so each file names itself in relation to the number of pre-existing images, so if there are 15 images already, the new image would be named image_16. For the second part, I made it so the images would be taken with 5 random non-repeating effects, which made it slightly more difficult.

## Copypasta

### Assignment Description

The goal of this assignment is to create a stop-motion animation with the pi camera.

### Evidence

![ezgif-2-19019bc9ed](https://user-images.githubusercontent.com/60944294/151417049-b93586c8-fbd4-4bab-875a-d1fe956f366f.gif)

### Wiring

![WIN_20220113_11_59_52_Pro (2)](https://user-images.githubusercontent.com/60944294/149380536-714a80be-2def-42e3-8995-4b81cb6f173c.jpg)

### Reflection

This assignment was easy to complete. it introduced me to a way to create a video out of images, as well as some more details on how the pi camera works. the button commands used here may also prove useful in the future.
