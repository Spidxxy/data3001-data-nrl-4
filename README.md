# **Analysing the Impact of Tackling Techniques on Play the Ball Speed in Rugby League**

## **Project Description**

The specific objective of this project is to determine how various tackling techniques and game contextual factors influence the speed of the 'Play the Ball' (PTB) in rugby league games. Play the Ball (PTB) speed refers to the time taken for a tackled player to place the ball on the ground and roll it backward with their foot to a teammate, allowing the attacking team to continue advancing the ball. The speed at which this occurs can significantly impact a team's performance and the flow of the game. By analysing data on different types of tackles, positions on the field, times within the game, and the current scores, we aim to predict the PTB speed following a tackle. This analysis will help us understand whether defensive strategies are adjusted to speed up or slow down the PTB based on the game’s current status, such as whether a team is leading or trailing, and during critical moments of the match. 

The speed of PTB in rugby league is a pivotal factor for strategic planning and real-time decision-making on the field. Our project seeks to predict PTB speed post-tackle, examining how different variables influence this critical aspect of the game. Insights from discussions with an ex-NRL coach highlighted the significant role of PTB speed in game outcomes, with strategies employed by teams like the 2005 West Tigers who illustrated how manipulating PTB can lead to victories.

In addition to examining tackling techniques, the introduction of new NRL rules has a notable impact on PTB speed and is therefore included in our analysis. We account for these changes using a variable called **RuleChange**:

* **The 6 Again Rule** (introduced in Round 9, 2020\) gives the attacking team another six tackles for ruck infringements (e.g., holding down the player too long), without stopping the play for a penalty. This rule has led to faster PTBs and increased ball momentum, making defensive strategies around PTB speed crucial.  
* **The Kick Restarts Rule** (introduced in 2022\) changed how the game restarts after the ball is kicked dead (e.g., a dropout instead of a scrum). This rule affects game flow and the overall PTB dynamics as it alters possession duration and field positioning, impacting how teams manage tackles and control PTB speed.

The RuleChange variable in our dataset accounts for these adjustments:

* **0**: Matches played before the rule changes (before Round 9, 2020).  
* **1**: Matches played after the **6 Again Rule** was introduced (Round 9, 2020 \- end of 2021).  
* **2**: Matches played from 2022 onwards, after both the **6 Again Rule** and **Kick Restarts Rule** were implemented.

This analysis will enable coaches to refine their team’s tactics and training regimens, focusing on specific tackling techniques that strategically accelerate or decelerate PTB under various game conditions. By integrating data science with practical sports strategy, our project not only enhances the analytical tools available to teams but also provides actionable insights that can transform competitive play.

**NRL Rules:**

The National Rugby League (NRL) is a professional rugby league competition played by two teams of 13 players on a rectangular field. The objective of the game is to score more points than the opposing team by grounding the ball in the opponent’s in-goal area (a try) or by kicking the ball through the opponent’s goalposts.  
Key rules to understand:

1. Scoring:  
   * Try: Worth 4 points, awarded when a player grounds the ball in the opponent’s in-goal area.  
   * Conversion Kick: After a try, the team attempts a kick for an extra 2 points.  
   * Penalty Goal: A team can take a penalty kick for 2 points.  
   * Field Goal: Worth 1 point, scored by kicking the ball between the posts during open play.  
2. Tackles and Possession:  
   * Each team has six tackles (or plays) to advance the ball down the field. After six tackles, possession is handed over to the other team.  
   * A tackle occurs when the defending team brings down a player holding the ball. After the tackle, the player must perform a Play the Ball (PTB), where they place the ball on the ground and roll it backward with their foot to a teammate.  
3. Play the Ball (PTB):  
   * The speed of the PTB is crucial as it affects how quickly the attacking team can continue their play. Defensive teams aim to slow down the PTB by holding down the tackled player (within the rules), while attacking teams aim for a fast PTB to maintain momentum.  
4. Possession Changes:  
   * If the attacking team fails to score or make significant progress after six tackles, they lose possession, and the defending team gains control of the ball.  
   * Possession can also change due to errors (like a forward pass or knock-on) or penalties.

### **Field Layout and Zone Explanation**

