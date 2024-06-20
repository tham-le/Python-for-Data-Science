#!/usr/bin/env python3

from load_csv import load
import matplotlib.pyplot as plt


def main():
    """displays the projection of life expectancy in relation
    to the gross national product of the year 1900 for each countr."""
    try:
        year = "1900"
        life_data = load("../life_expectancy_years.csv")
        life_expectancy_1900 = life_data[year]

        file = "../income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
        gdp_data = load(file)
        gdp_per_capita_1900 = gdp_data[year]

        plt.figure(figsize=(10, 8))
        plt.scatter(gdp_per_capita_1900, life_expectancy_1900)
        plt.xlabel("Gross domestic product")
        plt.xscale("log")
        plt.xticks([300, 1e3, 1e4], ["300", "1k", "10k"])
        plt.ylabel("Life expectancy")
        plt.title("Life expectancy vs GDP per capita in 1900")
        plt.show()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
