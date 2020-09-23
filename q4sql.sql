DELETE FROM orig_table 
WHERE EXISTS (
  SELECT 1
FROM orig_table c
WHERE c.user_name = orig_table.user_name AND c.site = orig_table.site AND c.customer = orig_table.customer AND c.supplier = orig_table.supplier AND c.rowid < orig_table.rowid
);

SELECT *
FROM orig_table;
-- (last 2 lines return updated table)

-- this works by deleting all rows from the table for which there exists a duplicate row with a smaller row id
-- I've made it to be at least compatible with sqlite3

-- N.B I've chosen field name 'user_name' instead of 'user' simply to bypass linting errors