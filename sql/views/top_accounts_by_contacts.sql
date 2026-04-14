CREATE VIEW IF NOT EXISTS top_accounts_by_contacts AS
SELECT
    a.company_name,
    COUNT(c.contact_id) AS contact_count
FROM accounts a
JOIN contacts c
ON a.company_name = c.company_name
GROUP BY a.company_name
HAVING contact_count > 0
ORDER BY contact_count DESC
LIMIT 10;