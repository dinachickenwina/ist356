# Write a sentinel-controlled loop to input a color until quit
# Add the color to a list and print the list each time
# Do not add a color if it is already there in the list or the 'colors' variable
# Keep a separate list of duplicate colors and print it at the end
colors = [] # Make an empty list
duplicates = []
while True:
  color = input("Enter a color (or 'quit' to exit): ")
  if color.lower() = 'quit':
    break
  if color not in colors:
      colors.append(color)
  else:
      duplicates.append(color)
  print(f"Current list: {colors}")
  
print(f"Duplicate colors: {duplicates}")

# Scaffolded the AI: Guiding its generation by providing structured context, step-by-step instructions, or constraints—like the comments in your code—so it produces accurate results without guessing.
