# Project name

summarizer

# Project Description

Background In data analysis we are operating with large dataframes, which can contain different types of data, such as binary, numeric, datetime and classification variables. Manual analysis of such dataframes is not efficient, and it could be very helpful to have some statistical overview of the dataframe.

The program takes pandas data frame as input, iterates over each of the columns of the frame and, based on the data type of the column and based on the data type of the columns to create summary statistics for each of them and output it as a table.

# Main Functions

The calculated summary includes the following items:

    ● column type
    ● min, max
    ● mean, median, mode
    ● percent of zero rows
    ● variance and standard deviation
    ● interquartile range and coefficient of variation
    ● number of distinct values


# Input
    ● data - Path to data file | --data
    ● output_type - Ouput type for saving (markdown, html or xlsx) | --type
    ● out_filename - Out filename| --filename
    ● save - Save directory. By default, the path to the directory is save| --save
    ● config - Yaml file with statistics items | --config

# Output

A markdown, html or xlsx report with summary statistics

# Installation

    1. Clone the repository
    git clone https://github.com/username/project-name.git

    2. Installation of dependencies (with pip)
    sh scripts/installation.sh

# Startup

    Running the example IRIS dataset:
    sh scripts/summary_iris.sh

# Requirements

    ● Python=3.11.10
    ● requirements.txt