import streamlit as st
import pandas as pd
import numpy as np

st.header('Example report')
st.write('Here is an example report that Manifold might find' +
         ' useful for presenting project updates to customers.' + 
         ' Let''s look at how horsepower affects mpg.')

# build a test df
hp = np.linspace(1,100, 100)
mpg = 10 * np.exp(-hp/20) + 1 * np.random.randn(100)
data = pd.DataFrame({'Horsepower': hp, 'mpg': mpg})
st.subheader('DF example:')
st.write(data)

st.subheader('Vega-lite example')
vega_spec = {
  "title": "How Horsepower effects mpg",
  "description": "A scatterplot showing horsepower and miles per gallons for various cars.",
  "data": {"url": "data/cars.json"},
  "mark": "point",
  "encoding": {
    "x": {"field": "Horsepower","type": "quantitative"},
    "y": {"field": "mpg","type": "quantitative"}
  }
}
# plot it
st.vega_lite_chart(data, vega_spec)
