# Which color scale to use when visualizing data

![[Images/Others/Color_scale_quantitative_and_qualitative_color_scale.png]]

In this part, we clarified terms like _categorical/qualitative color scale_, _sequential_, _diverging_, _classed_ and _unclassed_.

## What to color by

- Depend on the type of visualization, we decide to use color on specific characteristic of the data
- For example: The unemployment of the US in the 60s:
	-  In Choropleth map, we use color for the unemployment rate.
	-  In Line chart, we use color to represent different states
![[Images/Others/Color_scale_unemployment_example.png]]

## Categorical color scales

The most important things to keep in mind when using hues:

-   Give your hues different lightnesses so that they’d work in greyscale, too.
-   You don’t need to design a color palette yourself. Lots of people have created amazing color combinations you can use. [Here’s how to get inspired.](https://blog.datawrapper.de/colorguide/#3)

- Color combination suggested: yellow/orange/red and blue


## Sequential color scales

Sequential color scales are gradients that go from bright to dark or the other way round. They’re great for visualizing numbers that go from low to high.
- Using two or even more hues increases the color contrast between segments of your gradient, making it easier for readers to distinguish between them.
- To decide which data values correspond to which color in your gradient is called "interpolation" and has a massive influence on how readers perceive your values. [Here’s how to choose the best interpolation for your data.](https://academy.datawrapper.de/article/117-color-palette-for-your-map)

## Diverging color scales

- Diverging (also called _bipolar_ or _double-ended_) color scales have a bright middle value and then go darker to both ends of the scale in different hues.
- Diverging color scales are often used to visualize negative and positive values, election results, or Likert scales ("strongly agree, agree, neutral, disagree, strongly disagree").

![[Images/Others/Color_scale_diverging_color_scales_example_1.png]]

![[Images/Others/Color_scale_diverging_color_scales_example_2.png]]


## Highlighting/de-emphasizing

In any color scale, be it categorical, sequential, or diverging, you can highlight certain categories or value ranges that you consider especially important to your audience or story:

![[Images/Others/Color_scale_highlighting.png]]


# When to use quantitative and when to use qualitative color scales

- _shades_ and _gradients_ = quantitative color scale
- _hues_ = qualitative color scales.

## Use hues when your values don’t have an inherent order


Use hues when you can’t order your color-encoded values. Use a sequential or diverging color scale when you can.

![[Images/Pasted image 20210329115053.png]]

If you want to encode e.g., unemployment rates (3.4%, 1.4%, 2%) with color, use a quantitative color scale.
![[Images/Pasted image 20210329115113.png]]




















# 

---
Status: #writing

Tags: #color #idea #creativity

References:
- [# Which color scale to use when visualizing data](https://blog.datawrapper.de/which-color-scale-to-use-in-data-vis/)
- [# When to use quantitative and when to use qualitative color scales](https://blog.datawrapper.de/quantitative-vs-qualitative-color-scales/)
- [# When to use sequential and when to use diverging color scales](https://blog.datawrapper.de/diverging-vs-sequential-color-scales/)
- [# When to use classed and when to use unclassed color scales](https://blog.datawrapper.de/classed-vs-unclassed-color-scales/)

Related:
