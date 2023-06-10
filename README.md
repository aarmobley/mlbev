## Diving into MLB exit velocity stats from 2015-2022
<div id="header" align="center">
  <img src="https://sportslogosvg.com/wp-content/uploads/2020/09/mlb.png" width="600"/>
</div>


# Summary

<ul style="list-style-type:disc;">
  <li>Looked at 1,794 players from 2015-2017 to find out what stat is most important in determing max distance <br>
and average exit velocity. <br></li>
  <li>What could MLB scouts use to predict how far a player can hit a baseball and ultimatley project how many home runs <br>
they could hit? <br></li>
  <li>Started with comparing the Top 10 in average exit velocity for each year 2015-2022 </li>
  <li>Did the top 10 players average Exit Velocity increase from 2015 to 2022?
</ul>  

<a href = "https://public.tableau.com/app/profile/aaron.mobley/viz/AverageEXVeloMLBDash/Dashboard2" > Tableau <a/> <br>

<a href = "https://www.kaggle.com/datasets/mattop/mlb-batting-exit-velocity-data-2015-2022" > MLBDataset </a> <br>

# Code and Resources

<b>Python<b>: Pandas and numpy <br>
<b>R<b>: dplyr  <br>
<b>Tableau<b>  


# Data Exploration 🔭
  
  1. This dataset had a few NaN that needed to be corrected. <br>
  2. I built a correlation matrix to view the correlation between continous variables. <br>
  <div id="header" align="center">
  
  <img src="https://github.com/aarmobley/mlbev/blob/main/MLBcorr.png" width="850"/>
</div>
  
  

  <ul style="list-style-type:disc;">
    <li>Hard Hit Percentage and Average EV as well as Fly Ball/Line Drive and Average EV had some of <br>
      the highest correlation
      
 # Statistical Modeling      
      1. Stepwsie Regression Model in R - Hybrid 
          *A combination, testing at each step for variables to be included or excluded 
      2. Final model concluded that batted ball events, launch angle, max exit velocity, 
          hard hit percentage and average exit velocity are the top 5 major influencers in max distance
      

