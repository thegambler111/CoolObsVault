# Interviewing engineers

March 2021

Reading time: 13 minutes

I think tech industry hiring is pretty broken. If you feel the same and are looking for inspiration, I’ll tell you what I did differently when I was a hiring manager at MongoDB.

Caveat: I don’t claim this only way to interview. It’s just something I tried that I think is better than the typical way it’s done. Take my ideas if you’d like, but do your own experiments and see what works for you.

I’ve had two careers: one in consulting and one in technology. In both, I was (and still am) part of a hiring process that aims to hire only “the best”. In reality, this is [unrealistic](https://blog.nukemberg.com/post/talent-is-largely-a-myth/), myopic, and terribly prone to bias. But it’s probably the same goal your organization has and it leads most everyone to the same terrible processes.

Not long ago, I was in a role as hiring manager where I had the latitude to design a better interview process.

This is my story.

If you don’t want to read another rant about why things are broken, [jump to the details](https://xdg.me/interviewing-engineers/#changing-interview-processes-is-hard) of what I did.

### No one sets out to hire the average.[](https://xdg.me/interviewing-engineers/#no-one-sets-out-to-hire-the-average)

I’ve interviewed hundreds of people. I’ve seen how colleagues talk about candidates afterwards. I’ve seen how hiring decisions go right and go wrong. I’ve seen hires turn out great and terrible. So I have some sense of why companies interview the way they do.

Here are some things I believe:

-   Everyone wants to find the best in whatever pool of candidates they have.
-   Everyone is more worried about making a bad hire than missing out on a good candidate.
-   Most interviews have nothing to do with what candidates will do in the job or what will make them successful.
-   Most interviewers aren’t well-trained and don’t prepare.
-   Most interviewers don’t want to be outliers from their peers.

As a result, _most people interview with a conscious or unconscious intention of finding reasons not to make an offer_. Interviewers are biased towards safety – towards candidates who resemble themselves or people already at the company. The typical style of interview provides little signal for assessing if someone will be a good or bad hire.

Doing it this way is tailor-made for hiring “safe” candidates from overrepresented groups whose best skill is interviewing well. Many companies think this is good enough.

What’s wrong with this approach?

One obvious problem is that it leads to less diverse hiring. This should be motivating enough, but history proves otherwise. Let’s assume, for the sake of argument, that your company doesn’t care about diversity. (It _should_, but let’s assume it’s not sufficient motivation.) What _other_ problems are there?

### Hiring safe candidates makes recruiting slow and expensive.[](https://xdg.me/interviewing-engineers/#hiring-safe-candidates-makes-recruiting-slow-and-expensive)

Does your company complain about how hard it is to hire? Or can’t meet its growth goals? This might be a self-inflicted wound.

Being over-selective for “safe” candidates means you have to interview a lot more people to find ones that pass the filter. That’s slow and wasteful. How many engineer-hours are spent interviewing candidates you reject? Being overly selective is a tax on productive development.

And you know what good interviewers are also good at? Interviewing at other companies! The ones that pass your filter probably pass filters elsewhere, meaning that you’re more likely to be in a competitive hiring situation, driving up compensation costs and possibly losing out to more prestigious (or higher-paying) competition. Losing a competitive situation wastes all the expensive engineering hours you just put into interviewing.

I suspect that the high variance of interviewing has a subtle effect on the available pool of experienced candidates, too. If you’re doing well and secure in your job, would you want to spent a lot of time on interview prep and then interview with a high chance of being rejected for arbitrary reasons?

### Changing interview processes is hard.[](https://xdg.me/interviewing-engineers/#changing-interview-processes-is-hard)

I’ve sat in meetings, roundtables, and breakout groups on the problems with the interview process and ideas for what to do differently. I’ve compiled [dozens of articles](https://xdg.me/better-technical-interviewing/) about what’s wrong and what people are trying to do to fix it.

Change is hard for institutions. It’s risky for anyone to deviate from the way things are always done because the personal consequences of breaking something that works is scarier than the reward that comes from making things better.

As a hiring manager, I fought to run my own experiment. It was far easier to get permission in my own sandbox than change the company as a whole.

When I set out to create a better process, I had several goals:

-   Measure candidates on criteria that matter
-   Reduce candidate stress to get better signal
-   Make efficient use of everyone’s time
-   Treat people with respect, the way I’d want to be treated

### To find the best candidates, look to your promotion criteria.[](https://xdg.me/interviewing-engineers/#to-find-the-best-candidates-look-to-your-promotion-criteria)

Many hiring processes go awry because they’re sifting for the wrong criteria. My company’s interviewer training course talked about three levels of hiring assessment:

1.  appearance, manners, expressions, interests, resume (DON’T USE THESE)
2.  knowledge, skills, experience, education, references
3.  determination, motivation, endurance, communication, integrity

Not only are Level 1 topics not job-relevant, some may be [illegal](https://www.betterteam.com/illegal-interview-questions) as well.

We then did a fascinating exercise, setting aside interviewing criteria and brainstorming what characteristics would get someone promoted.

For example:

-   For a junior role: follows directions, asks good questions, writes readable code, makes few obvious error, shows attention to detail.
    
-   For a senior role: identifies alternatives, weighs tradeoffs, tailors work to business goals, communicates clearly, pushes back appropriately, teaches best practices, can move between projects and technologies.
    

Notice how these are mostly level 3 criteria? (Particularly at the senior level.)

### The success of a hire isn’t based what they do in their first week or first month.[](https://xdg.me/interviewing-engineers/#the-success-of-a-hire-isnt-based-what-they-do-in-their-first-week-or-first-month)

A hire is successful if they show value over time. And what do we do with those kinds of employees? We promote them! So instead of apply “hiring criteria” to candidates, we should be looking at how to apply “promotion criteria” during the interview and assessment process.

Unfortunately, despite such insightful interview training, almost every interview scorecard I ever saw focused mostly on level 2 criteria. So when I started hiring, I wrote my own.

In my guide for interviewers (which I’ll discuss later), I asked people to pick one or two level 3 criteria to focus on, and then note any level 2 criteria that come up in the interview. Different interview types might probe for _some_ level 2 specifics. And I said it was fine to leave scorecard categories blank if they didn’t come up.

Here is a slightly redacted copy of the scorecard. Feel free to use it as a model, but please customize the criteria for what’s important to you.

**Sample Interview Scorecard**

Guide to interviewers: This scorecard emphases level 3 and level 2 criteria. Interview questions and discussion can’t cover all the elements below, but should be chosen to provide signal on these criteria.

Level 3: Execution

-   Handles complexity and uncertainty
-   Makes good delivery tradeoffs
-   Takes initiative/is self-directed

Level 3: Personal Growth

-   Learns from failure/feedback
-   Seeks out new challenges
-   Strives for mastery

Level 3: Collaboration

-   Is intellectually honest
-   Lifts skills/output of others
-   Strong opinions, but low ego

Level 2: Coding Exercise Only

-   Correctness
-   Design
-   Efficiency
-   Factoring/structure
-   Readability
-   Robustness
-   Testing

Level 2: Design Exercise Only

-   Communication of ideas
-   Covers boundary cases
-   Creativity/inventiveness
-   Engagement/curiosity
-   Good questions
-   Good tradeoffs
-   Right level of abstraction/detail

Level 2: Knowledge/Experience

-   Agile development
-   Concurrency/parallelism
-   Mentoring
-   Network programming
-   Open source development
-   Coding language of interest (e.g. Go, Python, C++, etc.)
-   Technical leadership
-   Technical writing

### The hiring manager should lead from the front.[](https://xdg.me/interviewing-engineers/#the-hiring-manager-should-lead-from-the-front)

I’ve never understood why so many hiring managers wait for an onsite before interviewing a candidate. I decided to be responsible for the initial engineering phone screen (after the recruiter phone screen).

Why did I do this? _As hiring manager, if I’m not comfortable making a hire, it’s not going to happen._ So if I wait until the end of the process, I’ve just wasted hours of my team’s time on interviews if I decide against a hire. By interviewing first, I’m confident that my team’s time is well spent. In the next round, the team validates my assessment, digging deeper into the details to confirm my initial willingness to hire or to convince me otherwise.

Deciding to move a candidate forward from a phone screen is also a place where bias can creep in. Having a single person’s assessment make or break someone’s candidacy means the assessment better be as thorough and unbiased as possible. As hiring manager, I shouldn’t pass the buck. For one, if we’re going to use a single assessment, it should be the responsibility of the most experienced interviewer, not someone more junior. For another, if my pipeline is biased in the phone screen, I need to own that and not put the responsibility (and blame) on another engineer on the team.

The other responsibility I owned was rejection. Since I own the decision to reject a candidate, I was the one who told them, not the recruiter. For anyone who came onsite, I let them know by phone, not by email. This was something I’d learned to do at my old consulting firm and wanted to bring with me to engineering interviewing. It’s not easy to give people bad news (though it gets easier with practice), but it treats people with respect, the way I’d want to be treated.

### Save synchronous time for interaction, and let people code in private.[](https://xdg.me/interviewing-engineers/#save-synchronous-time-for-interaction-and-let-people-code-in-private)

Two of my goals included making efficient use of time and reducing candidate stress. For those reasons, I decided to get rid of one-on-one “whiteboard” style interviews for testing a candidate’s coding skill.

Unless you or the candidate regularly work in a pair-programming environment, it’s pretty rare to do your day to day work with someone looking over your shoulder. If you think back to my point about assessing on promotion criteria, does anyone make promotion decisions by watching someone write their code? Of course not! What matters is what they produce, not how they do it.

Leaving aside how unrepresentative algorithmic-puzzle, white-board questions are in the first place, this style of interview doesn’t tell us much about how people would perform on the job anyway. What these traditional coding interviews really screen for is how someone performs in an extremely unnatural, high-stress environment.

And it’s worse than that!

A 2020 NCSU study, [“Does Stress Impact Technical Interview Performance?"](https://news.ncsu.edu/2020/07/tech-job-interviews-anxiety/), found that not only do such interviews measure stress, but they also introduce bias. In the study, candidates were split into groups. Half did their work in front of an interviewer. The other half worked on a whiteboard alone in a private room.

Those coding in private did much better on assessment criteria. Moreover, as the summary article explains, **“all of the women who took the public interview failed, while all of the women who took the private interview passed”**! One study isn’t conclusive, but it should be a real warning flag of the biases introduced by the status quo.

In addition to depressing observed performance and contributing to bias, one-on-one coding interviews take time that could be better spent. Watching someone code is time that you’re not having a conversation with them. If interviews should be focusing on level 3 criteria, it’s essential to reserve time for talking.

With these thoughts in mind, I handled coding assessment in two ways. First, during the initial screening, I asked candidates to do a short take-home exercise. For the onsite, I let candidates code in private, and then we discussed their work with several engineers in a group code review.

### Only give a take-home if they pass a non-technical phone screen.[](https://xdg.me/interviewing-engineers/#only-give-a-take-home-if-they-pass-a-non-technical-phone-screen)

As I said, as hiring manager, I would do the first phone screen after the recruiter screen. These are “non-technical” interviews, which only means they didn’t involve coding or systems design. There’s plenty of technical content in the conversation itself.

In these interviews, I focused mostly on level 3 factors (attitudes, behaviors) and try to pick up level 2 factors (specific skills, experiences) in passing. I usually ignored the resume except to give me some clues for things to probe about – jumping off points for conversation – and I tried to derail a candidate walking me through the resume point by point because that’s an utter waste of time in an interview.

Never be afraid to interrupt a candidate and redirect the conversation. You have very little time in an interview so don’t waste it on things that aren’t giving you signal. Be polite about it, but be in charge. “I’m sorry, I need to interrupt. Being mindful of time, I want to shift gears and talk about …”

Before the interview, I would prepare two or three questions to get at some of the level 3 factors I want to focus on. During the interview, I kept digging into specifics of a candidate’s answers to find out interesting things about other level 3 or level 2 issues. (“Tell me more…” or “What happened next…?” or “What did you already know about that when you started? What did you need to learn? How did you do that?") By going deep, I could see if the answer has substance or is shallow.

For example, if someone was telling me about a project, I might ask about the stakeholders or business goals, or about design tradeoffs they made, or ask for an explanation of some particular technical factor (“I’m not familiar with embedded software power profile testing; can you explain more about how that works?"). Or I might ask about who did what. **This is particularly important for someone who talks about projects using “we”.**

> Candidate: “We did X, then we did Y”.
> 
> Me: “That sounds like a lot of work. How many people were on the team? … What did each person work on? … What did you work on, specifically?”

If I was concerned about a particular skill or experience, I might pick on the resume that seems like it would give insight into what they know.

> “I’m really curious about Project X. I know every project has roadblocks and speed bumps – what were some memorable ones you encountered on Project X? … Tell me more… \[go deep into tech details\]. … What did you learn from that experience? … What’s another project where you were able to apply that insight? … How did it work out?”

The goal of this kind of interview was to decide whether I could imagine hiring them if further interviews go well. If I didn’t think I would or I wasn’t sure, I _wouldn’t_ tell them at the interview. Instead, I would take time after the interview as I was writing up the scorecard to reflect more deeply on what I heard and confirm my decision not to move forward. I think this is an important step to avoid making snap rejections in the moment when unconscious bias is more likely to be a factor.

If I did think I’d hire if other interviews went well, then at the end of the interview, I would invite them to do a take-home exercise. I was willing to make a snap judgement (and risk bias) in this case because I think the value of sustaining momentum in the conversation and inviting to the take-home live outweighs the downside. If I was too optimistic in my initial assessment, then we would catch it in the take-home or subsequent interviews. Moving someone forward is a [reversible decision](https://fs.blog/2018/04/reversible-irreversible-decisions/), but rejecting someone is not.

Reflecting on this now, this means that candidates that matched my biases would get the in-person explanation of the take-home and the ones that didn’t only got a written explanation. That reinforces bias. I’d do this differently next time to put everyone on the same footing.

In [part 2](https://xdg.me/interviewing-engineers-2/) of this article, I’ll share some tactical ideas for giving humane take-homes, writing good coding questions, organizing onsites, and coaching your interviewers.