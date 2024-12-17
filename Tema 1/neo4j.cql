MATCH (tom:Person {name:"Tom Hanks"})-[:ACTED_IN]->(m:Movie)<-[:ACTED_IN]-(coActors:Person),
    (coActors)-[:ACTED_IN]->(m2:Movie)<-[:ACTED_IN]-(cocoActors)
  WHERE NOT (tom)-[:ACTED_IN]->(:Movie)<-[:ACTED_IN]-(cocoActors) AND tom <> cocoActors
  RETURN cocoActors.name AS Recommended, count(*) AS Strength ORDER BY Strength DESC