# Hours with Experts - Week 7: Visualizations

## Introduction

In this week we will be using the data that was inserted into the gold layer in Delta format and doing some visualizations on that data.

You should already have run the pipeline in week 6 and created an Athena table over that data using the 'Delta Lake' connector.

We will be using the open source package [Apache Superset](https://superset.apache.org/).  You will get instructions on how to login and the credentials in class.

## Assignment

1. Create an Apache Superset dataset over your gold layer data (prefix it with your userid, please).
* This can be against your raw table or using a SQL query.
2. Create at least three reports against your data.
* Total reviews by year bar chart.
* Pie chart which breaks down the total review by gender.
* Geography chart showing the average star reviews by state.
        (HINT: To get the states to show up you have to prefix them with 'US-')

If you have not completed week 6 and still want to use Superset, you can use the data in the 'demo' tables to do this assignment.
* demo_fact
* demo_customer
* demo_product
* demo_date

## Extra Credit

Create separate dimensions using Spark to create gold layer dimensions.

- Customer
- Product
- Purchase Date

Join these in Superset to create a custom dataset for your data.

You may have to redesign what you have done in week 6 to make this possible.
