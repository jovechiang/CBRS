##Description
A prototype of content-based recommendation system written in Python.  You can think it as an article recommendation based on what you liked or rated.

Today, most recommendation are based on collabaorative filter, which has a assumption : the thing most people like will also attract you. For this assumption, I'd say this is correct and wrong. 

Basically, people receive information for 2 reasons, 1.for fun. 2. for being informed.  Looking at current major social network:Facebook and Twitter. Facebook has a big problem ,privacy protection, which will prevent information propagation. Twitter has a good information propagation but the content is so shadow with limited text.Well, you can say with a hyperlink it can carry much more info.But still the way people receive those information is to subscribe certain info source. Technical speaking, it needs user first clearly define what they want to receive. But new topic comes up every day. Most of time, users don't realize this content is interested until they first view it. Now, content-based recommendar system is based "Category",like Tech,News, Life Style. But it is to ambiguous.

In my vision, there shoube be an automatically prediction and delivery mechanism. I found content-based recommendar system is an early stage of this mechanism. 

##Plan
Stage 1: focus on learning algorithm and feature vector construction of items

Stage 2: modelling user activity and profile learner

Stage 3: UI integration and get user feedback through click chain

Stage 4: scale out for more content.

##Data
In stage 1&2, I will just use research data from MIT. [20Newsgroup](http://qwone.com/~jason/20Newsgroups/). It contains 18846 articles

In stage 3,4, I will construct a pipe line to ingest data from web crawler.

##related posts in my blog
[Introduction](http://junjiang.me/recommender_system/2013/05/18/RS/)

[Item representation](http://junjiang.me/recommender_system/2013/06/30/RS2/)

[Profile Learner](http://junjiang.me/recommender_system/machine_learning/2013/07/10/RD4/)

##High-Level Architecture
<img src="/data/High-Level.png" alt="Architecture" title="Architecture" width="100%" />


##Reference
Recommendar System Handbook



