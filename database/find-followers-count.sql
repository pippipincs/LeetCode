# Write your MySQL query statement below
SELECT user_id, Count(user_id) as followers_count
From Followers
Group By user_id
Order By user_id ASC