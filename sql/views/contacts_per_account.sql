CREATE VIEW IF NOT EXISTS contacts_per_account AS
SELECT
    a.company_name,
    COUNT(c.contact_id) AS contact_count
FROM accounts a
LEFT JOIN contacts c
ON a.company_name = c.company_name
GROUP BY a.company_name
ORDER BY contact_count DESC;