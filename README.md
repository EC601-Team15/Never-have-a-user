# Club Helper
Hi, our names are Shuwei Li and Yumeng pan. This project is actually an assignment of EC601 of Boston University. 

## Product Mission
Our product will be used to analyze the sentiment content of the target users, in order to obtain the feedback of customers and improve the service of providers. Our current idea is to analyze the Tweets of fans of a specific football club, in order to help the club review their decisions, strategies, and service.

### Target Users
Our target users are football clubs. If possible, our target users can extend to other types of service providers, such as basketball club, restaurants, etc. However, we will only focus on football clubs right now. We will use Juventus, an Italian football club, as an example. This club has made a few aggressive strategies recently, which is very controversial.

### User Story
In the era of social media, the amount of fans of a football club can make a difference. The tickets sales and media rights, sponsorship and advertising, the sales of products and licenses are defined greatly by the number of fans. In order to create more revenue, as a manager of Juventus, a modern football club, I need to keep the current fans and make attempts to attract more. As a result, I must analyze fans’ reactions towards the service the club provides and the decision we make. The club can be beneficial from analyzing several aspects of the club:

First, the effects of transfer windows.  We signed a series of famous players last summer, including Cristiano Ronaldo, which costs a huge amount of money. Is it worth? How many fans will follow the players to the new club? How do the current fans react to the arrival of new players? Besides the positive effect, I should also be aware of the effects of the departures of some players. Fans could have negative emotions towards these events and thus unfollow the club.

Second, the experience of the service provided by the stadium.  As an international club, many fans take a long trip and spend a lot of money to watch a game. Are they served with respect? Are they satisfied with the experience they have? It can decide if they will come again or recommend it to others. This feedbacks can also be found on Twitter. I need to obtain the ratio of the negative comments and conclude the aspects need to be improved.

Third, fans’ satisfaction with matches. After a loss, how do they react on the Internet? Do they like the performance of the team or a specific player? Besides, Juventus decided to change the schedule of match time from evening to afternoon, in order to attract more Asian fans. Does the decision attract more Asian fans? However, local fans’ reactions are also important. Do they feel being ignored? I have to know public opinions to review our decisions. 

### Minimum Valuable Product 
There are only three core modules in this product, which are tweets obtaining module, sentiment analyzer module and visualization module. With them, our target users can obtain their fans' feedback on their service and decisions, and try to analyze them with diagrams. 

## System Design
The architecture of our project is uploaded as a file. 

Our users need to give our product a hashtag, such as "#AtleticoJuventus", which is used when fans discuss the match Juventus Vs. Atletico Madrid. Then, the hashtag will be processed by the tweepy module, using tweepy to obtain any tweets contain this tag. After that, these tweets will be sent to the Google Natural Language API to analyze the sentiment scores. In the end, the scores will be processed by the visualized module in order to display results.

## Test Result
![Image of Shuweili](https://github.com/EC601-Team15/Never-have-a-user/blob/master/Figure_1.png?raw=true)
![Image of Shuweili](https://github.com/EC601-Team15/Never-have-a-user/blob/master/result_example.png?raw=true)


## Lessons Learned
###What you liked doing?
Shuwei Li:
I feel like finding users' requirements, and design system architecture. 

###What you could have done better?
Shuwei Li:
I think, in order to analyze the fans comments of a match, we should identify who is the fans of our team. Because when we lose a match, our fans may give negative comments while rivals' fans give posstive comments. However, it is very difficult to identify which shirt is a user in. 

###What you will avoid in the future?
Shuwei Li:
I will avoid using wrong data structure and compile every time I finish a module.
