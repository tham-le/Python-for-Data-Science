#!/usr/bin/env python3.10

from load_csv import load
import matplotlib.pyplot as plt


def main():
    """Load the life expectancy data and plot
    the life expectancy projection for France"""
    try:
        country = "France"
        data = load("../life_expectancy_years.csv")
        if data is None:
            raise Exception("Data is not loaded")
        if len(data) == 0:
            raise Exception("Data is empty")
        if ("country" not in data.columns):
            raise Exception("Data is not in the correct format")
        if country not in data["country"].values:
            raise Exception(country + " is not in the data")

        country_data = data[data["country"] == country]
        years = country_data.columns[1:]
        life_expectancy = country_data.values[0][1:]
        plt.plot(years, life_expectancy)
        plt.xlabel("Year")
        plt.xticks(years[::40])
        plt.ylabel("Life expectancy (years)")
        plt.title(country + " Life expectancy Projection")
        plt.show()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
