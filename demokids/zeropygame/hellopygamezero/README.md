
- https://pygame-zero.readthedocs.io/en/stable/installation.html

- https://www.mattlayman.com/blog/2019/teach-kid-code-pygame-zero/
- https://pygame-zero.readthedocs.io/en/stable/introduction.html
- https://codewith.mu/en/tutorials/1.2/modes
- https://pygame-zero.readthedocs.io/en/stable/from-scratch.html
- https://pygame-zero.readthedocs.io/en/stable/introduction.html#creating-a-window
- https://pygame-zero.readthedocs.io/en/stable/builtins.html#screen
- https://www.toutes-les-couleurs.com/code-couleur-rvb.php



## Direct  Run
```
pip install pgzero

pgzrun intropygamezero.py


```



##  Import Mode
Example
Here is a Pygame Zero program that draws a circle. You can run this by pasting it into IDLE:
```
import pgzrun


WIDTH = 800
HEIGHT = 600

def draw():
    screen.clear()
    screen.draw.circle((400, 300), 30, 'white')


pgzrun.go()
```