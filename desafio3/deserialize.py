from pyspark.sql import SparkSession
from datetime import date
import os
spark = SparkSession.builder.appName('pract').getOrCreate()
df_pyspark = spark.read.json('Sellers.json')
df = df_pyspark.selectExpr(
    'body.site_id AS SiteId',
    'body.id as SellerId',
    'body.nickname as SellerNickname',
    'body.points as SellerPoints')
site_ids = df.filter(df.SellerPoints < 0).select("SiteId").distinct().collect()
full_date = date.today().strftime("%Y%m%d")
year = full_date[0:4]
month = full_date[4:6]
day = full_date[6:]
for site_id in site_ids:
    directorio = os.getcwd() + "/"+ site_id[0]+"/"+year +"/"+ month + "/"+ day
    df.filter((df.SellerPoints == 0) & (df.SiteId  == site_id[0])).write.option('header', True).format('csv').mode('overwrite').save(directorio + "/Cero")
    df.filter((df.SellerPoints > 0)& (df.SiteId == site_id[0])).write.option('header', True).format('csv').mode('overwrite').save(directorio + "/Positivo")
    df.filter((df.SellerPoints < 0) & (df.SiteId == site_id[0])).write.option('header', True).format('csv').mode('overwrite').save(directorio + "/Negativo")
