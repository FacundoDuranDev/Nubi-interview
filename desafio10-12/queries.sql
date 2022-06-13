
with ventas as
 (
    select * from Sales.SalesTaxRate
),
 personas as (
    select * from Person.StateProvince
)
select  personas.CountryRegionCode as country_region_code , avg(ventas.TaxRate) as average_tax_rate from ventas, personas where ventas.StateProvinceID = personas.StateProvinceId group by CountryRegionCode


with impuestos_venta as (
    select * from Sales.SalesTaxRate
), provincia as (
select * from Person.StateProvince
), divisa_region as (
    select * from Person.CountryRegion
), ratio_divisa as (
    select * from Sales.CurrencyRate
), divisa as (
    select * from Sales.Currency
), divisa_pais as (
    select * from Sales.CountryRegionCurrency
)
select divisa_region.name as country_name, divisa.name as currency_name,cast(max(ratio_divisa.EndOfDayRate)as Decimal(5,2)) as currency_rate, avg(impuestos_venta.TaxRate) as average_tax_rate from
 impuestos_venta,provincia,divisa_region,ratio_divisa,divisa, divisa_pais 
 where impuestos_venta.StateProvinceID = provincia.StateProvinceId 
 and  provincia.CountryRegionCode = divisa_region.CountryRegionCode 
 and provincia.CountryRegionCode = divisa_pais.CountryRegionCode 
 and ratio_divisa.ToCurrencyCode = divisa_pais.CurrencyCode
 and divisa_pais.CurrencyCode = divisa.CurrencyCode group by divisa.name , divisa_region.name , divisa_region.name
gi