In the data, the rugby league field is divided into 84 zones, with each zone representing a 10m x 10m section of the playing area. The field is further categorised into 7 horizontal sections running from left to right, labelled as SL (Sideline Left), NL (Numbers Left), L (Left), C (Center), R (Right), NR (Numbers Right), and SR (Sideline Right). These sections help us analyse and understand where specific plays, tackles, or movements occur on the field. The zones are numbered to reflect both the horizontal section and the vertical progression down the field, as shown in the visual.

**Real-Life Example:**  
If a player receives the ball in Zone 14 within the Sideline Right (SR) section near their own try-line, they are positioned near the right edge of the field. If that player breaks through the defence and runs straight down the sideline, advancing through zones like 21 (SR), 28 (SR), and continues running all the way to Zone 84 (SR) in the opponent’s try-line, the player has covered the full length of the field along the right sideline to score a try. 

**Previous Work**  
Previous analyses of play-the-ball (PTB) speed in the NRL have consistently shown a trend of increasing speed over recent years. For example, data from 2024 shows that PTB speeds have improved by one-tenth of a second compared to 2023, and 2023 was faster than 2022 by six-hundredths of a second. These trends indicate that the game is becoming faster over time.

However, multiple studies have concluded that there is no direct correlation between faster PTB speed and outcomes, such as winning games or increasing the margin of victory (the difference in points between the two teams). A recent analysis revealed an R-squared value of 0.002, confirming the lack of significant correlation between average PTB speed and match margins.

Research has found no relationship between PTB speed and a team’s position on the NRL ladder. Additionally, there is no correlation between PTB speeds and referees or PTB speeds and players (individual PTB speed) to impact match results or margin.  
Factors that do influence PTB speed include:

* Scoreboard: Teams tend to play faster when the score is tied to gain an advantage, on the contrary, teams will slow down the game when leading or trailing to manage the clock.  
* Position from tryline: PTB speeds tend to be slower when teams are near their own try line as the defending team wants to slow the game down to regroup. PTB speeds are slightly faster near the opposition’s try line to create scoring opportunities and catch the defending team off guard.  
* Time in the game: PTB speeds increase towards the end of each half, especially in close games where there is an increase in intensity to try to make the game winning play. 

Reference: LeagueEyeTest (2024). If play the ball speed means something but mostly nothing, what is a better metric? \- The Rugby League Eye Test. \[online\] The Rugby League Eye Test. Available at: https://www.rugbyleagueeyetest.com/2024/08/19/if-play-the-ball-speed-means-something-but-mostly-nothing-what-is-a-better-metric / \[Accessed 15 Sep. 2024\]

## **Sources**

The data used in this project consists of multiple datasets from NRL match events from 2020–2023. The key data sources include:

