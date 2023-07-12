-- list all band with glam rock as their style
-- rank by their longevity
-- if split year is null swap it for current year(2022)
SELECT band_name,
COALESCE(split, 2022) - formed AS lifespan
FROM metal_bands 
WHERE STYLE LIKE '%Glam rock%' 
ORDER BY lifespan DESC;
