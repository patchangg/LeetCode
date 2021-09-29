
SELECT Score,
DENSE_RANK() OVER (ORDER BY Score Desc) as "Rank"
FROM Scores;

/* Dense rank gives rankings based on the column with the same integers having
equal rank */