1. **Event Data**:  
   This dataset captures detailed information from NRL matches focusing on specific in-game actions like tackles and play-the-ball (PTB) events. Each row represents a unique event each with key features to better understand the game, these features include:  
   * **MatchId**: A unique identifier for each match, useful to track events of matches.  
   * **EventName**: The specific type of event (e.g. Tackle, PTB). This is a highly important feature because by filtering this field we can isolate the relevant tackle-PTB events for further processing.  
   * **X-Y Coordinates**: The exact location on the field where the event took place, with **XmPhysical** representing the horizontal position and **YmPhysical** representing the vertical position on the field. Each unit is equivalent to a metre and the field is modelled as 100 m long (X) and 70 m wide (Y), with the origin at the top left (0,0). Here is a diagram to better understand the layout:

     

     

     

     

     

   The defending team is always on the right and the attacking team is on the left, when the ball is handed over teams switch sides and coordinates change (e.g. if the attacking team completed their set at (80,35) the previous defending team now begins their attack at (20,35). As a result, the previous attacking team is now on the right and the previous defending team currently attacking is now on the left. This will be useful when analysing how distance from the tryline impacts PTB speed.

   * **GameMins** and **GameSecs**: Finds the time (GameMins in minutes and GameSecs in seconds) of an event from the game clock in the current half.   
   * **ElapsedMins** and **ElapsedSecs**: Finds the elapsed time of an event starting from kickoff (ElapsedMins in minutes and ElapsedSecs in seconds).  
   * **Qualifier 1 (Tackle type):** This feature describes the type of tackle.   
   * **Qualifier 2 (Tackler outcome):** This feature captures the outcome of the tackle.  
   * **Qualifier 3 (Tackle arrival order):** The order in which the tackler arrives to make the tackle during the play.  
   * **Score and OppScore**: These variables track the current score for both teams at the time of the event, which is useful for calculating the score margin (the difference between the winning team score and losing team score) and better understand how the scoreboard influences PTB speed.  
   * **RuleChange:** Derived from **SeasonId and RoundId** this feature was created to account for rule changes in NRL, the values for this feature include:  
     * **0:** Refers to matches played before the rule change (before round 9 2020\)  
     * **1:** Refers to matches where the first rule change (six-again) was implemented (round 9 2020 \- end of 2021\)  
     * **2:** Refers to matches played from 2022 and onwards with new rule change (kick restarts)   
   * **Set:** The set number of tackles within a set. Each team has 6 chances to score and after completing a set which is six tackles without an error on any of the plays, the attacking team hands the ball over to the opposing team and now the opposing team has 6 chances or tackles to score.   
2. **Match Data:** No match data variables were used for the final data product but variables in both event and match data variables were used for newly created features.  
   * **SeasonId and RoundId**: Used to track matches across different seasons and was especially useful for differentiating periods before and after rule changes.  
3. **Player Data (in event data):** Player-specific data such as player IDs, player positions and individual statistics were excluded from our analysis. Our focus was on understanding broader trends in PTB speed and the influence of game context rather than individual player performance. 

We will filter the Event Data to focus on the tackle-PTB pairs as these events are the most relevant for our analysis. Non-related events will be excluded from the dataset with the final dataset ready for the modelling team to use in their analysis of PTB speed and its in-game impact.

**Step 1: Filter Rows**  
*Filter rows to keep only the relevant information towards the objective with the aim to refine the dataset, make it more digestible and less complex.*

Using the *EventName* variable, we have filtered for PTB and Tackle events only. PTB and tackles are central to answering the objective, all other events only increase noise in the data. 

We have then further refined the data by filtering out events that are irrelevant to the objective. This includes the opponent information (‘opp’ variables) which are simply a duplicate of the event with the opponent team’s statistics and the information of the tackled players which has no effect on PTB. We have also filtered out certain tackles which do not lead to a PTB, these include:

* Ref Tackle \- unintentional tackle between a player and a referee.  
* Offloaded tackles \- player manages to pass the ball to a teammate after contact but before tackle is completed, so the ball remains in play.  
* Missed tackles \- when a defender attempts to make a tackle but fails to stop the attacking player.  
* Passive tackles (try conceded) \- a defensive failure where passive tackling leads to a try being scored by the opposition, hence no PTB follows.  
* Try save tackles \- critical tackle made by a defender that prevents an almost certain try being scored by the attacking team and does not lead to PTB. 

**Step 2: Adding additional features**   
*2.1 Create unified time columns.*  
Convert and unify the time columns (*ElapsedTime* and *GameTime*) into a single time format \- mm:ss. This improves readability and reduces the number of variables in the data. It also ensures that times are consistently formatted in the dataset. 

*2.2 RuleChange feature*  
Introduce a *RuleChange* column that accounts for the major rule changes that occurred in 2020 and 2022\. This new column is based on conditional logic around the *Year* and *Round* number, producing three identifying numbers:

* 0 \- before rule changes  
* 1 \- ‘6-again’ rule   
* 2 \- ‘kick restart’ rule 

\*Refer to the ‘*Project Description’* for further information about rule changes. 

As pointed out by the industry experts, the NRL rule changes have not only impacted gameplay but also the speed of the game. Hence, this new feature will help track the changes in PTB pre and post rule change, allowing for a more nuanced analysis.

**Step 3: Remove irrelevant variables**  
Many variables in the dataset do not directly affect the core analysis of PTB and tackles. Removing these variables not only decreases the dimensionality of the dataset but also prevents overfitting when creating the model.

The variables removed could be grouped as: 

* **Player, club and match official information**: we do not require the statistics of individuals as our analysis is focused on league-wide trends.  
* **Possession-related information**: statistics relating to possessions are not the focus of our analysis and will likely add noise.  
* **Detailed timing** e.g. milliseconds  
* **Event qualifiers**: each event is followed by 8 qualifiers, only three of which we have determined to be relevant to the objective.

\* For a full, detailed list of variables excluded please refer to the final code.

**Step 4: Match PTB and Tackle Matches**  
*Append the tackles and their relevant characteristics to their respective PTB. Add an additional column to account for the total number of tackles for each PTB.* 

Merging the tackles and their relevant characteristics together makes it easier for a ML model to pick up the relationship tackles may have to the PTB speed.

In order to append the tackles to their respective PTB events we first separated the two rows from each other using *EventName*. We then group together these rows based on the contextual variables *MatchId, Set* and *Tackle*. Putting these three variables together gives us all the unique PTBs and allows us to match the tackles that precede them. 

Each unique tackle has three relevant qualifiers: Tackle Type, Tackle Outcome and Tackle Arrival (refer to *‘Data Description’* for more details about these qualifiers) which we will append as columns at the end of each PTB row. All tackles are appended in sequential order and hence the additional columns are of the format:

* Tackle{i}\_TackleType  
* Tackle{i}\_TackleOutcome  
* Tackle{i}\_TackleArrival 

where *i* is the order number of the tackles. 

Additionally, we also create an extra feature column ‘*Number of Tackles*’ which gives the total tackles that preceded the PTB. 

**Data Description** 

The data product created in this project will leverage the historic NRL data provided in the most efficient way possible. Each **row** in the dataset will feature a tackle-PTB event pair. This will capture the critical moment related to PTB speed which is the tackle followed by the actual play-the-ball. 

The **features (columns)** will include crucial in-game variables of the event pair including where on the field the event took place, time of event, duration etc. External features will be considered on a case-by-case basis based on whether or not they contribute significantly to the PTB speed (see Workflow section). Finally, an additional variable will be added based on the year of event which accounts for the NRL rule change that was implemented in 2020\. 

**Game Information**

| Score | Score of the team currently in possession |
| :---- | :---- |
| OppScore | Opponents current score |
| Half | Game half, 1 or 2 for first and second half of regular play. 3 and 4 are halves of extra time for a tied game.  |
| MatchID | Unique numerical identifier for each Match |
| RoundID | The round in the season the game is being played |
| Set | Set number within the match |
| Tackle | Tackle number within the set |
| RuleChange | Introduced qualifier for major rule changes.  0: Refers to matches played before the rule change (before round 9 2020\) 1: Refers to matches where the first rule change (six-again) was implemented (round 9 2020 \- end of 2021\) 2: Refers to matches played from 2022 and onwards with new rule change (kick restarts)  |
| Tackle{1-10}\_TackleType | This feature describes the type of tackle. Defence line: The type of tackle made is by a player positioned on the primary line of defence and is an attempt to bring the ball carrier down before they can advance further up the field.  Marker: Involves a player close to the PTB area after an initial tackle has been made. Markers try to disrupt the attacking team's play by pressuring the ball carrier or being part of a secondary tackle after first contact.  Try saver: A tackle made which had it not, would have lead to a try.  Tackle cover: A tackle which acts as backup to an already made tackle. Usually made while in the defence line by the players adjacent to the play. |
| Tackle{1-10}\_TackleOutcome | This feature captures the outcome of the tackle these include: Made: A successful tackle where the defender brings down the ball carrier. Dominant: A tackle where the defender controls the ball carrier effectively, slowing down the attacking team's push and giving the defensive line time to reset. Turnover ball split: A tackle where the ball carrier loses possession, resulting in a turnover due to a loose carry or pressure from the tackle. Ball jolted: A tackle that causes the ball to be dislodged from the ball carrier's grasp, often leading to a knock-on or turnover. Stolen: A tackle where the defender legally strips the ball from the ball carrier, resulting in possession being gained by the defensive team. Forced/out: A tackle where the defender forces the ball carrier into touch (out of bounds), resulting in a turnover or a stoppage in play. |
| Tackle{1-10}\_TackleArrival | The arrival order, the initial tackler will be 1, next player to tackle will be 2, so on |
| Number of tackles | Number of unique tackles involved in the play right before the PTB |

**Positional Information**

| ChannelPhysical | Channel in which the event occurs, the order of the channels from left to right is as follows: SL, NL, L, C, R, NR, SR |
| :---- | :---- |
| ChannelPlayer | Channel in which the player is, the order of the channels from left to right is as follows: SL, NL, L, C, R, NR, SR |
| SectionPhysical | Coordinate of the event, ranges from \-10 to \-100, see diagrams for detail on the meaning of the values. |
| SectionPlayer | Coordinate of the player, ranges from \-10 to \-100, see diagrams for detail on the meaning of the values. |
| XmPhysical | Accurate X coordinate for the event, Range 0, 100\. To one decimal place. |
| YmPhysical | Accurate Y coordinate for the event, Range 0, 70\. To one decimal place. |
| XmPlayer | Accurate X coordinate for the player, Range 0, 100\. To one decimal place. |
| YmPlayer | Accurate X coordinate for the player, Range 0, 70\. To one decimal place. |
| ZonePhysical | Zone of the event, see diagram for information on zone positioning. Range 1-84 |
| ZonePlayer | Zone of the player, see diagram for information on zone positioning. Range 1-84 |

**Time Information**

| DurationSecs | Duration of the current event in seconds |
| :---- | :---- |
| MatchMinute | Minute on the clock,  |
| SeqNumber | A sequence number to ensure events within the same game are in time-based order |
| GameTime | Time on the in game clock, to the second.  |
| ElapsedTime | Time elapsed during the game, includes stoppages so expected to be larger than GameTime |

**Event Information**

| EventCode | Unique 4 letter code for each event:PBFSPBHSPBISPBNSPBSS |
| :---- | :---- |
| EventName | Description of event |
| Qualifier1 | Event Result {Won, Lost} |
| Qualifier1Name | Qualifier 1 name Event Result |
| Qualifier2 | PTB Contest {Lost, Stays on feet, Tackled to Ground} |
| Qualifier2Name | Qualifier 2 name Contest |
| Qualifier3 | Set type {Good Ball, Yardage} |
| Qualifier3Name | Qualifier 3 name Set type |

## **Project Status** 

We have completed our background research, asked experts in the field for what they find important in PTB speed, and explored the given datasets using Python to gain insights into their structure/ relationships. Our current work is on joining the event data for tackles, PTB speed, and other peripheral contextual information. 

After we complete this data filtering and joining, we will be working on cleaning the data. Removing anything that has inconsistencies, or large missing data points which could negatively affect accuracy of models using this data product. Then we will move onto the steps outlined in the *Workflow* to create the final data product.

**Usage** 

We plan for our product to be used for finding which factors affect PTB speed more in certain scenarios, likely scenarios that coaches would specifically ask about. A few ways this could be handled are using **K-Means Clustering** to get an intuition into how similar tackles occur, and the key differences that affect PTB speed between otherwise “similar” tackles. Or an ML model (e.g. Random Forest Regression) to get a decision tree which optimises for prediction accuracy, and comfortably handles non-linear relationships like the ones we expect to see in  this real world data with a high number of variables. To ensure readability and accuracy of models, it might be advisable to standardise the data before further analysis.

**Addressing peer review:**

By reviewing the feedback from the peer review we have made the following modifications to the README file:

1. Detail in data features:   
   * The peer review pointed out the lack of detail regarding features such how the X and Y coordinates work making it harder to work with and understand the dataset.  
   * The team addressed this issue by providing a more clear and comprehensive explanation in the data sources section. Additional detail on features such as the coordinates, time and tackle characteristics in the sources section from the NRL data have been addressed and explained in detail.   
2. Explanation of NRL rules and concepts:  
   * The peer review highlighted that our initial description of the project required a certain level of knowledge about NRL rules such as PTB speed and didn’t explain in detail what the concept was.   
   * To address this we added a definition of PTB in the project description as well as a description of the rules and any rule changes the NRL has implemented over the years for readers with no prior knowledge of the sport.   
3. Clarification of key variables in previous work:  
   * The feedback praised the analysis of previous work on PTB but suggested that a brief explanation of why certain variables were not relevant would be helpful.   
   * To address this we expanded on factors that influence PTB like scoreboard, position from tryline and time in the game, providing context for its relevance and included graphs to support these claims.

## **Support information:** Contact David on teams or via email [david.warton@unsw.edu.au](mailto:david.warton@unsw.edu.au).

## **Contributors:** Aiden Poswell, Ivy Williams-Kelly, Nabiha Imran Rajput, Tuvya Jugnarain 

If you would like to get involved with this project please contact David above\! 

