# Draw a circle using a while loop
import turtle as t

painter = t.Turtle()
painter.shape("circle")

count = 0
while (count < 18):
  t.forward(20)
  t.right(20)
  t.stamp # Stamp at every vertex
  count += 1

wn = t.Screen()
wn.mainloop()