Azure Data Factory Project
Table of Contents
Introduction
Tasks
Setup Instructions
Folder Structure
Usage Examples
Conclusion
Introduction
Hi Viewer! I hope you are doing well.

This project showcases my work on Azure Data Factory, where I accomplished the following tasks:

Fetch Country Data: Created a pipeline to fetch data for 5 countries (India, US, UK, China, Russia) from the Rest API and save it as JSON files, with filenames matching the country names.
Automated Trigger: Added a trigger to the above pipeline to run it twice daily at 12:00 AM and 12:00 PM IST.
Conditional Data Copy: Created a pipeline to copy customer data from a database to Azure Data Lake Storage (ADLS) only if the record count is more than 500. If the customer record count exceeds 600, a child pipeline is triggered to copy product data from the table.
Pipeline Parameterization: Designed the pipelines to pass the customer count to the child product pipeline via pipeline parameters.
I have implemented this project within a single Data Factory, creating appropriate Linked Services, Containers, Datasets, Pipelines, Triggers, and Activities. I also parameterized values that were repeated.

Tasks
Fetch Country Data Pipeline

Fetch data for India, US, UK, China, and Russia from the Rest API.
Save data in separate JSON files named after each country.
Automated Trigger

Set up a trigger to run the Fetch Country Data Pipeline at 12:00 AM and 12:00 PM IST daily.
Conditional Data Copy Pipeline

Copy customer data to ADLS if the record count is more than 500.
Trigger a child pipeline to copy product data if the customer record count exceeds 600.
Parameterization

Pass the customer count from the parent pipeline to the child product pipeline using pipeline parameters.
Setup Instructions
Prerequisites

Azure subscription.
Azure Data Factory instance.
Access to GitHub.
Clone the Repository

sh
Copy code
git clone https://github.com/YOUR_USERNAME/ADF-Pipelines.git
cd ADF-Pipelines
Configure Azure Data Factory

Set up Linked Services, Datasets, and Pipelines as per the JSON files in the repository.
Ensure you have the necessary permissions and access to the required data sources.
Folder Structure
Copy code
ADF-Pipelines/
│
├── ADF/
│   ├── Pipelines/
│   │   ├── FetchCountriesPipeline.json
│   │   ├── CopyCustomerDataPipeline.json
│   │   ├── CopyProductDataPipeline.json
│   │   └── ...
│   ├── Triggers/
│   │   ├── FetchCountriesTrigger.json
│   │   └── ...
│   ├── DataSets/
│   │   └── ...
│   ├── LinkedServices/
│   │   └── ...
│   └── ...
├── README.md
└── ...
Usage Examples
Running the Fetch Country Data Pipeline: This pipeline automatically runs at the scheduled times to fetch and save country data.
Conditional Data Copy Pipeline: This pipeline only copies customer data if the record count exceeds 500 and triggers the child pipeline if the count is above 600.
Conclusion
I have put a lot of effort into this project, applying all the knowledge gained during my internship and through my own research. I am happy to share my work and would love to answer any queries you might have.

Thank you!

Riya
