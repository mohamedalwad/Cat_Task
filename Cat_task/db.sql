SELECT 
    product_id, 
    product_name
FROM 
    product_table
WHERE 
    is_recyclable = TRUE
    AND is_low_fat = TRUE;
