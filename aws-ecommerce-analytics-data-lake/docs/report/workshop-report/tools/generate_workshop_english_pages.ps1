$ErrorActionPreference = "Stop"

$Root = Split-Path -Parent $PSScriptRoot
$WorkshopRoot = Join-Path $Root "content\5-Workshop"
$Utf8NoBom = New-Object System.Text.UTF8Encoding $false

function Page($title, $overview, $steps) {
    return @{
        Title = $title
        Overview = $overview
        Steps = $steps
    }
}

$Pages = @{
    "_index.md" = Page `
        "Workshop" `
        "This workshop builds a serverless e-commerce analytics data lake on AWS. The implementation starts from raw Kaggle e-commerce data, stores it in Amazon S3, catalogs it with AWS Glue, transforms it into analytics-ready Parquet data, queries it with Amazon Athena, visualizes it in Amazon QuickSight, and adds basic automation and monitoring." `
        @(
            "Prepare the raw source data and upload it to the S3 Raw Zone.",
            "Create Glue databases and crawlers for raw and curated data.",
            "Run a Glue ETL job to clean, validate, and convert the data to Parquet.",
            "Create Athena views for business-ready datasets.",
            "Build QuickSight dashboards for revenue, funnel, marketing, product, and A/B testing analysis.",
            "Automate the pipeline with Glue Workflow, EventBridge, CloudWatch Logs, and SNS alerts."
        )

    "5.1-Gioi-thieu/_index.md" = Page `
        "Build a Serverless E-Commerce Analytics Data Lake on AWS" `
        "This page introduces the complete workshop scope and the target architecture. The solution models a practical AWS Data Engineering pipeline for e-commerce analytics, from raw CSV files to business dashboards." `
        @(
            "Understand the business goal of analyzing e-commerce behavior and transactions.",
            "Review the main AWS services used in the pipeline: Amazon S3, AWS Glue, Amazon Athena, Amazon QuickSight, EventBridge, CloudWatch, and SNS.",
            "Map the data flow from local preprocessing to Raw Zone, Curated Zone, Athena semantic views, dashboards, and monitoring.",
            "Use the architecture diagram as the reference for the remaining workshop steps."
        )

    "5.2-Kaggle-Dataset-preprocessing-o-local/_index.md" = Page `
        "5.2. Kaggle Dataset Preprocessing Locally" `
        "This page prepares the source dataset before it is uploaded to AWS. The dataset contains event, product, and transaction data that will become the raw input of the data lake." `
        @(
            "Explore the main CSV files: events, products, and transactions.",
            "Review record counts and important columns in each file.",
            "Standardize timestamp fields so later Glue and Athena processing can use consistent names.",
            "Produce clean local CSV files ready to upload into the S3 Raw Zone."
        )

    "5.3-Tao-S3-Raw-Zone/_index.md" = Page `
        "5.3. Create the S3 Raw Zone" `
        "This page creates the S3 bucket and folder structure used as the raw storage layer of the data lake." `
        @(
            "Create an S3 bucket for the e-commerce analytics data lake.",
            "Create raw folders for events, products, and transactions.",
            "Upload the preprocessed local CSV files to the correct raw paths.",
            "Confirm that the raw files are available in S3 before cataloging them with Glue."
        )

    "5.4-Tao-Glue-Data-Catalog-cho-raw-data/_index.md" = Page `
        "5.4. Create the Glue Data Catalog for Raw Data" `
        "This section prepares AWS Glue to discover and catalog the raw CSV data stored in Amazon S3." `
        @(
            "Create an IAM role that allows AWS Glue to access the S3 data lake.",
            "Create the raw Glue database that will hold metadata for raw tables.",
            "Use a Glue Crawler to infer schemas from the raw CSV folders.",
            "Make the raw data queryable from Athena through the Glue Data Catalog."
        )

    "5.4-Tao-Glue-Data-Catalog-cho-raw-data/5.4.1-Tao-IAM-Role-cho-AWS-Glue/_index.md" = Page `
        "5.4.1. Create an IAM Role for AWS Glue" `
        "This page creates the IAM role used by Glue crawlers and jobs to read from and write to the S3 data lake." `
        @(
            "Open IAM and start creating a new role.",
            "Choose AWS Glue as the trusted service.",
            "Attach the required Glue and S3 access policies.",
            "Name the role and confirm that Glue can assume it during crawler and ETL execution."
        )

    "5.4-Tao-Glue-Data-Catalog-cho-raw-data/5.4.2-Tao-Glue-Database/_index.md" = Page `
        "5.4.2. Create the Glue Database" `
        "This page creates the Glue database that stores metadata for raw e-commerce tables." `
        @(
            "Open AWS Glue Data Catalog.",
            "Create a new database named ecommerce_raw.",
            "Use this database as the crawler output target for raw events, products, and transactions.",
            "Confirm that the database exists before running the raw crawler."
        )

    "5.5-Tao-Glue-Crawler-cho-Raw-Data/_index.md" = Page `
        "5.5. Create a Glue Crawler for Raw Data" `
        "This page configures a Glue Crawler to scan the S3 Raw Zone and create raw table definitions in the Glue Data Catalog." `
        @(
            "Create a crawler for the raw S3 paths.",
            "Add the events, products, and transactions folders as data sources.",
            "Choose the Glue IAM role created earlier.",
            "Set ecommerce_raw as the output database.",
            "Run the crawler and verify that the raw tables and schemas are created."
        )

    "5.6-Cau-hinh-Athena-query-result-location/_index.md" = Page `
        "5.6. Configure the Athena Query Result Location" `
        "This page configures Athena so SQL query results are written to a dedicated S3 location, then validates that the raw Glue tables can be queried." `
        @(
            "Open Amazon Athena and configure the query result location.",
            "Select the ecommerce_raw database.",
            "Run sample SELECT queries against raw_events, raw_products, and raw_transactions.",
            "Run simple aggregation queries to validate event types, categories, and transaction quantities."
        )

    "5.7-Glue-ETL-Job/_index.md" = Page `
        "5.7. Glue ETL Job" `
        "This section explains the ETL logic used to transform raw CSV tables into curated Parquet tables." `
        @(
            "Read raw events, products, and transactions from the Glue Data Catalog.",
            "Clean and cast columns into analytics-friendly types.",
            "Normalize timestamps and add year, month, and day partition columns.",
            "Separate invalid transaction records into an error path.",
            "Write curated Parquet outputs for fact_events, dim_products, and fact_transactions."
        )

    "5.7-Glue-ETL-Job/5.7.1-Tao-Glue-ETL-Job/_index.md" = Page `
        "5.7.1. Create the Glue ETL Job" `
        "This page creates and configures the AWS Glue Spark job that performs the raw-to-curated transformation." `
        @(
            "Open AWS Glue ETL jobs and create a Spark script job.",
            "Configure the job name, IAM role, and runtime settings.",
            "Add the BUCKET_NAME job parameter used by the script.",
            "Save and run the job.",
            "Check the run status and inspect errors in CloudWatch if the job fails."
        )

    "5.7-Glue-ETL-Job/5.7.2-Kiem-tra-output-tren-Amazon-S3/_index.md" = Page `
        "5.7.2. Check the Output on Amazon S3" `
        "This page validates that the Glue ETL job wrote curated Parquet data and error records to the expected S3 paths." `
        @(
            "Open the S3 bucket used by the data lake.",
            "Check the curated dim_products output.",
            "Check the curated fact_events output.",
            "Check the curated fact_transactions output.",
            "Check the error transaction path for invalid records separated by the ETL job."
        )

    "5.8-Tao-Glue-Data-Catalog-cho-Curated-Data/_index.md" = Page `
        "5.8. Create the Glue Data Catalog for Curated Data" `
        "This section catalogs the curated Parquet output so Athena and QuickSight can query the transformed data." `
        @(
            "Create the ecommerce_curated Glue database.",
            "Create a crawler for the curated S3 path.",
            "Run the crawler after the ETL job completes.",
            "Confirm that the curated fact and dimension tables appear in the Glue Data Catalog."
        )

    "5.8-Tao-Glue-Data-Catalog-cho-Curated-Data/5.8.1-Tao-Glue-Database-ecommerce-curated/_index.md" = Page `
        "5.8.1. Create the ecommerce_curated Glue Database" `
        "This page creates the Glue database that stores metadata for curated Parquet tables." `
        @(
            "Open AWS Glue Data Catalog.",
            "Create a new database named ecommerce_curated.",
            "Use this database as the target for the curated crawler.",
            "Confirm that the database is ready before crawling curated data."
        )

    "5.8-Tao-Glue-Data-Catalog-cho-Curated-Data/5.8.2-Tao-Glue-Crawler-cho-du-lieu-Curated-Parquet/_index.md" = Page `
        "5.8.2. Create a Glue Crawler for Curated Parquet Data" `
        "This page configures the crawler that discovers the curated Parquet tables written by the ETL job." `
        @(
            "Create a crawler named crawler_ecommerce_curated.",
            "Set the curated S3 folder as the data source.",
            "Choose the Glue IAM role.",
            "Set ecommerce_curated as the output database.",
            "Review and create the crawler."
        )

    "5.8-Tao-Glue-Data-Catalog-cho-Curated-Data/5.8.3-Chay-Glue-Crawler/_index.md" = Page `
        "5.8.3. Run the Glue Crawler" `
        "This page runs the curated crawler and validates the generated metadata tables." `
        @(
            "Run crawler_ecommerce_curated after the ETL output is available.",
            "Wait until the crawler finishes successfully.",
            "Open the ecommerce_curated database.",
            "Check the schemas for curated_fact_events, curated_dim_products, and curated_fact_transactions."
        )

    "5.8-Tao-Glue-Data-Catalog-cho-Curated-Data/5.8.4-Query-Curated-Tables-trong-Athena/_index.md" = Page `
        "5.8.4. Query Curated Tables in Athena" `
        "This page uses Athena to query the curated tables and confirm that the transformed data is available for analytics." `
        @(
            "Select the ecommerce_curated database in Athena.",
            "Run sample queries against curated_fact_events.",
            "Run sample queries against curated_fact_transactions.",
            "Run sample queries against curated_dim_products.",
            "Check that important columns and partitions are visible."
        )

    "5.9-Validate-curated-data/_index.md" = Page `
        "5.9. Validate Curated Data" `
        "This page runs validation queries against the curated tables to confirm data quality before creating business views." `
        @(
            "Check row counts for each curated table.",
            "Validate event type distribution.",
            "Validate product categories.",
            "Check negative revenue and refund logic.",
            "Check invalid negative transactions.",
            "Check important null fields in fact_transactions."
        )

    "5.10-Tao-Athena-Views-cho-analytics/_index.md" = Page `
        "5.10. Create Athena Views for Analytics" `
        "This page creates Athena views that package business logic for dashboards. The views keep repeated calculations out of QuickSight and provide reusable semantic datasets." `
        @(
            "Create funnel and traffic source views from curated_fact_events.",
            "Create discount, refund, executive, product, and campaign views from curated transaction and product tables.",
            "Create summary views for dashboard KPIs.",
            "Query each view after creation to confirm that it returns data.",
            "Verify that all views appear in ecommerce_curated."
        )

    "5.11-Ket-noi-QuickSight-voi-Athena/_index.md" = Page `
        "5.11. Connect QuickSight to Athena" `
        "This page connects Amazon QuickSight to Athena so dashboards can use the ecommerce_curated views as datasets." `
        @(
            "Confirm that QuickSight is using the correct AWS Region.",
            "Grant QuickSight access to Athena and the S3 buckets used by query results and data lake storage.",
            "Create a new Athena data source in QuickSight.",
            "Select the ecommerce_curated database and the required views.",
            "Finish dataset creation and prepare the datasets for dashboard authoring."
        )

    "5.12-Dashboard-1-Executive-Overview/_index.md" = Page `
        "5.12. Dashboard 1: Executive Overview" `
        "This page builds the executive overview dashboard in QuickSight. The dashboard summarizes revenue, orders, average order value, refunds, and business trends." `
        @(
            "Create calculated fields for year, month, and quarter filters.",
            "Add filter controls and configure their scope.",
            "Create KPI cards for total revenue, total orders, average order value, and refund rate.",
            "Add trend charts for revenue, orders, average order value, and refund rate.",
            "Review the completed dashboard with the April 2023 filter applied."
        )

    "5.13-Dashboard-2-Funnel-Analytics/_index.md" = Page `
        "5.13. Dashboard 2: Funnel Analytics" `
        "This page builds a QuickSight dashboard for user behavior funnel analysis, from views and clicks through add-to-cart and purchase." `
        @(
            "Create time filters for the funnel dataset.",
            "Create KPI cards for total events, views, clicks, add-to-carts, purchases, and bounce rate.",
            "Build a conversion funnel chart.",
            "Add daily funnel volume and conversion rate trend charts.",
            "Add source and device breakdowns for purchases, conversion rate, and bounce rate."
        )

    "5.14-Dashboard-3-Marketing-Performance/_index.md" = Page `
        "5.14. Dashboard 3: Marketing Performance" `
        "This page builds a marketing performance dashboard for traffic sources and campaign behavior." `
        @(
            "Create time filters for marketing analysis.",
            "Add KPI cards for events, views, clicks, add-to-carts, purchases, and bounce rate.",
            "Visualize funnel volume by traffic source.",
            "Compare source quality, purchases, conversion rates, and bounce rates over time.",
            "Analyze campaign-level purchases, conversion, bounce rate, and funnel volume."
        )

    "5.15-Dashboard-4-Product-Analytics/_index.md" = Page `
        "5.15. Dashboard 4: Product Analytics" `
        "This page builds a product analytics dashboard focused on revenue, sales volume, transaction value, and refund behavior." `
        @(
            "Create time filters for product analysis.",
            "Add KPI cards for revenue, transactions, units sold, average transaction value, refunded transactions, and refund rate.",
            "Build product revenue and sales trend charts.",
            "Compare category, brand, premium, and non-premium performance.",
            "Create top product, average transaction value, and refund rate visuals."
        )

    "5.16-Dashboard-5-AB-Testing/_index.md" = Page `
        "5.16. Dashboard 5: A/B Testing" `
        "This page builds an A/B testing dashboard that compares experiment groups across conversion, purchase, add-to-cart, and bounce metrics." `
        @(
            "Create time filters for the experiment dataset.",
            "Add KPI cards for total events, views, purchases, conversion rate, add-to-cart rate, and bounce rate.",
            "Compare experiment funnel volume by group.",
            "Compare key rates across groups.",
            "Add trend charts and a detail pivot table for A/B testing performance."
        )

    "5.17-Publish-Dashboards/_index.md" = Page `
        "5.17. Publish Dashboards" `
        "This page publishes the completed QuickSight dashboards so they can be shared and reviewed." `
        @(
            "Open each completed QuickSight analysis.",
            "Publish the analysis as a dashboard.",
            "Confirm dashboard name and sharing settings.",
            "Check that filters and visuals work after publishing.",
            "Use the published dashboards as the final BI output of the workshop."
        )

    "5.18-Automation-and-Monitoring-Layer/_index.md" = Page `
        "5.18. Automation and Monitoring Layer" `
        "This section adds automation and monitoring around the data lake pipeline. The goal is to reduce manual execution and make failures visible." `
        @(
            "Create SNS email notifications.",
            "Create a Glue Workflow to orchestrate raw crawler, ETL job, and curated crawler.",
            "Check Glue ETL logs in CloudWatch.",
            "Schedule workflow execution with EventBridge Scheduler.",
            "Create EventBridge rules that alert when Glue jobs or crawlers fail."
        )

    "5.18-Automation-and-Monitoring-Layer/5.18.1-Tao-SNS-Email-Notification/_index.md" = Page `
        "5.18.1. Create an SNS Email Notification" `
        "This page creates an SNS topic and email subscription for pipeline failure notifications." `
        @(
            "Open Amazon SNS.",
            "Create a topic for Glue pipeline alerts.",
            "Create an email subscription for the topic.",
            "Confirm the subscription from the email inbox.",
            "Use the topic as the notification target for EventBridge alert rules."
        )

    "5.18-Automation-and-Monitoring-Layer/5.18.2-Tao-Glue-Workflow/_index.md" = Page `
        "5.18.2. Create a Glue Workflow" `
        "This page creates a Glue Workflow to run the pipeline steps in order." `
        @(
            "Create a new Glue Workflow.",
            "Add the first trigger to start the raw crawler.",
            "Add a conditional trigger that runs the ETL job after the raw crawler succeeds.",
            "Add a conditional trigger that runs the curated crawler after the ETL job succeeds.",
            "Run the workflow and confirm that all nodes complete successfully."
        )

    "5.18-Automation-and-Monitoring-Layer/5.18.3-Kiem-tra-CloudWatch-Logs-cho-Glue-ETL-Job/_index.md" = Page `
        "5.18.3. Check CloudWatch Logs for the Glue ETL Job" `
        "This page shows where to inspect Glue ETL logs in CloudWatch after the workflow runs." `
        @(
            "Open Amazon CloudWatch from the AWS Management Console.",
            "Go to Logs and then Log groups.",
            "Check the common Glue log groups: /aws-glue/jobs/output and /aws-glue/jobs/error.",
            "Use the logs to follow ETL execution and debug read, write, schema, or PySpark errors."
        )

    "5.18-Automation-and-Monitoring-Layer/5.18.4-Su-dung-EventBridge-de-schedule/_index.md" = Page `
        "5.18.4. Use EventBridge Scheduler" `
        "This page schedules the Glue Workflow so the data pipeline can run automatically." `
        @(
            "Create an IAM policy and role that allow EventBridge Scheduler to start the Glue Workflow.",
            "Create a new EventBridge schedule.",
            "Choose the Glue StartWorkflowRun target.",
            "Provide the target input and schedule settings.",
            "Confirm that the schedule can trigger the workflow at the configured time."
        )

    "5.18-Automation-and-Monitoring-Layer/5.18.5-Kiem-tra-schedule/_index.md" = Page `
        "5.18.5. Check the Schedule" `
        "This page validates that the EventBridge schedule exists and is ready to run the workflow." `
        @(
            "Open EventBridge Scheduler.",
            "Find the schedule created for the Glue Workflow.",
            "Check the schedule expression and enabled state.",
            "Confirm that the target points to the correct Glue Workflow.",
            "Monitor the next run through Glue Workflow and CloudWatch Logs."
        )

    "5.18-Automation-and-Monitoring-Layer/5.18.6-EventBridge-Rule-dung-de-alert-loi/_index.md" = Page `
        "5.18.6. Create EventBridge Failure Alert Rules" `
        "This page creates EventBridge rules that detect Glue crawler and Glue job failures and send notifications through SNS." `
        @(
            "Create an EventBridge rule for raw and curated crawler failure events.",
            "Set the SNS topic as the rule target.",
            "Create an EventBridge rule for Glue ETL job failure events.",
            "Set the same SNS topic as the notification target.",
            "Use the alerts to detect pipeline failures without checking the console manually."
        )
}

function Get-FrontMatter($content) {
    $match = [regex]::Match($content, '(?s)\A---\r?\n.*?\r?\n---')
    if (-not $match.Success) {
        throw "Missing front matter"
    }
    return $match.Value
}

function Set-FrontValue($front, $key, $value) {
    $escaped = $value.Replace('\', '\\').Replace('"', '\"')
    $pattern = '(?m)^' + [regex]::Escape($key) + '\s*:\s*".*"\r?$'
    if ([regex]::IsMatch($front, $pattern)) {
        return [regex]::Replace($front, $pattern, ($key + ': "' + $escaped + '"'))
    }
    return $front
}

function Extract-CodeBlocks($content) {
    return [regex]::Matches($content, '(?s)```.*?```') |
        ForEach-Object { $_.Value.TrimEnd() } |
        Where-Object { $_ -notmatch '[^\x00-\x7F]' }
}

function Extract-Images($content) {
    $seen = @{}
    $images = New-Object System.Collections.Generic.List[string]
    [regex]::Matches($content, '(?m)^!\[[^\]]*\]\([^)]+\)') | ForEach-Object {
        $value = $_.Value
        if (-not $seen.ContainsKey($value)) {
            $seen[$value] = $true
            [void]$images.Add($value)
        }
    }
    return $images
}

function Build-Body($page, $viContent) {
    $lines = New-Object System.Collections.Generic.List[string]
    [void]$lines.Add("# $($page.Title)")
    [void]$lines.Add("")
    [void]$lines.Add($page.Overview)
    [void]$lines.Add("")
    [void]$lines.Add("## What This Page Covers")
    foreach ($step in $page.Steps) {
        [void]$lines.Add("- $step")
    }

    $codeBlocks = @(Extract-CodeBlocks $viContent)
    if ($codeBlocks.Count -gt 0) {
        [void]$lines.Add("")
        [void]$lines.Add("## Reference Commands and Queries")
        [void]$lines.Add("")
        [void]$lines.Add("The SQL, JSON, or command snippets used in the Vietnamese walkthrough are kept below for the English version.")
        foreach ($block in $codeBlocks) {
            [void]$lines.Add("")
            [void]$lines.Add($block)
        }
    }

    $images = @(Extract-Images $viContent)
    if ($images.Count -gt 0) {
        [void]$lines.Add("")
        [void]$lines.Add("## Screenshots")
        [void]$lines.Add("")
        [void]$lines.Add("The following screenshots match the implementation steps in this page.")
        foreach ($image in $images) {
            [void]$lines.Add("")
            [void]$lines.Add($image)
        }
    }

    return ($lines -join "`n").TrimEnd() + "`n"
}

foreach ($entry in $Pages.GetEnumerator()) {
    $relativePath = $entry.Key
    $page = $entry.Value
    $englishPath = Join-Path $WorkshopRoot ($relativePath -replace '/', '\')
    $vietnamesePath = $englishPath -replace '_index\.md$', '_index.vi.md'

    if (-not (Test-Path $englishPath)) {
        throw "Missing English file: $englishPath"
    }
    if (-not (Test-Path $vietnamesePath)) {
        throw "Missing Vietnamese file: $vietnamesePath"
    }

    $englishContent = [System.IO.File]::ReadAllText($englishPath, [System.Text.Encoding]::UTF8)
    $vietnameseContent = [System.IO.File]::ReadAllText($vietnamesePath, [System.Text.Encoding]::UTF8)
    $front = Get-FrontMatter $englishContent
    $front = Set-FrontValue $front "title" $page.Title
    $front = Set-FrontValue $front "linkTitle" $page.Title
    $front = Set-FrontValue $front "menuTitle" $page.Title

    $body = Build-Body $page $vietnameseContent
    $output = $front.TrimEnd() + "`n`n" + $body
    [System.IO.File]::WriteAllText($englishPath, $output, $Utf8NoBom)
}

Write-Host "Generated English workshop pages:" $Pages.Count
