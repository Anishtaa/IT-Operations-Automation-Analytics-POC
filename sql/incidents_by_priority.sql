SELECT
    priority,
    COUNT(*) AS incident_count
FROM incident_events
GROUP BY priority
ORDER BY incident_count DESC;
