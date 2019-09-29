
BEGIN BATCH
 update name_product
set name_product.product = name_product.provider
from product prod
    inner join provider prov on
        prod.name_product = prov.name_product
APPLY BATCH





