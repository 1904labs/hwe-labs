import gzip
import csv
from faker import Faker

# Initialize the Faker instance
fake = Faker()
Faker.seed(42)
#There are some big fields in the review data...
csv.field_size_limit(10 * 1024 * 1024)  # Set the field size limit to 10 MB

# Define the TSV.gz file path
input_file_path = 'resources/reviews.tsv.gz'
output_file_path = 'resources/customers.tsv.gz'

# Open the compressed file and read it using gzip
with gzip.open(input_file_path, 'rt', encoding='utf-8') as input_file, gzip.open(output_file_path, 'wt', encoding='utf-8') as output_file:

    # Create a CSV reader
    reader = csv.reader(input_file, delimiter='\t', quoting=csv.QUOTE_NONE)
    writer = csv.writer(output_file, delimiter='\t', lineterminator='\n')

    # Skip the header if present
    header = next(reader, None)
    writer.writerow(["customer_id", "customer_name", "gender", "date_of_birth", "city", "state"])
    seen_these = set()
    # Iterate over the rows
    for row in reader:
        # Extract the customer_id (second field)
        customer_id = row[1]
        if customer_id not in seen_these:
            # Add the customer_id to the set of unique IDs
            seen_these.add(customer_id)
            # Generate fake customer data
            gender = fake.random_element(["M", "F"])
            if gender == "M":
                customer_name = fake.name_male()
            else:
                customer_name = fake.name_female()
            date_of_birth = fake.date_of_birth()
            city = fake.city()
            state = fake.state()
            writer.writerow([customer_id, customer_name, gender, date_of_birth, city, state])

