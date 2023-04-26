#load packages
head(mlbexitvelo)

#stepwise regression to find the most important variables for max_distance

#get a baseline

mlb1 <- select(mlbexitvelo, -id, -rank, -year, -player)


FitAll = lm(max_distance ~ ., data = mlb1)

summary(FitAll)

step(FitAll, direction="both", scope=formula(FitAll))

#interpreting Final model
Final <- lm(formula = max_distance ~ batted_ball_events + launch_angle + 
     sweet_spot_percentage + max_ev + average_ev + fly_ball_line_drive_ev + 
     ground_ball_ev + average_distance + average_homerun + hard_hit_percentage + 
     hard_hit_swing_percentage + barrels_plate_appearance_percentage, 
   data = mlb1)

summary(Final)

#batted_ball_events, launch_angle, max_ev, average_ev, fly_ball_line_drive_ev
#average_distance, average_homerun, hard_hit_percentage, hard_hit_swing_percentage
#are strongest predictors in predicting max_distance

