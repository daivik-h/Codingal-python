def area_square(side_sqare):
   return side_sqare ** 2
def perimeter_sqaare(side_sqare_lenght):
   return side_sqare_lenght * 4
def area_rectangle(base_rec,height_rec):
   return base_rec * height_rec
def perimiet_rectangle(base_rec_p,height_rec_p):
   return (base_rec_p + height_rec_p) * 2
def area_triangle(base_tri,height_tri):
   return(base_tri * height_tri) / 2
def perimeter_triangle(side_1,side_2,side_3):
   return side_1 + side_2 + side_3
def area_circle(radius):
   return 3.14 * radius
def perimeter_circle(radius_cir):
   return radius_cir * 2 * 3.14


print('Hey there this is a Area and Perimeter/Circumference calculator')
shape = int(input("Please pick any shape\n1.Square\n2.Rectangle\n3.Triangle\n4.Circle\nNO SPACE NUMBER'S 1-4 ONLY!!!"))
if shape == 1:
    print("Ok a square what do you want to calculate?\n1.Area\n2.Perimeter\nNO SPACE NUMBER'S 1-2 ONLY!!!")
    oprator = int(input('Go Ahead Here:'))
    if oprator == 1:
       side_sqare = float(input('Enter A Side Of The Square(length): '))
       print(f'The Area of A Square With the Length {side_sqare} is {area_square (side_sqare)}')

    elif oprator == 2:
       side_sqare_lenght =  float(input('Ok Enter The Length Of A Side')) 
       print(f'The perimeter Of A Square With The Length {side_sqare_lenght} is {perimeter_sqaare (side_sqare_lenght)}')
    else:
       print("It was literally 1 or 2… just two choices… and you still managed to invent a completely different answer 💀 I’m starting to think instructions are more like optional side quests to you. At this point even guessing randomly would give better results than whatever you’re doing 😭 Honestly, it’s impressive how you turned two simple options into unlimited wrong answers.") 

       
elif shape == 2:
    print("Ok a Rectangle what do you want to calculate?\n1.Area\n2.Perimeter\nNO SPACE NUMBER'S 1-2 ONLY!!!")
    oprator = int(input('Go Ahead Here:'))
    if oprator == 1:
       base_rec = float(input('Enter The Base Of The Rectangle(length): '))
       height_rec = float(input('Enter The Base Of The Rectangle(length): '))
       print(f'The Area of A Rectangle With the base {base_rec} and height {height_rec} is {area_rectangle (base_rec,height_rec)}')

    elif oprator == 2:
       base_rec_p = float(input('Enter The Base Of The Rectangle(length): '))
       height_rec_p = float(input('Enter The Base Of The Rectangle(length): '))
       print(f'The Perimeter of A Rectangle With the base {base_rec_p} and height {height_rec_p} is {perimiet_rectangle (base_rec_p,height_rec_p)}')
       
    else:
       print("Did you go to school or did you just skip the part where you learn how to read 💀 Do you actually have eyes or are you just clicking things and hoping for the best 😭 It’s right there in front of you—two options—and somehow you still missed like it was hidden. At this point I’m convinced you’re not even trying, you’re just exploring new ways to be wrong.")   



elif shape == 3:
    print("Ok a Triangle what do you want to calculat?\n1.Area\n2.Perimeter\nNO SPACE NUMBER'S 1-2 ONLY!!!")
    oprator = int(input('Go Ahead Here:'))
    if oprator == 1:
       base_tri = float(input('Enter The Base Of The Triangle(length): '))
       height_tri = float(input('Enter The Base Of The Triangle(length): '))
       print(f'The Area of A Triangle With the base {base_tri} and height {height_tri} is {area_triangle (base_tri,height_tri)}')

    elif oprator == 2:
       side_1 = float(input('Enter The First Side Of The Triangle(length): '))
       side_2 = float(input('Enter The Second Side Of The Triangle(length): '))
       side_3 = float(input('Enter The Third Side Of The Triangle(length): '))
       print(f'The Perimeter of A Triangle With the first side {side_1} and second side {side_2} and the Third side {side_3} is {perimeter_triangle (side_1,side_2,side_3)}')

    else:
       print("I don’t know what you’re doing, but it definitely doesn’t look like reading instructions 💀 It’s almost impressive how you see something simple and instantly decide to do anything except that 😭 I gave you a clear path and you still managed to walk into a wall. At this point I’m convinced even a sign saying 'do not overthink' would confuse you.")

elif shape == 4:
    print("Ok a circle what do you want to calculat?\n1.Area\n2.Circumference\nNO SPACE NUMBER'S 1-2 ONLY!!!")
    oprator = int(input('Go Ahead Here:'))
    if oprator == 1:
        radius = float(input('Enter The Radius Of The Circle(Length): '))
        print(f'The Area Of a Circle With A Radius {radius} is {area_circle(radius)}')
    elif oprator == 2:
        radius_cir = float(input('Enter The Radius Of The Circle(Length): '))
        print(f'The Circumference Of a Circle With A Radius {radius_cir} is {perimeter_circle(radius_cir)}')
    else:
       print("I don’t even know how you managed to make something this simple feel like a boss fight 💀 It’s literally 1 or 2… that’s it… no hidden levels, no secret codes 😭 If this already feels hard, I’m starting to think the real challenge isn’t the program—it’s just reading what’s in front of you. Even then, I still believe you’ll get it… eventually… maybe… hopefully 😏")


else:
 print("💀 At this point, I’m not sure if you can’t follow instructions or if you’re just freelancing your own reality. I gave you FOUR options. FOUR. Not a creative writing assignment. Not a personality test. Just… press a number 😭 I’ve seen calculators with better decision-making skills. Even a microwave understands press 1-4 faster than you. Honestly, I’m impressed. Not in a good way—but still impressed.")