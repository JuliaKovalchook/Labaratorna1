pip install cassandra-driver
from cassandra.cluster import Cluster

cluster = Cluster()

from cassandra.cluster import Cluster

cluster = Cluster(['192.168.0.1', '192.168.0.2'])
from cassandra.cluster import Cluster
from cassandra.policies import DCAwareRoundRobinPolicy

cluster = Cluster(
    ['10.1.1.3', '10.1.1.4', '10.1.1.5'],
    load_balancing_policy=DCAwareRoundRobinPolicy(local_dc='US_EAST'),
    port=9042)
cluster = Cluster()
session = cluster.connect()

CONSISTENCY [LOCAL_ONE]
session.set_keyspace('user')
rows = session.execute('
SELECT * FROM user WHERE age >=20 AND age <=60; 
')
for user_row in rows:
    print user_row.user_id, user_row.age, user_row.country
INSERT INTO user (user_id, age, credits)
VALUES (123, 22, "USA")
CONSISTENCY [ one ]
session.set_keyspace('adv')
rows2 = session.execute('
select t.range, count(*) as num
from
   (select case
       when price_product < 50 then '0 - 50'
       when price_product >= 50 and price_product < 500 then '50 - 500'
       when price_product >= 500  then 'more 500'
       end
       as range,
       price_product
       from product)
	   as t
group by range
')
INSERT INTO product (name_adv, name_product)
VALUES (123, 22, "USA")
CONSISTENCY [ TWO ]
session.set_keyspace('product')
rows3 = session.execute('
SELECT DISTINCT name_product, id_product, name_provider, name_adv, price_product, count_product, factory 
FROM product, provider 
WHERE name_product_p.product = name_product.provider, name_provider.product=name_provider_p.provider;

')
INSERT INTO provider (name_product, id_product, name_provider, name_adv, price_product, count_product, factory )
VALUES ('laundry soap', 221, 'PandG', 'laundry soap adv', 99, 23, ['Kyiv factory', 'Kharkiv factory' ])
CONSISTENCY [ THREE ]

session.set_keyspace('provider')
rows4 = session.execute('
select name_product, name_provider, name_adv, price_product, sum(id_product) as id_product from product group by name_product, name_provider, name_adv, price_product;
')
INSERT INTO provider  (name_provider, factory, name_product_p)
values ('PandG', ['Kyiv factory', 'Kharkiv factory' ], 'laundry soap');



CONSISTENCY QUORUM;


// CONSISTENCY;
