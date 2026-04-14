CREATE VIEW IF NOT EXISTS accounts_by_industry AS
SELECT
    industry,
    COUNT(*) AS account_count
FROM accounts
GROUP BY industry
ORDER BY account_count DESC;