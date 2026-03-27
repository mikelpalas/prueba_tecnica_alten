MERGE `prueba-tecnica-alten.INTEGRATION.integration_prueba_tecnica` T
USING (
  SELECT 
    id, 
    title, 
    body, 
    userId,
    CURRENT_TIMESTAMP() as processing_date
  FROM `prueba-tecnica-alten.SANDBOX_prueba_tecnica.upload_prueba_tecnica`
) S
ON T.id = S.id
WHEN MATCHED THEN
  UPDATE SET T.title = S.title, T.processing_date = S.processing_date
WHEN NOT MATCHED THEN
  INSERT (id, title, body, userId, processing_date)
  VALUES (S.id, S.title, S.body, S.userId, S.processing_date);