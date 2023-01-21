# TLDR
- To be successful,
	- Talent matters
	- Luck is very important (might even more than talent)
- To get the most for society, resources should be evenly distributed
- In the environment rich in opportunities (i.e. developed country), talented people are more likely to succeed
- Ingredients of success:
	- A stimulating environment rich in opportunities
	- A good education
	- Intensive training
	- An efficient strategy for the distribution of funds and resources

# The world's assumption
- The secrets of the most successful people are their personal characteristics
- We assume that the most successful are also the most competent
- We tend to give out resources to those who have a past history of success, and tend to ignore those who have been unsuccessful

# Some recent findings
- About [half of the differences in income](http://documents.worldbank.org/curated/en/712251468165866186/pdf/946720JRN0Box30LIC00190rest0a000432.pdf) across people worldwide is explained by their country of residence and by the income distribution within that country
- Scientific impact is [randomly distributed](http://www.sciencesuccess.org/uploads/1/5/5/4/15543620/science_quantifying_aaf5239_sinatra.pdf), with high productivity alone having a limited effect on the likelihood of high-impact work in a scientific career
- The chance of becoming a CEO is influenced by [your name or month of birth](http://hanswisbrun.nl/wp-content/uploads/2015/07/Zomerbabies.pdf)
- The number of CEOs [born in June and July](http://hanswisbrun.nl/wp-content/uploads/2015/07/Zomerbabies.pdf) is much smaller than the number of CEOs born in other months
- Those with [last names earlier in the alphabet](http://pubs.aeaweb.org/doi/pdfplus/10.1257/089533006776526085?utm_source=weibolife) are more likely to receive tenure at top departments
- The [display of middle initials](http://ulir.ul.ie/bitstream/handle/10344/5412/Igou_2014_middle.pdf?sequence=4) increases positive evaluations of people's intellectual capacities and achievements
- People with [easy to pronounce names](http://pdfs.semanticscholar.org/7abf/3823a05c49e01ed140a7b95838e108e20a3a.pdf) are judged more positively than those with difficult-to-pronounce names
- Females with [masculine sounding names](http://sbmblog.typepad.com/files/ssrn-id1348280.pdf) are more successful in legal careers
- There is [a certain number of traits](https://www.amazon.com/Wired-Create-Unraveling-Mysteries-Creative/dp/0399175660) that can significantly affect success:
	- Passion
	- Perseverance
	- Imagination
	- Intellectual curiosity
	- Openness to experience
- [Talent develops over time](https://www.amazon.com/Ungifted-Intelligence-Scott-Barry-Kaufman/dp/0465025544), and is not a fixed quantity of the individual

# The first experiment: Luck and talent during a worklife

## Setup
![[03_Life_experience/Career building/The Role of Luck in Life Success/Figure 1.webp]]
- The experiment simulated the evolution of careers over a worklife of 40 years (from age 20-60).
- The key is that more talented people will get more out of a given opportunity
	- See [here](http://journals.sagepub.com/doi/abs/10.1111/1467-8721.00110) for support of this assumption
	- Talent is set of personal characteristics allow a person to exploit lucky opportunities
		- I've argued [elsewhere](https://www.theguardian.com/science/2013/jul/07/can-science-spot-talent-kaufman) that this is a reasonable definition of talent
	- Talent can include traits such as intelligence, skill, motivation, determination, creative thinking, emotional intelligence, etc.

## Procedure
- All 1000 agents began with the same level of success (10 "units").
- Talent was normally distributed
- Every 6 months, individuals were exposed to a certain number of lucky events (in green) and a certain amount of unlucky events (in red).
	- Whenever a person encountered an unlucky event, their success was reduced in half
	- Whenever a person encountered a lucky event, their success doubled proportional to their talent
		- (to reflect the real-world interaction between talent and opportunity).

## Result
- A small number of people will end up achieving the success of most of the population
	- The 20 most successful individuals held 44% of the total amount of success
	- Almost half of the population remained under 10 units of success (the initial value)
	- This is consistent with real-world data
		- Though in real world, wealth success is even more unevenly distributed, with [just eight men owning the same wealth as the poorest half of the world](https://www.oxfam.org/en/research/economy-99).
- **Talent mattered**
	- The most successful agents were mostly at least average in talent
- **The most successful agents are slightly above average in talent but with a lot of luck**
	- The most successful agents tended to be those who were only slightly above average in talent but with a lot of luck in their lives
	- The most talented individuals were rarely the most successful
	- In general, mediocre-but-lucky people were much more successful than more-talented-but-unlucky individuals
- Even a great talent becomes useless against the fury of misfortune

# The second experiment: Effective funding strategy
- Many meritocratic strategies used to assign honors, funds, or rewards are often based on the past success of the person.
	- Which makes the rich get richer and the poor get poorer

## The past experiment
- Consider a [study](http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0065263) conducted by Jean-Michel Fortin and David Currie
	- They found a positive, but only very small relationship between funding and impact
	- Those who received a second grant were not more productive than those who only received a first grant
- In a [more recent study](https://arxiv.org/pdf/1602.07396.pdf), researchers looked at the funding provided to 12,720 researchers in Quebec over a fifteen year period.
	- Funding strategies that focus more on targeting diversity than "excellence" are likely to be more productive to society
	- They concluded that "both in terms of the quantity of papers produced and of their scientific impact, the concentration of research funding in the hands of a so-called 'elite' of researchers generally produces diminishing marginal returns."

## Setup
- The team use the same setup of the first experiment

## Procedure
- They applied different strategies every five years during the 40 year worklife of each agent in the simulation

## Results
![[03_Life_experience/Career building/The Role of Luck in Life Success/Figure 10.webp]]
- This table reveals the most efficient funding strategies over the 40 year period (i.e., requiring the least amount of funding for the greatest return on the investment)
- In complex social and economic contexts where chance is likely to play a role, strategies that incorporate randomness can perform better than strategies based on the "naively meritocratic" approach
	- The least effective funding strategies are those that give a certain percentage of the funding to only the already most successful individuals
	- The "mixed" strategies that combine giving a certain percentage to the most successful people and equally distributing the rest is a bit more effective
	- Distributing funds at random is even more efficient
	- This last finding is intriguing because it is consistent with [other](https://arxiv.org/pdf/1209.5881.pdf) research
- The best funding strategy of them all was one where an equal number of funding was distributed to everyone
	- Distributing funds at a rate of 1 unit every five years resulted in 60% of the most talented individuals having a greater than average level of success
	- Distributing funds at a rate of 5 units every five years resulted in 100% of the most talented individuals having an impact

# The third experiment: Stimulating environment

## Setup
- They simulated 2 environment
	- A very stimulating environment, rich of opportunities for everyone (like that of rich and industrialized countries such as the U.S.)
	- A much less stimulating environment, with very few opportunities (like that of Third World countries)

## Result
![[03_Life_experience/Career building/The Role of Luck in Life Success/Figure 13.webp]]
- In the environment rich in opportunities (top)
	- A number of medium to highly talented individuals were able to reach very high levels of success
	- The average number of medium-highly talented individuals who reached at least above average levels of success was quite high
- In the environment poor in opportunities (bottom)
	- The overall level of success of the society was low
	- An average of only 18 individuals able to increase their initial level of success

# Conclusion
- Luck and opportunity play an underappreciated role in determining the final level of individual success
- Rewards and resources are usually given to those who are already highly rewarded
	- It doesn't take into account the important role of luck
	- It also cause the lack of opportunities for those who are most talented (i.e., have the greatest potential to actually benefit from the resources)
- Ingredients of success:
	- A stimulating environment rich in opportunities
	- A good education
	- Intensive training
	- An efficient strategy for the distribution of funds and resources

#
---
- Status: #done
- Tags: #career
- References:
	- [The Role of Luck in Life Success Is Far Greater Than We Realized](https://blogs.scientificamerican.com/beautiful-minds/the-role-of-luck-in-life-success-is-far-greater-than-we-realized/)
	- [Twitter Source](https://twitter.com/dvassallo/status/1611094849746538497)
- Related:
