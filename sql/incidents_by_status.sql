SELECT
    incident_state,
    COUNT(*) AS incident_count
FROM incident_events
GROUP BY incident_state
ORDER BY incident_count DESC;
