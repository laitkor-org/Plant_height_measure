

from PIL import Image, ImageDraw

# Load the plant image in its original size
plant_image = Image.open('bottle1.jpg')
plant_width, plant_height = plant_image.size




actual_height_in_inches = 13       #only do the changes in this and generate the images ,,,,,, think about approximate height of plant suppose it is 8.3 inch so mention here 9 .and run the code 

# Calculate pixels per inch based on the plant image's pixel height
pixels_per_inch = plant_height / actual_height_in_inches

# Create a blank canvas larger than the plant image to accommodate rulers
canvas_width = plant_width + 50  # 50 pixels extra for the left ruler
canvas_height = plant_height + 50  # 50 pixels extra for the bottom ruler
canvas = Image.new('RGB', (canvas_width, canvas_height), 'white')
draw = ImageDraw.Draw(canvas)

# for drawing scale value on vertical side ................   0,  0.5, 1, 1.5, 2, 2.5, 3, 3.5...................so on  
for i in range(0, int(plant_height / (pixels_per_inch * 0.5)) + 1):
    # Calculate position and inch value
    y_position = canvas_height - 50 - int(i * pixels_per_inch * 0.5)
    inch_value = i * 0.5

    # Draw tick mark and add text label every 1 inch for better readability
    draw.line((0, y_position, 10, y_position), fill='black')
    if inch_value.is_integer():  # Display labels only at whole numbers
        draw.text((15, y_position - 5), f"{int(inch_value)} in", fill='black')
    else:
        draw.text((15, y_position - 5), f"{inch_value:.1f} in", fill='black')

# for drawing scale value on horizontal side ................   0,  0.5, 1, 1.5, 2, 2.5, 3, 3.5...................so on  
for i in range(0, int(plant_width / (pixels_per_inch * 0.5)) + 1):
    # Calculate position and inch value
    x_position = 50 + int(i * pixels_per_inch * 0.5)
    inch_value = i * 0.5

    # Draw tick mark and add text label every 1 inch for better readability
    draw.line((x_position, canvas_height - 10, x_position, canvas_height), fill='black')
    if inch_value.is_integer():  # Display labels only at whole numbers
        draw.text((x_position, canvas_height - 25), f"{int(inch_value)} in", fill='black')
    else:
        draw.text((x_position, canvas_height - 25), f"{inch_value:.1f} in", fill='black')



    
    
    
# Position to paste the plant image on the canvas (leaving space for rulers)
plant_position = (50, canvas_height - plant_height - 50)

# Paste the original plant image onto the canvas without resizing
canvas.paste(plant_image, plant_position)

# Save the final image with the plant and rulers
canvas.save('image_with_plant_and_rulers_high_quality_ONE.png')

print("The image with the plant and rulers has been saved at original quality.")
