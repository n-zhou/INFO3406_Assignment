SELECT title, gross,
AVG(valence), AVG(arousal), AVG(dominance)
from movies
INNER JOIN (select * from vad where word NOT LIKE '% %') as vad_clean
on to_tsvector(title) @@ to_tsquery(word)
GROUP BY title;

SELECT movies.movieid, AVG(rating), title, STRING_AGG(word, ', '),
AVG(positive), AVG(negative), AVG(anger), AVG(anticipation), AVG(disgust), AVG(fear), AVG(joy), AVG(sadness), AVG(surprise), AVG(trust)
from ratings INNER JOIN movies
on movies.movieid = ratings.movieid
INNER JOIN nrc_emotion
on to_tsvector(title) @@ to_tsquery(word)
GROUP BY movies.movieid
ORDER BY movieid ASC;
