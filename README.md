# GitHub traffic

Github reports traffic to a repository in the Insights/Graphs section of a repository.
This includes the number of visits to the repository, the number of times it was
cloned each day, popular pages, and referring sites.
Number of visitors and number of clones is only reported for two weeks.
This information is also available via the GitHub API.

## Installation

Install this project to a python environment using pip:

    pip install git+https://github.com/MTG/github-traffic.git

A script will be installed to `bin/get_github_traffic`

## Configuration

Create a directory to save the output of the script to.

Copy the configuration file, `config.ini`. You can put it in the same directory
that you create above.

Open GitHub settings, and go to the section *Personal access tokens*. Create a new
token. The only permission that this key needs is `public_repo`, to read statistics
for a public repository.

## Running

Run the script, specifying the path to the config file and the output directory:

    get_github_traffic -c gh_traffic/config.ini -o gh_traffic

This script can be run via cron once a week to keep a full record of historical data.

