import altair as alt # not working
from vega_datasets import data


# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='/chromedriver_win32/chromedriver.exe')

cars = data.cars.url

chart = alt.Chart(cars).mark_point().encode(
    x='Horsepower:Q',
    y='Miles_per_Gallon:Q',
    color='Origin:N',
)

# chart
chart.save('chart.png')
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
img=mpimg.imread('chart.png')
imgplot = plt.imshow(img)