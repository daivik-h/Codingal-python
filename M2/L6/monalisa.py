import turtle

def draw_embedded_monalisa():
    # 1. The Color Palette (Hex Codes)
    D = "#1b140c" # Dark hair / Background shadows
    S = "#c39b75" # Light skin tone
    M = "#9b6b47" # Mid skin / shadow (Sfumato)
    E = "#000000" # Eyes
    B = "#3d422a" # Dark olive dress
    
    # 2. The Baked-In Image Data
    # To make this higher resolution, you would simply expand this list
    # with more rows and more color variables.
    pixel_matrix = [
        [D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D],
        [D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D],
        [D, D, D, M, M, M, M, M, M, M, M, D, D, D, D, D],
        [D, D, M, S, S, S, S, S, S, S, S, M, D, D, D, D],
        [D, D, M, S, S, S, S, S, S, S, S, M, D, D, D, D],
        [D, D, M, S, E, S, S, S, S, E, S, M, D, D, D, D],
        [D, D, M, S, S, S, S, S, S, S, S, M, D, D, D, D],
        [D, D, M, S, S, M, M, M, M, S, S, M, D, D, D, D],
        [D, D, D, M, S, S, M, M, S, S, M, D, D, D, D, D],
        [D, D, D, M, M, S, S, S, S, M, M, D, D, D, D, D],
        [D, D, D, D, M, M, M, M, M, M, D, D, D, D, D, D],
        [D, D, D, B, B, B, M, M, B, B, B, D, D, D, D, D],
        [D, D, B, B, B, B, B, B, B, B, B, B, D, D, D, D],
        [D, B, B, B, B, B, B, B, B, B, B, B, B, D, D, D],
        [B, B, B, B, B, B, B, B, B, B, B, B, B, B, D, D],
        [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, D]
    ]

    # 3. Setup Turtle Environment
    screen = turtle.Screen()
    screen.title("Standalone Pointillism")
    screen.bgcolor("white")
    
    # CRITICAL: Turn off animations. 
    # If you turn this on, watching the dots draw will take forever.
    turtle.tracer(0, 0) 

    t = turtle.Turtle()
    t.hideturtle()
    t.penup()

    # 4. Matrix Rendering Configuration
    # We scale the coordinates so the tiny 16x16 grid stretches across the screen.
    # A scale of 20 means each dot is placed 20 pixels apart.
    scale = 20 
    dot_size = 25 # Make the dots overlap slightly to blend colors
    
    # Calculate starting position to center the drawing
    rows = len(pixel_matrix)
    cols = len(pixel_matrix[0])
    start_x = -((cols * scale) / 2)
    start_y = ((rows * scale) / 2)

    # 5. The Drawing Loop
    print("Executing pointillism render...")
    for row_idx, row in enumerate(pixel_matrix):
        for col_idx, color in enumerate(row):
            
            # Calculate coordinates
            x = start_x + (col_idx * scale)
            y = start_y - (row_idx * scale)
            
            # Move and draw
            t.goto(x, y)
            t.dot(dot_size, color)

    # Update screen once all calculations and dots are placed
    screen.update()
    print("Render complete!")
    
    # Keep the window open
    screen.exitonclick()

if __name__ == "__main__":
    draw_embedded_monalisa()