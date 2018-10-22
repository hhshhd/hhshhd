def queen(A, cur=0):
    global l
    if cur == len(A):
        l +=1
        return 0
    for col in range(len(A)):
        A[cur], flag = col, True
        for row in range(cur):
            if A[row] == col or abs(col - A[row]) == cur - row:
                flag = False
                break
        if flag:
            queen(A, cur+1)
l = 0
temp = eval(input("Number of Queens:"))
queen(['']*temp)

def draw_board(the_board):
    import pygame
    import sys
    """ Draw a chess board with queens, as determined by the the_board. """

    pygame.init()
    colors = [(255,0,0), (0,0,0)]    # Set up colors [red, black]

    n = len(the_board)         # This is an NxN chess board.
    surface_sz = 480          # Proposed physical surface size.
    sq_sz = surface_sz // n    # sq_sz is length of a square.
    surface_sz = n * sq_sz     # Adjust to exactly fit n squares.

    # Create the surface of (width, height), and its window.
    surface = pygame.display.set_mode((surface_sz, surface_sz))

    ball = pygame.image.load("ball.png")

    # Use an extra offset to centre the ball in its square.
    # If the square is too small, offset becomes negative,
    #   but it will still be centered :-)
    ball = pygame.transform.scale(ball,(sq_sz,sq_sz))
    ball_offset = (sq_sz-ball.get_width()) // 2

    while True:

        # Look for an event from keyboard, mouse, etc.
         ev = pygame.event.poll()
         if ev.type == pygame.KEYDOWN:
             if ev.key == pygame.K_SPACE:
                 break
         if ev.type == pygame.QUIT:
            sys.exit()

        # Draw a fresh background (a blank chess board)
         for row in range(n):           # Draw each row of the board.
             c_indx = row % 2           # Alternate starting color
             for col in range(n):       # Run through cols drawing squares
                the_square = (col*sq_sz, row*sq_sz, sq_sz, sq_sz)
                surface.fill(colors[c_indx], the_square)
                # Now flip the color index for the next square
                c_indx = (c_indx + 1) % 2

        # Now that squares are drawn, draw the queens.
         for (col, row) in enumerate(the_board):
             surface.blit(ball,
                   (col*sq_sz+ball_offset,row*sq_sz+ball_offset))

         pygame.display.flip()


    pygame.quit()

#if __name__ == "__main__":
#    draw_board([0, 5, 3, 1, 6, 4, 2])    # 7 x 7 to test window size
#    draw_board([6, 4, 2, 0, 5, 7, 1, 3])
#    draw_board([9, 6, 0, 3, 10, 7, 2, 4, 12, 8, 11, 5, 1])  # 13 x 13
#    draw_board([11, 4, 8, 12, 2, 7, 3, 15, 0, 14, 10, 6, 13, 1, 5, 9])
    
class Point:
    """ Create a new Point, at coordinates x, y """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y

#    def distance_from_origin(self):
#        """ Compute my distance from the origin """
#        return ((self.x ** 2) + (self.y ** 2)) ** 0.5
#    
#    def to_string(self):
#        return "({0}, {1})".format(self.x, self.y)
#    
#    def __str__(self):    # All we have done is renamed the method
#            return "({0}, {1})".format(self.x, self.y)
#    
#    def halfway(self, target):
#        """ Return the halfway point between myself and the target """
#        mx = (self.x + target.x)/2
#        my = (self.y + target.y)/2
#        return Point(mx, my)
#    
#    
#class Rectangle:
#    """ A class to manufacture rectangle objects """
#
#    def __init__(self, posn, w, h):
#        """ Initialize rectangle at posn, with width w, height h """
#        self.corner = posn
#        self.width = w
#        self.height = h
#
#    def __str__(self):
#        return  "({0}, {1}, {2})".format(self.corner, self.width, self.height)
#    
#    def grow(self, delta_width, delta_height):
#        """ Grow (or shrink) this object by the deltas """
#        self.width += delta_width
#        self.height += delta_height
#
#    def move(self, dx, dy):
#        """ Move this object by the deltas """
#        self.corner.x += dx
#        self.corner.y += dy
#box = Rectangle(Point(0, 0), 100, 200)
#bomb = Rectangle(Point(100, 80), 5, 10)    # In my video game
#print("box: ", box)
#print("bomb: ", bomb)

def share_diagonal(x0, y0, x1, y1):
    """ Is (x0, y0) on a shared diagonal with (x1, y1)? """
    dy = abs(y1 - y0)        # Calc the absolute y distance
    dx = abs(x1 - x0)        # CXalc the absolute x distance
    return dx == dy          # They clash if dx == dy

def col_clashes(bs, c):
    """ Return True if the queen at column c clashes
         with any queen to its left.
    """
    for i in range(c):     # Look at all columns to the left of c
          if share_diagonal(i, bs[i], c, bs[c]):
              return True

    return False           # No clashes - col c has a safe placement.

def has_clashes(the_board):
    """ Determine whether we have any queens clashing on the diagonals.
        We're assuming here that the_board is a permutation of column
        numbers, so we're not explicitly checking row or column clashes.
    """
    for col in range(1,len(the_board)):
        if col_clashes(the_board, col):
            return True
    return False

    return False           # No clashes - col c has a safe placement.
def main():
    global temp
    import random
    rng = random.Random()   # Instantiate a generator
    bd = list(range(temp))     # Generate the initial permutation
    num_found = 0
    tries = 0
    while num_found < l+1:
       rng.shuffle(bd)
       tries += 1
       if not has_clashes(bd):
           draw_board(bd)
           print("Found solution {0} in {1} tries.".format(bd, tries))
           tries = 0
           num_found += 1

main()