# TLDR

- Use yellow / orange / red and blue
- Avoid pure green, make them yellow green or blue green instead
- Smaller hue range, better use of saturation and lightness
- Avoid pure colors, bright and saturated colors or same lightness colors
- Make only one or two colors stand out, others are equally attention-grabbing



# Color space
The color space using in this article will mostly be HSB (**H**ue, **S**aturation, **B**rightness) or HSV (**H**ue, **S**aturation, **V**alue):

-   **Hue** ranges from 0° to 360°…that’s your typical color wheel: ![[Images/Others/Beautiful_color_hue.png]]
-   **Saturation** ranges from 0% (grey) to 100% (super duper colorful!!): ![[Images/Others/Beautiful_color_saturation.png]]
-   **Brightness/Value** ranges from 0% (black) to 100% (the actual color: ![[Images/Others/Beautiful_color_brightness.png]]



# Broaden your understanding of colors

![[Images/Others/Beautiful_color_boarden_colors.png]]

There are a lots of color. Using only basic color is fine but it is better to use different color scales and when to use them.


# Don’t dance all over the color wheel

![[Images/Others/Beautiful_color_not_all_color_wheel.png]]

 It will look more professional – and therefore more trustworthy – when it only uses a few hues and their neighbors.

# Use saturation and lightness to make your hues work

![[Images/Others/Beautiful_color_S_and_B_are_important.png]]

Saturation and brightness are as important as hue. In fact, you can create new colors when you just change the saturation and brightness. 
Here are two color pairs with the same hue, just different saturation and lightness: ![[Images/Others/Beautiful_color_same_H_diff_SB.png]]


# Use warm colors & blue

![[Images/Others/Beautiful_color_warm_and_blue.png]]

- There’s a complementary color combination that is especially loved by data visualization designers: **yellow/orange/red and blue**
	- **Yellow, orange and red** look very pleasing together, but people will still perceive them as different colors: ![[Images/Others/Beautiful_color_yellow_orange_red.png]]
	- **Blue** is more flexible than any other hue: Lots of blues, no matter if dark ![[Images/Others/Beautiful_color_dark_blue.png]] or light ![[Images/Others/Beautiful_color_light_blue.png]] or saturated ![[Images/Others/Beautiful_color_saturated_blue.png]] or not saturated ![[Images/Others/Beautiful_color_not_saturated_blue.png]], look pleasing, calming and professional.
	- Colorblind people can easily distinguish blue and orange/red from each other.

# When using green, make it a yellow or blue one

![[Images/Others/Beautiful_color_not_pure_green.png]]

Few well-designed visualizations use green because:
- Forest green is very dark, lightening it up gives an awkward neon
	- => Need to lighten up and desaturate green more than other colors to get to a nice one.
- A pure green in combination with red, orange, or brown is hard for colorblind people to distinguish
=> When using green, make it a bit yellow or a bit blue.

# Avoid pure colors

![[Images/Others/Beautiful_color_color_wheel.png]]


"Pure" hues are the ones that are located at exactly 60°, 120°, 180°, 240°, 300° or 360°/0° in the color wheel:


![[Images/Others/Beautiful_color_change_hue.png]]

To make your colors look more natural and pleasing to your readers’ eyes, you can either tune down the saturation of pure colors or make them darker.

In the image above, the red and orange, the blues and the greens have the same saturation and lightness. The only difference is the hue

# Avoid bright, saturated colors

![[Images/Others/Beautiful_color_avoid_bright_and_saturated.png]]

- Neon colors will definitely attract the attention of readers. However, most of us get a bit stressed out when we see them.
- If your colors come close to 100% saturation **and** 100% brightness, it’s likely your colors are too colorful. ![[Images/Others/Beautiful_color_too_colorful.png]]


# Combine colors with different lightness

![[Images/Others/Beautiful_color_different_lightness_colors.png]]


- To check if your colors has the same lightness or not, just convert your colors in black & white. If they all have the same grey, they’re the same lightness.
- There are 2 ways to fix this:
	- "Get it right in black & white": change the darkness of each area, making some brighter and some darker, from ![[Images/Others/Beautiful_color_same_lightness.png]] to ![[Images/Others/Beautiful_color_different_lightness.png]]. They look like this in greyscale: ![[Images/Others/Beautiful_color_different_lightness_grayscale.png]]
	- Separate the areas, e.g. with a white border 
- In fact, a valid way to pick colors for categorical data is to pick colors from gradients like those below. All those gradients move smoothly from light to dark, so colors you pick from there will all have a different lightness


![[Images/Others/Beautiful_color_gradients.png]]

# Make your colors similarly "colorful"

![[Images/Others/Beautiful_color_color_stand_out.png]]

- There are different ways to make colors stand out:
	- They’re way darker ![[Images/Others/Beautiful_color_color_stand_out_darker.png]]
	- They’re way lighter ![[Images/Others/Beautiful_color_color_stand_out_lighter.png]]
	- They’re more saturated ![[Images/Others/Beautiful_color_color_stand_out_more_saturated.png]]
	- They’re more"pure" ![[Images/Others/Beautiful_color_color_stand_out_more_pure.png]]
- However, you usually just want one or two colors to stand out
- Most of your colors are supposed to be **more or less equally attention-grabbing**:
	- Color with different lightness: 
		- Desaturate bright colors
		- Put more saturation in dark colors.
	- Pure hue colors ![[Images/Others/Beautiful_color_pure_hue_red.png]]:
		- Darken them ![[Images/Others/Beautiful_color_darken_red.png]]
		- Change the hue value ![[Images/Others/Beautiful_color_red_to_orange.png]]

# Avoid too little contrast to the background

![[Images/Others/Beautiful_color_little_contrast.png]]

When your colors are too desaturated & light ![[Images/Others/Beautiful_color_lack_contrast.png]]
- Increase the saturation: ![[Images/Others/Beautiful_color_more_saturation.png]]
-  Make them darker: ![[Images/Others/Beautiful_color_darker.png]]
-  Or do both for the best result:![[Images/Others/Beautiful_color_more_saturation_and_darker.png]]


# Avoid too much contrast to the background

![[Images/Others/Beautiful_color_much_contrast.png]]

When your colors are too dark and saturated:
- Make them lighter
- Reduce saturation

# Choose a background that’s desaturated enough


![[Images/Others/Beautiful_color_desaturated_background.png]]

- Colorful backgrounds have two drawbacks
	- They easily distract from your data
	- They’re limiting your potential color palette =>hard to work with
- Rules of thumbs for the HSB/HSV color space:
	- If you want a light background, stay away from colors below 95% lightness and above 7% saturation.
	- If you want a dark background, stay below 20% saturation. Also, [don’t go full black](https://ianstormtaylor.com/design-tip-never-use-black/) – keep your lightness between 10% and 25%.


# Copy colors, or understand them

![[Images/Others/Beautiful_color_picking_color.png]]


If you do want to build a better intuitive understanding of which colors fit well together, try analyze them:
- Select a picture with colors you consider beautiful, like an art piece or photo of nature. Then pick colors out of them and try to use them in your next chart.
- Pick colors from beautiful data visualizations. **Change a few colors.** Do they still work well together?








# 

---
Status: #done

Tags: #color #visualization 

References:
- [How to pick more beautiful colors for your data visualizations](https://blog.datawrapper.de/beautifulcolors)

Related:
