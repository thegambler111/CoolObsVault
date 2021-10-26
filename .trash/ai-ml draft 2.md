# Interviewing engineers, part 2

March 2021

Reading time: 11 minutes

Welcome back! In [part 1](https://xdg.me/interviewing-engineers) of this article, I said:

> I think tech industry hiring is pretty broken. If you feel the same and are looking for inspiration, I'll tell you what I did differently when I had the chance.

Part 1 covered my philosophy about interviewing and I described changes I made to the hiring process:

-   Using promotion criteria to guide hiring criteria
-   Having the hiring manager do the first interview
-   Saving synchronous time for interaction, not coding
-   Using take-home exercises as part of the initial screen

I also gave examples for [effective non-technical interviewing](https://xdg.me/interviewing-engineers/#only-give-a-take-home-if-they-pass-a-non-technical-phone-screen).

In part 2, I'll share some tactical ideas for giving humane take-homes, writing good coding questions, organizing onsites, and coaching your interviewers.

### A humane take-home exercise is short and deserves feedback.[](https://xdg.me/interviewing-engineers-2/#a-humane-take-home-exercise-is-short-and-deserves-feedback)

Take-home exercises are controversial. Some companies treat a take-home as an opportunity to give a substantially bigger programming project than they would give onsite. Take-homes can be biased against people who don't have that kind of free time to program. Or companies worry that people will cheat and get help.

I believe that a _short_ take-home addresses these problem. By "short", I mean taking no longer than an in-person interview would take. I pitch it like this:

> "instead of doing an in-person coding exercise, I'd like to ask you to do a take-home; it should take the same amount of time but you can do it in your own coding environment and at a convenient time for you"

Because it takes the same amount of time as another phone screen, it's no more time-consuming than a normal interview and has the benefit of not having to be rigidly scheduled into a mutually agreeable hour. That helps people who are challenged for free time. Because it's short, the payoff from cheating is lower; it's not impossible, but it's less likely.

The other thing I did is promise that every take-home would get written feedback from me.

This is part of treating people with respect. I'm asking someone to invest their time into this evaluation process. Whether we go forward or not, I feel I owe them some of my time in return. I'm going to take notes _anyway_ as I read their code, so turning that into a quick email doesn't even require much extra effort.

My feedback was generally five to ten bullet points. I talked about what I liked in their work and what I didn't like or thought could have been done a different or better way. If there was a mistake or bug I found, I mentioned that, too.

Here's a template that I used when emailing the take-home instructions:

Hi, *name*. It was a pleasure getting to know you today.

You can find the take-home exercise here: *link*

I think it explains things well, but feel free to email me if not. Please aim to spend no more than an hour on it.

After you've looked at the exercise description, please email me to let me know when you think you'll have a chance to get it back to me.

You can email me a tarball at this email address when you're done and I'll review it and give you feedback.

Regards, David

In the exercise instructions, I described the problem for them to solve, reminded them that they could ask questions, and reminded them how to return their code. I preferred an emailed tarball or zip file, to keep the exercise out of a public repository.

### A good coding question relates to a real-world problem.[](https://xdg.me/interviewing-engineers-2/#a-good-coding-question-relates-to-a-real-world-problem)

It's a cliché that coding exercises are ‘leet code' algorithm puzzles that even [famous programmers aren't good at](https://twitter.com/dhh/status/834146806594433025). The reality is that most programming _outside of interviews_ doesn't require memorization of CS techniques. If we want signal on what someone would be like on the team, we should give them problems that are similar to what we expect them to work on.

Ideally, you should be able to explain how a coding exercise relates to a real problem you or the team had to solve, even if simplified. For example, I have a problem involving hierarchical, document-type data structures, but I'll ask them to solve it only for string values instead of the 20+ possible supported types.

When I was explaining to my team how come up with coding questions, I shared my thoughts on some hallmarks of a good exercise:

-   An existing coworker could solve it in the expected amount of time without any special prep. (Try it!)
-   The problem is intellectually engaging, provoking curiosity.
-   It combines more than one data structure or algorithm; neither should be esoteric.
-   There is more than one valid way to solve it.
-   There are edge cases or error handling to consider.

Not every exercise will meet all criteria, but it's something to strive for.

Another way to think about it is to imagine what coworkers actually do day to day. How can interviews replicate those conditions or test for success on those terms?

For example, at work…

-   People read tickets and implement a solution
-   People ask questions about ambiguous tasks
-   People diagnose bugs
-   People write tests
-   People review others' code

So imagine a coding exercise like writing a ticket. Describe a problem with enough context that they can implement it. Maybe give them existing code to extend! Maybe leave some things out and see if they ask questions or make assumptions. See if they write tests. Or give them some code with a bug and some sample, buggy output and have them find and fix the problem.

Any of these will give much better signal on whether someone can **actually do the work** than puzzles like "find the longest substring with K distinct characters".

### An onsite applies the same principles as the phone screen.[](https://xdg.me/interviewing-engineers-2/#an-onsite-applies-the-same-principles-as-the-phone-screen)

Assuming a candidate passed the phone screen and take-home, it was time to bring them onsite. (These days, it would be a ‘remote onsite'.) At MongoDB, like many, this was usually a full day of interviews.

I described the principles I applied to the phone screen and take-home in [part 1](https://xdg.me/interviewing-engineers). The onsite was more of the same, with a few adjustments. Here is the structure I used.

**Sample onsite schedule**

1.  Coding exercise (2 hours) – this is essentially a "double take-home", done onsite. Candidate is given a list of coding exercises similar to the take-home and has 2 hours to choose and complete 2 of the exercises.
    
    -   As with the take-home exercise, the candidate works on their own in a private room, with their own laptop, with access to the Internet, etc. I stay nearby to answer any questions that come up.
2.  Group code review (1 hour) – The candidate presents their work from #1 to a group of 3-5 engineers, including the hiring manager and at least one other senior+ engineer.
    
    -   Candidates are expected to walk through their work and answer questions or respond to feedback that the reviewers have about it.
        
    -   In addition to assessing code, this also examines how the candidate communicates technical topics and how they react to criticism.
        
3.  Lunch (1 hour) – The candidate eats lunch and socializes with a small group of engineers.
    
    -   Interviewers should balance between casually probing the candidate's experiences and selling the company.
        
    -   On the one hand, this is a mental break for the candidate. On the other, candidates sometimes let down their guard and we may see their more genuine self.
        
4.  Non-technical interview (1 hour) – This is similar to the phone screen focusing on level 3 criteria. The interviewer should generally be at or above the seniority level of the candidate.
    
5.  Design interview (1 hour) – For a senior+ candidate, they'll do a [system design](https://xdg.me/resources-for-system-design-interview-prep/) exercise. The interviewer should generally be at or above the seniority level of the candidate.
    
    -   The interviewer should prompt the candidate with a design question that will help assess factors in the [scorecard](https://xdg.me/interviewing-engineers/#the-success-of-a-hire-isnt-based-what-they-do-in-their-first-week-or-first-month) section on design interviews. It's helpful for calibration if interviewers use the same design question for all candidates, if possible.
        
    -   [Susan Fowler](https://www.susanjfowler.com/blog/2016/10/7/the-architecture-interview) has a great write up on how to give these sorts of interviews.
        
6.  Executive interview (1 hour) – At the time, my company had an executive above the level of the hiring manager participate and give a non-technical interview. If this wasn't mandatory, I would have added another non-technical interview with a team member or peer.
    
7.  Recruiter interview (1 hour) – My company had the recruiter wrap up with a candidate at the end of the day. YMMV.
    

This schedule has a balance between technical and non-technical interviews. It gave a lot of people a chance to meet the candidate, reducing the risk of a single bad interview skewing the outcome. And since I did the pre-screening, I was comfortable investing the team's time significantly in this way because I was already inclined to say yes. Think of it like a null hypothesis. The team's job was to back up my initial assessment with additional evidence **or** turn up evidence that the initial thinking was a mistake.

In hindsight, I really liked giving candidates a choice of coding questions and wished I had done the same for the take-home exercise. The point is to replicate – however imperfectly – how they would work in a low-stress, day to day situation on a familiar codebase. An interview is too artificial for that, but letting them choose questions to answer means they're deciding what they think shows their best work. That means we're getting better signal.

At the time, we didn't have enough questions prepared to do that for the take-home as well as the onsite, but if I'm in this position again, I'd make sure to have enough questions to give a choice for both parts of the interview process.

### Coach your interviewers on how to interview and give feedback.[](https://xdg.me/interviewing-engineers-2/#coach-your-interviewers-on-how-to-interview-and-give-feedback)

Before interviewing anyone, the recruiter and I drew up a list of team members and assigned them to the various parts of the schedule. Whenever possible, we had people play the same role for all candidates. This helps with calibration – the more people you see solve a particular exercise or answer a particular question, the better you're able to judge the quality of the answers you'll get.

In addition, I made a "Guide to interviewing for David's Team" that I shared with everyone. Here's an excerpt from it:

Before an Interview

-   DO review the scorecard and strategize how your questions will illuminate particular portions of it. Consider printing it out and bringing it with you for reference.
    
-   DO share your planned questions on the group slack channel.
    
-   DO review this document: it's a helpful refresher on things to keep in mind for each interview.
    

During an Interview

-   DO give the candidate an agenda for the time you'll be with them – knowing what will happen sets candidates at ease.
    
    -   E.g. "So you know what to expect in this interview, first I'm going to tell you a bit about my role here, then I'm going to ask you some questions about your professional experiences, then we'll take some time working through a design exercise. At the end, I'll reserve some time for you to ask me some questions. Does that make sense?"
-   DO take notes. The means of doing this is up to the interviewer. The purpose of note-taking is to ensure that we accurately capture salient aspects of the candidate's response to questions.
    
-   DO sell the company: This is can be done implicitly by your interaction during the interview, but will likely be more explicit toward the end of the meeting - supported also by the candidate's questions.
    

After an Interview

-   DO provide detailed feedback on \[our interview website\] soon after your interview - while your memory is fresh.
    
    -   For scorecard elements: please add short comments to any item you rate to give context for the rating; don't rate things you didn't get signal on during the interview.
        
    -   For the summary: include observed pros/cons and any details about the interview that would be helpful in reaching a decision.
        
    -   Take a stand – "No decision" means your interview failed to provide actionable insights and you should do a retrospective with the hiring manager or recruiter to see how you can improve your interviewing technique.
        
-   DO attend the debrief that is scheduled after all interviews are completed.
    

These are all intentionally phrased positively. But all my interviewers had been through interview training and I relied on that for the things they shouldn't do (e.g. asking questions about legally protected characteristics).

Thinking back, while I wanted to minimize bias in the interview process, I didn't write down specific suggestions in the guidelines about it. I think I'd do more on that the next time.

### Change what you can, but accept what you can't.[](https://xdg.me/interviewing-engineers-2/#change-what-you-can-but-accept-what-you-cant)

I was able to try a very different process because I pitched it as an experiment. But there were things I wasn't able to change. For example, I'd really wanted to explore alternate ways of getting people into the recruiting funnel, but I wasn't able to convince people to let me try. In the end, I took what I could get and created the best process I could. I think what I came up with was effective at getting signal, was less stressful for candidates, and made good use of everyone's time.

I've rotated back to an IC role, so my experiment has stopped for now. I wrote this article as a letter to my future self for the next time I'm in a position to hire and as inspiration to others frustrated with the status quo.

If you're a hiring manager and don't like your current process, I encourage you to try your own experiments! Use this article for inspiration, or look at my [curated links on better technical interviewing](https://xdg.me/better-technical-interviewing/) for more ideas. And if you try something new, I'd love to hear how it works for you!