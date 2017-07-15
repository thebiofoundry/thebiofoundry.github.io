from PIL import Image as image

img = image.open('C:/Users/Ngai_/Documents/GitHub/thebiofoundry.github.io/img/portfolio/cell_circuit.jpg')
img2 = img.crop((0,0,650,350))
img2.save("C:/Users/Ngai_/Documents/GitHub/thebiofoundry.github.io/img/portfolio/cell_circuit2.jpg")

img = image.open('C:/Users/Ngai_/Documents/GitHub/thebiofoundry.github.io/img/portfolio/skeet.jpg')
img2 = img.crop((0,0,650,350))
img2.save("C:/Users/Ngai_/Documents/GitHub/thebiofoundry.github.io/img/portfolio/skeet2.jpg")

img = image.open('C:/Users/Ngai_/Documents/GitHub/thebiofoundry.github.io/img/portfolio/tailings-pond.jpg')
img2 = img.crop((0,0,650,350))
img2.save("C:/Users/Ngai_/Documents/GitHub/thebiofoundry.github.io/img/portfolio/tailings-pond2.jpg")



img = image.open('C:/Users/Ngai_/Documents/GitHub/thebiofoundry.github.io/img/portfolio/terpenoid.png')
img2 = img.crop((0,0,650,350))
img2.save("C:/Users/Ngai_/Documents/GitHub/thebiofoundry.github.io/img/portfolio/terpenoid2.png")


img = image.open('C:/Users/Ngai_/Documents/GitHub/thebiofoundry.github.io/img/portfolio/biofuels.jpg')
img2 = img.crop((0,0,650,350))
img2.save("C:/Users/Ngai_/Documents/GitHub/thebiofoundry.github.io/img/portfolio/biofuels2.jpg")


# img = image.open('C:/Users/Ngai_/Documents/GitHub/thebiofoundry.github.io/img/portfolio/biofuels.jpg')

# half_the_width = img.size[0] / 2
# half_the_height = img.size[1] / 2
# img2 = img.crop(
#     (
#         half_the_width - 50,
#         half_the_height - 75,
#         half_the_width + 50,
#         half_the_height + 75
#     )
# )