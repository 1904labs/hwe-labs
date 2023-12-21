from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.types import StructType, StructField, StringType
import pandas as pd

# Welcome to the stretch challenge. The code below has two sections:
#
#   1) The method under test - you will fill out the method body
#       implementing the behavior called out in the doc string.
#
#   2) The tests verifying the method operates per the documentation - 
#       you simply execute these and keep iterating on the method under
#       test until all of these pass.


################# method under test

def get_most_frequent_product_categories(df: DataFrame) -> DataFrame:
    '''
    Gets the most frequently occurring values from the String 'product_category'
     column passed into the DataFrame.
    
    Raises:
        ValueError: The DataFrame does not contain a 'product_category' column.
         
    Parameters:
        df (DataFrame): The DataFrame that contains the 'product_category' column.

    Returns:
        A DataFrame with one column named 'product_category' containing only the 
        most frequent 'product_category' values.  If no rows are included in the
        input DataFrame, zero rows are returned in the output DataFrame.   
    '''
    # TODO: fill in with actual implementation    
    return None


################# tests

def get_most_frequent_product_categories__one_most_frequent__most_frequent_returned():
    ### ARRANGE
    sample_data = [{"color": "yellow", "product_category": "movies", "title": "Mary Poppins"},
            {"color": "blue", "product_category": "board games", "title": "Monopoly"},
            {"color": "green", "product_category": "video games", "title": "Halo"},
            {"color": "red", "product_category": "board games", "title": "Risk"}]
    df = spark.createDataFrame(sample_data)

    expected_data = [{"product_category": "board games"}]
    expected_df = spark.createDataFrame(data=expected_data)
    
    ### ACT
    result_df: DataFrame = get_most_frequent_product_categories(df)

    ### ASSERT
    pd.testing.assert_frame_equal(result_df.toPandas(), expected_df.toPandas())


def get_most_frequent_product_categories__two_most_frequent__two_frequent_returned():
    ### ARRANGE
    sample_data = [{"color": "yellow", "product_category": "movies", "title": "Mary Poppins"},
            {"color": "blue", "product_category": "board games", "title": "Monopoly"},
            {"color": "green", "product_category": "video games", "title": "Halo"},
            {"color": "red", "product_category": "board games", "title": "Risk"},
            {"color": "purple", "product_category": "movies", "title": "Purple Rain"}]
    df = spark.createDataFrame(sample_data)
    expected_data = [{"product_category": "movies"}, {"product_category": "board games"}]
    expected_df = spark.createDataFrame(data=expected_data)

    ### ACT
    result_df = get_most_frequent_product_categories(df)

    ### ASSERT
    pd.testing.assert_frame_equal(result_df.toPandas(), expected_df.toPandas())


def get_most_frequent_product_categories__no_rows__none_returned():
    ### ARRANGE
    # define the schema, but include no data
    schema = StructType([
        StructField("color", StringType(), True),
        StructField("product_category", StringType(), True),
        StructField("title", StringType(), True)
    ])
    df = spark.createDataFrame([], schema)

    ### ACT
    result = get_most_frequent_product_categories(df)

    ### ASSERT
    assert result is None

################# executing tests

spark = SparkSession.builder.appName("Testing get_most_frequent_product_categories").getOrCreate()

get_most_frequent_product_categories__one_most_frequent__most_frequent_returned()
get_most_frequent_product_categories__two_most_frequent__two_frequent_returned()
get_most_frequent_product_categories__no_rows__none_returned()

spark.stop()