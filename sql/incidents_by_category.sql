SELECT
    category,
    COUNT(*) AS incident_count
FROM incident_events
GROUP BY category
ORDER BY incident_count DESC;
